def LevenshteinDifference(s1,s2):
	distances = [[-1 for x in range(len(s2)+1)] for y in range(len(s1)+1)] 

	def getLevenshteinDifference(i,j):

		if min(i,j) == 0:
			distances[i][j] = max(i,j)
			return max(i,j)

		if distances[i-1][j] != -1:
			delete = distances[i-1][j] + 1
		else:
			delete = getLevenshteinDifference(i-1,j) + 1

		if distances[i][j-1] != -1:
			insert = distances[i][j-1] + 1
		else:
			insert = getLevenshteinDifference(i,j-1) + 1
		
		if distances[i-1][j-1] != -1:
			substitute = distances[i-1][j-1]
		else:
			substitute = getLevenshteinDifference(i-1,j-1)

		if(s1[i-1]!=s2[j-1]):
			substitute += 1

		cost = min(delete,insert,substitute)
		distances[i][j] = cost
		return cost
		
	return getLevenshteinDifference(len(s1),len(s2))


with open('2_input.txt', 'r') as f:
	lines = f.readlines()
	word1 = ''
	word2 = ''
	cost = 1000

	for line1 in lines:
		for line2 in lines:
			
			if line1 != line2:
				newCost = LevenshteinDifference(line1, line2)
				if newCost < cost:
					cost = newCost
					word1 = line1
					word2 = line2
					if cost == 1:
						break
	
	print(word1)
	print(word2)
	print(cost)