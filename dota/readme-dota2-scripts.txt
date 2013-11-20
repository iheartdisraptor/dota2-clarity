// Dota 2 Autoexec Script Anita (Octavia, u/iheartdisraptor)

// Credits to Filk for an earlier version and various Reddit threads on autoexec
// scripts. This script belongs to the community. Feel free to extend and
// rerelease this script.

// Installation:
// 1. Place all *.cfg files in Steam/SteamApps/common/dota 2 beta/dota/cfg.
// 2. Restart Dota 2.

// Notes:
// - Some keys may not work until you unbind them in the GUI settings (top left
//   corner of start screen).
// - Many console variables are boolean (0 means off and 1 means on), so they
//   can be enabled/disabled that way.
// - To disable a line, use '//' at the beginning of the line, like this one.

// Changelog:
// 1.4-6.79, 13.11.18
// - Added gameui_activate on F1 and escape to close UI
// - Added command to display spawn boxes
// - Added training mission camp warding
// - Added net_graphpos 0 to fix a disappearing net grpah
// - Added Culling Blade thresholds to F3 health per marker toggler
// - Reorganized drills into component scripts
// 1.3, 13.11.11
// - Added advanced spectator controls with F7 (enabled by default or entering
//   spectator_controls in console)
// - Moved reload autoexec button to F10
// - Combined debug output into a toggle button (F11)
// - Improved cheats
//   - Combined cheat keys into a toggle button (F8)
//   - Added free_camera and fixed_camera bound to toggle on KP_DIVIDE
//   - Added controls for setting camera distance (-/+/* on keypad)
// - Added options for the courier message, including no message
// - dota_range_display now defaults to 1300 (XP range)
// - Improved organization, documentation, and comments
// 1.2, 13.11.05
// - Added net graph positioning for 1920x1080
// - Added keys to enable/disable debug output
// - Added key to exec autoexec.cfg
// - Improved organization and comments
// - Fixed "unknown command 's'" bug
// - Moved alias to before drills
// 1.1, 13.11.04
// - Added right click deny (credits to Jakeyzz)
// - Added minimap icon scaling by heroes distance from each other
//   (credits to gramathy)
// 1.0, 13.11.04
// - Initial version