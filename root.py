import argparse
import os
from app import display, export_csv, set_config
from app.model import Model
from dotenv import load_dotenv

load_dotenv()

def call():
    parser=argparse.ArgumentParser(description='Cli expense tracker')
    parser.add_argument('-des', '--description', help="Description of where you spend" )
    parser.add_argument('-a', '--amount', type=int, help='Amount of money you spend', default=0)
    parser.add_argument('-ls', '--list', action='store_true', \
                    help="list of expense")
    parser.add_argument('-s', '--summary', action='store_true', help='total expense')
    parser.add_argument('-rm', '--remove', type=int, \
                        help='delete any row of expense')
    parser.add_argument('-ms', '--msummary', type=int, help='Expense of a particular month')
    parser.add_argument('--csv', action='store_true', help='Export all data into a .csv file')
    parser.add_argument('-t', action='store_true', help="Use only for testing.")
    args=parser.parse_args()
    # implementing thoes features 
    if args.t:      #first need to set config for test case or 
        set_config(False)
    else:
        set_config()
    m=Model()

    if args.description is not None and args.amount:        #add 
        data=m.insert({
            'Description': args.description,
            'Amount': args.amount
            })
        print('Data added successfully.')
        
    if args.list:     #show list
        data=[]
        for row in m:
            data.append(row)
        display(data)

    if args.summary:    #total expense
        print(f'# Total expense {m.summary()}')
    
    if args.remove:
        m.delete(args.remove)
        print('#Expense delete successfully.')

    if args.msummary:
        print(f'# Total expense for {args.msummary} month: {m.summary(args.msummary)}') 
    
    if args.csv:
        data=[]
        for i in m:
            data.append(i)
        export_csv(data)

if __name__=="__main__":
    call()