with open('2_input.txt','r') as f:
	lines = f.readlines()
	two = 0
	three = 0

	for line in lines:
		line = sorted(line.strip())
		count = 1
		c = line[0]
		c2 = 1
		hasTwo = False
		hasThree = False
	
		while(c2 < len(line)):
			if c == line[c2]:
			count += 1
			else:
			if count == 2:
				hasTwo = True
				if hasThree:
					break
			if count == 3:
				hasThree = True
				if hasTwo:
					break
			count = 1

			c = line[c2] 
			c2 += 1

		if hasTwo or count == 2:
			two += 1
		if hasThree or count == 3:
			three += 1

	print(two*three)