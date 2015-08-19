__author__ = 'okhaz'

import re
import sys
from collections import OrderedDict
import filecmp

input_file = '/home/okhaz/Downloads/test_cases/input003.txt'
my_file =  '/home/okhaz/Downloads/test_cases/ouput_ok_3.txt'
output_check = '/home/okhaz/Downloads/test_cases/output003.txt'

last_first = re.compile('\w+,\w+')
last_first_middle = re.compile('\w+,\w+ \w+')


fid  = open(input_file)
fid_wrt  = open(my_file,'w+')

lines = fid.readlines()
dict = OrderedDict()


for line in lines:
   if len(re.split(':',line))!=1:
        name, SSN = re.split(':',line)
        SSN = SSN.strip('\n')
        if dict.has_key(SSN):
            dict[SSN].append(name)
        else:
            dict.update({SSN:[]})
            dict[SSN].append(name)



for SSN in dict.iterkeys():
    name_array=dict[SSN]
    print name_array
    split_name=[]
    name_array.sort(key=lambda item: (-len(item), item))
    if re.match(last_first_middle,name_array[0]) or re.match(last_first,name_array[0]):
                split_name=re.findall(r"[\w']+", name_array[0])
                if re.match(last_first_middle,name_array[0]):
                        normal_form = split_name[1]+' '+split_name[2]+' '+split_name[0]
                elif re.match(last_first,name_array[0]):
                        normal_form = split_name[1]+' '+split_name[0]
    else:
                normal_form=name_array[0]
    fid_wrt.write(normal_form+':'+SSN+'\n')

print 'Test went successfully: ', filecmp.cmp(my_file,output_check)