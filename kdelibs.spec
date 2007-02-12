#
# Conditional build:
%bcond_without	alsa		# build without ALSA support
%bcond_without	apidocs		# don't prepare API documentation
%bcond_without  autoreqdep	# don't care about package name deps generated by rpm
%bcond_without	heimdal		# disable kerberos
%bcond_with	verbose		# verbose build
%bcond_without	hidden_visibility	# pass '--fvisibility=hidden'
					# & '--fvisibility-inlines-hidden'
					# to g++
#
%define		_state		unstable

Summary:	K Desktop Environment - libraries
Summary(es.UTF-8):   K Desktop Environment - bibliotecas
Summary(ko.UTF-8):   KDE - 라이브러리
Summary(pl.UTF-8):   K Desktop Environment - biblioteki
Summary(pt_BR.UTF-8):   Bibliotecas de fundação do KDE
Summary(ru.UTF-8):   K Desktop Environment - Библиотеки
Summary(uk.UTF-8):   K Desktop Environment - Бібліотеки
Name:		kdelibs
Version:	3.80.2
Release:	0.2
Epoch:		9
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	697cb962328c21b69ccf81c810030fce
Source1:	pnm.protocol
Source2:	x-icq.mimelnk
Source3:	x-mplayer2.desktop
Patch0:		%{name}-findqt4.patch
URL:		http://www.kde.org/
BuildRequires:	OpenEXR-devel >= 1.2.2
BuildRequires:	Qt3Support-devel >= 4.2.0
BuildRequires:	QtCore-devel >= 4.2.0
BuildRequires:	QtDBus-devel >= 4.2.0
BuildRequires:	QtDesigner-devel >= 4.2.0
BuildRequires:	QtGui-devel >= 4.2.0
BuildRequires:	QtSvg-devel >= 4.2.0
BuildRequires:	QtUiTools-devel >= 4.2.0
BuildRequires:	QtXml-devel >= 4.2.0
BuildRequires:	acl-devel
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	aspell-devel
BuildRequires:	audiofile-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6.1
BuildRequires:	bzip2-devel
BuildRequires:	cmake
BuildRequires:	cups-devel
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-utils
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	ed
BuildRequires:	fam-devel
%{?with_hidden_visibility:BuildRequires:	gcc-c++ >= 5:4.1.0-0.20051206r108118.1}
BuildRequires:	gettext-devel
%{?with_apidocs:BuildRequires:	graphviz}
%{?with_heimdal:BuildRequires:	heimdal-devel}
BuildRequires:	hspell-devel
BuildRequires:	jasper-devel >= 1.600
BuildRequires:	libart_lgpl-devel
BuildRequires:	libidn-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel >= 2.0
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:1.5-2
BuildRequires:	libvorbis-devel
BuildRequires:	libwmf-devel >= 2:0.2.0
BuildRequires:	libxml2-devel >= 2.4.9
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel >= 1.0.7
BuildRequires:	lua50-devel
BuildRequires:	mdns-bonjour-devel
BuildRequires:	openmotif-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pcre-devel >= 3.5
BuildRequires:	pkgconfig
%{?with_apidocs:BuildRequires:	qt4-doc}
BuildRequires:	qt4-qmake
BuildRequires:	qt4-build
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	zlib-devel
%if %{with autoreqdep}
BuildConflicts:	kdebase-core < 9:3.4.0
BuildConflicts:	kdepim-korganizer-libs
BuildConflicts:	kdepim-libkdepim < 3:3.3.0
%endif
Requires:	QtCore >= 4.2.0
Requires:	arts >= %{artsver}
Requires:	docbook-dtd412-xml
Requires:	docbook-dtd42-xml
Requires:	docbook-style-xsl
Requires:	hicolor-icon-theme
Requires:	setup >= 2.4.6-7
Requires:	xorg-app-iceauth
Obsoletes:	arts-kde
Obsoletes:	kde-theme-keramik
Obsoletes:	kdelibs-kabc
Obsoletes:	kdelibs-sound
Obsoletes:	kdelibs2
Obsoletes:	kdelibs2-sound
Obsoletes:	kdesupport
Obsoletes:	kdesupport-devel
Obsoletes:	kdesupport-mimelib
Obsoletes:	kdesupport-mimelib-devel
Obsoletes:	kdesupport-mimelib-static
Obsoletes:	kdesupport-static
Obsoletes:	kimproxy
# No longer supported/existing
Obsoletes:	arts-message
Obsoletes:	kde-sdscreen-KDEGirl
Obsoletes:	kde-sdscreen-default
Obsoletes:	kde-splash-KDEGirl < 03-5
Obsoletes:	kde-splash-default
Obsoletes:	kde-splash-keramik
Obsoletes:	kdeadmin-kwuftpd
Obsoletes:	kdeadmin-kxconfig
Obsoletes:	kdebase-kwmtheme
Obsoletes:	kdebase-mailnews
Obsoletes:	kdeedu-kgeo
Obsoletes:	kdegames-megami
Obsoletes:	kdenetwork-kmail
Obsoletes:	kdenetwork-knode
Obsoletes:	kdenetwork-kxmlrpcd
Obsoletes:	kdepim-commonlibs
Obsoletes:	kdepim-kaplan
Obsoletes:	kdesdk
Obsoletes:	kdesdk-devel
# More
Obsoletes:	kde-style-plastik
Obsoletes:	kdepim-kaddressbook < 3:3.1.91.030918-1
Obsoletes:	kdepim-kmail < 3:3.1.91.030918-1
Obsoletes:	kdepim-kontact < 3:3.1.91.030918-1
Obsoletes:	kdepim-korganizer < 3:3.1.91.030918-1
Obsoletes:	kdepim-libkcal < 3:3.1.91.030918-1
Obsoletes:	kdepim-libkdenetwork < 3:3.1.91.030918-1
Obsoletes:	kdepim-libkdepim < 3:3.2.90
Obsoletes:	kdetoys-kaphorism < 9:3.2.0
Obsoletes:	openoffice-mimelinks
Conflicts:	kaffeine <= 0.5-1
Conflicts:	kdeaddons-konqueror < 1:3.4.0
Conflicts:	kdebase-core < 9:3.4.0
Conflicts:	kdenetwork-kit < 10:3.3.0
Conflicts:	kdepim-devel < 3:3.2.90
Conflicts:	kmplayer <= 2:0.8.4-1
Conflicts:	kplayer < 0.5.1-5
Conflicts:	pixieplus < 0.3-4
Conflicts:	sim < 0.9.3-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	libtool(.*)

