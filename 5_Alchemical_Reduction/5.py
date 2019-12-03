import string
import sys

def reduceSequence(sequence):
	if len(sequence) < 2:
		return sequence
	elif len(sequence) == 2:
		c1 = sequence[0]
		c2 = sequence[1]
		if c1.lower() == c2.lower():
			if (c1.islower() and c2.isupper()) or (c2.islower() and c1.isupper()):
				return ''
		return sequence	
	else:
		firstHalf = reduceSequence(sequence[:int(len(sequence)/2)])
		secondHalf = reduceSequence(sequence[int(len(sequence)/2):])
		middle = ''
		while(len(middle)!=2 and len(firstHalf)!=0 and len(secondHalf)!=0):
			middle = reduceSequence(firstHalf[-1:] + secondHalf[:1])
			firstHalf = firstHalf[:-1]
			secondHalf = secondHalf[1:]
		return firstHalf + middle + secondHalf

sequence = ''
with open('input.txt', 'r') as f:
	sequence = f.readlines()[0]

#Challenge 1
reducedLength = 0	
if len(sequence) % 2 == 1:
	sequence = sequence + ' '
	reducedLength = -1
reducedLength += len(reduceSequence(sequence))
print(reducedLength)

# Challenge 2
minLength = sys.maxsize
alphabet = string.ascii_lowercase
for char in alphabet:
	reducedLength = 0
	sequenceClone = sequence[:].replace(char, '').replace(char.upper(), '')
	if len(sequenceClone) % 2 == 1:
		sequenceClone += ' '
		reducedLength = -1
	reducedLength += len(reduceSequence(sequenceClone))
	if reducedLength < minLength:
		minLength = reducedLength
print(minLength)