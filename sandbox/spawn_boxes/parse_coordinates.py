import fileinput
import re

outputFile = open('coordinates_out.txt', 'w')

lineCount = 0

for line in fileinput.input('coordinates.txt'):
	lineCount = lineCount + 1
	trimmed = re.sub('[()]', '', line)
	elements = trimmed.split()
	coords = []
	for element in elements:
		coords.append(float(element))
	coords[2] = coords[2] + 10
	coords[8] = coords[8] + 10
	coordsStr = []
	for coord in coords:
		coordsStr.append(str(coord))
	#outputFile.write('box ' + elements[0] + ' ' + elements[1] + ' ' + elements[2] + ' ' + elements[6] + ' ' + elements[7] + ' ' + elements[8] + '\n')
	outputFile.write('box ' + coordsStr[0] + ' ' + coordsStr[1] + ' ' + coordsStr[2] + ' ' + coordsStr[6] + ' ' + coordsStr[7] + ' ' + coordsStr[8] + '\n')
	if lineCount == 6:
		lineCount = 0;
		outputFile.write('\n')

outputFile.close()

#input()
