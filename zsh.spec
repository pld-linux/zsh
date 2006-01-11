#
# todo:
# - add zsh-lovers man page from http://grml.org/zsh/
#
# Conditional build:
%bcond_with	static # build static version
#
Summary:	Enhanced Bourne shell
Summary(de):	Enhanced Bourne Shell
Summary(es):	Shell bourne mejorada
Summary(fr):	Bourne shell amИliorИ
Summary(pl):	Ulepszona powЁoka Bourne'a
Summary(pt_BR):	Shell bourne melhorada
Summary(ru):	Командный процессор (shell) похожый на ksh, но с улучшениями
Summary(tr):	GeliЧmiЧ bir BASH sЭrЭmЭ
Summary(uk):	Командний процесор (shell) схожий на ksh, але з покращеннями
Name:		zsh
%define	snap	20051216
Version:	4.3.0
Release:	0.%{snap}.1
License:	BSD-like
Group:		Applications/Shells
URL:		http://www.zsh.org/
Source0:	%{name}-%{snap}.tar.gz
# Source0-md5:	da3b30feb6705f735c42c434723d8c90
Source1:	%{name}.1.pl
Source2:	http://zsh.sunsite.dk/Guide/zshguide.pdf
# Source2-md5:	0d80ba1ef39052c512cfabf368f3bf20
Source3:	zprofile
Source4:	zshrc
Patch0:		%{name}-info.patch
Patch1:		%{name}-addons.patch
Patch2:		%{name}-paths.patch
Patch3:		%{name}-completions.patch
Patch4:		%{name}-nolibs.patch
Patch5:		%{name}-broken_configure.patch
Patch6:		%{name}-svn.patch
Patch7:		%{name}-restore-histfile.patch
BuildRequires:	autoconf
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
Obsoletes:	zsh-doc-html, zsh-doc-ps, zsh-doc-dvi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/bin
%define		specflags_ia32	 -fomit-frame-pointer 

%description
zsh is an enhanced version of the Bourne shell with csh additions and
most features of ksh, bash, and tcsh.

%description -l es
zsh es una versiСn mejorada del bourne shell con estas
caracterМsticas:
- muy prСximo de la gramАtica del ksh/sh, con adiciones csh,
- varias caracterМsticas del ksh, bash y tcsh,
- 75 funciones empotradas, 89 opciones, 154 combinaciones de teclas,
- selecciСn,
- funciones shell ...y mucho mАs.

%description -l ja
zsh ╔╥╔╖╔К╓обпоце╙╓й╔М╔╟╔╓╔С╔╥╔╖╔К╓х╓╥╓фмЬмя╡дг╫╓й╔Ё╔ч╔С╔и╔╓╔С╔©╔Й╔©
╓г╓╒╓Й║╒╔╥╔╖╔К╔╧╔╞╔Й╔в╔х╔Ё╔ч╔С╔и╓Б╫ХмЩ╓г╓╜╓ч╓╧. zsh ╓о ksh(the Korn
shell) ╓к╩В╓ф╓╓╓ч╓╧╓╛,╓╚╓й╓ЙЁхд╔╓╣╓Л╓ф╓╓╓ч╓╧. zsh
╓о╔Ё╔ч╔С╔и╔И╔╓╔С╓г╓нйт╫╦╣║г╫, ах╓ъ╧Ч╓ч╓Л╓©╔╧╔з╔К╫╓ю╣╣║г╫, ╔в╔М╔╟╔И╔ъ╔С
╔╟╡дг╫╓й╔Ё╔ч╔С╔ийД╢╟╣║г╫, (ф╟е╙╔М║╪╔и╓╣╓Л╓К)╔╥╔╖╔К╣║г╫, ╔р╔╧╔х╔Й╣║╧╫
╓й╓и╓Р╩Щ╓а╓ч╓╧.

%description -l pl
zsh jest ulepszon╠ powЁok╠ Bourne'a z elementami powЁoki csh. Posiada
wiЙkszo╤Ф cech ksh, bash i tcsh.

%description -l pt_BR
zsh И uma versЦo melhorada do bourne shell com essas caracterМsticas:
- muito prСximo da gramАtica do ksh/sh, com adiГУes csh,
- vАrias caracterМsticas do ksh, bash e tcsh,
- 75 funГУes embutidas, 89 opГУes, 154 combinaГУes de teclas,
- seleГЦo,
- funГУes shell ...e muito mais.

%description -l ru
zsh - это командный процессор напоминающий ksh (Korn shell), но
включающий много улучшений. zsh поддерживает редактирование командной
строки, встроенную коррекцию написания, программируемое завершение
команд, shell-функции (с автозагрузкой), историю команд и многое
другое.

%description -l uk
zsh - це командний процесор, що нагаду╓ ksh (Korn shell), але включа╓
багато покращень. zsh п╕дтриму╓ редагування командного рядка,
вбудовану корекц╕ю написання, програмоване завершення команд,
shell-функц╕╖ (з автозавантаженням), ╕стор╕ю команд та багато ╕ншого.

%package completions
Summary:	Files needed for advanced TAB-completion
Summary(pl):	Pliki potrzebne dla zaawansowanej TAB-completion
Group:		Applications/Shells
Conflicts:	kdesdk-completions-zsh <= 3:3.2.3-2
Requires:	%{name} = %{version}-%{release}

%description completions
This package contains files needed for advanced tab completion in zsh.

%description completions -l pl
Ten pakiet zawiera pliki wymagane przez zsh dla zaawansowanej
TAB-completion.

%package static
Summary:	Statically linked Enhanced Bourne shell
Summary(pl):	Zaawansowana powЁoka Bourne'a - skonsolidowana statycznie
Group:		Applications/Shells
Requires(post,preun):	grep
Requires(preun):	fileutils
Requires:	%{name} = %{version}-%{release}

%description static
zsh is an enhanced version of the Bourne shell with csh additions and
most features of ksh, bash, and tcsh.

%description static -l pl
zsh jest ulepszon╠ powЁok╠ Bourne'a z elementami powЁoki csh. Posiada
wiЙkszo╤Ф cech ksh, bash i tcsh. W tym pakiecie jest wersja
skonsolidowana statycznie.

%package guide
Summary:	A User's Guide to the Z-Shell
Summary(pl):	PodrЙcznik U©ytkownika Z-Shella
Group:		Documentation
URL:		http://zsh.sunsite.dk/Guide/

%description guide
A User's Guide to the Z-Shell.

%description guide -l pl
PodrЙcznik U©ytkownika Z-Shella.

%prep
%setup -q -n %{name}
#%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
#%patch5 -p1
#%patch6 -p0
%patch7 -p1

install %{SOURCE2} .

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}
%{__autoheader}
echo > stamp-h.in
CPPFLAGS="-I/usr/include/ncurses"

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
if [ ! -f /etc/shells ]; then
	echo "%{_bindir}/zsh" >> /etc/shells
else
	grep -q '^%{_bindir}/zsh$' /etc/shells || echo "%{_bindir}/zsh" >> /etc/shells
fi
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} > /dev/null 2>&1
for i in zlogin zlogout zprofile zshenv zshrc; do
	[ -f /etc/$i ] && zsh -c "zcompile /etc/$i"
done

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
