#
# Conditional build:
# _without_static	- without static version
#
Summary:	Enhanced Bourne shell
Summary(de):	Enhanced Bourne Shell
Summary(es):	Shell bourne mejorada
Summary(fr):	Bourne shell amélioré
Summary(pl):	Ulepszona pow³oka Bourne'a
Summary(pt_BR):	Shell bourne melhorada
Summary(ru):	ëÏÍÁÎÄÎÙÊ ÐÒÏÃÅÓÓÏÒ (shell) ÐÏÈÏÖÙÊ ÎÁ ksh, ÎÏ Ó ÕÌÕÞÛÅÎÉÑÍÉ
Summary(tr):	Geliþmiþ bir BASH sürümü
Summary(uk):	ëÏÍÁÎÄÎÉÊ ÐÒÏÃÅÓÏÒ (shell) ÓÈÏÖÉÊ ÎÁ ksh, ÁÌÅ Ú ÐÏËÒÁÝÅÎÎÑÍÉ
Name:		zsh
Version:	4.1.1
Release:	8
License:	BSD-like
Group:		Applications/Shells
URL:		http://www.zsh.org/
Source0:	ftp://ftp.zsh.org/pub/zsh/%{name}-%{version}.tar.bz2
# Source0-md5:	48958b1a3fc86261a26eea40a4f7d4af
Source1:	%{name}.1.pl
Source2:	http://zsh.sunsite.dk/Guide/zshguide.pdf
# Source2-md5:	0d80ba1ef39052c512cfabf368f3bf20
Patch0:		%{name}-info.patch
Patch1:		%{name}-tinfo.patch
Patch2:		%{name}-addons.patch
Patch3:		%{name}-paths.patch
Patch4:		%{name}-no_nis.patch
Patch5:		%{name}-completions.patch
Patch6:		%{name}-zle_misc.patch
BuildRequires:	autoconf
%{!?_without_static:BuildRequires:	glibc-static}
BuildRequires:	libcap-devel
BuildRequires:	ncurses-devel >= 5.1
%{!?_without_static:BuildRequires:	ncurses-static}
BuildRequires:	pcre-devel
BuildRequires:	texinfo
Requires(post,preun):	grep
Requires(preun):	fileutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	zsh-doc-html, zsh-doc-ps, zsh-doc-dvi

%define		_bindir		/bin
%define		specflags_ia32	"-fomit-frame-pointer"

%description
zsh is an enhanced version of the Bourne shell with csh additions and
most features of ksh, bash, and tcsh.

%description -l es
zsh es una versión mejorada del bourne shell con estas
características:
- muy próximo de la gramática del ksh/sh, con adiciones csh,
- varias características del ksh, bash y tcsh,
- 75 funciones empotradas, 89 opciones, 154 combinaciones de teclas,
- selección,
- funciones shell ...y mucho más.

%description -l ja
zsh ¥·¥§¥ë¤ÏÂÐÏÃÅª¤Ê¥í¥°¥¤¥ó¥·¥§¥ë¤È¤·¤ÆÍøÍÑ²ÄÇ½¤Ê¥³¥Þ¥ó¥É¥¤¥ó¥¿¥ê¥¿
¤Ç¤¢¤ê¡¢¥·¥§¥ë¥¹¥¯¥ê¥×¥È¥³¥Þ¥ó¥É¤â½èÍý¤Ç¤­¤Þ¤¹. zsh ¤Ï ksh(the Korn
shell) ¤Ë»÷¤Æ¤¤¤Þ¤¹¤¬,¤«¤Ê¤ê³ÈÄ¥¤µ¤ì¤Æ¤¤¤Þ¤¹. zsh
¤Ï¥³¥Þ¥ó¥É¥é¥¤¥ó¤Ç¤ÎÊÔ½¸µ¡Ç½, ÁÈ¤ß¹þ¤Þ¤ì¤¿¥¹¥Ú¥ë½¤Àµµ¡Ç½, ¥×¥í¥°¥é¥ß¥ó
¥°²ÄÇ½¤Ê¥³¥Þ¥ó¥ÉÊä´°µ¡Ç½, (Æ°Åª¥í¡¼¥É¤µ¤ì¤ë)¥·¥§¥ëµ¡Ç½, ¥Ò¥¹¥È¥êµ¡¹½
¤Ê¤É¤ò»ý¤Á¤Þ¤¹.

%description -l pl
zsh jest ulepszon± pow³ok± Bourne'a z elementami pow³oki csh. Posiada
wiêkszo¶æ cech ksh, bash i tcsh.

