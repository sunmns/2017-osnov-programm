import sys

lines=0
tokens=0
characters=0
vowels=0
syllables=0

for c in sys.stdin.read():
	if c in 'аэиоуеёйөүюя': 
		vowels=vowels+1
	if c=='/n':
		lines=lines+1
	characters=characters+1
	if c==' ':
		tokens=tokens+1
syllables=vowels/tokens

print(lines, tokens, characters, vowels, syllables)
