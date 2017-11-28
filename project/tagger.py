import sys
import csv
word = []
for s in sys.stdin:
		s = s.split()
		if len(s) >1:
			word.append(s[1])

else:
	with open("model.tsv") as tsvfile:	
		tsv = csv.reader(tsvfile)
		for t in tsv:																			
			print(t)