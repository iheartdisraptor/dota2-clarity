; Toggle Autohotkey script with win+`
#`::Suspend Toggle

;; Dota 2 controls ;;

#IfWinActive DOTA 2

; Swap ctrl and alt
*LCtrl::SendInput {Blind}{LAlt Down}
*LCtrl Up::SendInput {Blind}{LAlt Up}
*LAlt::SendInput {Blind}{LCtrl Down}
*LAlt Up::SendInput {Blind}{LCtrl Up}

#IfWinActive

;; Controls for all programs ;;

; Swap capslock and scrolllock for using capslock button as a PTT without affecting the capslock state.
CapsLock::ScrollLock
ScrollLock::CapsLock

;; Windows key controls ;;

;; Use qwas to change workspaces
;#q::SendInput {LCtrl Down}{LAlt Down}{q Down}
;#q up::SendInput {LCtrl Up}{LAlt Up}{q Up}
;#w::SendInput {LCtrl Down}{LAlt Down}{w Down}
;#w up::SendInput {LCtrl Up}{LAlt Up}{w Up}
;#a::SendInput {LCtrl Down}{LAlt Down}{a Down}
;#a up::SendInput {LCtrl Up}{LAlt Up}{a Up}
;#s::SendInput {LCtrl Down}{LAlt Down}{s Down}
;#s up::SendInput {LCtrl Up}{LAlt Up}{s Up}
;
;; Use edc to position windows in top corners, sides, and bottom corners
;#e::SendInput {LCtrl Down}{LAlt Down}{Numpad7 Down}
;#e up::SendInput {LCtrl Up}{LAlt Up}{Numpad7 Up}
;#d::SendInput {LCtrl Down}{LAlt Down}{Numpad4 Down}
;#d up::SendInput {LCtrl Up}{LAlt Up}{Numpad4 Up}
;#c::SendInput {LCtrl Down}{LAlt Down}{Numpad1 Down}
;#c up::SendInput {LCtrl Up}{LAlt Up}{Numpad1 Up}
;
;; Use zx to move windows between screens
;#z::SendInput {LCtrl Down}{LAlt Down}{1 Down}
;#z up::SendInput {LCtrl Up}{LAlt Up}{1 Up}
;#x::SendInput {LCtrl Down}{LAlt Down}{2 Down}
;#x up::SendInput {LCtrl Up}{LAlt Up}{2 Up}
;
;; Use v to maximize windows
;#v::SendInput {LCtrl Down}{LAlt Down}{PgUp Down}
;#v up::SendInput {LCtrl Up}{LAlt Up}{PgUp Up}
;
;; Launch often used programs with rtfg
;#r::Run explorer C:\Users\mahsman
;#t::Run explorer C:\
;#f::Run chrome
;#g::Run chrome.exe --incognito

;; ctrl+alt key controls ;;

;; Use qwas to change workspaces
;^!q::SendInput {LCtrl Down}{LAlt Down}{q Down}
;^!q up::SendInput {LCtrl Up}{LAlt Up}{q Up}
;^!w::SendInput {LCtrl Down}{LAlt Down}{w Down}
;^!w up::SendInput {LCtrl Up}{LAlt Up}{w Up}
;^!a::SendInput {LCtrl Down}{LAlt Down}{a Down}
;^!a up::SendInput {LCtrl Up}{LAlt Up}{a Up}
;^!s::SendInput {LCtrl Down}{LAlt Down}{s Down}
;^!s up::SendInput {LCtrl Up}{LAlt Up}{s Up}
;
;; Use edc to position windows in top corners, sides, and bottom corners
;^!e::SendInput {LCtrl Down}{LAlt Down}{Numpad7 Down}
;^!e up::SendInput {LCtrl Up}{LAlt Up}{Numpad7 Up}
;^!d::SendInput {LCtrl Down}{LAlt Down}{Numpad4 Down}
;^!d up::SendInput {LCtrl Up}{LAlt Up}{Numpad4 Up}
;^!c::SendInput {LCtrl Down}{LAlt Down}{Numpad1 Down}
;^!c up::SendInput {LCtrl Up}{LAlt Up}{Numpad1 Up}
;
;; Use zx to move windows between screens
;^!z::SendInput {LCtrl Down}{LAlt Down}{1 Down}
;^!z up::SendInput {LCtrl Up}{LAlt Up}{1 Up}
;^!x::SendInput {LCtrl Down}{LAlt Down}{2 Down}
;^!x up::SendInput {LCtrl Up}{LAlt Up}{2 Up}
;
;; Use v to maximize windows
;^!v::SendInput {LCtrl Down}{LAlt Down}{PgUp Down}
;^!v up::SendInput {LCtrl Up}{LAlt Up}{PgUp Up}
;
;; Launch often used programs with rtfg
;^!r::Run explorer C:\Users\mahsman
;;^!t::Run explorer C:\
;^!t::Run explorer /e,::{20D04FE0-3AEA-1069-A2D8-08002B30309D}
;^!f::Run chrome
;^!g::Run chrome.exe --incognito
