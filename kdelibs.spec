Summary:	K Desktop Environment - Libraries
Summary(pl):	K Desktop Environment - biblioteki
Name:		kdelibs
Version:	1.1.1
Release:	1
Vendor:		The KDE Team
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/distribution/tar/generic/source/bz2/%{name}-%{version}.tar.bz2
Source1:	kdelnk2wmconfig
Source2:	kderc.PLD
Group:		X11/KDE/Libraries
Group(pl):	X11/KDE/Biblioteki
Copyright:	LGPL
BuildPrereq:	qt-devel >= 1.44
Requires:	qt >= 1.44
URL:		http://www.kde.org/
BuildRoot:	/tmp/%{name}-%{version}-root

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
Group:		X11/KDE/Libraries
Group(pl):	X11/KDE/Biblioteki
Requires:	%{name} = %{version}

%description devel
This package contains header files and development documentation for
kdelibs.

%description -l pl devel
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy pisaniu
własnych programów wykorzystujących kdelibs.

%prep
%setup -q 

%build
# Setup KDE directories to be compatible with FSSTD
# Other KDE apps will use them automatically
export KDEDIR=/usr/X11R6
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

CXXFLAGS="$RPM_OPT_FLAGS -Wall -fno-rtti -fno-exceptions" \
CFLAGS="$RPM_OPT_FLAGS -Wall" \
./configure %{_target} \
	--prefix=$KDEDIR \
	--with-install-root=$RPM_BUILD_ROOT \
	--disable-path-check
make

(cd mediatool/Documentation; make)
dvips -f < mediatool/Documentation/Doc.dvi | gzip -9nf > mediatool.ps.gz

%install
rm -rf $RPM_BUILD_ROOT

# create directories for KDE apps (they should belong to some package)
install -d $RPM_BUILD_ROOT/etc/X11/kde/{applnk,mimelnk} \
	$RPM_BUILD_ROOT/usr/X11R6/{bin,share/kde/{wallpapers,icons/mini,sounds}} \
	$RPM_BUILD_ROOT/usr/X11R6/lib/kde/{cgi-bin,parts}

export KDEDIR=/usr/X11R6
make prefix="$RPM_BUILD_ROOT$KDEDIR" install