# confuses OpenEXR detection
%undefine	configure_cache

%description
This package includes libraries that are central to the development
and execution of a KDE program, misc HTML documentation and theme
modules.

Included in this package are among others:
- kdecore - KDE core library,
- kdeui - KDE user interface library,
- khtml - KDE HTML widget with javascript and CSS support,
- kwallet - KDE password manager.

%description -l es.UTF-8
Bibliotecas para KDE.

%description -l pl.UTF-8
Ten pakiet zawiera biblioteki potrzebne do rozwijania i uruchamiania
aplikacji KDE, różną dokumentację oraz moduły z motywami wyglądu KDE.

Pakiet ten zawiera między innymi:
- kdecore - podstawową bibliotekę KDE,
- kdeui - interfejs użytkownika KDE,
- khtml - obsługę HTML, javascript oraz CSS dla KDE,
- kwallet - system zarządzania hasłami w KDE.

%description -l pt_BR.UTF-8
Bibliotecas de fundação do KDE requeridas por todo e qualquer
aplicativo KDE.

%description -l ru.UTF-8
Библиотеки для K Desktop Environment.

Включены библиотеки KDE:
- jscript (javascript),
- kdecore (ядро KDE),
- kdeui (интерфейс пользователя),
- khtmlw (работа с HTML),
- kimgio (обработка изображений).
- kspell (проверка орфографии),

%description -l uk.UTF-8
Бібліотеки для K Desktop Environment.

Включені такі бібліотеки KDE:
- jscript (javascript),
- kdecore (ядро KDE),
- kdeui (інтерфейс користувача),
- khtmlw (робота з HTML),
- kimgio (обробка зображень).
- kspell (перевірка орфографії),

%package libs
Summary:	KDE libraries
Summary(pl.UTF-8):   Biblioteki KDE
Group:		Libraries

%description libs
KDE libraries.

%description libs -l pl.UTF-8
Biblioteki KDE.

