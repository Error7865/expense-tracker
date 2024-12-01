import csv
import os

config={}

def set_config(typ: bool = True)-> None:
    '''True means that use in case of production
    and False mean it use in test case'''
    if typ:
        config['file']= os.environ.get('database')
    else:       #test case 
        config['file']= os.environ.get('test_database')  

def length_of_max_values(data: list)->dict:
    keys=list(data[0].keys())
    length_dict={key: len(key) for key in keys}
    for dic in data:
        for key in keys:
            try:
                length=len(dic[key])
            except TypeError:
                length= len(str(dic[key]))
            if length > length_dict[key]:
                length_dict[key] = length

    return length_dict

def adjust_str(value, num:int)->str:
    '''This function will return string with adding extra space
    based on num'''
    try:
        value_len=len(value)
    except TypeError:
        value_len=len(str(value))
    if value_len == num:
        return str(value)+' |'
    need_spac=num - value_len
    return str(value)+" "*need_spac+' |'

def print_hipen(num:int):
    print('-'*num)

def display(data:list)->None:
    keys=list(data[0].keys())
    max_len=length_of_max_values(data=data)
    # print headers 
    line='|'
    for key in keys:
        line+= adjust_str(key, max_len[key])
    print(line)     #header
    
    for dic in data:    #printing data
        line='|'
        for key in keys:
            line += adjust_str(dic[key], max_len[key])
        print(line)


def export_csv(data):
    keys = list(data[0].keys())
    with open('records.csv', 'w') as file:
        writer=csv.DictWriter(file, keys)
        writer.writeheader()
        writer.writerows(data)