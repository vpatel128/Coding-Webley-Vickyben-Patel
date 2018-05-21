# -*- coding: utf-8 -*-
"""
@author: Vickyben Patel
"""

import csv
from itertools import combinations
import itertools
import sys

dict_item={}
dict_items={}

# Read csv file
try:
    filename = sys.argv[1]
except IndexError:
    print ("Please enter csv filename")
    sys.exit(1)
file_reader= open(filename, "rt")
read = csv.reader(file_reader)
for row in read :
    dict_item = dict(itertools.zip_longest(*[iter(row)] * 2, fillvalue=""))
    dict_items.update(dict_item)

# Print error message if uploaded file is empty
if len(dict_items)==0:
    print("The File", filename,", you are trying to read is empty")
else:
    # Make combinations
    comb_list=[]
    list_items=list(dict_items.keys())[1:]
    for i in range(0,len(list_items)+1):
        for comb in combinations(list_items,i):
            if(set(comb)):
                comb_list.append(comb)
    
    result=[]
    # Calculate the sum of every combinations and compare it with target price 
    for comb in comb_list:
        sum=0.0
        for item in comb:
            sum=sum+float(((dict_items.get(item)).split('$')[1]).rstrip())
        if sum==float(((dict_items['Target price']).split('$')[1]).rstrip()):
            result.append(comb)
    
    if len(result)==0:
        print('There is no combination of dishes that is equal to the target price')
    else:
        print('combination of dishes that is equal to the target price:',result)
