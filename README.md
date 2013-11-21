dota2-clarity
=============

dota2-clarity features custom console commands and training missions for Dota 2.

Features
--------

* Cheat key bindings add convenience in practice lobbies
* Advanced spectator controls make active spectating easier
* Disable HUD partially or entirely
* Display neutral camp spawn boxes
* Seven grouped chat wheels that encapsulate almost every response
* Practice drills
  - These aliases can be used in a local practice game to train a specific skill
  - Warding
  - Juke paths
  - Lasthitting under towers
  - Stacking and pulling
  - Tower range
* Custom training missions
  - Pull camp warding
  - Rune warding
  - Radiant juke paths
* Various useful console variables
  - Health bar settings
  - Minimap icon settings
  - Gameplay settings
  - net_graph
* Various other aliases and key bindings to augment your Dota 2 experience
  - Quick courier
  - Cycle camera focus between runes and hero

Credits
-------

* Cyborgmatt for the original HUD disabling commands
* devilesk for the exact neutal spawn camp box coordinates
* Various Reddit threads

Usage
-----

The file structure is designed so that you can include only the parts of
dota2-clarity that you want to use and ignore the rest. This works by keeping
all files in .../dota/cfg/clarity and exec'ing them from your autoexec.cfg.

Installation
------------

1. Copy the dota/cfg/clarity folder itself to
   Steam/SteamApps/common/dota 2 beta/dota/cfg.
2. Copy all custom_*.txt files from dota/scripts/tutorial to
   Steam/SteamApps/common/dota 2 beta/dota/scripts/tutorial.
3. Enable the Dota 2 console:
   http://wyksblog.com/guide-activating-the-console-in-dota-2/

Enable Only Training Missions
-----------------------------

1. In your Steam/SteamApps/common/dota 2 beta//dota/cfg/autoexec.cfg file,
   add "exec clarity/tutorials.cfg".
2. Restart Dota 2, open the console, and enter one of the commands to start
   a training mission, e.g. "tutorial_radiant_juke_paths",
   "tutorial_pull_wards", or "tutorial_rune_wards".

Enable All
----------

1. In your Steam/SteamApps/common/dota 2 beta//dota/cfg/autoexec.cfg file,
   add "exec clarity/autoexec.cfg".

Enable Some
-----------

1. Open clarity/autoexec.cfg and clarity/binds.cfg.
2. Copy the lines that include the features you want.

Ownership
---------

These scripts belong to the community. Feel free to extend them and share
your changes.
