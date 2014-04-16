#!/usr/bin/env python

# Highest index accepted by the chatwheel_say console command
MAX_PHRASE_INDEX = 70

# Number of phrases available to chatwheel_say (include index 0)
NUM_PHRASES = MAX_PHRASE_INDEX + 1

# Number of phrases on a chatwheel
PHRASES_PER_CHATWHEEL = 8

# Number of chatwheels necessary
NUM_CHATWHEELS = NUM_PHRASES / PHRASES_PER_CHATWHEEL

# Open the output file for writing
output = open('chatwheel.cfg', 'w')

# For each chatwheel
for chatwheel in enumerate(NUM_CHATWHEELS):
	output.write('alias chat{}\n')

# Close the output file
output.close()
