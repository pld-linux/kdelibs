Summary:	K Desktop Environment - Libraries
Summary(pl):	K Desktop Environment - biblioteki
Name:		kdelibs
Version:	1.1.2
Release:	13
Group:		X11/KDE/Libraries
Group(pl):	X11/KDE/Biblioteki
Copyright:	LGPL
Vendor:		The KDE Team
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/distribution/tar/generic/source/bz2/%{name}-%{version}.tar.bz2
Source1:	kderc.PLD
Patch0:		kdelibs-DESTDIR.patch
Patch1:		kdelibs-iconpaths.patch
Patch2:		kdelibs-x-kdelnk.patch
Icon:		kdelibs.xpm
BuildRequires:	qt-devel >= 1.44
BuildRequires:	XFree86-devel
Requires:	qt >= 1.44
URL:		http://www.kde.org/
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix 		/usr/X11R6
%define		_sysconfdir		/etc/X11/kde
%define		_kde_htmldir		%{_datadir}/doc/HTML
%define		_kde_icondir		%{_datadir}/icons
%define		_kde_minidir		%{_datadir}/icons/mini
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
kdeui:     Biblioteka KDE do interfejsu użytkownika
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
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy pisaniu
własnych programów wykorzystujących kdelibs.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

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

automake
perl admin/automoc -padmin
CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -Wall -DNO_DEBUG"
LDFLAGS="-s"
export CXXFLAGS LDFLAGS
%configure \
	--with-qt-dir=%{_prefix} \
	--disable-path-check
make

(cd mediatool/Documentation; make)
dvips -f < mediatool/Documentation/Doc.dvi | gzip -9nf > mediatool.ps.gz

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR="$RPM_BUILD_ROOT"

#install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/kde/kderc

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

%find_lang kde

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kde.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%config /etc/X11/kde
%{_kde_toolbardir}
%{_kde_datadir}

%lang(br) %{_kde_locale}/br/charset
%lang(ca) %{_kde_locale}/ca/charset
%lang(cs) %{_kde_locale}/cs/charset
%lang(da) %{_kde_locale}/da/charset
%lang(de) %{_kde_locale}/de/charset
%lang(eo) %{_kde_locale}/eo/charset
%lang(es) %{_kde_locale}/es/charset
%lang(et) %{_kde_locale}/et/charset
%lang(fi) %{_kde_locale}/fi/charset
%lang(fr) %{_kde_locale}/fr/charset
%lang(he) %{_kde_locale}/he/charset
%lang(hr) %{_kde_locale}/hr/charset
%lang(hu) %{_kde_locale}/hu/charset
%lang(is) %{_kde_locale}/is/charset
%lang(it) %{_kde_locale}/it/charset
%lang(no) %{_kde_locale}/no/charset
%lang(pl) %{_kde_locale}/pl/charset
%lang(pt) %{_kde_locale}/pt*/charset
%lang(ro) %{_kde_locale}/ro/charset
%lang(ru) %{_kde_locale}/ru/charset
%lang(sk) %{_kde_locale}/sk/charset
%lang(sl) %{_kde_locale}/sl/charset
%lang(sv) %{_kde_locale}/sv/charset

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_includedir}/*.h
%{_libdir}/lib*.la
