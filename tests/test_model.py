import unittest
import os
import csv
from datetime import datetime
from app.model import Model

class TestModel(unittest.TestCase):

    # @unittest.skip
    def test_insert(self):
        m=Model()
        data=m.insert({
            'Description': 'face wash',
            'Amount': 200
        })
        data=m.insert({
            'Description': 'Purches book',
            'Amount': 1000
        })
        data=m.insert({
            'Description': 'Mobile Recharge',
            'Amount': 210
        })
        self.assertIn('Amount', list(data.keys()), msg='There was not any amount key.')
    
    # @unittest.skip
    def test_update(self):
        m=Model()
        data=m.update(2, {'Description': 'Buy book'})
        self.assertEqual(data['ID'], '2', msg="ID isn't present in updated data")
        self.assertEqual('Buy book', data['Description'], msg="Description isn't present in updated data")
        self.assertIn('Date', str(data), msg="Date isn't present in updated data")
        with self.assertRaises(ValueError) as e:        #testing out of randge data
            data=m.update(9999, {'Description': 'Buy book'})

    # @unittest.skip
    def test_j_delete(self):
        m=Model()
        self.assertIsNone(m.delete(1))
    
    def test_summary(self):
        m=Model()
        #Total expense
        with open('data.txt', 'r') as file:
            reader=csv.DictReader(file)
            total=0
            for line in reader:
                total+=int(line['Amount'])
        self.assertEqual(m.summary(), total)

        #expense of a particular month
        month_expense=0
        month=11
        with open('data.txt', 'r') as file:
            reader=csv.DictReader(file)
            for line in reader:
                line['Date']=datetime.strptime(line['Date'], "%Y-%m-%d %H:%M:%S.%f")
                if line['Date'].month == month:
                    month_expense+=int(line['Amount'])
        self.assertEqual(m.summary(11), month_expense)