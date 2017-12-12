import sys

sent_id=1
 
for c in sys.stdin.readlines():
	number=1
	c=c.strip()
	c=c.replace('.', ' .')
	c=c.replace(',', ' ,')
	c=c.replace(':', ' :')
	c=c.replace(';', ' ;')
	c=c.split(' ')
	
	print('#sent_id=%d'%(sent_id))
	print('#text=',' '.join(c))
	for a in c:
		print('%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_'%(number,a))
		number=number+1
	sent_id=sent_id+1
        
	