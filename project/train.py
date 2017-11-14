import sys
from collections import Counter
import re
import string
word=[]
pos=[]
word_pos=[]
new_list=[]
new_list1=[]
strlist = {}
strlist1 = {}
strlist2 = {}
strlist3 = {}
#read text from 3rd row
for c in sys.stdin.readlines():
    if not "#" in c:       
        if c.strip():
    #get word after first tab
            word.append(c.split('\t')[1])
    #if second column has '-' then get 5th column pos
            if c.split('\t')[3] in '_':
                pos.append(c.split('\t')[4])
    #get 4th column word
            else:
                pos.append(c.split('\t')[3]) 
else:
    for val1, val2 in zip(word,pos):
        new_list.append(val2+" "+val1) 
        
    # 2nd tuple contains
    for newValue in new_list:
        if newValue in strlist:
            strlist[newValue] += 1
        else:
            strlist[newValue] = 1
    for posValue in pos:
        new_list1.append(posValue)
    for newValue1 in new_list1:
        if newValue1 in strlist2:
            strlist2[newValue1] += 1
        else:
            strlist2[newValue1] = 1    
    else:
        str_list = strlist.keys()
        str_list1 = strlist.values()
        str_list2 = strlist2.keys()
        str_list3 = strlist2.values()
        print("# P","count","tag","  "+"form")
        for words1,values1 in zip(str_list2,str_list3):
            print(values1/len(word),values1, "    "+words1.strip(),"_")
        for words,values in zip(str_list,str_list1):
            print(values/values,values,"    "+words)