# $Revision: 1.26 $ $Date: 2001-03-11 00:55:22 $
Summary:	Enhanced bourne shell
Summary(de):	Enhanced Bourne Shell
Summary(fr):	Bourne shell amélioré
Summary(tr):	Geliþmiþ bir BASH sürümü
Summary(pl):	Ulepszona pow³oka Bourne'a
Name:		zsh
Version:	3.1.9
Release:	6
License:	GPL
Group:		Applications/Shells
Group(de):	Applikationen/Shells
Group(pl):	Aplikacje/Pow³oki
URL:		http://www.zsh.org/
Source0:	ftp://ftp.zsh.org/pub/zsh/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-sys_capability.patch
Patch3:		%{name}-cap_get_proc.patch
Patch4:		%{name}-tinfo.patch
Patch5:		%{name}-addons.patch
BuildRequires:	ncurses-devel >= 5.1
BuildRequires:	glibc-static
BuildRequires:	ncurses-static
BuildRequires:	texinfo
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	zsh-doc-html, zsh-doc-ps, zsh-doc-dvi

%define		_bindir		/bin

%description
zsh is an enhanced version of the Bourne shell with csh additions and
most features of ksh, bash, and tcsh.

%description -l pl
zsh jest ulepszon± pow³ok± Bourne'a z elementami pow³oki csh. Posiada
wiêkszo¶æ cech ksh, bash i tcsh.

%package static
Summary:	Statically linked Enhanced bourne shell
Summary(pl):	Zaawansowany bourne SHell - linkowany statycznie
Group:		Applications/Shells
Group(de):	Applikationen/Shells
Group(pl):	Aplikacje/Pow³oki
Requires:	%{name} = %{version}

%description static
zsh is an enhanced version of the Bourne shell with csh additions and
most features of ksh, bash, and tcsh.

%description -l pl static
zsh jest ulepszon± pow³ok± Bourne'a z elementami pow³oki csh. Posiada
wiêkszo¶æ cech ksh, bash i tcsh. W tym pakiecie jest statycznie
linkowany.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

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
gzip -9nf Etc/* README ChangeLog META-FAQ

%post
if [ ! -f /etc/shells ]; then
	echo "/bin/zsh" >> /etc/shells
else
	while read SHNAME; do
	        if [ "$SHNAME" = "/bin/zsh" ]; then
        	        HAS_ZSH=1
	        fi
	done < /etc/shells
	if [ -n "$HAS_ZSH" ]; then
		echo "/bin/zsh" >> /etc/shells
	fi
fi
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} > /dev/null 2>&1

%preun
if [ "$1" = "0" ]; then
	while read SHNAME; do
		if [ "$SHNAME" = "/bin/zsh" ]; then
			echo "$SHNAME"
		fi
	done < /etc/shells > /etc/shells.new
	mv -f /etc/shells.new /etc/shells
fi
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} > /dev/null 2>&1

%post static
if [ ! -f /etc/shells ]; then
	echo "/bin/zsh.static" >> /etc/shells
else
	while read SHNAME; do
	        if [ "$SHNAME" = "/bin/zsh.static" ]; then
        	        HAS_ZSH_STATIC=1
	        fi
	done < /etc/shells
	if [ -n "$HAS_ZSH_STATIC" ]; then
		 echo "/bin/zsh.static" >> /etc/shells
	fi
fi

%preuni static
if [ "$1" = "0" ]; then
	while read SHNAME; do
		if [ "$SHNAME" = "/bin/zsh.static" ]; then
			echo "$SHNAME"
		fi
	done < /etc/shells > /etc/shells.new
	mv -f /etc/shells.new /etc/shells
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
