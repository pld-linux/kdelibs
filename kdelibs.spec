Summary:	K Desktop Environment - Libraries
Summary(pl):	K Desktop Environment - biblioteki
Name:		kdelibs
Version:	1.1.2
Release:	2.1
Group:		X11/KDE/Libraries
Group(pl):	X11/KDE/Biblioteki
Copyright:	LGPL
Vendor:		The KDE Team
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/distribution/tar/generic/source/bz2/%{name}-%{version}.tar.bz2
Source1:	kderc.PLD
BuildRequires:	qt-devel >= 1.44
BuildRequires:	XFree86-devel
BuildRequires:	mico-devel
Requires:	qt >= 1.44
URL:		http://www.kde.org/
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix /usr/X11R6

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
Group:		X11/KDE/Libraries
Group(pl):	X11/KDE/Biblioteki
Requires:	%{name} = %{version}

%description devel
This package contains header files and development documentation for
kdelibs.

%description -l pl devel
Pakiet ten zawiera pliki nag³ówkowe i dokumentacjê potrzebn± przy pisaniu
w³asnych programów wykorzystuj±cych kdelibs.

%prep
%setup -q

%build
# Setup KDE directories to be compatible with FSSTD
# Other KDE apps will use them automatically
export KDEDIR=%{_prefix}
export kde_locale='\$(prefix)/share/locale'
export kde_htmldir='\$(prefix)/share/kde/doc/HTML'
export kde_datadir='\$(prefix)/share/kde/apps'
export kde_icondir='\$(prefix)/share/kde/icons'
export kde_toolbardir='\$(prefix)/share/kde/toolbar'
export kde_wallpaperdir='\$(prefix)/share/kde/wallpapers'
export kde_sounddir='\$(prefix)/share/kde/sounds'
export kde_cgidir='\$(prefix)/lib/kde/cgi-bin'
export kde_partsdir='\$(prefix)/lib/kde/parts'
# these must be relative to $(prefix) for BuildRoot to work :-(
export kde_confdir='\$(prefix)/../../etc/X11/kde'
export kde_mimedir='\$(prefix)/../../etc/X11/kde/mimelnk'
export kde_appsdir='\$(prefix)/../../etc/X11/kde/applnk'

CXXFLAGS="$RPM_OPT_FLAGS -Wall -fno-rtti" \
CFLAGS="$RPM_OPT_FLAGS -Wall" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=$KDEDIR \
	--with-install-root=$RPM_BUILD_ROOT \
	--with-qt-dir=%{_prefix} \
	--disable-path-check
make

(cd mediatool/Documentation; make)
dvips -f < mediatool/Documentation/Doc.dvi | gzip -9nf > mediatool.ps.gz

%install
rm -rf $RPM_BUILD_ROOT

# create directories for KDE apps (they should belong to some package)
install -d $RPM_BUILD_ROOT/etc/X11/kde/{applnk,mimelnk} \
	$RPM_BUILD_ROOT{%{_bindir},%{_datadir}/kde/{wallpapers,icons/mini,sounds}} \
	$RPM_BUILD_ROOT%{_libdir}/kde/{cgi-bin,parts}

export KDEDIR=/usr/X11R6
make prefix="$RPM_BUILD_ROOT$KDEDIR" install

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/kde/kderc

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
%docdir %{_datadir}/kde/doc
%{_datadir}/kde/doc/*
%{_datadir}/kde/toolbar
%{_datadir}/kde/apps
%{_datadir}/kde/wallpapers
%{_datadir}/kde/icons
%{_datadir}/kde/sounds
%{_libdir}/kde/cgi-bin
%{_libdir}/kde/parts

%lang(br) %{_datadir}/locale/br/charset
%lang(ca) %{_datadir}/locale/ca/charset
%lang(cs) %{_datadir}/locale/cs/charset
%lang(da) %{_datadir}/locale/da/charset
%lang(de) %{_datadir}/locale/de/charset
%lang(eo) %{_datadir}/locale/eo/charset
%lang(es) %{_datadir}/locale/es/charset
%lang(et) %{_datadir}/locale/et/charset
%lang(fi) %{_datadir}/locale/fi/charset
%lang(fr) %{_datadir}/locale/fr/charset
%lang(he) %{_datadir}/locale/he/charset
%lang(hr) %{_datadir}/locale/hr/charset
%lang(hu) %{_datadir}/locale/hu/charset
%lang(is) %{_datadir}/locale/is/charset
%lang(it) %{_datadir}/locale/it/charset
%lang(no) %{_datadir}/locale/no/charset
%lang(pl) %{_datadir}/locale/pl/charset
%lang(pt) %{_datadir}/locale/pt*/charset
%lang(ro) %{_datadir}/locale/ro/charset
%lang(ru) %{_datadir}/locale/ru/charset
%lang(sk) %{_datadir}/locale/sk/charset
%lang(sl) %{_datadir}/locale/sl/charset
%lang(sv) %{_datadir}/locale/sv/charset

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_includedir}/kde.pot
%{_includedir}/*.h
%{_libdir}/lib*.la
