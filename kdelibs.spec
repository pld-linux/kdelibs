Summary:     K Desktop Environment - Libraries
Summary(pl): K Desktop Environment - biblioteki
Name:        kdelibs
Version:     1.0
Release:     4
Source:      ftp://ftp.kde.org/pub/kde/stable/%{version}/distribution/tar/generic/source/%{name}-%{version}.tar.gz
Group:       X11/KDE/Base
Copyright:   LGPL
Requires:    qt >= 1.40
Vendor:      The KDE Team
BuildRoot:   /tmp/%{name}-%{version}-root

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
Summary:     kdelibs - header files and development documentation
Group:       X11/KDE/Development
Requires:    %{name} = %{version}

%description devel
This package contains header files and development documentation for
kdelibs.

%description -l pl devel
Pakiet ten zawiera pliki nag³ówkowe i dokumentacjê potrzebn± przy pisaniu
w³asnych programów wykorzystuj±cych kdelibs.

%prep
%setup -q

%build
export KDEDIR=/usr/X11R6
CXXFLAGS="$RPM_OPT_FLAGS -Wall" CFLAGS="$RPM_OPT_FLAGS -Wall" \
./configure --prefix=$KDEDIR \
	--disable-path-check \
	--with-qt-includes=/usr/X11R6/include/qt
make KDEDIR=$KDEDIR

(cd mediatool/Documentation; make)
dvips -f < mediatool/Documentation | gzip -9nf > mediatool.gz

%install
rm -rf $RPM_BUILD_ROOT
export KDEDIR=/usr/X11R6
make prefix=$RPM_BUILD_ROOT$KDEDIR install

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644, root, root, 755)
%attr(755, root, root) /usr/X11R6/lib/lib*.so.*.*
/usr/X11R6/share/apps/*
/usr/X11R6/share/config
/usr/X11R6/share/doc
/usr/X11R6/share/toolbar

%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kde.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kde.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/kde.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kde.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kde.mo
%lang(en) /usr/X11R6/share/locale/en*/LC_MESSAGES/kde.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kde.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kde.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kde.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kde.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kde.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kde.mo
%lang(mk) /usr/X11R6/share/locale/mk/LC_MESSAGES/kde.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kde.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kde.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kde.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kde.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kde.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kde.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kde.mo
%lang(sl) /usr/X11R6/share/locale/sl/LC_MESSAGES/kde.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kde.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kde.mo

%files devel
%defattr(644, root, root, 755)
%doc mediatool.gz
/usr/X11R6/lib/lib*.so
/usr/X11R6/lib/lib*.la
/usr/X11R6/include/*.h

%changelog
* Tue Sep 15 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0-4]
- changed KDEDIR to /usr/X11R6.

* Mon Aug  3 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0-3]
- removed using macros kdename, version and kderelease,
- added pl translation,
- added real %files,
- added using $RPM_OPT_FLAGS during compilation,
- added postscript %doc for mediatool (devel),
- removed qt-egcs-10x, redhat-release from Requires list,
- added devel subpackage,
- removed Packager field from spec (if you want recompile package and
  redistribute this package later put this in your private .rpmrc),
- removed Distribution field (this also must be placed in private .rpmrc),
- removed comment about RH from %description,
- base dir changed to /usr,
- added -q an emoved -n %setup parameter,
- Buildroot changed to /tmp/%%{name}-%%{version}-root,
- simplified %post{un} and now ldconfig is -p parameter this sections,
- added using %%{name} and %%{version} macros in Source,
- added %lang macros for /usr/share/locale/*/LC_MESSAGES/ files,
- "rm -rf $RPM_BUILD_ROOT" moved from %prep to %install.
