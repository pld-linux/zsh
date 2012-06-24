# $Revision: 1.1 $ $Date: 1999-07-23 12:49:26 $
Summary:	Enhanced bourne shell
Summary(de):	Enhanced Bourne Shell
Summary(fr):	Bourne shell am�lior�
Summary(tr):	Geli�mi� bir BASH s�r�m�
Summary(pl):	Ulepszona pow�oka Bourne'a
Name:		zsh
Version:	3.0.5
Release:	1
Copyright:	GPL
Group:		Shells
Group(pl):	Pow�oki
Source:		ftp://ftp.zsh.org/pub/zsh/%{name}-%{version}.tar.gz
Prereq:		/bin/grep /sbin/install-info /bin/awk /bin/sed
Buildroot:	/tmp/%{name}-%{version}-root

%define		_exec_prefix		/

%description
zsh is an enhanced version of the Bourne shell with csh additions
and most features of ksh, bash, and tcsh.

%description -l pl
zsh jest ulepszon� pow�ok� Bourne'a zawieraj�c� dodatki z csh. Posiada
wi�kszo�� cech pow�ok ksh, bash i tcsh.

%prep
%setup -q

%build
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_infodir},%{_mandir}/man1,%{_bindir},/etc}

install -s Src/zsh	$RPM_BUILD_ROOT%{_bindir}/zsh
install    Doc/*.1	$RPM_BUILD_ROOT%{_mandir}/man1
install	   Doc/*.info*	$RPM_BUILD_ROOT%{_infodir}

# Tym si� na razie nie przejmowa� - planuj� zrobi� jakie� �adne konfigi
# i je tu wsadzi�.
touch	$RPM_BUILD_ROOT/etc/{zlogout,zprofile,zshrc,zlogin,zshenv}

rm Etc/Makefile*
gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/zsh*,%{_mandir}/man1/*} \
	  Etc/* README ChangeLog META-FAQ

%post
if [ ! -f /etc/shells ]; then
	echo "/bin/zsh" > /etc/shells
else
	if ! grep '^/bin/zsh$' /etc/shells > /dev/null; then
		echo "/bin/zsh" >> /etc/shells
	fi
fi

%postun
if [ $1 = 0 ]; then
	grep -v /bin/zsh /etc/shells > /etc/shells.new
	mv /etc/shells.new /etc/shells
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {META-FAQ,README,ChangeLog}.gz Etc/* Util Functions

# Przy okazji - jak oznaczy� te konfigi? /etc/bashrc nie ma niczego. Ja da�em
# %config, ale nie wiem jak to najlepiej zrobi�...
%config /etc/*

%attr(755,root,root) /bin/zsh
%{_mandir}/man1/zsh*.1
%{_infodir}/zsh.info*
