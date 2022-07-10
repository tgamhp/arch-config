#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls -lah --color=auto'
alias grep='grep --color=auto'

### "vim" as manpager
export MANPAGER='/bin/bash -c "vim -MRn -c \"set buftype=nofile showtabline=0 ft=man ts=8 nomod nolist norelativenumber nonu noma\" -c \"normal L\" -c \"nmap q :qa<CR>\"</dev/tty <(col -b)"'


#############################
# Shell prompt customization
#############################

# Function to construct color values in rgb
# \e is the same as \033 (both are used to start color code)
# all are mandatory except for the arguments:
# 	$1 Red value
# 	$2 Green value
# 	$3 Blue value
# 	$4 text style
#
# Text Styles:
# 0 -> Normal text
# 1 -> Bold or light text (depending on terminal emulator) 
# 2 -> Dim text
# 3 -> Italicized bold text 
# 4 -> Underlined text
# 5 -> Blinking text (doesn't work in most terminal emulators)
# 7 -> Reversed text (inverts the foreground and background colors)
# 8 -> Hidden text
#
# REMEMBER: 
#	'echo' is used to return values
#	'return' is used for exit codes (between 0 and 255), 0 means success

color_construct () {
   echo "\[\e[0$4;38;2;$1;$2;$3m\]"
}

blue="$(color_construct 102 204 204 1)"
red="$(color_construct 204 102 102 1)"
green="$(color_construct 153 204 102 1)"
yellow="$(color_construct 204 204 102 1)"
white="$(color_construct 255 255 255 0)"
reset="\[$(tput sgr0)\]"

PS1="\n${red}┌──${green}[${red}\u${green}@${green}\h${green}]-${yellow}[\w] \n${red}└──${green}\$ ${reset}"