install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/bin
install %{SOURCE2} $RPM_BUILD_ROOT/etc/X11/kde/kderc

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/lib/lib*.so.*.*
%config /etc/X11/kde
%docdir /usr/X11R6/share/kde/doc
/usr/X11R6/share/kde/doc/*
/usr/X11R6/share/kde/toolbar
/usr/X11R6/share/kde/apps
/usr/X11R6/share/kde/wallpapers
/usr/X11R6/share/kde/icons
/usr/X11R6/share/kde/sounds
/usr/X11R6/lib/kde/cgi-bin
/usr/X11R6/lib/kde/parts

%lang(br)           /usr/X11R6/share/locale/br/LC_MESSAGES/kde.mo
%lang(br)           /usr/X11R6/share/locale/br/charset
%lang(ca)           /usr/X11R6/share/locale/ca/LC_MESSAGES/kde.mo
%lang(ca)           /usr/X11R6/share/locale/ca/charset
%lang(cs)           /usr/X11R6/share/locale/cs/LC_MESSAGES/kde.mo
%lang(cs)           /usr/X11R6/share/locale/cs/charset
%lang(da)           /usr/X11R6/share/locale/da/LC_MESSAGES/kde.mo
%lang(da)           /usr/X11R6/share/locale/da/charset
%lang(de)           /usr/X11R6/share/locale/de/LC_MESSAGES/kde.mo
%lang(de)           /usr/X11R6/share/locale/de/charset
%lang(el)           /usr/X11R6/share/locale/el/LC_MESSAGES/kde.mo
%lang(en_UK)        /usr/X11R6/share/locale/en_UK/LC_MESSAGES/kde.mo
%lang(eo)           /usr/X11R6/share/locale/eo/LC_MESSAGES/kde.mo
%lang(eo)           /usr/X11R6/share/locale/eo/charset
%lang(es)           /usr/X11R6/share/locale/es/LC_MESSAGES/kde.mo
%lang(es)           /usr/X11R6/share/locale/es/charset
%lang(et)           /usr/X11R6/share/locale/et/LC_MESSAGES/kde.mo
%lang(et)           /usr/X11R6/share/locale/et/charset
%lang(fi)           /usr/X11R6/share/locale/fi/LC_MESSAGES/kde.mo
%lang(fi)           /usr/X11R6/share/locale/fi/charset
%lang(fr)           /usr/X11R6/share/locale/fr/LC_MESSAGES/kde.mo
%lang(fr)           /usr/X11R6/share/locale/fr/charset
%lang(he)           /usr/X11R6/share/locale/he/LC_MESSAGES/kde.mo
%lang(he)           /usr/X11R6/share/locale/he/charset
%lang(hr)           /usr/X11R6/share/locale/hr/LC_MESSAGES/kde.mo
%lang(hr)           /usr/X11R6/share/locale/hr/charset
%lang(hu)           /usr/X11R6/share/locale/hu/LC_MESSAGES/kde.mo
%lang(hu)           /usr/X11R6/share/locale/hu/charset
%lang(is)           /usr/X11R6/share/locale/is/LC_MESSAGES/kde.mo
%lang(is)           /usr/X11R6/share/locale/is/charset
%lang(it)           /usr/X11R6/share/locale/it/LC_MESSAGES/kde.mo
%lang(it)           /usr/X11R6/share/locale/it/charset
%lang(ko)           /usr/X11R6/share/locale/ko/LC_MESSAGES/kde.mo
%lang(mk)           /usr/X11R6/share/locale/mk/LC_MESSAGES/kde.mo
%lang(nl)           /usr/X11R6/share/locale/nl/LC_MESSAGES/kde.mo
%lang(no)           /usr/X11R6/share/locale/no/LC_MESSAGES/kde.mo
%lang(no)           /usr/X11R6/share/locale/no/charset
%lang(pl)           /usr/X11R6/share/locale/pl/LC_MESSAGES/kde.mo
%lang(pl)           /usr/X11R6/share/locale/pl/charset
%lang(pt_BR)        /usr/X11R6/share/locale/pt_BR/LC_MESSAGES/kde.mo
%lang(pt_BR)        /usr/X11R6/share/locale/pt_BR/charset
%lang(ro)           /usr/X11R6/share/locale/ro/LC_MESSAGES/kde.mo
%lang(ro)           /usr/X11R6/share/locale/ro/charset
%lang(ru)           /usr/X11R6/share/locale/ru/LC_MESSAGES/kde.mo
%lang(ru)           /usr/X11R6/share/locale/ru/charset
%lang(sk)           /usr/X11R6/share/locale/sk/LC_MESSAGES/kde.mo
%lang(sk)           /usr/X11R6/share/locale/sk/charset
%lang(sl)           /usr/X11R6/share/locale/sl/LC_MESSAGES/kde.mo
%lang(sl)           /usr/X11R6/share/locale/sl/charset
%lang(sv)           /usr/X11R6/share/locale/sv/LC_MESSAGES/kde.mo
%lang(sv)           /usr/X11R6/share/locale/sv/charset
%lang(tr)           /usr/X11R6/share/locale/tr/LC_MESSAGES/kde.mo
%lang(zh_CN.GB2312) /usr/X11R6/share/locale/zh_CN.GB2312/LC_MESSAGES/kde.mo
%lang(zh_TW.Big5)   /usr/X11R6/share/locale/zh_TW.Big5/LC_MESSAGES/kde.mo

%files devel
%defattr(644,root,root,755)
%doc mediatool/Documentation
%attr(755,root,root) /usr/X11R6/bin/*
/usr/X11R6/lib/lib*.so
/usr/X11R6/lib/lib*.la
/usr/X11R6/include/*.h

%changelog
* Mon Apr  3 1999 Jacek Konieczny <jajcus@zeus.polsl.gliwice.pl>
  [1.1-2]
- URL added
- more locales added
- charset files added
- lib*.so.* files added

* Mon Dec  9 1998 Tomasz Kłoczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0-7]
- recompiled against libstdc++.so.2.9.

* Sun Sep 27 1998 Jacek Konieczny <jajcus@zeus.polsl.gliwice.pl>
  [1.0-6]
- prefix changed to $KDEDIR,
- Group changed to /X11/KDE/Libraries.

* Sun Sep 27 1998 Jacek Konieczny <jajcus@zeus.polsl.gliwice.pl>
  [1.0-5]
- added custom kderc file to properly configure icons path (for
  icons from fvwm) ,
- make basic KDE directories owned by this package,
- changed filename "mediatool.gz" to "mediatool.ps.gz" for file type
  to be clear,
- changed directory structure - config dirs to /etc/X11/kde,
  other shared to /usr/X11R6/share/kde,
- added script "kdelnk2wmconfig" to devel package, to make packaging KDE
  applications easier,
- changed qt-includes to /usr/X11R6/include/X11/qt to be compatible with PLD's
  qt-devel package.
  
* Tue Sep 15 1998 Tomasz Kłoczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0-4]
- changed KDEDIR to /usr/X11R6.

* Mon Aug  3 1998 Tomasz Kłoczko <kloczek@rudy.mif.pg.gda.pl>
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
- added %lang macros for %{_datadir}/locale/*/LC_MESSAGES/ files,
- "rm -rf $RPM_BUILD_ROOT" moved from %prep to %install.
