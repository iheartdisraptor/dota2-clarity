dota2-clarity
=============

dota2-clarity features custom console commands and training missions for Dota 2.

---
1. Features
-----------

* Cheat key bindings add convenience in practice lobbies
* Advanced spectator controls make active spectating easier
* Disable HUD partially or entirely
* Display neutral camp spawn boxes
* Display tower range circles
* Seven grouped chat wheels that encapsulate almost every response
* Practice drills (aliases and key bindings to be used in in a local game to
  practice specific skills; these are the training mission controls and setup
  without the training mission events)
  - Warding
  - Stacking and pulling
  - Juke paths
  - Lasthitting under towers
  - Tower range
* Custom training missions
  - Pull warding
  - Rune warding
  - Vision warding
  - Radiant juke paths
  - Dire juke paths
* Various useful console variables
  - Health bar settings
  - Minimap icon settings
  - Gameplay settings
  - Net graph to show FPS and ping
* Various other aliases and key bindings
  - Quick courier
  - Cycle camera focus between runes and hero

---
2. Quick Installation
---------------------

If you don't already have an autoexec.cfg, installation is easy. Simply copy
the cfg/ and scripts/ folders to Steam/SteamApps/common/dota 2 beta/dota/.
This will install and enable the aliases and tutorials (the bindings and
console variables will not be enabled by default; you should browse those
and use the ones you like).

If you do have an autoexec.cfg, copy the cfg/clarity/ folder to
Steam/SteamApps/common/dota 2 beta/dota/cfg and the scripts/tutorial/
folder to Steam/SteamApps/common/dota 2 beta/dota/scripts. Then add the
following to your autoexec.cfg:

    con_enable 1
    exec clarity/use_tutorials_and_aliases.cfg

---
3. Detailed Installation
------------------------

The file structure is designed so that you can include only the parts of
dota2-clarity that you want to use and ignore the rest. This works by keeping
all files in Steam/SteamApps/common/dota 2 beta/dota/cfg/clarity and `exec`uting
them from your autoexec.cfg.

1. Copy the cfg/clarity/ folder to
   Steam/SteamApps/common/dota 2 beta/dota/cfg.
2. Copy the scripts/tutorial/ folder to
   Steam/SteamApps/common/dota 2 beta/dota/scripts.

To enable only training missions and aliases (recommended):

3. In your Steam/SteamApps/common/dota 2 beta/dota/cfg/autoexec.cfg file,
   add `exec clarity/use_tutorials_and_aliases.cfg`.
4. Restart Dota 2, open the console, and enter one of the commands to start
   a training mission:
   * `train_radiant_juke_paths`
   * `train_dire_juke_paths`
   * `train_pull_wards`
   * `train_rune_wards`
   * `train_vision_wards`

To enable only some features (recommended):

3. Open clarity/use_all.cfg and clarity/example_binds.cfg.
4. Copy and modify the lines for the features you want to use into your
   autoexec.cfg.

To enable all features (not recommended):

3. In your Steam/SteamApps/common/dota 2 beta/dota/cfg/autoexec.cfg file,
   add `exec clarity/use_all.cfg`.

---
4. Usage
--------

Explore the clarity/ directory and read the documentation in the files that
interest you. Of particular interest is clarity/example_binds.cfg, which defines
key bindings for aliases defined by Clarity.

To use practice drills:

1. Start a local game with cheats enabled.
2. Open the console and enter the command to start the drill you want to run,
   e.g. `drill_juke_paths`.
3. Press the apostrophe key to print cheat keys to the console.

To use training missions:

1. At the main interface without a game started, open the console and enter the
   command to start the tutorial, e.g. `drill_rune_wards`.
2. Press the apostrophe key to print cheat keys to the console.

---
5. Credits
----------

* Cyborgmatt for the original HUD disabling commands
* devilesk for the exact neutal spawn camp box coordinates
* Filk for one of the early autoexec.cfg's
* TheParadoxataur (critwhale.com) for their map of juke paths
* Chudooder for their chat wheel generator
* gso's warding guide
* Various Reddit threads    

---
6. Ownership
------------

These scripts belong to the community. Feel free to extend them and share
your changes.

---
7. Changelog
------------

1.2-6.80

* Reorganized the file structure for ease of use and installation.
* Fixed an issue where the quest log does not appear in the tutorials due
  to a change in the way tutorial scripts are written.

1.1-6.79

* Added Dire juke paths training mission (`train_dire_juke_paths`).
* Added vision warding training mission (`train_vision_wards`).
* Fixed errors with the UI disablind aliases being too long.
* For convenience, to run tutorials you can type `train_...`
  instead of `tutorial_...`.
* Made it harder to override all your console settings with those from
  dota2-clarity.

1.0-6.79

* Initial release
