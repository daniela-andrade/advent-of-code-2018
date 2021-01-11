import operator
import re

lines = []
# id -> time sleeping
records = dict()
times = dict()
guard = ''
start = -1


def addRecord(time, recordType):
	global guard
	global start

	#print('Adding record: %s, %s' %(recordType, time))

	if recordType[0] == '#':
		try:
			guard = int(recordType[1:])
			if guard not in records:
				records[guard] = [0] * 60
				times[guard] = 0
		except ValueError:
			print('%s is not an int' % recordType)
		

	elif recordType == 'falls' and guard != '':
		try:
			start = int(time)
		except ValueError:
			print('%s is not an int' % time)

	elif guard != '' and start != -1:
		try:
			end = int(time)
			for minute in range(start, end):
				records[guard][minute] += 1
			times[guard] += (end - start)
		except ValueError:
			print('%s is not an int' % time)


def getMaxRecord_strategyOne():
	timesSorted = sorted(times.items(), key=operator.itemgetter(1), reverse=True)
	guardId = timesSorted[0][0]
	allMinutes = records[timesSorted[0][0]]
	maxMinute = allMinutes.index(max(allMinutes))
	
	return guardId * maxMinute

def getMaxRecord_strategyTwo():
	globalMax = 0
	guardId = ''
	for record in records:
		recordMax = max(records[record])
		if (recordMax > globalMax):
			globalMax = recordMax
			guardId = record
	return guardId * records[guardId].index(globalMax)

with open('input.txt', 'r') as file:
	lines = sorted(file.readlines())

pattern = re.compile(r".*:(\d*).*(#\d*|falls|wakes)")
for line in lines:
	
	time, recordType = pattern.search(line).groups()
	addRecord(time, recordType)


print(getMaxRecord_strategyOne())
print(getMaxRecord_strategyTwo())