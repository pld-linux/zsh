# $Revision: 1.3 $ $Date: 1999-10-25 00:04:44 $
Summary:	Enhanced bourne shell
Summary(de):	Enhanced Bourne Shell
Summary(fr):	Bourne shell amélioré
Summary(tr):	Geliþmiþ bir BASH sürümü
Summary(pl):	Ulepszona pow³oka Bourne'a
Name:		zsh
Version:	3.1.6
Release:	3
Copyright:	GPL
Group:		Shells
Group(pl):	Pow³oki
Source0:	ftp://ftp.zsh.org/pub/zsh/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.zsh.org/pub/zsh/%{name}-%{version}-doc.tar.gz
Prereq:		/bin/grep /usr/sbin/fix-info-dir /bin/awk /bin/sed
Buildroot:	/tmp/%{name}-%{version}-root

%define		_exec_prefix		/

%description
zsh is an enhanced version of the Bourne shell with csh additions
and most features of ksh, bash, and tcsh.

%description -l pl
zsh jest ulepszon± pow³ok± Bourne'a z elementami pow³oki csh.
Posiada wiêkszo¶æ cech pow³ok ksh, bash i tcsh.

%prep
%setup -q -b 1

%build
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure \
	--libdir=%{_libdir}
make

%install
rm -rf $RPM_BUILD_ROOT
install -d
$RPM_BUILD_ROOT{%{_mandir}/man1,%{_infodir},%{_bindir},%{_libdir}/zsh/%{version},/etc}

install -s Src/zsh	$RPM_BUILD_ROOT%{_bindir}/zsh
install -s Src/*/*.so	$RPM_BUILD_ROOT%{_libdir}/zsh/%{version}
install    Doc/*.1	$RPM_BUILD_ROOT%{_mandir}/man1
install    Doc/*info*	$RPM_BUILD_ROOT%{_infodir}

touch	$RPM_BUILD_ROOT/etc/{zlogout,zprofile,zshrc,zlogin,zshenv}

rm Etc/Makefile*
gzip -9nf $RPM_BUILD_ROOT{%{_mandir}/man1/*,%{_infodir}/*} \
	  Etc/* README ChangeLog META-FAQ

%post
if [ ! -f /etc/shells ]; then
	echo "/bin/zsh" > /etc/shells
else
	if ! grep '^/bin/zsh$' /etc/shells > /dev/null; then
		echo "/bin/zsh" >> /etc/shells
	fi
fi

/usr/sbin/fix-info-dir -c %{_infodir} > /dev/null 2>&1

%postun
if [ $1 = 0 ]; then
	grep -v /bin/zsh /etc/shells > /etc/shells.new
	mv /etc/shells.new /etc/shells
fi

/usr/sbin/fix-info-dir -c %{_infodir} > /dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {META-FAQ,README,ChangeLog}.gz Etc/* Util Functions
%dir %{_libdir}/zsh/%{version}
%config /etc/*

%attr(755,root,root) %{_bindir}/zsh
%attr(755,root,root) %{_libdir}/zsh/%{version}/*
%{_mandir}/man1/zsh*.1.gz
%{_infodir}/*
