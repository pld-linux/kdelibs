Summary:	K Desktop Environment - Libraries
Summary(pl):	K Desktop Environment - biblioteki
Name:		kdelibs
Version:	2.0
Release:	2
Epoch:		6
License:	LGPL
Vendor:		The KDE Team
Group:		X11/KDE/Libraries
Group(de):	X11/KDE/Libraries
Group(pl):	X11/KDE/Biblioteki
Source0:	ftp://ftp.kde.org/pub/kde/stable/2.0/distribution/generic/tar/src/%{name}-%{version}.tar.bz2
Patch0:		%{name}-final.patch
Patch1:		%{name}-nodebug.patch
Icin:		%{name}.xpm
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
BuildRequires:	qt-devel >= 2.2.1
BuildRequires:	unixODBC-devel
Requires:	qt >= 2.2.1
URL:		http://www.kde.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	 		/usr/X11R6
%define		_includedir		%{_prefix}/include/kde

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

%description devel
This package contains header files and development documentation for
kdelibs.

%description -l pl devel
Pakiet ten zawiera pliki nag³ówkowe i dokumentacjê potrzebn± przy
pisaniu w³asnych programów wykorzystuj±cych kdelibs.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--enable-final
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf arts/doc/{LICENSE,MCOP,TODO}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/Arts
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/[^l]*.so
%attr(755,root,root) %{_libdir}/Arts/*
%attr(755,root,root) %{_bindir}/artscat
%attr(755,root,root) %{_bindir}/artsd
%attr(755,root,root) %{_bindir}/artsdsp
%attr(755,root,root) %{_bindir}/artsplay
%attr(755,root,root) %{_bindir}/artswrapper
%attr(755,root,root) %{_bindir}/dcop
%attr(755,root,root) %{_bindir}/dcopidl
%attr(755,root,root) %{_bindir}/dcopserver
%attr(755,root,root) %{_bindir}/kbuildsycoca
%attr(755,root,root) %{_bindir}/kcookiejar
%attr(755,root,root) %{_bindir}/kdb2html
%attr(755,root,root) %{_bindir}/kded
%attr(755,root,root) %{_bindir}/kdeinit
%attr(755,root,root) %{_bindir}/kdeinit_wrapper
%attr(755,root,root) %{_bindir}/kdesu_stub
%attr(755,root,root) %{_bindir}/kio_http_cache_cleaner
%attr(755,root,root) %{_bindir}/kio_uiserver
%attr(755,root,root) %{_bindir}/klauncher
%attr(755,root,root) %{_bindir}/kmailservice
%attr(755,root,root) %{_bindir}/knotify
%attr(755,root,root) %{_bindir}/ksendbugmail
%attr(755,root,root) %{_bindir}/lnusertemp
%attr(755,root,root) %{_bindir}/settheme

%config %{_datadir}/config
%{_datadir}/apps
%{_datadir}/doc
%{_datadir}/mimelnk
%{_datadir}/icons
%{_datadir}/services
%{_datadir}/servicetypes

%files devel
%defattr(644,root,root,755)
%docdir %{_docdir}/%{_name}-%{_version}-devel/Arts
%doc arts/doc/*
%attr(755,root,root) %{_bindir}/artsc-config
%attr(755,root,root) %{_bindir}/dcopidl2cpp
%attr(755,root,root) %{_bindir}/mcopidl

%{_libdir}/lib*.so
%{_libdir}/*.la
%{_includedir}/*.h
%{_includedir}/arts
%{_includedir}/artsc
%{_includedir}/dom
%{_includedir}/kio
%{_includedir}/kparts
%{_includedir}/kdesu
%{_includedir}/kjs
%{_includedir}/libkmid