%package devel
Summary:	kdelibs - header files and development documentation
Summary(pl.UTF-8):   kdelibs - pliki nagłówkowe i dokumentacja do kdelibs
Summary(pt_BR.UTF-8):   Arquivos de inclusão e documentação para compilar aplicativos KDE
Summary(ru.UTF-8):   Хедеры и документация для компилляции программ KDE
Summary(uk.UTF-8):   Хедери та документація для компіляції програм KDE
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	acl-devel
Requires:	fam-devel
Requires:	libart_lgpl-devel
Requires:	libidn-devel
Requires:	mdns-bonjour-devel
Requires:	pcre-devel
#Requires:	qt-devel >= 6:3.3.3-4
Requires:	xorg-lib-libXmu-devel
Requires:	xorg-lib-libXt-devel
Obsoletes:	arts-kde-devel
Obsoletes:	kdelibs-sound-devel
Obsoletes:	kdelibs-static
Obsoletes:	kdelibs2-devel
Obsoletes:	kdelibs2-sound-devel
Obsoletes:	kttsd-devel
Conflicts:	kdebase-devel <= 9:3.1.90

%description devel
This package contains header files and development documentation for
kdelibs.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących kdelibs.

%description devel -l pt_BR.UTF-8
Este pacote contém os arquivos de inclusão que são necessários para
compilar aplicativos KDE.

%description devel -l ru.UTF-8
Этот пакет содержит хедеры, необходимые для компиляции программ для
KDE.

%description devel -l uk.UTF-8
Цей пакет містить хедери, необхідні для компіляції програм для KDE.

%package apidocs
Summary:	API documentation
Summary(pl.UTF-8):   Dokumentacja API
Group:		Documentation
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	kttsd-apidocs

%description apidocs
Annotated reference of KDE libraries programming interface including:
- class lists
- class members
- namespaces

%description apidocs -l pl.UTF-8
Dokumentacja interfejsu programowania bibliotek KDE z przypisami.
Zawiera:
- listy klas i ich składników
- listę przestrzeni nazw (namespace)

%package artsmessage
Summary:	Program used to display aRts daemon messages
Summary(pl.UTF-8):   Program do wyświetlania komunikatów demona aRts
Group:		Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	arts-message

%description artsmessage
This program is run when a -m option argument is passed to aRts
daemon. It displays messages generated by daemon.

%description artsmessage -l pl.UTF-8
Ten program jest uruchamiany, gdy do demona aRts zostanie przekazana
opcja z parametrem -m. Będzie on używany do wyświetlenia komunikatów
demona.

%package kgrantpty
Summary:	Helper program to fix terminal permissions
Summary(pl.UTF-8):   Program pomocniczy do ustawiania uprawnień terminala
Group:		Applications/Terminal
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description kgrantpty
This suid root program fixes the permissions of pseudo-terminal device
files so that they cannot be eavesdropped by other local users.
Systems that support /dev/pts (typical PLD installations do) don't
require an extra program to do it, in that case this package is
useless.

Install this package if you're running a custom system that lacks
Unix98 pts support and privacy from other local users is a concern for
you.

%description kgrantpty -l pl.UTF-8
Ten program, działający z uprawnieniami roota, poprawia uprawnienia
plików pseudo-terminali, żeby uniknąć ich podsłuchiwania przez innych
lokalnych użytkowników. Systemy obsługujące /dev/pts (typowe
instalacje PLD go obsługują) nie wymagają do tego dodatkowego
programu, w tym przypadku ten pakiet jest bezużyteczny.

Zainstaluj ten pakiet jeżeli korzystasz z nietypowej konfiguracji
nieobsługującej pts-ów typu Unix98 i obawiasz się inwigilacji ze
strony innych użytkowników lokalnych.

%prep
%setup -q
%patch0 -p0

%build
export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}
export KDEDIR=%{_prefix}
export QTDIR=%{_prefix}
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cd build
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

#install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/services
#install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/mimelnk/application/x-icq.desktop
#install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/mimelnk/application

install -d \
	$RPM_BUILD_ROOT/etc/security \
	$RPM_BUILD_ROOT%{_libdir}/kconf_update_bin \
	$RPM_BUILD_ROOT%{_datadir}/applnk/.hidden \
	$RPM_BUILD_ROOT%{_datadir}/apps/khtml/kpartplugins \
	$RPM_BUILD_ROOT%{_datadir}/apps/profiles \
	$RPM_BUILD_ROOT%{_datadir}/apps/remotes \
	$RPM_BUILD_ROOT%{_datadir}/config/magic \
	$RPM_BUILD_ROOT%{_datadir}/config.kcfg \
	$RPM_BUILD_ROOT%{_datadir}/services/kconfiguredialog \
	$RPM_BUILD_ROOT%{_iconsdir}/crystalsvg/{16x16,22x22,32x32,48x48,64x64,128x128}/apps

