#
# TODO: package http://www.zsh.org/pub/zsh-%{version}-doc.tar.xz
# Conditional build:
%bcond_with	static	# build static version
%bcond_without	tests	# don't perform "make test"
#
Summary:	Enhanced Bourne shell
Summary(de.UTF-8):	Enhanced Bourne Shell
Summary(es.UTF-8):	Shell bourne mejorada
Summary(fr.UTF-8):	Bourne shell amélioré
Summary(hu.UTF-8):	Kiterjesztett Bourne Shell
Summary(pl.UTF-8):	Ulepszona powłoka Bourne'a
Summary(pt_BR.UTF-8):	Shell bourne melhorada
Summary(ru.UTF-8):	Командный процессор (shell) похожый на ksh, но с улучшениями
Summary(tr.UTF-8):	Gelişmiş bir BASH sürümü
Summary(uk.UTF-8):	Командний процесор (shell) схожий на ksh, але з покращеннями
Name:		zsh
Version:	5.9
Release:	3
License:	BSD-like
Group:		Applications/Shells
Source0:	https://downloads.sourceforge.net/zsh/%{name}-%{version}.tar.xz
# Source0-md5:	182e37ca3fe3fa6a44f69ad462c5c30e
Source1:	%{name}.1.pl
Source2:	https://zsh.sourceforge.io/Guide/zshguide.pdf
# Source2-md5:	409cbf8cbabb2c6bee88aac5c8279718
Source3:	zprofile
Source4:	%{name}rc
Patch0:		%{name}-info.patch
Patch1:		%{name}-addons.patch
Patch2:		%{name}-paths.patch
Patch3:		%{name}-nolibs.patch
Patch4:		comp-all-ssh-hosts.patch
URL:		http://www.zsh.org/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	gdbm-devel
%{?with_static:BuildRequires:	glibc-static}
BuildRequires:	libcap-devel
BuildRequires:	ncurses-devel >= 5.1
%{?with_static:BuildRequires:	ncurses-static}
BuildRequires:	pcre-devel
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.470
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
BuildRequires:	xz
BuildRequires:	yodl
Requires(post,preun):	grep
Requires(preun):	fileutils
Requires:	findutils
Obsoletes:	zsh-doc-dvi
Obsoletes:	zsh-doc-html
Obsoletes:	zsh-doc-ps
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/bin
%define		specflags_ia32	-fomit-frame-pointer

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

%description -l hu.UTF-8
zsh a Bourne shell egy kiterjesztett verziója csh kiegészítésekkel és
a ksh, bash és csh legtöbb lehetőségével felvértezve.

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
Summary(hu.UTF-8):	A haladó TAB-kiegészítéshez szükséges fájlok
Summary(pl.UTF-8):	Pliki potrzebne dla zaawansowanej TAB-completion
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Conflicts:	kdesdk-completions-zsh <= 3:3.2.3-2
BuildArch:	noarch

%description completions
This package contains files needed for advanced tab completion in zsh.

%description completions -l hu.UTF-8
Ez a csomag tartalmazza a haladó TAB-kiegészítéshez szükséges fájlokat
a zsh shell-hez.

%description completions -l pl.UTF-8
Ten pakiet zawiera pliki wymagane przez zsh dla zaawansowanej
TAB-completion.

%package static
Summary:	Statically linked Enhanced Bourne shell
Summary(hu.UTF-8):	A zsh statikus verziója
Summary(pl.UTF-8):	Zaawansowana powłoka Bourne'a - skonsolidowana statycznie
Group:		Applications/Shells
Requires(post,preun):	grep
Requires(preun):	fileutils
Requires:	%{name} = %{version}-%{release}

%description static
zsh is an enhanced version of the Bourne shell with csh additions and
most features of ksh, bash, and tcsh.

%description static -l hu.UTF-8
A zsh statikus verziója.

%description static -l pl.UTF-8
zsh jest ulepszoną powłoką Bourne'a z elementami powłoki csh. Posiada
większość cech ksh, bash i tcsh. W tym pakiecie jest wersja
skonsolidowana statycznie.

%package guide
Summary:	A User's Guide to the Z-Shell
Summary(hu.UTF-8):	Felhasználói útmutató a Z-Shell-hez
Summary(pl.UTF-8):	Podręcznik Użytkownika Z-Shella
Group:		Documentation
URL:		http://zsh.sunsite.dk/Guide/
BuildArch:	noarch

%description guide
A User's Guide to the Z-Shell.

%description guide -l hu.UTF-8
Felhasználói útmutató a Z-Shell-hez.

%description guide -l pl.UTF-8
Podręcznik Użytkownika Z-Shella.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

install %{SOURCE2} .

find Functions -type f -exec %{__sed} -i -e 's|#!.*/zsh|#!/bin/zsh|g' "{}" ";"

%build
%{__autoconf}
%{__autoheader}
echo > stamp-h.in
CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses"

%if %{with static}
LDFLAGS="%{rpmldflags} -static"
%configure \
	--enable-maildir-support \
	--enable-multibyte \
	--with-tcsetpgrp \
	--disable-dynamic
%{__make} \
	DLLDFLAGS=""
%{__mv} Src/zsh Src/zsh.static
%{__make} clean || :
LDFLAGS="%{rpmldflags}"
%endif

%configure \
	ac_cv_have_dev_ptmx=yes \
	--enable-maildir-support \
	--enable-cap \
	--enable-gdbm \
	--enable-pcre \
	--enable-multibyte \
	--with-tcsetpgrp
%{__make}

cd Doc
makeinfo zsh.texi
cd ..

%if %{with tests}
if ! tty; then
	%{__rm} Test/{C02cond,E01options,Y01completion,Y02compmatch,Y03arguments,V08zpty,W02jobs,W03jobparameters,X02zlevi,X03zlebindkey,X04zlehighlight}.ztst
fi
%{__make} test
%endif

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

%{__rm} -f Etc/Makefile*
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
%doc Etc/* ChangeLog FEATURES LICENCE META-FAQ README Misc StartupFiles Util
%attr(755,root,root) %{_bindir}/zsh
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/zlogin
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/zlogout
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/zprofile
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/zshenv
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/zshrc
%ghost %{_sysconfdir}/z*.zwc
%dir %{_datadir}/zsh/%{version}*
%dir %{_datadir}/zsh/%{version}*/functions
%{_datadir}/zsh/%{version}*/functions/[!_c]*
%{_datadir}/zsh/%{version}*/functions/c[!o]*
%{_datadir}/zsh/%{version}*/functions/co[!m]*
%{_datadir}/zsh/%{version}*/help
%{_datadir}/zsh/%{version}*/scripts
%{_datadir}/zsh/latest
%dir %{_libdir}/zsh
%dir %{_libdir}/zsh/%{version}*
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
