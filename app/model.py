import csv
import os
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Model:
    def __init__(self): 
        '''Model header :
        ID, Date, Description, Amount'''
        self.__filename=os.environ.get('database')
        ls=os.listdir(os.getcwd())
        if self.__filename not in ls:   #not present 
            with open(self.__filename, 'w') as file:
                writer=csv.writer(file)
                writer.writerow(['ID', 'Date', 'Description', 'Amount'])
        self.__index=0 #for iter 

    def __dict_read(self):
        data=list()
        with open(self.__filename, 'r') as file:
            reader=csv.DictReader(file)
            for line in reader:
                line['ID']=int(line["ID"])
                line['Date']=datetime.strptime(line['Date'], "%Y-%m-%d %H:%M:%S.%f")
                line['Amount']=int(line['Amount'])
                data.append(line)
        return data
    
    def insert(self, data: dict):
        '''insert new row inside data.txt
        data must have`Description`,`Amount` keys'''
        # get last id of exiting data
        last_line=[]
        with open(self.__filename, 'r') as file:
            reader=csv.reader(file)
            for line in reader:
                # print('From line ', line)
                last_line=line

        #now got last line
        if 'Date' not in list(data.keys()):
            data['Date']=str(datetime.now())
        try: 
            data['ID']=int(last_line[0])+1  #It will throw ValueError when in data have no
                                                #row only contain header
        except ValueError:  #So that case make id of new row 1
            data['ID']=1
        with open(self.__filename, 'a') as file:
            writer=csv.DictWriter(file, ['ID', 'Date', 'Description', 'Amount'])
            writer.writerow(data)
        return data

    def update(self, id:int, data:dict):
        '''Update exits data based on id'''
        keys=list(data.keys())
        data_ls,  is_match=[], False
        with open(self.__filename, 'r') as file:
            reader=csv.DictReader(file)
            for line in reader:
                if int(line['ID']) == id:
                    is_match=True
                    for key in keys:
                        try:
                            line[key] = data[key]
                        except KeyError:
                            pass
                    return_value=line
                data_ls.append(line)
        if not is_match:
            raise ValueError('There have not any row with ', id)
        with open(self.__filename, 'w') as file:
            writer=csv.DictWriter(f=file, fieldnames=['ID', 'Date', 'Description', 'Amount'])
            writer.writeheader()
            writer.writerows(data_ls)
        return  return_value

    def delete(self, id:int):
        data_ls=[]
        with open(self.__filename, 'r') as file:
            reader=csv.DictReader(file)
            for line in reader:
                if int(line['ID']) != id:
                    data_ls.append(line)
        
        with open(self.__filename, 'w') as file:
            writer=csv.DictWriter(file, ['ID', 'Date', 'Description', 'Amount'])
            writer.writeheader()
            writer.writerows(data_ls)
    
    def summary(self, month=0):
        data=self.__dict_read()
        total_expense=0
        month_expense=0
        for line in data:
            if month == line['Date'].month:
                month_expense+=line['Amount']
            total_expense+=line['Amount']
        if month == 0:
            return total_expense
        return month_expense

    def __iter__(self):
        return self
    
    def __next__(self):
        len_data=len(Path(self.__filename).read_text().splitlines())-1     #substract headers
        data=self.__dict_read()
        if self.__index >= len_data:
            raise StopIteration
        val=data[self.__index]
        self.__index+=1
        return val