import sys
from collections import Counter
import re
import string
word=[]
pos=[]
new_list=[]
new_list1=[]
strlist = {}
strlist1 = {}
strlist2 = {}
strlist3 = {}
#read text from POS.txt from 3rd row
for c in sys.stdin.readlines():
    #read line that does not contain #
    if not "#" in c:
        #if the string contains something besides whitespace
        if c.strip():
    #get word after first tab and add an element to the list
            word.append(c.split('\t')[1])
    #if second column has '-' then get 5th column POS and add an element to the list
            if c.split('\t')[3] in '_':
                pos.append(c.split('\t')[4])
    #get 4th column word and add an element to the list
            else:
                pos.append(c.split('\t')[3])
#The else clause executes when the loop completes normally
else:
    #using zip function to loop several list simultaneously
    for val1, val2 in zip(word,pos):
        #adds an element to the list
        new_list.append(val2+" "+val1) 
    # loop list that was taken from above 
    for newValue in new_list:
        #if dictionary contains value then add plus one 
        if newValue in strlist:
            strlist[newValue] += 1
        # does not contains then 1
        else:
            strlist[newValue] = 1
    #loop POS list 
    for posValue in pos:
        #add elements to list
        new_list1.append(posValue)
    #loop list that was taken from above 
    for newValue1 in new_list1:
        #if dictionary contains value then add plus one 
        if newValue1 in strlist2:
            strlist2[newValue1] += 1
        # does not contains then 1    
        else:
            strlist2[newValue1] = 1   
    #The else clause executes when the loop completes normally
    else:
        #returns a list of all the available keys in the dictionary
        str_list = strlist.keys()
        #returns a list of all the available values in the dictionary
        str_list1 = strlist.values()
        #returns a list of all the available keys in the dictionary
        str_list2 = strlist2.keys()
        #returns a list of all the available values in the dictionary
        str_list3 = strlist2.values()
        #print titles
        print("# P","count","tag","  "+"form")
        #using zip function to loop several lists simultaneously
        for words1,values1 in zip(str_list2,str_list3):
            #print the number of POS
            print(values1/len(word),values1, "    "+words1.strip(),"_")
        for words,values in zip(str_list,str_list1):
            #print the tag of the same words
            print(values/values,values,"    "+words)