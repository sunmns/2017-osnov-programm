import sys

sent_id=1
dict = str.maketrans("абвгдеёжзийклмноөпрстуүфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОӨПРСТУҮФХЦЧШЩЪЫЬЭЮЯ", "abvgdeëžziiklmnoöprstuüfhcčšŝiyieûâABVGDEЁŽZIIKLMNOÖPRSTUÜFHCČŠŜIYIEÛÂ")

for c in sys.stdin.readlines():
	number=1
	c=c.replace('.', ' .')
	c=c.replace(',', ' ,')
	c=c.replace(':', ' :')
	c=c.replace(';', ' ;')
	c=c.split(' ')
	print('#sent_id=%d'%(sent_id))
	for a in c:
		print('%d\t%s\t_\t_\t_\t_\t_\t_\t_\ttranslit=%s'%(number,a,a.translate(dict)))
		number=number+1
	sent_id=sent_id+1
	
