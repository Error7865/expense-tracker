import unittest
import os
from pathlib import Path
class TestRoot(unittest.TestCase):

    def test_add(self):
        res=os.system('python3 root.py -t -des "Rent" -a 4000')
        # self.assertEqual(res, 0)
        file=Path.cwd() / 'test_data.txt'
        data=file.read_text()
        self.assertIn('Rent', data)
        self.assertIn('4000', data)
        
    def test_remove(self):
        res=os.system('python3 root.py -t -r 1')

    def test_zclean(self):
        file=Path.cwd() / 'test_data.txt'
        if file.exists():
            file.unlink()
        self.assertFalse(file.exists(), msg="File was not delete.")
        