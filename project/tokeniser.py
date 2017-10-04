import sys

sent_id=1
 
for c in sys.stdin.readlines():
	number=1
	c=c.replace('.', ' .')
	c=c.replace(',', ' ,')
	c=c.replace(':', ' :')
	c=c.replace(';', ' ;')
	c=c.split(' ')
	print(sent_id)
	for a in c:
		print(number, a,'_\t_\t_\t_\t_\t_\t_\t_')
		number=number+1
	sent_id=sent_id+1

	