# For fileshare
touch $RPM_BUILD_ROOT/etc/security/fileshare.conf
%{__sed} -i -e 's|/etc/init.d|/etc/rc.d/init.d|g' $RPM_BUILD_ROOT%{_bindir}/fileshare*

if [ -d $RPM_BUILD_ROOT%{_kdedocdir}/en/%{name}-%{version}-apidocs ] ; then
	mv -f $RPM_BUILD_ROOT%{_kdedocdir}/en/%{name}-{%{version}-,}apidocs
fi

# packaged by hicolor-icon-theme
rm $RPM_BUILD_ROOT%{_iconsdir}/hicolor/index.theme

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%ghost /etc/security/fileshare.conf
%attr(755,root,root) %{_bindir}/checkXML
%attr(755,root,root) %{_bindir}/cupsdconf
%attr(755,root,root) %{_bindir}/cupsdoprint
%attr(2755,root,fileshare) %{_bindir}/fileshareset
%attr(755,root,root) %{_bindir}/kaddprinterwizard
%attr(755,root,root) %{_bindir}/imagetops
%attr(755,root,root) %{_bindir}/kbuildsycoca
%attr(755,root,root) %{_bindir}/kcmshell
%attr(755,root,root) %{_bindir}/kconf_update
%attr(755,root,root) %{_bindir}/kcookiejar
%attr(755,root,root) %{_bindir}/kde4-config
%attr(755,root,root) %{_bindir}/kde-menu
%attr(755,root,root) %{_bindir}/kded
%attr(755,root,root) %{_bindir}/kdeinit
%attr(755,root,root) %{_bindir}/kdeinit_shutdown
%attr(755,root,root) %{_bindir}/kdeinit_wrapper
%attr(755,root,root) %{_bindir}/kdesu_stub
%attr(755,root,root) %{_bindir}/kdontchangethehostname
%attr(755,root,root) %{_bindir}/kdostartupconfig
%attr(755,root,root) %{_bindir}/kfile
%attr(755,root,root) %{_bindir}/khotnewstuff
%attr(755,root,root) %{_bindir}/kinstalltheme
%attr(755,root,root) %{_bindir}/kio_http_cache_cleaner
%attr(755,root,root) %{_bindir}/kio_uiserver
%attr(755,root,root) %{_bindir}/kioexec
%attr(755,root,root) %{_bindir}/kioslave
%attr(755,root,root) %{_bindir}/kjscmd
%attr(755,root,root) %{_bindir}/kjsconsole
%attr(755,root,root) %{_bindir}/klauncher
%attr(755,root,root) %{_bindir}/kmailservice
%attr(755,root,root) %{_bindir}/knotify
%attr(755,root,root) %{_bindir}/knotifytest
%attr(755,root,root) %{_bindir}/kpac_dhcp_helper
%attr(755,root,root) %{_bindir}/ksendbugmail
%attr(755,root,root) %{_bindir}/kshell
%attr(755,root,root) %{_bindir}/kstartupconfig
%attr(755,root,root) %{_bindir}/ksvgtopng
%attr(755,root,root) %{_bindir}/ktelnetservice
%attr(755,root,root) %{_bindir}/ktradertest
%attr(755,root,root) %{_bindir}/kunittestmodrunner
%attr(755,root,root) %{_bindir}/kwrapper
%attr(755,root,root) %{_bindir}/lnusertemp
%attr(755,root,root) %{_bindir}/make_driver_db_cups
%attr(755,root,root) %{_bindir}/make_driver_db_lpr
%attr(755,root,root) %{_bindir}/makekdewidgets
%attr(755,root,root) %{_bindir}/meinproc
%attr(755,root,root) %{_bindir}/preparetips

