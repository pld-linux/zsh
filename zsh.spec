# $Revision: 1.14 $ $Date: 2000-06-05 14:33:52 $
Summary:	Enhanced bourne shell
Summary(de):	Enhanced Bourne Shell
Summary(fr):	Bourne shell amélioré
Summary(tr):	Geliþmiþ bir BASH sürümü
Summary(pl):	Ulepszona pow³oka Bourne'a
Name:		zsh
Version:	3.1.8
Release:	1
License:	GPL
Group:		Shells
Group(pl):	Pow³oki
Source0:	ftp://ftp.zsh.org/pub/zsh/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.zsh.org/pub/zsh/%{name}-%{version}-doc.tar.gz
Patch0:		zsh-info.patch
Patch1:		zsh-DESTDIR.patch
Patch2:		zsh-sys_capability.patch
Patch3:		zsh-cap_get_proc.patch
Patch4:		zsh-tinfo.patch
Patch5:		zsh-addons.patch
Prereq:		grep
Prereq:		gawk
Prereq:		sed
BuildRequires:	ncurses-devel
BuildRequires:	glibc-static
BuildRequires:	ncurses-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix		/

%description
zsh is an enhanced version of the Bourne shell with csh additions and
most features of ksh, bash, and tcsh.

%description -l pl
zsh jest ulepszon± pow³ok± Bourne'a z elementami pow³oki csh. Posiada
wiêkszo¶æ cech ksh, bash i tcsh.

%package static
Summary:	Statically linked Enhanced bourne shell
Summary(pl):	 Zaawansowany bourne SHell - linkowany statycznie
Group:		Shells
Group(pl):	Pow³oki
Requires:	%{name} = %{version}

%description static
zsh is an enhanced version of the Bourne shell with csh additions and
most features of ksh, bash, and tcsh.

%description -l pl static
zsh jest ulepszon± pow³ok± Bourne'a z elementami pow³oki csh. Posiada
wiêkszo¶æ cech ksh, bash i tcsh. W tym pakiecie jest statycznie
linkowany.

%package doc-html
Summary:		HTML documentation for zsh	
Group:		Shells

%description doc-html
HTML documentation for zsh.

%package doc-ps
Summary:		Postscript version of zsh documentation
Group:		Shells

%description doc-ps
Postscript version of zsh documentation.

%package doc-dvi
Summary:		DVI version of zsh documentation
Group:		Shells

%description doc-dvi 
DVI version of zsh documentation.

%prep
%setup -q
%setup -q -b 1 -D
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
autoconf

LDFLAGS="-static -s"; export LDFLAGS
%configure
make
mv Src/zsh Src/zsh.static

LDFLAGS="-s"; export LDFLAGS
%configure --enable-maildir-support
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

install Src/zsh.static $RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{_infodir}
install Doc/zsh.info* $RPM_BUILD_ROOT%{_infodir}

install -d $RPM_BUILD_ROOT%{_sysconfdir}
touch	$RPM_BUILD_ROOT%{_sysconfdir}/{zlogout,zprofile,zshrc,zlogin,zshenv}

rm Etc/Makefile*
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	  Etc/* README ChangeLog META-FAQ \
		$RPM_BUILD_ROOT/%{_infodir}/zsh.info*

%post
if [ ! -f /etc/shells ]; then
	echo "/bin/zsh" > /etc/shells
else
	if ! grep '^/bin/zsh$' /etc/shells > /dev/null; then
		echo "/bin/zsh" >> /etc/shells
	fi
fi

[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} > /dev/null 2>&1

%postun
if [ "$1" = "0" ]; then
	grep -v /bin/zsh /etc/shells > /etc/shells.new
	mv /etc/shells.new /etc/shells
fi

[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} > /dev/null 2>&1

%post static
if [ ! -f /etc/shells ]; then
	echo "/bin/zsh.static" > /etc/shells
else
	grep '^/bin/zsh.static$' /etc/shells > /dev/null || echo "/bin/zsh.static" >> /etc/shells
fi

%postun static
if [ ! -x /bin/zsh.static ]; then
	grep -v '^/bin/zsh.static$' /etc/shells > /etc/shells.rpm
	mv /etc/shells.rpm /etc/shells
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {META-FAQ,README,ChangeLog}.gz Etc/* Util Functions
%doc %{_infodir}/zsh.info*
%dir %{_libdir}/zsh/%{version}
%config %{_sysconfdir}/*

%attr(755,root,root) %{_bindir}/zsh
%attr(755,root,root) %{_libdir}/zsh/%{version}/*
%{_mandir}/man1/zsh*.1.gz

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/zsh.static

%files doc-html
%defattr(644,root,root,755)
%doc Doc/*html

%files doc-ps
%defattr(644,root,root,755)
%doc Doc/*ps

%files doc-dvi
%defattr(644,root,root,755)
%doc Doc/*dvi
