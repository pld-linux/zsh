# $Revision: 1.32 $ $Date: 2001-07-04 15:51:42 $
Summary:	Enhanced bourne shell
Summary(de):	Enhanced Bourne Shell
Summary(fr):	Bourne shell am�lior�
Summary(tr):	Geli�mi� bir BASH s�r�m�
Summary(pl):	Ulepszona pow�oka Bourne'a
Name:		zsh
Version:	4.0.2
Release:	2
License:	BSD-like
Group:		Applications/Shells
Group(de):	Applikationen/Shells
Group(pl):	Aplikacje/Pow�oki
URL:		http://www.zsh.org/
Source0:	ftp://ftp.zsh.org/pub/zsh/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-tinfo.patch
Patch2:		%{name}-addons.patch
Patch3:		%{name}-paths.patch
Prereq:		grep
Prereq:		fileutils
Obsoletes:	zsh-doc-html, zsh-doc-ps, zsh-doc-dvi
BuildRequires:	ncurses-devel >= 5.1
BuildRequires:	glibc-static
BuildRequires:	ncurses-static
BuildRequires:	texinfo
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/bin

%description
zsh is an enhanced version of the Bourne shell with csh additions and
most features of ksh, bash, and tcsh.

%description -l pl
zsh jest ulepszon� pow�ok� Bourne'a z elementami pow�oki csh. Posiada
wi�kszo�� cech ksh, bash i tcsh.

%package static
Summary:	Statically linked Enhanced bourne shell
Summary(pl):	Zaawansowany bourne SHell - linkowany statycznie
Group:		Applications/Shells
Group(de):	Applikationen/Shells
Group(pl):	Aplikacje/Pow�oki
Requires:	%{name} = %{version}

%description static
zsh is an enhanced version of the Bourne shell with csh additions and
most features of ksh, bash, and tcsh.

%description -l pl static
zsh jest ulepszon� pow�ok� Bourne'a z elementami pow�oki csh. Posiada
wi�kszo�� cech ksh, bash i tcsh. W tym pakiecie jest statycznie
linkowany.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoconf

%configure
%{__make}
mv -f Src/zsh Src/zsh.static

%configure \
	--enable-maildir-support
%{__make}

(cd Doc; makeinfo zsh.texi)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_infodir},%{_sysconfdir},%{_bindir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install Src/zsh.static	$RPM_BUILD_ROOT%{_bindir}
install Doc/zsh.info*	$RPM_BUILD_ROOT%{_infodir}

touch $RPM_BUILD_ROOT%{_sysconfdir}/{zlogout,zlogin,zshenv}
echo    ". /etc/profile"                > $RPM_BUILD_ROOT%{_sysconfdir}/zprofile
echo -e "PS1='[%n@%m %~]%(!.#.%\$) '\nbindkey -e >/dev/null 2>&1" > \
                                          $RPM_BUILD_ROOT%{_sysconfdir}/zshrc
					
rm -f Etc/Makefile*
gzip -9nf Etc/* README LICENCE ChangeLog META-FAQ

%post
if [ ! -f /etc/shells ]; then
	echo "%{_bindir}/zsh" >> /etc/shells
else
	grep -q '^%{_bindir}/zsh$' /etc/shells || echo "%{_bindir}/zsh" >> /etc/shells
fi
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} > /dev/null 2>&1

%preun
if [ "$1" = "0" ]; then
	grep -v '^%{_bindir}/zsh$' /etc/shells > /etc/shells.new
	mv -f /etc/shells.new /etc/shells
fi

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} > /dev/null 2>&1

%post static
if [ ! -f /etc/shells ]; then
	echo "%{_bindir}/zsh.static" >> /etc/shells
else
	grep -q '^%{_bindir}/zsh\.static$' /etc/shells || echo "%{_bindir}/zsh.static" >> /etc/shells
fi

%preun static
if [ "$1" = "0" ]; then
	grep -v '^%{_bindir}/zsh\.static$' /etc/shells > /etc/shells.new
	mv -f /etc/shells.new /etc/shells
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz Etc/* Util Functions
%attr(755,root,root) %{_bindir}/zsh
%config %{_sysconfdir}/*
%dir %{_libdir}/zsh
%dir %{_libdir}/zsh/%{version}
%attr(755,root,root) %{_libdir}/zsh/%{version}/*
%{_infodir}/zsh.info*
%{_mandir}/man1/zsh*.1*

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/zsh.static