%description -l pt_BR
zsh é uma versão melhorada do bourne shell com essas características:
- muito próximo da gramática do ksh/sh, com adições csh,
- várias características do ksh, bash e tcsh,
- 75 funções embutidas, 89 opções, 154 combinações de teclas,
- seleção,
- funções shell ...e muito mais.

%description -l ru
zsh - ÜÔÏ ËÏÍÁÎÄÎÙÊ ÐÒÏÃÅÓÓÏÒ ÎÁÐÏÍÉÎÁÀÝÉÊ ksh (Korn shell), ÎÏ
×ËÌÀÞÁÀÝÉÊ ÍÎÏÇÏ ÕÌÕÞÛÅÎÉÊ. zsh ÐÏÄÄÅÒÖÉ×ÁÅÔ ÒÅÄÁËÔÉÒÏ×ÁÎÉÅ ËÏÍÁÎÄÎÏÊ
ÓÔÒÏËÉ, ×ÓÔÒÏÅÎÎÕÀ ËÏÒÒÅËÃÉÀ ÎÁÐÉÓÁÎÉÑ, ÐÒÏÇÒÁÍÍÉÒÕÅÍÏÅ ÚÁ×ÅÒÛÅÎÉÅ
ËÏÍÁÎÄ, shell-ÆÕÎËÃÉÉ (Ó Á×ÔÏÚÁÇÒÕÚËÏÊ), ÉÓÔÏÒÉÀ ËÏÍÁÎÄ É ÍÎÏÇÏÅ
ÄÒÕÇÏÅ.

%description -l uk
zsh - ÃÅ ËÏÍÁÎÄÎÉÊ ÐÒÏÃÅÓÏÒ, ÝÏ ÎÁÇÁÄÕ¤ ksh (Korn shell), ÁÌÅ ×ËÌÀÞÁ¤
ÂÁÇÁÔÏ ÐÏËÒÁÝÅÎØ. zsh Ð¦ÄÔÒÉÍÕ¤ ÒÅÄÁÇÕ×ÁÎÎÑ ËÏÍÁÎÄÎÏÇÏ ÒÑÄËÁ,
×ÂÕÄÏ×ÁÎÕ ËÏÒÅËÃ¦À ÎÁÐÉÓÁÎÎÑ, ÐÒÏÇÒÁÍÏ×ÁÎÅ ÚÁ×ÅÒÛÅÎÎÑ ËÏÍÁÎÄ,
shell-ÆÕÎËÃ¦§ (Ú Á×ÔÏÚÁ×ÁÎÔÁÖÅÎÎÑÍ), ¦ÓÔÏÒ¦À ËÏÍÁÎÄ ÔÁ ÂÁÇÁÔÏ ¦ÎÛÏÇÏ.

%package completions
Summary:	Files needed for advanced TAB-completion
Summary(pl):	Pliki potrzebne dla zaawansowanej TAB-completion
Group:		Applications/Shells
Requires:	%{name} = %{version}

%description completions
This package contains files needed for advanced tab completion in zsh.

%description completions -l pl
Ten pakiet zawiera pliki wymagane przez zsh dla zaawansowanej
TAB-completion.

%package static
Summary:	Statically linked Enhanced Bourne shell
Summary(pl):	Zaawansowana pow³oka Bourne'a - skonsolidowana statycznie
Group:		Applications/Shells
Requires(post,preun):	grep
Requires(preun):	fileutils
Requires:	%{name} = %{version}

%description static
zsh is an enhanced version of the Bourne shell with csh additions and
most features of ksh, bash, and tcsh.

%description static -l pl
zsh jest ulepszon± pow³ok± Bourne'a z elementami pow³oki csh. Posiada
wiêkszo¶æ cech ksh, bash i tcsh. W tym pakiecie jest wersja
skonsolidowana statycznie.

%package guide
Summary:	A User's Guide to the Z-Shell
Summary(pl):	Podrêcznik U¿ytkownika Z-Shella
Group:		Applications/Shells
URL:		http://zsh.sunsite.dk/Guide/

%description guide
A User's Guide to the Z-Shell.

%description guide -l pl
Podrêcznik U¿ytkownika Z-Shella.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p0

install %{SOURCE2} .

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}

%if %{!?_without_static:1}%{?_without_static:0}
LDFLAGS="%{rpmldflags} -static"
%configure \
	--disable-dynamic
%{__make} \
	DLLDFLAGS=""
