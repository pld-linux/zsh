#
# todo:
# - add zsh-lovers man page from http://grml.org/zsh/
#
# Conditional build:
%bcond_with	static # build static version
#
Summary:	Enhanced Bourne shell
Summary(de.UTF-8):	Enhanced Bourne Shell
Summary(es.UTF-8):	Shell bourne mejorada
Summary(fr.UTF-8):	Bourne shell amélioré
Summary(pl.UTF-8):	Ulepszona powłoka Bourne'a
Summary(pt_BR.UTF-8):	Shell bourne melhorada
Summary(ru.UTF-8):	Командный процессор (shell) похожый на ksh, но с улучшениями
Summary(tr.UTF-8):	Gelişmiş bir BASH sürümü
Summary(uk.UTF-8):	Командний процесор (shell) схожий на ksh, але з покращеннями
Name:		zsh
Version:	4.3.4
Release:	3
License:	BSD-like
Group:		Applications/Shells
URL:		http://www.zsh.org/
Source0:	ftp://ftp.zsh.org/pub/%{name}-%{version}.tar.bz2
# Source0-md5:	8410a30e4f5c6160790bc3afc096424f
Source1:	%{name}.1.pl
Source2:	http://zsh.sunsite.dk/Guide/%{name}guide.pdf
# Source2-md5:	e42b6b6ff487bb2a95543f3937287b99
Source3:	zprofile
Source4:	%{name}rc
Patch0:		%{name}-info.patch
Patch1:		%{name}-addons.patch
Patch2:		%{name}-paths.patch
Patch3:		%{name}-completions.patch
Patch4:		%{name}-nolibs.patch
Patch5:		%{name}-lfs.patch
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_static:BuildRequires:	glibc-static}
BuildRequires:	libcap-devel
BuildRequires:	ncurses-devel >= 5.1
%{?with_static:BuildRequires:	ncurses-static}
BuildRequires:	pcre-devel
BuildRequires:	texinfo
BuildRequires:	yodl
Requires(post,preun):	grep
Requires(preun):	fileutils
Requires:	findutils
Obsoletes:	zsh-doc-html
Obsoletes:	zsh-doc-ps
Obsoletes:	zsh-doc-dvi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/bin
%define		specflags_ia32	 -fomit-frame-pointer 

%description
zsh is an enhanced version of the Bourne shell with csh additions and
most features of ksh, bash, and tcsh.

%description -l es.UTF-8
zsh es una versión mejorada del bourne shell con estas
características:
- muy próximo de la gramática del ksh/sh, con adiciones csh,
- varias características del ksh, bash y tcsh,
- 75 funciones empotradas, 89 opciones, 154 combinaciones de teclas,
- selección,
- funciones shell ...y mucho más.

%description -l ja.UTF-8
zsh シェルは対話的なログインシェルとして利用可能なコマンドインタリタ
であり、シェルスクリプトコマンドも処理できます. zsh は ksh(the Korn
shell) に似ていますが,かなり拡張されています. zsh
はコマンドラインでの編集機能, 組み込まれたスペル修正機能, プログラミン
グ可能なコマンド補完機能, (動的ロードされる)シェル機能, ヒストリ機構
などを持ちます.

%description -l pl.UTF-8
zsh jest ulepszoną powłoką Bourne'a z elementami powłoki csh. Posiada
większość cech ksh, bash i tcsh.

%description -l pt_BR.UTF-8
zsh é uma versão melhorada do bourne shell com essas características:
- muito próximo da gramática do ksh/sh, com adições csh,
- várias características do ksh, bash e tcsh,
- 75 funções embutidas, 89 opções, 154 combinações de teclas,
- seleção,
- funções shell ...e muito mais.

%description -l ru.UTF-8
zsh - это командный процессор напоминающий ksh (Korn shell), но
включающий много улучшений. zsh поддерживает редактирование командной
строки, встроенную коррекцию написания, программируемое завершение
команд, shell-функции (с автозагрузкой), историю команд и многое
другое.

%description -l uk.UTF-8
zsh - це командний процесор, що нагадує ksh (Korn shell), але включає
багато покращень. zsh підтримує редагування командного рядка,
вбудовану корекцію написання, програмоване завершення команд,
shell-функції (з автозавантаженням), історію команд та багато іншого.

%package completions
Summary:	Files needed for advanced TAB-completion
Summary(pl.UTF-8):	Pliki potrzebne dla zaawansowanej TAB-completion
Group:		Applications/Shells
Conflicts:	kdesdk-completions-zsh <= 3:3.2.3-2
Requires:	%{name} = %{version}-%{release}

%description completions
This package contains files needed for advanced tab completion in zsh.

