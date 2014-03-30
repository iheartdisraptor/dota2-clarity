import fileinput
import math

lines_per_alias = 5

# Calculate the line segments of a discretized circle
def getCircleSegments(x, y, radius, segments):
	# Calculate the angle step size
	angleStep = 2 * math.pi / segments

	currentStartAngle = 0
	currentEndAngle = angleStep 

	results = []

	# For each segment
	for i in range(segments):
		# Calculate the starting point
		x1 = round(x + radius * math.cos(currentStartAngle), 4)
		y1 = round(y + radius * math.sin(currentStartAngle), 4)

		# Calculate the ending point
		x2 = round(x + radius * math.cos(currentEndAngle), 4)
		y2 = round(y + radius * math.sin(currentEndAngle), 4)

		# Advance angles
		currentStartAngle = currentStartAngle + angleStep
		currentEndAngle = currentEndAngle + angleStep

		# Add the coordinates to the list
		results.append([x1, y1, x2, y2])

	return results

# open output file
outputFile = open('tower_circles.cfg', 'w')

##


# Generate toggle aliases

# Build list of names
nameList = []
for line in fileinput.input('circles_in.txt'):
	tokens = line.split()
	if len(tokens) != 6:
		continue
	nameList.append(tokens[5])
numPairs = int(len(nameList) / 2)

outputFile.write('alias toggle_tower_prev toggle_tower_' + str(numPairs-1) + '\n')
outputFile.write('alias toggle_tower_next toggle_tower_1\n')

# For each two names
for index in range(numPairs):
	prevIndex = index - 1
	nextIndex = index + 1
	if prevIndex == -1:
		prevIndex = numPairs - 1
	if nextIndex == numPairs:
		nextIndex = 0
	# Create toggle step
	outputFile.write(
		'alias toggle_tower_' + str(index) + ' \"' +
		'echo Displaying tower ranges: ' + nameList[index*2] + ', ' + nameList[index*2+1] + '; ' +
		'tower_' + nameList[index*2] + '; tower_' + nameList[index*2+1] + '; ' +
		'alias toggle_tower_prev toggle_tower_' + str(prevIndex) + '; ' +
		'alias toggle_tower_next toggle_tower_' + str(nextIndex) + '\"\n')

outputFile.write('\n')

##

# Generate actual circle drawing aliases
# for each line
for line in fileinput.input('circles_in.txt'):
	# Split the line into 6 strings
	tokens = line.split()
	if len(tokens) != 6:
		continue

	# Get x, y, z, radius, segments as floats
	x = float(tokens[0])
	y = float(tokens[1])
	z = float(tokens[2])
	radius = float(tokens[3])
	segments = int(tokens[4])
	name = tokens[5]

	# Draw circle to get list of line segments
	segmentList = getCircleSegments(x, y, radius, segments)

	# Generate main alias
	outputFile.write('alias tower_' + name + ' \"')
	aliases = int(segments / lines_per_alias)
	for index in range(aliases):
		outputFile.write('tower_' + name + '_' + str(index) + '; ')
	outputFile.write('\"\n')

	# Generate drawlines commands

	lineCount = 0
	aliasCount = 0

	outputFile.write('alias tower_' + name + '_' + str(aliasCount) + ' \"')

	# For each line segment
	for segment in segmentList:

		# Output the drawline command
		outputFile.write('drawline ')
		outputFile.write(
			str(segment[0]) + ' ' +
			str(segment[1]) + ' ' +
			str(z) + ' ')
		outputFile.write(
			str(segment[2]) + ' ' +
			str(segment[3]) + ' ' +
			str(z) + '; ')

		lineCount = lineCount + 1

		if lineCount == lines_per_alias:
			lineCount = 0
			aliasCount = aliasCount + 1
			outputFile.write('\"\n')

			if aliasCount != aliases:
				outputFile.write(
					'alias tower_' + name +
					'_' + str(aliasCount) + ' \"')

	outputFile.write('\n')

outputFile.close()
