Summary:	K Desktop Environment - Libraries
Summary(pl):	K Desktop Environment - biblioteki
Name:		kdelibs
Version:	1.93
Release:	1
Group:		X11/KDE/Libraries
Group(pl):	X11/KDE/Biblioteki
Copyright:	LGPL
Vendor:		The KDE Team
Source0:	ftp://ftp.kde.org/pub/kde/snapshots/current/%{name}-%{version}.tar.bz2
Patch0:		%{name}-install-catalog.patch
BuildRequires:	qt-devel >= 2.2.0_beta2
BuildRequires:	XFree86-devel
BuildRequires:	libstdc++-devel >= 2.0
BuildRequires:	kdesupport-mimelib-devel = %{version}
BuildRequires:	unixODBC-devel
BuildRequires:	kdesupport-uulib-devel = %{version}
Requires:	qt >= 2.2.0_beta2
URL:		http://www.kde.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix 		/usr/X11R6
%define		_sysconfdir		/etc/X11/kde
%define		_kde_htmldir		%{_datadir}/doc/HTML
%define		_kde_icondir		%{_datadir}/pixmaps
%define		_kde_minidir		%{_kde_icondir}/mini
%define		_kde_appsdir		%{_datadir}/applnk
%define		_kde_sounddir		%{_datadir}/sounds
%define		_kde_datadir		%{_datadir}/apps
%define		_kde_locale		%{_datadir}/locale
%define		_kde_cgidir		%{_libdir}/kde/cgi-bin
%define		_kde_confdir		%{_sysconfdir}
%define		_kde_mimedir		%{_datadir}/mimelnk
%define		_kde_toolbardir		%{_datadir}/kde/toolbar
%define		_kde_wallpaperdir	%{_datadir}/wallpapers
%define		_kde_bindir		%{_bindir}
%define		_kde_partsdir		%{_libdir}/parts

%description
Libraries for the K Desktop Environment.

Included with this package are:

jscript:   KDE javascript library
kdecore:   KDE core library 
kdeui:     KDE user interface library
kfmlib:    KDE file manager library
khtmlw:    KDE HTML widget
mediatool: KDE mediatool library

%description -l pl
Biblioteki do K Desktop Environment.

Pakiet ten zawiera:

jscript:   biblioteka KDE do javascript
kdecore:   Biblioteka podstawowa KDE
kdeui:     Biblioteka KDE do interfejsu u¿ytkownika
kfmlib:    Biblioteka KDE file manager library
khtmlw:    Biblioteka KDE z HTML widget
mediatool: Biblioteka KDE mediatool

%package devel
Summary:	kdelibs - header files and development documentation
Summary(pl):	kdelibs - pliki nagówkowe i dokumentacja do kdelibs
Group:		X11/KDE/Development/Libraries
Group(pl):	X11/KDE/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This package contains header files and development documentation for
kdelibs.

%description -l pl devel
Pakiet ten zawiera pliki nag³ówkowe i dokumentacjê potrzebn± przy pisaniu
w³asnych programów wykorzystuj±cych kdelibs.

%prep
%setup  -q
%patch0 -p1
%build
export KDEDIR=%{_prefix}

kde_htmldir=%{_kde_htmldir}
kde_icondir=%{_kde_icondir}
kde_minidir=%{_kde_minidir}
kde_appsdir=%{_kde_appsdir}
kde_sounddir=%{_kde_sounddir}
kde_datadir=%{_kde_datadir}
kde_locale=%{_kde_locale}
kde_cgidir=%{_kde_cgidir}
kde_confdir=%{_kde_confdir}
kde_mimedir=%{_kde_mimedir}
kde_toolbardir=%{_kde_toolbardir}
kde_wallpaperdir=%{_kde_wallpaperdir}
kde_bindir=%{_kde_bindir}
kde_partsdir=%{_kde_partsdir}
export  kde_htmldir kde_icondir kde_minidir kde_appsdir kde_sounddir \
	kde_datadir kde_locale kde_cgidir kde_confdir kde_mimedir \
	kde_toolbardir kde_wallpaperdir kde_bindir kde_partsdir
aclocal
#autoheader
#automake
autoconf
CXXFLAGS="$RPM_OPT_FLAGS -Wall -DNO_DEBUG"; export CXXFLAGS
LDFLAGS="-s"; export LDFLAGS
%configure \
	--with-qt-dir=%{_prefix} \
	--disable-path-check
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

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
%config /etc/X11/kde
%{_kde_datadir}
%{_datadir}/doc/*
%{_datadir}/mimelnk/*
%{_datadir}/pixmaps/*
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
