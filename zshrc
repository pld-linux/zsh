# for interactive shell

alias which=whence
alias cd='builtin cd'
alias precmd=' precmd'

# SYSTEM WIDE ALIASES ETC.
for i in /etc/shrc.d/**/*.sh(N); do
	. $i
done
unset i

setopt hist_ignore_space hist_ignore_all_dups list_packed transient_rprompt

bindkey -e >/dev/null 2>&1

bindkey $terminfo[khome] beginning-of-line >/dev/null 2>&1
bindkey $terminfo[kend] end-of-line >/dev/null 2>&1
bindkey $terminfo[kich1] quoted-insert >/dev/null 2>&1
bindkey $terminfo[kdch1] delete-char >/dev/null 2>&1
bindkey $terminfo[kpp] up-history >/dev/null 2>&1
bindkey $terminfo[knp] end-of-history >/dev/null 2>&1
bindkey $terminfo[kcuu1] history-beginning-search-backward >/dev/null 2>&1
bindkey $terminfo[kcud1] history-beginning-search-forward >/dev/null 2>&1

PS1='[%n@%m %~]%(!.#.%\$) '

case "$TERM" in
	xterm*|nxterm|gnome*|rxvt*|konsole*)
		precmd () { print -Pn "\e]0;%n@%m: %~\a" }
		bindkey '^[[H' beginning-of-line >/dev/null 2>&1
		bindkey '^[[F' end-of-line >/dev/null 2>&1
		bindkey '^[[A' history-beginning-search-backward >/dev/null 2>&1
		bindkey '^[[B' history-beginning-search-forward >/dev/null 2>&1
		;;
esac
