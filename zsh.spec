# $Revision: 1.37 $ $Date: 2001-07-19 07:37:25 $
Summary:	Enhanced bourne shell
Summary(de):	Enhanced Bourne Shell
Summary(fr):	Bourne shell amélioré
Summary(tr):	Geliþmiþ bir BASH sürümü
Summary(pl):	Ulepszona pow³oka Bourne'a
Name:		zsh
Version:	4.0.2
Release:	4
License:	BSD-like
Group:		Applications/Shells
Group(de):	Applikationen/Shells
Group(pl):	Aplikacje/Pow³oki
URL:		http://www.zsh.org/
Source0:	ftp://ftp.zsh.org/pub/zsh/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-tinfo.patch
Patch2:		%{name}-addons.patch
Patch3:		%{name}-paths.patch
Patch4:		%{name}-no_nis.patch
Prereq:		grep
Prereq:		fileutils
BuildRequires:	autoconf
BuildRequires:	ncurses-devel >= 5.1
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	zsh-doc-html, zsh-doc-ps, zsh-doc-dvi

%define		_bindir		/bin

%description
zsh is an enhanced version of the Bourne shell with csh additions and
most features of ksh, bash, and tcsh.

%description -l pl
zsh jest ulepszon± pow³ok± Bourne'a z elementami pow³oki csh. Posiada
wiêkszo¶æ cech ksh, bash i tcsh.

%package completions
Summary:        Files needed for advanced TAB-completion
Summary(pl):    Pliki potrzebne dla zaawansowanej TAB-completion
Group:          Applications/Shells
Group(de):      Applikationen/Shells
Group(pl):      Aplikacje/Pow³oki
Requires:       %{name} = %{version}

%description completions
This package contains files needed for advanced tab completion in zsh.

%description -l pl completions
Ten pakiet zawiera pliki wymagane przez zsh dla zaawansowanej
TAB-completion.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
autoconf

%configure \
	--enable-maildir-support
%{__make}

(cd Doc; makeinfo zsh.texi)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_infodir},%{_sysconfdir},%{_bindir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install Doc/zsh.info*	$RPM_BUILD_ROOT%{_infodir}

touch $RPM_BUILD_ROOT%{_sysconfdir}/{zlogout,zlogin,zshenv}
echo    ". /etc/profile"                > $RPM_BUILD_ROOT%{_sysconfdir}/zprofile
echo -e "PS1='[%%n@%%m %%~]%%(!.#.%%\\$) '\nbindkey -e >/dev/null 2>&1" > \
                                          $RPM_BUILD_ROOT%{_sysconfdir}/zshrc

rm -f Etc/Makefile*
find Functions Util StartupFiles -name .distfiles -o -name .cvsignore | xargs rm -f
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz Etc/* Util StartupFiles
%attr(755,root,root) %{_bindir}/zsh
%config %{_sysconfdir}/*
%dir %{_libdir}/zsh
%dir %{_libdir}/zsh/%{version}
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions
%dir %{_datadir}/zsh/%{version}
%dir %{_datadir}/zsh/%{version}/functions
%{_datadir}/zsh/%{version}/functions/[^_c]*
%{_datadir}/zsh/%{version}/functions/c[^o]*
%{_datadir}/zsh/%{version}/functions/co[^m]*
%attr(755,root,root) %{_libdir}/zsh/%{version}/*
%{_infodir}/zsh.info*
%{_mandir}/man1/zsh*.1*

%files completions
%defattr(644,root,root,755)
%{_datadir}/zsh/%{version}/functions/comp*
%{_datadir}/zsh/%{version}/functions/_*
