This folder contains the main content of the console command library
dota2-clarity, including aliases, tutorials, key bindings, and cvars.

If you don't already have an autoexec.cfg, installation is easy. Simply copy
the contents of this folder to <Steam>/SteamApps/common/dota 2 beta/dota. This
will install the aliases and tutorials (but not the bindings or cvars, as those
should be specific to your setup).

If you do have an autoexec.cfg, copy the cfg/clarity/ folder to
<Steam>/SteamApps/common/dota 2 beta/dota/cfg and the scripts/tutorial folder to
<Steam>/SteamApps/common/dota 2 beta/dota/scripts. Then add the following to
your autoexec.cfg:

con_enable 1
exec clarity/use_tutorials_and_aliases.cfg
