# $Revision: 1.11 $ $Date: 2000-05-23 14:27:35 $
Summary:	Enhanced bourne shell
Summary(de):	Enhanced Bourne Shell
Summary(fr):	Bourne shell amélioré
Summary(tr):	Geliþmiþ bir BASH sürümü
Summary(pl):	Ulepszona pow³oka Bourne'a
Name:		zsh
Version:	3.1.7
%define dev_ver pre-4
Release:	3
License:	GPL
Group:		Shells
Group(pl):	Pow³oki
Source0:	ftp://ftp.zsh.org/pub/zsh/development/%{name}-%{version}-%{dev_ver}.tar.gz
Patch0:		zsh-info.patch
Patch1:		zsh-DESTDIR.patch
Patch2:		zsh-config2.patch
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
wiêkszo¶æ cech pow³ok ksh, bash i tcsh.

%package static
Summary:	Statcly linked Enhanced bourne shell
Summary(pl):	Statycznie linkowany Zaawansowany bourne shell 
Group:		Shells
Group(pl):	Pow³oki
Requires:	%{name} = %{version}

%description static
zsh is an enhanced version of the Bourne shell with csh additions and
most features of ksh, bash, and tcsh.

%description -l pl static
zsh jest ulepszon± pow³ok± Bourne'a z elementami pow³oki csh. Posiada
wiêkszo¶æ cech pow³ok ksh, bash i tcsh. W tym pakiecie jest statycznie
linkowany zsh.

%prep
%setup -q -n %{name}-%{version}-%{dev_ver}
%patch0 -p1
%patch1 -p1

%build
#autoconf
#LDFLAGS="-static -s"; export LDFLAGS
#%configure
#make
#
#mv zsh zsh.static

LDFLAGS="-s"; export LDFLAGS
%configure
patch -p1 < %{PATCH2}
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# install zsh.static $RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{_sysconfdir}
touch	$RPM_BUILD_ROOT%{_sysconfdir}/{zlogout,zprofile,zshrc,zlogin,zshenv}

rm Etc/Makefile*
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	  Etc/* README ChangeLog META-FAQ

%post
if [ ! -f /etc/shells ]; then
	echo "/bin/zsh" > /etc/shells
else
	if ! grep '^/bin/zsh$' /etc/shells > /dev/null; then
		echo "/bin/zsh" >> /etc/shells
	fi
fi

[ -x /usr/sbin/fix-info-dir ] && /usr/sbin/fix-info-dir -c %{_infodir} > /dev/null 2>&1

%postun
if [ "$1" = "0" ]; then
	grep -v /bin/zsh /etc/shells > /etc/shells.new
	mv /etc/shells.new /etc/shells
fi

# /usr/sbin/fix-info-dir -c %{_infodir} > /dev/null 2>&1

#%post static
#if [ ! -f /etc/shells ]; then
#	echo "/bin/zsh.static" > /etc/shells
#else
#	grep '^/bin/zsh.static$' /etc/shells > /dev/null || echo "/bin/zsh.static" >> /etc/shells
#fi
#
#%postun static
#if [ ! -x /bin/zsh.static ]; then
#	grep -v '^/bin/zsh.static$' /etc/shells > /etc/shells.rpm
#	mv /etc/shells.rpm /etc/shells
#fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {META-FAQ,README,ChangeLog}.gz Etc/* Util Functions
%dir %{_libdir}/zsh/%{version}-%{dev_ver}
%config %{_sysconfdir}/*

%attr(755,root,root) %{_bindir}/zsh
%attr(755,root,root) %{_libdir}/zsh/%{version}-%{dev_ver}/*
%{_mandir}/man1/zsh*.1.gz

#%files static
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/zsh.static
