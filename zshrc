# for interactive shell

alias which=whence
alias cd='builtin cd'
alias precmd=' precmd'

setopt hist_ignore_space hist_ignore_all_dups list_packed transient_rprompt

bindkey -e >/dev/null 2>&1

bindkey `tput khome` beginning-of-line >/dev/null 2>&1
bindkey `tput kend` end-of-line >/dev/null 2>&1
bindkey `tput kich1` quoted-insert >/dev/null 2>&1
bindkey `tput kdch1` delete-char >/dev/null 2>&1
bindkey `tput kpp` up-history >/dev/null 2>&1
bindkey `tput knp` end-of-history >/dev/null 2>&1
bindkey `tput kcuu1` history-beginning-search-backward >/dev/null 2>&1
bindkey `tput kcud1` history-beginning-search-forward >/dev/null 2>&1

case "$TERM" in
	xterm*)
		precmd () { print -Pn "\e]0;%n@%m: %~\a" }
		bindkey '^[[H' beginning-of-line >/dev/null 2>&1
		bindkey '^[[F' end-of-line >/dev/null 2>&1
		;;
esac
