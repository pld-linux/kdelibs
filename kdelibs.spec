# NOTE:	cc1plus takes 136+MB at one time so better prepare a lot of swap
# 	space.
%define	sver	beta1
Summary:	K Desktop Environment - Libraries
Summary(pl):	K Desktop Environment - biblioteki
Name:		kdelibs
Version:	2.2
Release:	0.%{sver}
Epoch:		6
License:	LGPL
Vendor:		The KDE Team
Group:		X11/KDE/Libraries
Group(de):	X11/KDE/Libraries
Group(pl):	X11/KDE/Biblioteki
Source0:	ftp://ftp.kde.org/pub/kde/unstable/%{version}%{sver}/src/%{name}-%{version}%{sver}.tar.bz2
Patch0:		%{name}-final.patch
Patch1:		%{name}-nodebug.patch
Patch2:		%{name}-directories.patch
Patch3:		%{name}-klauncher-escape.patch
Patch4:		%{name}-use_system_libltdl.patch
Icon:		kdelibs.xpm
BuildRequires:	XFree86-devel
%ifnarch sparc sparc64
BuildRequires:	alsa-lib-devel
%endif
BuildRequires:	audiofile-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel >= 2.0
BuildRequires:	libtiff-devel
#BuildRequires:	kdesupport-mimelib-devel => 2.1
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	qt-devel >= 2.3.0
BuildRequires:	gettext-devel
BuildRequires:	zlib-devel
# For Netscape plugin support in Konqueror.
BuildRequires:	motif-devel
BuildRequires:	openssl-devel
BuildRequires:	bzip2-devel
#BuildRequires:	unixODBC-devel
#BuildRequires:	postgresql-devel
# ??? BuildRequires:	OpenGL-devel
BuildRequires:	libxml2-devel
BuildRequires:	pcre-devel
# Needs libltdlc.la which is not present in our libltdl
# BuildRequires:	libltdl-devel
Requires:	qt >= 2.2.4
Requires:	arts = %{version}
URL:		http://www.kde.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	kdelibs2
Obsoletes:	kdelibs2-sound
Obsoletes:	kdelibs-sound

%define         _prefix         /usr/X11R6
%define		_htmldir	%{_datadir}/doc/kde/HTML

%description
Libraries for the K Desktop Environment.

Included with this package are:
- jscript - KDE javascript library,
- kdecore - KDE core library,
- kdeui - KDE user interface library,
- kfmlib - KDE file manager library,
- khtmlw - KDE HTML widget,
- mediatool - KDE mediatool library.

%description -l pl
Biblioteki do K Desktop Environment.

Pakiet ten zawiera:
- jscript - biblioteka KDE do javascript,
- kdecore - Biblioteka podstawowa,
- KDE kdeui - Biblioteka KDE do interfejsu u¿ytkownika,
- kfmlib - Biblioteka KDE file manager library,
- khtmlw: Biblioteka KDE z HTML widget,
- mediatool: Biblioteka KDE mediatool.

%package devel
Summary:	kdelibs - header files and development documentation
Summary(pl):	kdelibs - pliki nagówkowe i dokumentacja do kdelibs
Group:		X11/KDE/Development/Libraries
Group(de):	X11/KDE/Entwicklung/Libraries
Group(pl):	X11/KDE/Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	arts-devel = %{version}
Obsoletes:	kdelibs-sound-devel
Obsoletes:	kdelibs2-devel
Obsoletes:	kdelibs2-sound-devel

%description devel
This package contains header files and development documentation for
kdelibs.

%description -l pl devel
Pakiet ten zawiera pliki nag³ówkowe i dokumentacjê potrzebn± przy
pisaniu w³asnych programów wykorzystuj±cych kdelibs.

%package -n arts
Summary:	aRts sound server
Summary(pl):	serwer d¼wiêku
Group:		Libraries
Group(pl):	Biblioteki

%description -n arts
aRts sound server.

%description -l pl -n arts
Serwer d¼wiêku aRts.

%package -n arts-devel
Summary:	sound server - header files
Summary(pl):	serwer d¼wiêku - pliki nag³ówkowe
Group:		Developement/Libraries
Group(pl):	Programowanie/Biblioteki

