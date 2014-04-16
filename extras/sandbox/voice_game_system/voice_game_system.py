#!/usr/bin/env python

from collections import OrderedDict

#
# Define the dictionary of phrase index to phrase.
# This data is courtesy of u/rer0tsaz.
# http://www.reddit.com/r/DotA2/comments/1imca4/chat_wheel_scripting/
#

phrases = {}
phrases[0]  = "Okay"
phrases[1]  = "Care"
phrases[2]  = "Get Back"
phrases[3]  = "Need Wards"
phrases[4]  = "Stun"
phrases[5]  = "Help"
phrases[6]  = "Push"
phrases[7]  = "Well played"
phrases[8]  = "Missing"
phrases[9]  = "Missing top"
phrases[10] = "Missing mid"
phrases[11] = "Missing bottom"
phrases[12] = "Go!"
phrases[13] = "Initiate!"
phrases[14] = "Follow me"
phrases[15] = "Group up"
phrases[16] = "Spread out"
phrases[17] = "Split farm"
phrases[18] = "Attack now!"
phrases[19] = "Be right back"
phrases[20] = "Dive!"
phrases[21] = "On my way"
phrases[22] = "Get ready"
phrases[23] = "Bait"
phrases[24] = "Heal"
phrases[25] = "Mana"
phrases[26] = "Out of mana"
phrases[27] = "Cooldown"
phrases[28] = "Ulti ready"
phrases[29] = "Returned"
phrases[30] = "All miss"
phrases[31] = "Incoming"
phrases[32] = "Invis enemy"
phrases[33] = "Enemy has rune"
phrases[34] = "Split push"
phrases[35] = "Coming to gank"
phrases[36] = "Request gank"
phrases[37] = "Under tower"
phrases[38] = "Deny tower"
phrases[39] = "Buy courier"
phrases[40] = "Upgrade courier"
phrases[41] = "We need detection"
phrases[42] = "They have detection"
phrases[43] = "Buy TP"
phrases[44] = "Re-use courier"
phrases[45] = "Deward"
phrases[46] = "Building Mek"
phrases[47] = "Building Pipe"
phrases[48] = "Stack and pull"
phrases[49] = "Pull creeps"
phrases[50] = "Pulling creeps"
phrases[51] = "Stack neutrals"
phrases[52] = "Jungling"
phrases[53] = "Roshan"
phrases[54] = "Affirmative"
phrases[55] = "Wait"
phrases[56] = "Pause"
phrases[57] = "Current Time"
phrases[58] = "Check runes"
phrases[59] = "Smoke gank!"
phrases[60] = "Good luck"
phrases[61] = "Nice"
phrases[62] = "Thanks"
phrases[63] = "Sorry"
phrases[64] = "Don't give up"
phrases[65] = "That just happened"
phrases[66] = "Game is hard"
phrases[67] = "New meta"
phrases[68] = "My bad"
phrases[69] = "Regret"
phrases[70] = "Relax"

#
# Setup
#

# Define array of keys to use (of size n, where n^2 >= MAX_PHRASE_INDEx)
KEYS = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l']

# Define the lead key (resets combination)
LEAD_KEY = 'n'

# Highest index accepted by the chatwheel_say console command
MAX_PHRASE_INDEX = len(phrases) - 1

# Number of phrases available to chatwheel_say (include index 0)
NUM_PHRASES = MAX_PHRASE_INDEX + 1

# Open the output file for writing
output = open('voice_game_system.cfg', 'w')

#
# Generate key combo dictionary
#

# Define the key combo dictionary
combos = OrderedDict()

phrase = 0

# For each key (first level)
for key1 in KEYS:
	# For each key (second level)
	for key2 in KEYS:
		# Add the combination to the dictionary with its chatwheel index
		combos[(key1, key2)] = phrase

		# Go to the next chatwheel phrase
		phrase = phrase + 1

#
# Output comments/documentation
#

