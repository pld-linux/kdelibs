Summary:	K Desktop Environment - Libraries
Summary(pl):	K Desktop Environment - biblioteki
Name:		kdelibs
Version:	1.94
Release:	1
License:	LGPL
Vendor:		The KDE Team
Group:		X11/KDE/Libraries
Group(de):	X11/KDE/Libraries
Group(pl):	X11/KDE/Biblioteki
Source0:	ftp://ftp.kde.org/pub/kde/unstable/distribution/2.0Beta4/tar/src/%{name}-%{version}.tar.bz2
BuildRequires:	qt-devel >= 2.2.0
BuildRequires:	XFree86-devel
BuildRequires:	libstdc++-devel >= 2.0
BuildRequires:	kdesupport-mimelib-devel = %{version}
BuildRequires:	unixODBC-devel
BuildRequires:	kdesupport-uulib-devel = %{version}
Requires:	qt >= 2.2.0
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
%build
%configure \
	--enable-final
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/Arts
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/Arts/*
%attr(755,root,root) %{_bindir}/*
%config %{_datadir}/config
%{_datadir}/apps
%{_datadir}/doc/*
%{_datadir}/mimelnk/*
%{_datadir}/icons/*
%{_datadir}/services/*
%{_datadir}/servicetypes/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*.h
%{_includedir}/kde.pot
%{_includedir}/arts/*.h
%{_includedir}/arts/*.idl
%{_includedir}/artsc/*.h
%{_includedir}/dom/*.h
%{_includedir}/kio/*.h
%{_includedir}/kparts/*.h
%{_includedir}/kdesu/*.h
%{_includedir}/kjs/*.h
%{_includedir}/libkmid/*.h
