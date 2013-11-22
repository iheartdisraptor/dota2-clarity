dota2-clarity
=============

dota2-clarity features custom console commands and training missions for Dota 2.

1. Features
-----------

* Cheat key bindings add convenience in practice lobbies
* Advanced spectator controls make active spectating easier
* Disable HUD partially or entirely
* Display neutral camp spawn boxes
* Seven grouped chat wheels that encapsulate almost every response
* Practice drills (aliases and key bindings to be used in in a local game to
  practice specific skills)
  - Warding
  - Stacking and pulling
  - Juke paths
  - Lasthitting under towers
  - Tower range
* Custom training missions
  - Pull warding
  - Rune warding
  - Radiant juke paths
* Various useful console variables
  - Health bar settings
  - Minimap icon settings
  - Gameplay settings
  - Net graph to show FPS and ping
* Various other aliases and key bindings
  - Quick courier
  - Cycle camera focus between runes and hero

2. Installation
---------------

The file structure is designed so that you can include only the parts of
dota2-clarity that you want to use and ignore the rest. This works by keeping
all files in .../dota/cfg/clarity and exec'ing them from your autoexec.cfg.

1. Copy the dota/cfg/clarity folder itself to
   Steam/SteamApps/common/dota 2 beta/dota/cfg.
2. Copy all custom_*.txt files from dota/scripts/tutorial to
   Steam/SteamApps/common/dota 2 beta/dota/scripts/tutorial.
3. Enable the Dota 2 console:
   http://wyksblog.com/guide-activating-the-console-in-dota-2/

To enable all features:

1. In your Steam/SteamApps/common/dota 2 beta//dota/cfg/autoexec.cfg file,
   add "exec clarity/autoexec.cfg".

To enable only some features:

1. Open clarity/autoexec.cfg and clarity/binds.cfg.
2. Copy the lines that include the features you want.

To enable only training missions:

1. In your Steam/SteamApps/common/dota 2 beta//dota/cfg/autoexec.cfg file,
   add "exec clarity/tutorials.cfg".
2. Restart Dota 2, open the console, and enter one of the commands to start
   a training mission, e.g. "tutorial_radiant_juke_paths",
   "tutorial_pull_wards", or "tutorial_rune_wards".

3. Usage
--------

Explore the clarity/ directory and read the documentation in the files that
interest you. Of particular interest is clarity/binds.cfg, which defines
key bindings for aliases defined by Clarity.

To use practice drills:

1. Start a local game with cheats enabled.
2. Open the console and enter the command to start the drill you want to run,
   e.g. "drill_juke_paths".
3. Press the apostrophe key to print cheat keys to the console.

To use training missions:

1. At the main interface without a game started, open the console and enter the
   command to start the tutorial, e.g. "drill_rune_wards".
2. Press the apostrophe key to print cheat keys to the console.

4. Credits
----------

* Cyborgmatt for the original HUD disabling commands
* devilesk for the exact neutal spawn camp box coordinates
* Filk for one of the early autoexec.cfg's
* TheParadoxataur (critwhale.com) for their map of juke paths
* Chudooder for their chat wheel generator
* Various Reddit threads

5. Ownership
------------

These scripts belong to the community. Feel free to extend them and share
your changes.
