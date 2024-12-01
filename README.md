# Expese Tracker 
Expense tracker is a basic python project that use to track your expense. It used command line arguments to achieve it's outcome. \
It capable to perform following type of operation:

1. Add new expense.
2. Delete any present expense.
3. Display all expense list.
4. Display total expense.
5. Display expense of a month.
6. Export all data to a CSV file.

## ADD:
  To add a new expense you should execute following command on shell:
  ```
  $ python3 root.py -des "<expense_name>" -a <amount>
  ```
  Here amount should be an integer or float value
  
## DELETE:
  To delete any existing expense record command should like:
  ```
  python3 root.py -rm <expense_id>
  ```

## LIST:
  To display list of all records execute this:
  ```
  python3 root.py -ls
  ```
## TOTAL:
  Whenever you need to know total expense use follow command:
  ```
  python3 root.py -s
  ```
## MONTH EXPENSE:
  If you want any particular month expense then use this command:
  ```
  python3 root.py -ms <month_index>
  ```
  month_index should be by represting number of that particular month from 1-12

## CSV:
  Suppose you have an emergency case when you need to all records of expense in a particular csv file.
  Then you need this magic stick:
  ```
    python3 root.py -csv
```
  Then it will generate a csv file name `records.csv' which contain all your expense data.


  This project create by following [roadmap.sh](https://roadmap.sh/projects/expense-tracker)
