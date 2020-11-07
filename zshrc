# for interactive shell

alias which=whence
alias cd='builtin cd'

# mc: don't clutter history
alias precmd=' precmd'

# avoid accidental execution from history by inhibiting saving in the first place
# (easier to mitigate than HISTORY_IGNORE, which in turn might be used for mkfs*)
alias kill=' kill'
alias halt=' halt'
alias init=' init'
alias poweroff=' poweroff'
alias reboot=' reboot'
alias shutdown=' shutdown'
alias telinit=' telinit'

# SYSTEM WIDE ALIASES ETC.
for i in /etc/shrc.d/**/*.sh(N); do
	. $i
done
unset i

setopt hist_ignore_space hist_ignore_all_dups list_packed transient_rprompt hist_verify

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
		function precmd () { print -Pn "\e]0;%n@%m: %~\a" }
		bindkey '^[[H' beginning-of-line >/dev/null 2>&1
		bindkey '^[[F' end-of-line >/dev/null 2>&1
		bindkey '^[[A' history-beginning-search-backward >/dev/null 2>&1
		bindkey '^[[B' history-beginning-search-forward >/dev/null 2>&1
		;;
esac
if [ "$TERM" = 'screen' ]; then
		screen_title () { print -Pn "\ek%n@%m: %~\e\\" }
		precmd_functions=(screen_title)
fi
