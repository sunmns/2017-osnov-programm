import sys
from collections import Counter
import re
import string
word=[]
pos=[]
word_pos=[]
strlist = {}
strlist1 = {}
#read text from 3rd row
for c in sys.stdin.readlines()[2:]:
    #get word after first tab
    word.append(c.split('\t')[1])
    #if second column has '-' then get 5th column pos
    if c.split('\t')[3] in '_':
         pos.append(c.split('\t')[4])
    #get 4th column word
    else:
         pos.append(c.split('\t')[3]) 
else:
    # 2nd tuple contains
    for val1, val2 in zip(word,pos):
        if val1+val2 in strlist:
            strlist[val1] += 1
        else:
            strlist[val1] = 1
    
    else:
        str_list = strlist.keys()
        str_list1 = strlist.values()
        
        for words,values in zip(str_list,str_list1):
            print(words,values)