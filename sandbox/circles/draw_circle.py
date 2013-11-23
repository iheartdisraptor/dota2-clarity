import fileinput
import math

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
outputFile = open('circles_out.cfg', 'w')

# for each line
for line in fileinput.input('circles_in.txt'):
	# Split the line into 5 strings
	tokens = line.split()

	# Get x, y, z, radius, segments as floats
	x = float(tokens[0])
	y = float(tokens[1])
	z = float(tokens[2])
	radius = float(tokens[3])
	segments = int(tokens[4])

	# Draw circle to get list of line segments
	segmentList = getCircleSegments(x, y, radius, segments)

	# For each line segment
	for segment in segmentList:
		# Output the drawline command
		outputFile.write('drawline ')
		outputFile.write(str(segment[0]) + ' ' + str(segment[1]) + ' ' + str(z) + ' ')
		outputFile.write(str(segment[2]) + ' ' + str(segment[3]) + ' ' + str(z) + '\n')

	outputFile.write('\n')

outputFile.close()
