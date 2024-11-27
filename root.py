import argparse
from app import display
from app.model import Model

def call():
    parser=argparse.ArgumentParser(description='Cli expense tracker')
    parser.add_argument('-del', '--description', help="Description of where you spend" )
    parser.add_argument('-a', '--amount', type=int, help='Amount of money you spend', default=0)
    parser.add_argument('-ls', '--list', action='store_true', \
                    help="list of expense")
    parser.add_argument('-s', '--summary', action='store_true', help='total expense')
    parser.add_argument('-rm', '--remove', type=int, \
                        help='delete any row of expense')
    parser.add_argument('-ms', '--msummary', type=int, help='Expense of a particular month')
    args=parser.parse_args()
    m=Model()
    # implementing thoes features 
    if args.description is not None:        #add 
        data=m.insert({
            'Description': args.description,
            'Amount': args.amount
            })
        
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

if __name__=="__main__":
    call()