freq = 0
lines = []

with open('input.txt','r') as f:
	lines = f.readlines()

for line in lines:
	try:
		freq += int(line)
	except ValueError:
		print('Invalid input  %s' % line)

print(freq)