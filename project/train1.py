import sys
from collections import Counter
import re
import string
dict = str.maketrans("абвгдеёжзийклмноөпрстуүфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОӨПРСТУҮФХЦЧШЩЪЫЬЭЮЯ", "abvgdeëžziiklmnoöprstuüfhcčšŝiyieûâABVGDEЁŽZIIKLMNOÖPRSTUÜFHCČŠŜIYIEÛÂ")
strlist = {}
for c in sys.stdin.readlines():
	if '#text=' in c:
		str = c[6:61]
		print(str)
		cyril2 = re.findall(u"[\u0400-\u0500]+", str) 
		countTotal = re.findall(u"[\u0400-\u0500]+", str)
		print(cyril2)
		for word in cyril2:
		    count = strlist.get(word,0)
		    strlist[word] = count + 1
		    str_list = strlist.keys()
		
		for words in str_list:
		    print(strlist[word] / strlist[word], words, strlist[word])