%dir %{_datadir}/apps
%dir %{_datadir}/apps/kconf_update
%attr(755,root,root) %{_datadir}/apps/kconf_update/*.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/*.sh
%{_datadir}/apps/kconf_update/*.upd

%{_datadir}/apps/LICENSES
%{_datadir}/apps/katepart
%{_datadir}/apps/kcertpart
%{_datadir}/apps/kcm_componentchooser
%{_datadir}/apps/kdeprint
%{_datadir}/apps/kdeui
%{_datadir}/apps/kdewidgets
%{_datadir}/apps/khtml
%{_datadir}/apps/kio_uiserver
%{_datadir}/apps/kjava
%{_datadir}/apps/knotify
%{_datadir}/apps/ksgmltools2
%{_datadir}/apps/kssl
%{_datadir}/apps/kstyle
%{_datadir}/apps/ktexteditor_docwordcompletion
%{_datadir}/apps/ktexteditor_insertfile
%{_datadir}/apps/ktexteditor_isearch
%{_datadir}/apps/ktexteditor_kdatatool
%{_datadir}/apps/proxyscout

%dir %{_datadir}/apps/emoticons
%{_datadir}/apps/emoticons/Default

%dir %{_datadir}/apps/knotifytest
%{_datadir}/apps/knotifytest/knotifytest.notifyrc
%{_datadir}/apps/knotifytest/knotifytestui.rc

%dir %{_datadir}/apps/solidfakehwbackend
%{_datadir}/apps/solidfakehwbackend/fakecomputer.xml
%dir %{_datadir}/apps/solidfakenetbackend
%{_datadir}/apps/solidfakenetbackend/fakenetworking.xml

%dir %{_datadir}/services
%{_datadir}/services/kded
%{_datadir}/services/*.desktop
%{_datadir}/services/*.protocol

%dir %{_datadir}/services/qimageioplugins
%{_datadir}/services/qimageioplugins/*.desktop

%dir %{_datadir}/services/solidbackends
%{_datadir}/services/solidbackends/*.desktop

%dir %{_datadir}/services/phononbackends
%{_datadir}/services/phononbackends/fake.desktop

%{_iconsdir}/crystalsvg

%dir %{_datadir}/apps/kde
%{_datadir}/apps/kde/kde.notifyrc

%dir %{_docdir}/HTML/en
%lang(en) %{_docdir}/HTML/en/common

%dir %{_datadir}/applnk
%dir %{_datadir}/applnk/.hidden
%dir %{_datadir}/apps/profiles
%dir %{_datadir}/apps/remotes
%dir %{_datadir}/config.kcfg
%dir %{_datadir}/services/kconfiguredialog

%{_datadir}/config
%{_datadir}/locale/all_languages
%{_datadir}/mimelnk
%{_datadir}/servicetypes

%dir %{_prefix}%{_sysconfdir}/xdg/menus
%{_prefix}%{_sysconfdir}/xdg/menus/applications.menu

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkde3support.so.*
%attr(755,root,root) %{_libdir}/libkdecore.so.*
%attr(755,root,root) %{_libdir}/libkdefakes.so.*
%attr(755,root,root) %{_libdir}/libkdefx.so.*
%attr(755,root,root) %{_libdir}/libkdeprint.so.*
%attr(755,root,root) %{_libdir}/libkdeprint_management.so.*
%attr(755,root,root) %{_libdir}/libkdesu.so.*
%attr(755,root,root) %{_libdir}/libkdeui.so.*
%attr(755,root,root) %{_libdir}/libkdnssd.so.*
%attr(755,root,root) %{_libdir}/libkdocument.so.*
%attr(755,root,root) %{_libdir}/libkhtml.so.*
%attr(755,root,root) %{_libdir}/libkimproxy.so.*
%attr(755,root,root) %{_libdir}/libkio.so.*
%attr(755,root,root) %{_libdir}/libkjs.so.*
%attr(755,root,root) %{_libdir}/libkjsembed.so.*
%attr(755,root,root) %{_libdir}/libkmediaplayer.so.*
%attr(755,root,root) %{_libdir}/libknewstuff.so.*
%attr(755,root,root) %{_libdir}/libknotifyconfig.so.*
%attr(755,root,root) %{_libdir}/libkntlm.so.*
%attr(755,root,root) %{_libdir}/libkparts.so.*
%attr(755,root,root) %{_libdir}/libkspell2.so.*
%attr(755,root,root) %{_libdir}/libktexteditor.so.*
%attr(755,root,root) %{_libdir}/libkunittest.so.*
%attr(755,root,root) %{_libdir}/libkutils.so.*
%attr(755,root,root) %{_libdir}/libkwalletbackend.so.*
%attr(755,root,root) %{_libdir}/libkwalletclient.so.*
%attr(755,root,root) %{_libdir}/libkxmlcore.so.*
%attr(755,root,root) %{_libdir}/libphononcore.so.*
%attr(755,root,root) %{_libdir}/libphononui.so.*
%attr(755,root,root) %{_libdir}/libsolid.so.*
%attr(755,root,root) %{_libdir}/libsolidifaces.so.*
%attr(755,root,root) %{_libdir}/libthreadweaver.so.*

%dir %{_libdir}/kde4
%attr(755,root,root) %{_libdir}/kde4/*.so
%dir %{_libdir}/kde4/plugins
%dir %{_libdir}/kde4/plugins/designer
%attr(755,root,root) %{_libdir}/kde4/plugins/designer/kdewidgets.so
%dir %{_libdir}/kde4/plugins/styles
%attr(755,root,root) %{_libdir}/kde4/plugins/styles/keramik.so
%attr(755,root,root) %{_libdir}/kde4/plugins/styles/plastik.so
%dir %{_libdir}/kde4/plugins/imageformats
%attr(755,root,root) %{_libdir}/kde4/plugins/imageformats/kimg*.so
%dir %{_libdir}/kconf_update_bin

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kconfig_compiler
%{_datadir}/apps/cmake
%attr(755,root,root) %{_libdir}/libkdeinit_kaddprinterwizard.so
%attr(755,root,root) %{_libdir}/libkde3support.so
%attr(755,root,root) %{_libdir}/libkdecore.so
%attr(755,root,root) %{_libdir}/libkdefakes.so
%attr(755,root,root) %{_libdir}/libkdefx.so
%attr(755,root,root) %{_libdir}/libkdeinit_cupsdconf.so
%attr(755,root,root) %{_libdir}/libkdeinit_kbuildsycoca.so
%attr(755,root,root) %{_libdir}/libkdeinit_kcmshell.so
%attr(755,root,root) %{_libdir}/libkdeinit_kconf_update.so
%attr(755,root,root) %{_libdir}/libkdeinit_kded.so
%attr(755,root,root) %{_libdir}/libkdeinit_kio_http_cache_cleaner.so
%attr(755,root,root) %{_libdir}/libkdeinit_kio_uiserver.so
%attr(755,root,root) %{_libdir}/libkdeinit_klauncher.so
%attr(755,root,root) %{_libdir}/libkdeinit_knotify.so
%attr(755,root,root) %{_libdir}/libkdeprint.so
%attr(755,root,root) %{_libdir}/libkdeprint_management.so
%attr(755,root,root) %{_libdir}/libkdesu.so
%attr(755,root,root) %{_libdir}/libkdeui.so
%attr(755,root,root) %{_libdir}/libkdnssd.so
%attr(755,root,root) %{_libdir}/libkdocument.so
%attr(755,root,root) %{_libdir}/libkhtml.so
%attr(755,root,root) %{_libdir}/libkimproxy.so
%attr(755,root,root) %{_libdir}/libkio.so
%attr(755,root,root) %{_libdir}/libkjs.so
%attr(755,root,root) %{_libdir}/libkjsembed.so
%attr(755,root,root) %{_libdir}/libkmediaplayer.so
%attr(755,root,root) %{_libdir}/libknewstuff.so
%attr(755,root,root) %{_libdir}/libknotifyconfig.so
%attr(755,root,root) %{_libdir}/libkntlm.so
%attr(755,root,root) %{_libdir}/libkparts.so
%attr(755,root,root) %{_libdir}/libkspell2.so
%attr(755,root,root) %{_libdir}/libktexteditor.so
%attr(755,root,root) %{_libdir}/libkunittest.so
%attr(755,root,root) %{_libdir}/libkutils.so
%attr(755,root,root) %{_libdir}/libkwalletbackend.so
%attr(755,root,root) %{_libdir}/libkwalletclient.so
%attr(755,root,root) %{_libdir}/libkxmlcore.so
%attr(755,root,root) %{_libdir}/libphononcore.so
%attr(755,root,root) %{_libdir}/libphononui.so
%attr(755,root,root) %{_libdir}/libsolid.so
%attr(755,root,root) %{_libdir}/libsolidifaces.so
%attr(755,root,root) %{_libdir}/libthreadweaver.so
%{_includedir}/*

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
#%{_kdedocdir}/en/%{name}*-apidocs
%endif

%files artsmessage
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/artsmessage

%files kgrantpty
%defattr(644,root,root,755)
%attr(4755,root,root) %{_bindir}/kgrantpty