output.write('''// Dota 2 Voice Game System by u/iheartdisraptor
//
// This config file implements a voice game system similar to the one used in
// Tribes, where players press a combination of keys to display various chat
// messages.
//
// Installation:
// 1. Copy this file to
//    Steam/SteamApps/common/dota 2 beta/dota/cfg/voice_game_system.cfg.
// 2. Create an autoexec.cfg in Steam/SteamApps/common/dota 2 beta/dota/cfg.
// 3. Edit your autoexec.cfg and add `exec voice_game_system.cfg` as a line.
// 4. Restart Dota 2 or enter `exec autoexec.cfg` into the console.
//
// Usage:
// 1. By default, the lead key is n (i.e. all key combinations start with n).
//    You can change this key below.
// 2. To say one of the 70 chat phrases, use the lead key plus two additional
//    keys from the set {y, u, i, o, p, h, j, k, l}.
// 3. If enabled, you will be able to see what combinations are available
//    in the top left corner (enabled by default, see below).
// 4. To see a master list of all commands, enter the console and enter
//    `vgs_help`. To see a list of commands for a specific key, enter
//    `vgs_help_<key>`, e.g. vgs_help_y.
// 5. Successive phrases from the same group (key) don't require you to
//    enter again the lead key and the group key. For example, to call
//    all lanes missing you could enter n - u - y - u - i. The first two
//    characters select the 'u' group of phrases and the last three
//    execute phrases from that group.
//

// Enable console output in the top left corner
developer 1

// Display the last 15 lines of the console in the top left corner
contimes 15

// Keep the console output in the top left corner for 8 seconds
con_notifytime 8

// Filter console output
//con_filter_enable 1

// Tag used to filter text
//con_filter_text [VGS]

''')

#
# Output lead key binding
#

output.write('// Bind the lead key, which resets the combination aliases\n')
output.write('bind {} "vgs_help_n; vgs_bind_key1"\n\n'.format(LEAD_KEY))

#
# Output display help command
#

output.write('alias vgs_help "')

# For each key (first level)
for key1 in KEYS:
	output.write('vgs_help_{}; '.format(key1))

output.write('"\n')

#
# Output display help command for lead key
#

output.write('alias vgs_help_{} "'.format(LEAD_KEY))
output.write('echo .; echo .; echo .; echo .; ')

# For each key (first level)
for key1 in KEYS:
	output.write('echo {0}{1} : {1} messages;'.format(LEAD_KEY, key1))

output.write('"\n')

#
# Output display help commands for individual keys
#

# For each key (first level)
for key1 in KEYS:
	output.write('alias vgs_help_{} "'.format(key1))
	output.write('echo .; echo .; echo .; echo .; ')

	# For each key (second level)
	for key2 in KEYS:
		# Get the phrase for the key combo
		index = combos[(key1, key2)]
		if index <= MAX_PHRASE_INDEX:
			phrase = phrases[index]
		else:
			phrase = "Undefined"

		output.write('echo {}{}{} : {}; '.format(
			LEAD_KEY, key1, key2, phrase))

	output.write('"\n')

output.write('\n')

#
# Output second level binding aliases
#

# For each key (first level)
for key1 in KEYS:
	# Output alias to bind phrases for this key:

	output.write('alias vgs_bind_{} "'.format(key1))
	output.write('vgs_help_{}; '.format(key1))

	# For each key (second level):
	for key2 in KEYS:
		# Get the phrase index for this combo
		index = combos[(key1, key2)]

		output.write('bind {} chatwheel_say_{}; '.format(key2, index))

	output.write('"\n')

output.write('\n')

#
# Output first level binding alias
#

output.write('alias vgs_bind_key1 "')

# For each key (first level)
for key1 in KEYS:
	# Bind the alias to this key
	output.write('bind {0} vgs_bind_{0}; '.format(key1))

output.write('"\n')

output.write('\n')

#
# Output the chatwheel aliases (workaround for lack of nested quotes)
#

# For each possible chat phrase
for index, phrase in phrases.items():
	output.write('alias chatwheel_say_{0} "chatwheel_say {0}"\n'.format(index))

# Close the output file
output.close()
