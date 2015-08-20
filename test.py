__author__ = 'okhaz'

import unittest
from main import delete_duplicates
import filecmp
BASE_PATH = 'test_cases/'



class TestDeDupMethod(unittest.TestCase):

    def testFile1(self):
        input_file = BASE_PATH+'input001.txt'
        my_file =  BASE_PATH+'ouput_ok_1.txt'
        output_check = BASE_PATH+'output001.txt'
        delete_duplicates(input_file, my_file)
        self.assertTrue(filecmp.cmp(my_file,output_check))


    def testFile2(self):
        input_file = BASE_PATH+'input002.txt'
        my_file =  BASE_PATH+'ouput_ok_2.txt'
        output_check = BASE_PATH+'output002.txt'
        delete_duplicates(input_file, my_file)
        self.assertTrue(filecmp.cmp(my_file,output_check))

    def testFile3(self):
        input_file = BASE_PATH+'input003.txt'
        my_file =  BASE_PATH+'ouput_ok_3.txt'
        output_check = BASE_PATH+'output003.txt'
        delete_duplicates(input_file, my_file)
        self.assertTrue(filecmp.cmp(my_file,output_check))


suite = unittest.TestLoader().loadTestsFromTestCase(TestDeDupMethod)
unittest.TextTestRunner(verbosity=2).run(suite)