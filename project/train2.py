import sys
from collections import Counter
import re
import string
word=[]
pos=[]
word_pos=[]
strlist = {}
strlist1 = {}
for c in sys.stdin.readlines()[2:]:
    
    word.append(c.split('\t')[1])
    if c.split('\t')[3] in '_':
         pos.append(c.split('\t')[4])
    else:
         pos.append(c.split('\t')[3]) 
else:
    for val1, val2 in zip(word,pos):
        count = strlist.get(val1,0)
        count1 = strlist1.get(val2,0)
        strlist[val1] = count + 1
        str_list = strlist.keys()
        strlist1[val2] = count1 + 1
        str_list1 = strlist1.keys()

    for words,pos1 in zip(str_list,str_list1):
            print(words, pos1,strlist1[val2]