%description -n arts-devel
Header files required to compile programs using arts.

%description -l pl -n arts-devel
Pliki nag³ówkowe niezbêdne do budowania aplikacji korzystaj±cych z arts.

%prep
%setup  -q -n %{name}-%{version}%{sver}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
#%patch4 -p1

# Just to expose errors.
#rm -rf libltdl

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

#autoupdate
#libtoolize --force --copy
#aclocal
#autoheader
#autoconf
#automake -a -c

#cd libltdl
#libtoolize --force --copy
#aclocal
#autoheader
#autoconf
#automake -a -c
#cd ..

CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcflags}" 
ENABLE_DEBUG="%{?debug:--enable-debug}"

%configure2_13 \
	$ENABLE_DEBUG \
	--enable-final \
	--disable-mysql \
	--disable-informix \
	--with-alsa \
	--enable-mitshm \
	#--enable-pgsql
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_pixmapsdir}/{hicolor,locolor}/{16x16,22x22,32x32,48x48}/{actions,apps,devices,filesystems,mimetypes}
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip arts/doc/{README,NEWS,TODO}

%find_lang %{name} --with-kde --all-name

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kdelibs.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dcop
%attr(755,root,root) %{_bindir}/dcopserver
%attr(755,root,root) %{_bindir}/make*
%attr(755,root,root) %{_bindir}/[ilkps]*
%attr(755,root,root) %{_libdir}/[bdhk]*.??
%attr(755,root,root) %{_libdir}/libk[adfhijpst]*.so.*.*
%attr(755,root,root) %{_libdir}/libk[adfijpt]*.la
%attr(755,root,root) %{_libdir}/libkhtml.la
%attr(755,root,root) %{_libdir}/libkspell.la
%attr(755,root,root) %{_libdir}/libkssl.la
%attr(755,root,root) %{_libdir}/libksycoca.la
%attr(755,root,root) %{_libdir}/libkmid.so.*.*
%attr(755,root,root) %{_libdir}/libkmid.la
%attr(755,root,root) %{_libdir}/libkhtmli*.??
# Not found.
# %attr(755,root,root) %{_libdir}/libksasl.??
%attr(755,root,root) %{_libdir}/kde2
%attr(755,root,root) %dir %{_libdir}/mcop

%config %{_datadir}/config
%{_pixmapsdir}
%{_datadir}/apps
%{_datadir}/mimelnk
%{_datadir}/services
%{_datadir}/servicetypes

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dcopidl*
%{_libdir}/libD*.so
%{_libdir}/libk[dfijpt]*.so
%{_libdir}/libks[psy]*.so
%{_libdir}/libkhtml.so
%{_libdir}/libkmid.so
%{_libdir}/libkab.so
# All subdirs not starting with 'a' and all *.h files.
%{_includedir}/[!a]*
%{_includedir}/addressbook.h

%files -n arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artscat
%attr(755,root,root) %{_bindir}/artsd
%attr(755,root,root) %{_bindir}/artsdsp
%attr(755,root,root) %{_bindir}/artsmessage
%attr(755,root,root) %{_bindir}/artsplay
%attr(755,root,root) %{_bindir}/artsshell
%attr(755,root,root) %{_bindir}/artswrapper
%attr(755,root,root) %{_libdir}/lib[amqsx]*.so.*.*
%attr(755,root,root) %{_libdir}/lib[amqsx]*.la
%attr(755,root,root) %{_libdir}/libD*.so.*.*
%attr(755,root,root) %{_libdir}/libD*.la
%attr(755,root,root) %{_libdir}/libkmedia*.so.*.*
%attr(755,root,root) %{_libdir}/libkmedia*.la
%{_libdir}/mcop/*

%files -n arts-devel
%defattr(644,root,root,755)
%doc arts/doc/*.gz
%attr(755,root,root) %{_bindir}/artsc-config
%attr(755,root,root) %{_bindir}/mcopidl
%{_libdir}/lib[amqsx]*.so
%{_libdir}/libkmedia*.so
%{_includedir}/arts
%{_includedir}/artsc