%description completions -l pl.UTF-8
Ten pakiet zawiera pliki wymagane przez zsh dla zaawansowanej
TAB-completion.

%package static
Summary:	Statically linked Enhanced Bourne shell
Summary(pl.UTF-8):	Zaawansowana powłoka Bourne'a - skonsolidowana statycznie
Group:		Applications/Shells
Requires(post,preun):	grep
Requires(preun):	fileutils
Requires:	%{name} = %{version}-%{release}

%description static
zsh is an enhanced version of the Bourne shell with csh additions and
most features of ksh, bash, and tcsh.

%description static -l pl.UTF-8
zsh jest ulepszoną powłoką Bourne'a z elementami powłoki csh. Posiada
większość cech ksh, bash i tcsh. W tym pakiecie jest wersja
skonsolidowana statycznie.

%package guide
Summary:	A User's Guide to the Z-Shell
Summary(pl.UTF-8):	Podręcznik Użytkownika Z-Shella
Group:		Documentation
URL:		http://zsh.sunsite.dk/Guide/

%description guide
A User's Guide to the Z-Shell.

%description guide -l pl.UTF-8
Podręcznik Użytkownika Z-Shella.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

install %{SOURCE2} .

sed -i -e 's|#!.*/zsh|#!/bin/zsh|g' Functions/*/*

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}
%{__autoheader}
echo > stamp-h.in
CPPFLAGS="-I/usr/include/ncurses $CPPFLAGS"

%if %{with static}
LDFLAGS="%{rpmldflags} -static"
%configure \
	--enable-maildir-support \
	--enable-multibyte \
	--with-tcsetpgrp \
	--disable-dynamic
%{__make} \
	DLLDFLAGS=""
mv -f Src/zsh Src/zsh.static
%{__make} clean || :
LDFLAGS="%{rpmldflags}"
%endif

%configure \
	ac_cv_have_dev_ptmx=yes \
	--enable-maildir-support \
	--enable-cap \
	--enable-pcre \
	--enable-multibyte \
	--with-curses-terminfo \
	--with-tcsetpgrp
%{__make}

cd Doc
makeinfo zsh.texi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_infodir},%{_sysconfdir},%{_bindir},%{_mandir}/pl/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{?with_static:install Src/zsh.static $RPM_BUILD_ROOT%{_bindir}}
install Doc/zsh.info* $RPM_BUILD_ROOT%{_infodir}

touch $RPM_BUILD_ROOT%{_sysconfdir}/{zlogin,zlogout,zshenv}
touch $RPM_BUILD_ROOT%{_sysconfdir}/{zlogin,zlogout,zprofile,zshenv,zshrc}.zwc
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}

rm -f Etc/Makefile*
find Functions Util StartupFiles -name .distfiles -o -name .cvsignore | xargs rm -f
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man1/zsh.1

# for kdesdk's completion
ln -sf %{version} $RPM_BUILD_ROOT%{_datadir}/zsh/latest

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} > /dev/null 2>&1
if [ ! -f /etc/shells ]; then
	echo "%{_bindir}/zsh" >> /etc/shells
else
	grep -q '^%{_bindir}/zsh$' /etc/shells || echo "%{_bindir}/zsh" >> /etc/shells
fi
for i in zlogin zlogout zprofile zshenv zshrc; do
	[ -f /etc/$i ] && zsh -c "zcompile /etc/$i"
done

%preun
if [ "$1" = "0" ]; then
	umask 022
	grep -v '^%{_bindir}/zsh$' /etc/shells > /etc/shells.new
	mv -f /etc/shells.new /etc/shells
fi

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

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
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/*[!w]?
%ghost %{_sysconfdir}/*.zwc
%dir %{_libdir}/zsh
%dir %{_libdir}/zsh/%{version}*
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/latest
%dir %{_datadir}/zsh/%{version}*
%dir %{_datadir}/zsh/%{version}*/scripts
%{_datadir}/zsh/%{version}*/scripts/newuser
%dir %{_datadir}/zsh/%{version}*/functions
%{_datadir}/zsh/%{version}*/functions/[!_c]*
%{_datadir}/zsh/%{version}*/functions/c[!o]*
%{_datadir}/zsh/%{version}*/functions/co[!m]*
%attr(755,root,root) %{_libdir}/zsh/%{version}*/*
%{_infodir}/zsh.info*
%{_mandir}/man1/zsh*.1*
%lang(pl) %{_mandir}/pl/man1/zsh*.1*

%files completions
%defattr(644,root,root,755)
%{_datadir}/zsh/%{version}*/functions/comp*
%{_datadir}/zsh/%{version}*/functions/_*

%files guide
%defattr(644,root,root,755)
%doc zshguide.pdf

%if %{with static}
%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/zsh.static
%endif