mv -f Src/zsh Src/zsh.static
%{__make} clean || :
LDFLAGS="%{rpmldflags}"
%endif

%configure \
	--enable-maildir-support
%{__make}

cd Doc
makeinfo zsh.texi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_infodir},%{_sysconfdir},%{_bindir},%{_mandir}/pl/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{!?_without_static:install Src/zsh.static $RPM_BUILD_ROOT%{_bindir}}
install Doc/zsh.info*	$RPM_BUILD_ROOT%{_infodir}

touch $RPM_BUILD_ROOT%{_sysconfdir}/{zlogout,zlogin,zshenv}
echo "setopt no_function_argzero" > $RPM_BUILD_ROOT%{_sysconfdir}/zprofile
echo ". %{_sysconfdir}/profile" >> $RPM_BUILD_ROOT%{_sysconfdir}/zprofile

cat << EOF > $RPM_BUILD_ROOT%{_sysconfdir}/zshrc
# System wide functions and aliases
# Environment stuff goes in /etc/profile

# Aliases:
alias which=whence
alias cd='builtin cd'
alias precmd=' precmd'

setopt histignorespace

# Setup key bindings:
bindkey -e >/dev/null 2>&1

bindkey \`tput khome\` beginning-of-line >/dev/null 2>&1
bindkey \`tput kend\` end-of-line >/dev/null 2>&1
bindkey \`tput kich1\` quoted-insert >/dev/null 2>&1
bindkey \`tput kdch1\` delete-char >/dev/null 2>&1
bindkey \`tput kpp\` up-history >/dev/null 2>&1
bindkey \`tput knp\` end-of-history >/dev/null 2>&1
bindkey \`tput kcuu1\` history-beginning-search-backward >/dev/null 2>&1
bindkey \`tput kcud1\` history-beginning-search-forward >/dev/null 2>&1

case "$TERM" in
	xterm*)
		precmd () { print -Pn "\e]0;%n@%m: %~\a"i; }
		;;
esac
EOF

rm -f Etc/Makefile*
find Functions Util StartupFiles -name .distfiles -o -name .cvsignore | xargs rm -f
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man1/zsh.1

# for kdesdk's completion
ln -sf %{version} $RPM_BUILD_ROOT%{_datadir}/zsh/latest

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
if [ ! -f /etc/shells ]; then
	echo "%{_bindir}/zsh" >> /etc/shells
else
	grep -q '^%{_bindir}/zsh$' /etc/shells || echo "%{_bindir}/zsh" >> /etc/shells
fi
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} > /dev/null 2>&1

%preun
if [ "$1" = "0" ]; then
	umask 022
	grep -v '^%{_bindir}/zsh$' /etc/shells > /etc/shells.new
	mv -f /etc/shells.new /etc/shells
fi

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} > /dev/null 2>&1

%post static
umask 022
if [ ! -f /etc/shells ]; then
	echo "%{_bindir}/zsh.static" >> /etc/shells
else
	grep -q '^%{_bindir}/zsh\.static$' /etc/shells || echo "%{_bindir}/zsh.static" >> /etc/shells
fi

%preun static
if [ "$1" = "0" ]; then
	umask 022
	grep -v '^%{_bindir}/zsh\.static$' /etc/shells > /etc/shells.new
	mv -f /etc/shells.new /etc/shells
fi

%files
%defattr(644,root,root,755)
%doc Etc/* README LICENCE ChangeLog META-FAQ Util StartupFiles
%attr(755,root,root) %{_bindir}/zsh
%config(noreplace,missingok) %verify(not md5 size mtime) %{_sysconfdir}/*
%dir %{_libdir}/zsh
%dir %{_libdir}/zsh/%{version}
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/latest
%dir %{_datadir}/zsh/%{version}
%dir %{_datadir}/zsh/%{version}/functions
%{_datadir}/zsh/%{version}/functions/[!_c]*
%{_datadir}/zsh/%{version}/functions/c[!o]*
%{_datadir}/zsh/%{version}/functions/co[!m]*
%attr(755,root,root) %{_libdir}/zsh/%{version}/*
%{_infodir}/zsh.info*
%{_mandir}/man1/zsh*.1*
%lang(pl) %{_mandir}/pl/man1/zsh*.1*

%files completions
%defattr(644,root,root,755)
%{_datadir}/zsh/%{version}/functions/comp*
%{_datadir}/zsh/%{version}/functions/_*

%files guide
%defattr(644,root,root,755)
%doc zshguide.pdf

%if %{!?_without_static:1}%{?_without_static:0}
%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/zsh.static
%endif
