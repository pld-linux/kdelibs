Summary:	K Desktop Environment - Libraries
Summary(pl):	K Desktop Environment - biblioteki
Name:		kdelibs
Version:	2.1
Release:	4
Epoch:		6
License:	LGPL
Vendor:		The KDE Team
Group:		X11/KDE/Libraries
Group(de):	X11/KDE/Libraries
Group(pl):	X11/KDE/Biblioteki
Source0:	ftp://ftp.kde.org/pub/kde/stable/2.1/distribution/tar/generic/src/%{name}-%{version}.tar.bz2
Patch0:		%{name}-final.patch
Patch1:		%{name}-nodebug.patch
Patch2:		%{name}-directories.patch
Patch3:		%{name}-Japanese.patch
Patch4:		%{name}-klauncher-escape.patch
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
BuildRequires:	kdesupport-mimelib-devel = %{version}
BuildRequires:	openssl-devel
BuildRequires:	qt-devel >= 2.2.2
BuildRequires:	unixODBC-devel
BuildRequires:	gettext-devel
BuildRequires:	zlib-devel
BuildRequires:	openssl-devel
BuildRequires:	bzip2-devel
BuildRequires:	postgresql-devel
Requires:	qt >= 2.2.4
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
Requires:	%{name} = %{version}

%description -n arts
aRts sound server.

%description -l pl -n arts
Serwer d¼wiêku aRts.

%package -n arts-devel
Summary:	sound server - header files
Summary(pl):	serwer d¼wiêku - pliki nag³ówkowe
Group:		Developement/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description -n arts-devel
Header files required to compile programs using arts.

%description -l pl -n arts-devel
Pliki nag³ówkowe niezbêdne do budowania aplikacji korzystaj±cych z arts.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

CFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O0 -g}"
CXXFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O0 -g}" 
ENABLE_DEBUG="%{?debug:--enable-debug}"
%configure \
	$ENABLE_DEBUG \
	--enable-final \
	--disable-mysql \
	--disable-informix \
	--enable-pgsql
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde --all-name

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kdelibs.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/[^a]*

%attr(755,root,root) %{_libdir}/lib[^a]*.so.*.*
%attr(755,root,root) %{_libdir}/[^l]*.so
%attr(755,root,root) %{_libdir}/libkhtmli*.so
%attr(755,root,root) %{_libdir}/libksasl.so
%{_libdir}/[^l]*.la
%{_libdir}/lib[^a]*.la
%attr(755,root,root) %{_libdir}/kde2
%attr(755,root,root) %dir %{_libdir}/mcop

%config %{_datadir}/config
%{_htmldir}/default
%{_pixmapsdir}
%{_datadir}/apps
%{_datadir}/mimelnk
%{_datadir}/services
%{_datadir}/servicetypes

%files devel
%defattr(644,root,root,755)
%doc arts/doc/*
%attr(755,root,root) %{_bindir}/artsc-config
%attr(755,root,root) %{_bindir}/dcopidl2cpp
%attr(755,root,root) %{_bindir}/mcopidl

%{_libdir}/libkd*.so
%{_libdir}/libkf*.so
%{_libdir}/libkhtml.so
%{_libdir}/libki*.so
%{_libdir}/libkj*.so
%{_libdir}/libkm*.so
%{_libdir}/libkp*.so
%{_libdir}/libksp*.so
%{_libdir}/libkss*.so
%{_libdir}/libksy*.so
%{_libdir}/libkt*.so
%{_libdir}/libD*.so
%{_libdir}/libmcop.so
%{_libdir}/libqtmcop.so
%{_libdir}/libsound*.so
%{_libdir}/libx11*.so
%{_includedir}/addressbook.h
%{_includedir}/[^a]*

%files -n arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artscat
%attr(755,root,root) %{_bindir}/artsd
%attr(755,root,root) %{_bindir}/artsdsp
%attr(755,root,root) %{_bindir}/artsplay
%attr(755,root,root) %{_bindir}/artsshell
%attr(755,root,root) %{_bindir}/artswrapper

%attr(755,root,root) %{_libdir}/liba*.so.*.*
%attr(755,root,root) %{_libdir}/liba*.la
%attr(755,root,root) %{_libdir}/mcop/Arts
%{_libdir}/mcop/*.*

%files -n arts-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artsc-config
%{_includedir}/arts
%{_includedir}/artsc
