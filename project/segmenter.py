import sys

for c in sys.stdin.read():
	print(c.replace('.', '.\n'), end='')