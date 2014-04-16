#!/usr/bin/env python

import math

# Keys to be used for chat wheels
KEYS = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l']

# Highest index accepted by the chatwheel_say console command
MAX_PHRASE_INDEX = 70

# Number of phrases available to chatwheel_say (include index 0)
NUM_PHRASES = MAX_PHRASE_INDEX + 1

# Number of phrases on a chatwheel
PHRASES_PER_CHATWHEEL = 8

# Number of chatwheels necessary
NUM_CHATWHEELS = math.ceil(NUM_PHRASES / PHRASES_PER_CHATWHEEL)

# Open the output file for writing
output = open('chatwheel.cfg', 'w')

# For each chatwheel
for chatwheel in range(NUM_CHATWHEELS):
	output.write('bind {} "+chatwheel; chat{}"\n'.format(
		KEYS[chatwheel], chatwheel))

output.write('\n')

# For each chatwheel
for chatwheel in range(NUM_CHATWHEELS):
	output.write('alias chat{} "'.format(chatwheel))

	# Determine the phrase indices for this chatwheel
	start = chatwheel * PHRASES_PER_CHATWHEEL
	end = start + 8

	index = 0
	for phrase in range(start, end):
		output.write('chat_wheel_phrase_{} {}; '.format(index, phrase))
		index = index + 1
		if index > MAX_PHRASE_INDEX:
			index = MAX_PHRASE_INDEX

	output.write('"\n')

# Close the output file
output.close()
