; Dota 2 controls

#IfWinActive DOTA 2

; Swap ctrl and alt
*LCtrl::SendInput {Blind}{LAlt Down}
*LCtrl Up::SendInput {Blind}{LAlt Up}
*LAlt::SendInput {Blind}{LCtrl Down}
*LAlt Up::SendInput {Blind}{LCtrl Up}

#IfWinActive

; Controls for all programs

; Swap capslock and scrolllock for using capslock button as a PTT
; without affecting the capslock state.
CapsLock::ScrollLock
ScrollLock::CapsLock

; Toggle autohotkey on/off with win+`
#`::Suspend Toggle
