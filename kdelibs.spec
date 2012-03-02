# TODO
# - switch to kde trinity: http://trinity.pearsoncomputing.net/ (see TRINITY branch of kdelibs.spec)
#
# Conditional build:
%bcond_without	alsa			# build without ALSA support
%bcond_with	arts			# build with aRts support
%bcond_without	apidocs			# don't prepare API documentation
%bcond_without	autoreqdep		# don't care about package name deps generated by rpm
%bcond_without	kerberos5		# disable kerberos
%bcond_without	hidden_visibility	# no gcc hidden visibility

%define		_state		stable
%define		artsver		13:1.5.10

Summary:	K Desktop Environment 3 libraries
Summary(es.UTF-8):	K Desktop Environment 3 - bibliotecas
Summary(ko.UTF-8):	KDE 3 - 라이브러리
Summary(pl.UTF-8):	Biblioteki K Desktop Environment 3
Summary(pt_BR.UTF-8):	Bibliotecas de fundação do KDE 3
Summary(ru.UTF-8):	K Desktop Environment 3 - Библиотеки
Summary(uk.UTF-8):	K Desktop Environment 3 - Бібліотеки
Name:		kdelibs
Version:	3.5.10
Release:	26
Epoch:		9
License:	LGPL v2
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	43cd55ed15f63b5738d620ef9f9fd568
Source1:	%{name}-wmfplugin.tar.bz2
# Source1-md5:	df0d7c2a13bb68fe25e1d6c009df5b8d
Source2:	pnm.protocol
Source3:	x-icq.mimelnk
Source4:	x-mplayer2.desktop
Source5:	https://www.cacert.org/certs/root.crt
# Source5-md5:	fb262d55709427e2e9acadf2c1298c99
Patch100:	%{name}-branch.diff
Patch0:		kde-common-PLD.patch
Patch1:		%{name}-kstandarddirs.patch
Patch2:		%{name}-inotify.patch
Patch3:		%{name}-use_system_sgml.patch
Patch4:		%{name}-fileshareset.patch
Patch5:		%{name}-appicon_themable.patch
Patch6:		%{name}-kbugreport-https.patch
Patch7:		%{name}-xgl.patch
Patch8:		kde-ac260-lt.patch
Patch9:		%{name}-lib_loader.patch
# http://kate-editor.org/downloads/syntax_highlighting?kateversion=2.5
Patch10:	%{name}-kate-syntax.patch
Patch11:	%{name}-konqueror-ti-agent.patch
Patch12:	%{name}-konqueror-agent.patch
Patch13:	kde-am.patch
Patch14:	ac264.patch
Patch15:	dcopobject-destruct-crash.patch
Patch16:	kdelibs-3.5.10-gcc_4.4-2.patch
Patch17:	kdelibs-3.5.10-LDFLAG_fix-1.patch
# http://www.thel.ro/kde3-fedora/SOURCES/kdelibs-3.5.10-ossl-1.x.patch
Patch18:	kdelibs-3.5.10-ossl-1.x.patch
Patch19:	kdelibs-gcc4.patch
URL:		http://www.kde.org/
BuildRequires:	OpenEXR-devel >= 1.4.0.a
BuildRequires:	acl-devel
%{?with_alsa:BuildRequires:	alsa-lib-devel}
%{?with_arts:BuildRequires:	arts-qt-devel >= %{artsver}}
%{?with_arts:BuildRequires:	artsc-devel >= %{artsver}}
BuildRequires:	aspell-devel
BuildRequires:	audiofile-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6.1
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	bzip2-devel
BuildRequires:	cups-devel >= 1:1.3.0
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	fam-devel
%{?with_hidden_visibility:BuildRequires:	gcc-c++ >= 5:4.1.0-0.20051206r108118.1}
BuildRequires:	gettext-devel
# <sys/inotify.h>
BuildRequires:	glibc-devel >= 6:2.4
%{?with_kerberos5:BuildRequires:	heimdal-devel}
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
BuildRequires:	qt-devel >= 6:3.3.3-4
%{?with_hidden_visibility:BuildRequires:	qt-devel >= 6:3.3.5.051113-1}
%{?with_apidocs:BuildRequires:	qt-doc}
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.129
#BuildRequires:	unsermake >= 040511
BuildRequires:	zlib-devel
%if %{with autoreqdep}
BuildConflicts:	kdebase-core < 9:3.4.0
BuildConflicts:	kdepim-korganizer-libs
BuildConflicts:	kdepim-libkdepim < 3:3.3.0
%endif
%{?with_arts:Requires:	arts >= %{artsver}}
Requires:	cups-lib >= 1:1.3.0
Requires:	docbook-dtd412-xml
Requires:	docbook-dtd42-xml
Requires:	docbook-style-xsl
Requires:	hicolor-icon-theme
Requires:	kde-common-dirs
Requires:	libxml2-progs
Requires:	qt >= 6:3.3.3-4
Requires:	setup >= 2.4.6-7
Requires:	xorg-app-iceauth
Obsoletes:	arts-kde
Obsoletes:	kde-theme-keramik
Obsoletes:	kdelibs-kabc
Obsoletes:	kdelibs-libs < 9:3.5.10-17
Obsoletes:	kdelibs-shared
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

# confuses OpenEXR detection
%undefine	configure_cache

# build broken with spaces in CC
%undefine	with_ccache

%description
This package includes libraries that are central to the development
and execution of a KDE 3 programs, misc HTML documentation and theme
modules.

Included in this package are among others:
- kdecore - KDE core library,
- kdeui - KDE user interface library,
- khtml - KDE HTML widget with javascript and CSS support,
- kwallet - KDE password manager.

%description -l es.UTF-8
Bibliotecas para KDE 3.

%description -l pl.UTF-8
Ten pakiet zawiera biblioteki potrzebne do rozwijania i uruchamiania
aplikacji KDE 3, różną dokumentację oraz moduły z motywami wyglądu
KDE.

Pakiet ten zawiera między innymi:
- kdecore - podstawową bibliotekę KDE,
- kdeui - interfejs użytkownika KDE,
- khtml - obsługę HTML, javascript oraz CSS dla KDE,
- kwallet - system zarządzania hasłami w KDE.

%description -l pt_BR.UTF-8
Bibliotecas de fundação do KDE 3 requeridas por todo e qualquer
aplicativo KDE.

%description -l ru.UTF-8
Библиотеки для K Desktop Environment 3.

Включены библиотеки KDE:
- jscript (javascript),
- kdecore (ядро KDE),
- kdeui (интерфейс пользователя),
- khtmlw (работа с HTML),
- kimgio (обработка изображений).
- kspell (проверка орфографии),

%description -l uk.UTF-8
Бібліотеки для K Desktop Environment 3.

Включені такі бібліотеки KDE:
- jscript (javascript),
- kdecore (ядро KDE),
- kdeui (інтерфейс користувача),
- khtmlw (робота з HTML),
- kimgio (обробка зображень).
- kspell (перевірка орфографії),

%package devel
Summary:	kdelibs 3 - header files and development documentation
Summary(pl.UTF-8):	kdelibs 3 - pliki nagłówkowe i dokumentacja do kdelibs
Summary(pt_BR.UTF-8):	Arquivos de inclusão e documentação para compilar aplicativos KDE 3
Summary(ru.UTF-8):	Хедеры и документация для компилляции программ KDE 3
Summary(uk.UTF-8):	Хедери та документація для компіляції програм KDE 3
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	acl-devel
%{?with_arts:Requires:	arts-qt-devel >= %{artsver}}
%{?with_arts:Requires:	artsc-devel >= %{artsver}}
Requires:	fam-devel
Requires:	libart_lgpl-devel
Requires:	libidn-devel
Requires:	mdns-bonjour-devel
Requires:	pcre-devel
Requires:	qt-devel >= 6:3.3.3-4
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
Summary(pl.UTF-8):	Dokumentacja API
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
Summary(pl.UTF-8):	Program do wyświetlania komunikatów demona aRts
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
Summary(pl.UTF-8):	Program pomocniczy do ustawiania uprawnień terminala
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

# unresolved symbols in libkscreensaver.so.X (by design)
%define	no_install_post_check_so	1

%prep
%setup -q -a1
%patch100 -p0
%patch0 -p1
%patch2 -p1
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%if "%{pld_release}" == "ti"
%patch11 -p1
%else
%patch12 -p1
%endif
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1

mv -f configure{,.dist}

# add https://www.cacert.org/ root certificate
cp -a %{SOURCE5} kio/kssl/kssl/cacert.pem
echo 'cacert.pem' >> kio/kssl/kssl/localcerts

%build
# merge cacert root certificate
cd kio/kssl/kssl
./mergelocal
cd -

cp /usr/share/automake/config.sub admin
export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}
if [ ! -f configure ]; then
	%{__make} -f admin/Makefile.common cvs
fi

export path_sudo=/usr/bin/sudo
%configure \
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	%{!?debug:--disable-rpath} \
	--disable-final \
	%{?with_hidden_visibility:--enable-gcc-hidden-visibility} \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--enable-mitshm \
	--with%{!?with_alsa:out}-alsa \
	--with%{!?with_arts:out}-arts \
	--with-distribution="PLD Linux Distribution" \
	--with-ldap=no \
	--with-lua-includes=%{_includedir}/lua50 \
	--with-qt-libraries=%{_libdir} \
	--with-sudo-kdesu-backend

%{__make}
%{?with_apidocs:%{__make} apidox}
rm -f makeinstall.stamp

%install
if [ ! -f makeinstall.stamp -o ! -d $RPM_BUILD_ROOT ]; then
	rm -rf makeinstall.stamp installed.stamp $RPM_BUILD_ROOT

	%{__make} install \
		DESTDIR=$RPM_BUILD_ROOT \
		kde_htmldir=%{_kdedocdir}
		kde_libs_htmldir=%{_kdedocdir}

	touch makeinstall.stamp
fi

if [ ! -f installed.stamp ]; then
	cp -a %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/services
	cp -a %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/mimelnk/application/x-icq.desktop
	cp -a %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/mimelnk/application

	install -d \
		$RPM_BUILD_ROOT/etc/security \
		$RPM_BUILD_ROOT%{_libdir}/kconf_update_bin \
		$RPM_BUILD_ROOT%{_datadir}/applnk/.hidden \
		$RPM_BUILD_ROOT%{_datadir}/services/.hidden \
		$RPM_BUILD_ROOT%{_datadir}/apps/khtml/kpartplugins \
		$RPM_BUILD_ROOT%{_datadir}/apps/profiles \
		$RPM_BUILD_ROOT%{_datadir}/apps/remotes \
		$RPM_BUILD_ROOT%{_datadir}/config/magic \
		$RPM_BUILD_ROOT%{_datadir}/services/kconfiguredialog \
		$RPM_BUILD_ROOT%{_iconsdir}/crystalsvg/{16x16,22x22,32x32,48x48,64x64,128x128}/apps

	install -d $RPM_BUILD_ROOT%{_kdedocdir}/{ca,cs,da,de,en,en_GB,es,et,fi,fr,hu,it,ja,nb,nl,pl,pt,pt_BR,ro,ru,sk,sl,sv,tr,uk,zh_TW}/common

	# should be hardlinked, not copied
	ln -nf $RPM_BUILD_ROOT%{_bindir}/{kdeinit_wrapper,kdeinit_shutdown}

	# For fileshare
	touch $RPM_BUILD_ROOT/etc/security/fileshare.conf
	%{__sed} -i -e 's|/etc/init.d|/etc/rc.d/init.d|g' $RPM_BUILD_ROOT%{_bindir}/fileshare*

	if [ -d $RPM_BUILD_ROOT%{_kdedocdir}/en/%{name}-%{version}-apidocs ] ; then
		mv -f $RPM_BUILD_ROOT%{_kdedocdir}/en/%{name}-{%{version}-,}apidocs
	fi

	# packaged by hicolor-icon-theme
	%{__rm} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/index.theme

	# remove *.la for dynamic plugins. kde lib loader handles .so now.
	%{__rm} $RPM_BUILD_ROOT%{_libdir}/kde3/*.la
	# keep $RPM_BUILD_ROOT%{_libdir}/kde3/plugins/designer/kdewidget.la for kdebase and others.
	%{__rm} $RPM_BUILD_ROOT%{_libdir}/kde3/plugins/styles/*.la
	%{__rm} $RPM_BUILD_ROOT%{_libdir}/libkdeinit_*.la

	# remove unwanted boost deps from .la
	sed -i 's:-lboost_filesystem -lboost_regex::' $RPM_BUILD_ROOT%{_libdir}/kde3/plugins/designer/kdewidgets.la
	sed -i 's:-lboost_filesystem -lboost_regex::' $RPM_BUILD_ROOT%{_libdir}/*.la

	touch installed.stamp
fi

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%ghost /etc/security/fileshare.conf
%attr(755,root,root) %{_bindir}/checkXML
%attr(755,root,root) %{_bindir}/cupsdconf
%attr(755,root,root) %{_bindir}/cupsdoprint
%attr(755,root,root) %{_bindir}/dcop
%attr(755,root,root) %{_bindir}/dcopclient
%attr(755,root,root) %{_bindir}/dcopfind
%attr(755,root,root) %{_bindir}/dcopidlng
%attr(755,root,root) %{_bindir}/dcopobject
%attr(755,root,root) %{_bindir}/dcopquit
%attr(755,root,root) %{_bindir}/dcopref
%attr(755,root,root) %{_bindir}/dcopserver
%attr(755,root,root) %{_bindir}/dcopserver_shutdown
%attr(755,root,root) %{_bindir}/dcopstart
#%attr(755,root,root) %{_bindir}/ghns
%attr(2755,root,fileshare) %{_bindir}/filesharelist
%attr(2755,root,fileshare) %{_bindir}/fileshareset
%attr(755,root,root) %{_bindir}/imagetops
%attr(755,root,root) %{_bindir}/kaddprinterwizard
%attr(755,root,root) %{_bindir}/kbuildsycoca
%attr(755,root,root) %{_bindir}/kcmshell
%attr(755,root,root) %{_bindir}/kconf_update
%attr(755,root,root) %{_bindir}/kcookiejar
%attr(755,root,root) %{_bindir}/kde-config
%attr(755,root,root) %{_bindir}/kde-menu
%attr(755,root,root) %{_bindir}/kded
%attr(755,root,root) %{_bindir}/kdeinit
%attr(755,root,root) %{_bindir}/kdeinit_shutdown
%attr(755,root,root) %{_bindir}/kdeinit_wrapper
%attr(755,root,root) %{_bindir}/kdesu_stub
%attr(755,root,root) %{_bindir}/kdontchangethehostname
%attr(755,root,root) %{_bindir}/kdostartupconfig
%attr(755,root,root) %{_bindir}/kfile
%attr(755,root,root) %{_bindir}/kfmexec
%attr(755,root,root) %{_bindir}/khotnewstuff
# removed?
#%attr(755,root,root) %{_bindir}/kimage_concat
%attr(755,root,root) %{_bindir}/kinstalltheme
%attr(755,root,root) %{_bindir}/kio_http_cache_cleaner
%attr(755,root,root) %{_bindir}/kio_uiserver
%attr(755,root,root) %{_bindir}/kioexec
%attr(755,root,root) %{_bindir}/kioslave
%attr(755,root,root) %{_bindir}/klauncher
%attr(755,root,root) %{_bindir}/kmailservice
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
%attr(4755,root,root) %{_bindir}/start_kdeinit
%attr(755,root,root) %{_bindir}/start_kdeinit_wrapper

%dir %{_datadir}/apps
%{_datadir}/apps/LICENSES
%dir %{_datadir}/apps/dcopidlng
%attr(755,root,root) %{_datadir}/apps/dcopidlng/kalyptus
%{_datadir}/apps/dcopidlng/*.pm
%{_datadir}/apps/katepart
%{_datadir}/apps/kcertpart
%{_datadir}/apps/kcm_componentchooser
%{_datadir}/apps/kconf_update/*.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/*.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/*.sh
%{_datadir}/apps/kdeprint
%{_datadir}/apps/kdeui
%{_datadir}/apps/kdewidgets
# also contains 3rdparty kpartplugins dir
%{_datadir}/apps/khtml
%{_datadir}/apps/knewstuff
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
%dir %{_datadir}/autostart
%{_datadir}/config
%dir %{_datadir}/emoticons
%{_datadir}/emoticons/Default
%{_datadir}/locale/all_languages
%{_datadir}/mimelnk
%dir %{_datadir}/services
%dir %{_datadir}/services/kresources
%dir %{_datadir}/services/.hidden
%{_datadir}/services/kresources/kabc_manager.desktop
%{_datadir}/services/kded
%{_datadir}/services/http_cache_cleaner.desktop
%{_datadir}/services/katepart.desktop
%{_datadir}/services/kbzip2filter.desktop
%{_datadir}/services/kcertpart.desktop
%{_datadir}/services/kgzipfilter.desktop
%{_datadir}/services/khtml.desktop
%{_datadir}/services/khtmlimage.desktop
%{_datadir}/services/kio_uiserver.desktop
%{_datadir}/services/kjavaappletviewer.desktop
%{_datadir}/services/kmailservice.protocol
%{_datadir}/services/kmultipart.desktop
%{_datadir}/services/knotify.desktop
%{_datadir}/services/kspell_aspell.desktop
%{_datadir}/services/kspell_ispell.desktop
%{_datadir}/services/kspell_hspell.desktop
%{_datadir}/services/ktexteditor_docwordcompletion.desktop
%{_datadir}/services/ktexteditor_insertfile.desktop
%{_datadir}/services/ktexteditor_isearch.desktop
%{_datadir}/services/ktexteditor_kdatatool.desktop
%{_datadir}/services/wmfthumbnail.desktop
%{_datadir}/services/bmp.kimgio
%{_datadir}/services/dds.kimgio
%{_datadir}/services/eps.kimgio
%{_datadir}/services/exr.kimgio
%{_datadir}/services/gif.kimgio
%{_datadir}/services/hdr.kimgio
%{_datadir}/services/ico.kimgio
%{_datadir}/services/jp2.kimgio
%{_datadir}/services/jpeg.kimgio
#%{_datadir}/services/krl.kimgio
%{_datadir}/services/mng.kimgio
%{_datadir}/services/pbm.kimgio
%{_datadir}/services/pcx.kimgio
%{_datadir}/services/pgm.kimgio
%{_datadir}/services/png.kimgio
%{_datadir}/services/ppm.kimgio
%{_datadir}/services/psd.kimgio
%{_datadir}/services/rgb.kimgio
%{_datadir}/services/tga.kimgio
%{_datadir}/services/tiff.kimgio
%{_datadir}/services/xbm.kimgio
%{_datadir}/services/xcf.kimgio
%{_datadir}/services/xpm.kimgio
%{_datadir}/services/xv.kimgio
%{_datadir}/services/data.protocol
%{_datadir}/services/file.protocol
%{_datadir}/services/ftp.protocol
%{_datadir}/services/ghelp.protocol
%{_datadir}/services/help.protocol
%{_datadir}/services/http.protocol
%{_datadir}/services/https.protocol
%{_datadir}/services/metainfo.protocol
%{_datadir}/services/mms.protocol
%{_datadir}/services/pnm.protocol
%{_datadir}/services/rlogin.protocol
%{_datadir}/services/rtsp.protocol
%{_datadir}/services/shellscript.desktop
%{_datadir}/services/ssh.protocol
%{_datadir}/services/telnet.protocol
%{_datadir}/services/webdav.protocol
%{_datadir}/services/webdavs.protocol
%{_datadir}/services/mmst.protocol
%{_datadir}/services/mmsu.protocol
%{_datadir}/services/rtspt.protocol
%{_datadir}/services/rtspu.protocol
%{_datadir}/servicetypes
%dir %{_desktopdir}/kde
# contains also 3rdparty hicolor & crystalsvg/apps trees
%{_iconsdir}/crystalsvg
%{_iconsdir}/default.kde
%dir %{_docdir}/kde
%dir %{_kdedocdir}
%dir %{_kdedocdir}/en
%lang(en) %{_kdedocdir}/en/common
%lang(en) %{_kdedocdir}/en/kspell

%lang(ca) %dir %{_kdedocdir}/ca
%lang(ca) %dir %{_kdedocdir}/ca/common
%lang(cs) %dir %{_kdedocdir}/cs
%lang(cs) %dir %{_kdedocdir}/cs/common
%lang(da) %dir %{_kdedocdir}/da
%lang(da) %dir %{_kdedocdir}/da/common
%lang(de) %dir %{_kdedocdir}/de
%lang(de) %dir %{_kdedocdir}/de/common
%lang(es) %dir %{_kdedocdir}/es
%lang(es) %dir %{_kdedocdir}/es/common
%lang(en_GB) %dir %{_kdedocdir}/en_GB
%lang(en_GB) %dir %{_kdedocdir}/en_GB/common
%lang(et) %dir %{_kdedocdir}/et
%lang(et) %dir %{_kdedocdir}/et/common
%lang(fi) %dir %{_kdedocdir}/fi
%lang(fi) %dir %{_kdedocdir}/fi/common
%lang(fr) %dir %{_kdedocdir}/fr
%lang(fr) %dir %{_kdedocdir}/fr/common
%lang(hu) %dir %{_kdedocdir}/hu
%lang(hu) %dir %{_kdedocdir}/hu/common
%lang(it) %dir %{_kdedocdir}/it
%lang(it) %dir %{_kdedocdir}/it/common
%lang(ja) %dir %{_kdedocdir}/ja
%lang(ja) %dir %{_kdedocdir}/ja/common
%lang(nb) %dir %{_kdedocdir}/nb
%lang(nb) %dir %{_kdedocdir}/nb/common
%lang(nl) %dir %{_kdedocdir}/nl
%lang(nl) %dir %{_kdedocdir}/nl/common
%lang(pl) %dir %{_kdedocdir}/pl
%lang(pl) %dir %{_kdedocdir}/pl/common
%lang(pt) %dir %{_kdedocdir}/pt
%lang(pt) %dir %{_kdedocdir}/pt/common
%lang(pt_BR) %dir %{_kdedocdir}/pt_BR
%lang(pt_BR) %dir %{_kdedocdir}/pt_BR/common
%lang(ro) %dir %{_kdedocdir}/ro
%lang(ro) %dir %{_kdedocdir}/ro/common
%lang(ru) %dir %{_kdedocdir}/ru
%lang(ru) %dir %{_kdedocdir}/ru/common
%lang(sk) %dir %{_kdedocdir}/sk
%lang(sk) %dir %{_kdedocdir}/sk/common
%lang(sl) %dir %{_kdedocdir}/sl
%lang(sl) %dir %{_kdedocdir}/sl/common
%lang(sv) %dir %{_kdedocdir}/sv
%lang(sv) %dir %{_kdedocdir}/sv/common
%lang(tr) %dir %{_kdedocdir}/tr
%lang(tr) %dir %{_kdedocdir}/tr/common
%lang(uk) %dir %{_kdedocdir}/uk
%lang(uk) %dir %{_kdedocdir}/uk/common
%lang(zh_TW) %dir %{_kdedocdir}/zh_TW
%lang(zh_TW) %dir %{_kdedocdir}/zh_TW/common

# 3rdparty directories
%dir %{_datadir}/services/kconfiguredialog

# merged kabc files
%attr(755,root,root) %{_bindir}/kab2kabc
%{_datadir}/apps/kabc
%{_datadir}/autostart/kab2kabc.desktop
%{_datadir}/services/kresources/kabc
%{_desktopdir}/kde/kresources.desktop

%dir %{_libdir}/kde3
%dir %{_libdir}/kde3/plugins
%dir %{_libdir}/kde3/plugins/designer
%attr(755,root,root) %{_libdir}/kde3/plugins/designer/kdewidgets.so
%dir %{_libdir}/kde3/plugins/styles
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/highcolor.so
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/highcontrast.so
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/keramik.so
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/kthemestyle.so
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/light.so
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/plastik.so
%attr(755,root,root) %{_libdir}/kde3/cupsdconf.so
%attr(755,root,root) %{_libdir}/kde3/dcopserver.so
%attr(755,root,root) %{_libdir}/kde3/kaddprinterwizard.so
%attr(755,root,root) %{_libdir}/kde3/kbuildsycoca.so
%attr(755,root,root) %{_libdir}/kde3/kbzip2filter.so
%attr(755,root,root) %{_libdir}/kde3/kcmshell.so
%attr(755,root,root) %{_libdir}/kde3/kconf_update.so
%attr(755,root,root) %{_libdir}/kde3/kcookiejar.so
%attr(755,root,root) %{_libdir}/kde3/kded.so
%attr(755,root,root) %{_libdir}/kde3/kded_kcookiejar.so
%attr(755,root,root) %{_libdir}/kde3/kded_kdeprintd.so
%attr(755,root,root) %{_libdir}/kde3/kded_kdetrayproxy.so
%attr(755,root,root) %{_libdir}/kde3/kded_kpasswdserver.so
%attr(755,root,root) %{_libdir}/kde3/kded_kssld.so
%attr(755,root,root) %{_libdir}/kde3/kded_kwalletd.so
%attr(755,root,root) %{_libdir}/kde3/kded_proxyscout.so
%attr(755,root,root) %{_libdir}/kde3/kdeprint_cups.so
%attr(755,root,root) %{_libdir}/kde3/kdeprint_ext.so
%attr(755,root,root) %{_libdir}/kde3/kdeprint_lpdunix.so
%attr(755,root,root) %{_libdir}/kde3/kdeprint_lpr.so
%attr(755,root,root) %{_libdir}/kde3/kdeprint_rlpr.so
%attr(755,root,root) %{_libdir}/kde3/kdeprint_tool_escputil.so
%attr(755,root,root) %{_libdir}/kde3/kgzipfilter.so
%attr(755,root,root) %{_libdir}/kde3/khtmlimagepart.so
%attr(755,root,root) %{_libdir}/kde3/kimg_dds.so
%attr(755,root,root) %{_libdir}/kde3/kimg_eps.so
%attr(755,root,root) %{_libdir}/kde3/kimg_exr.so
%attr(755,root,root) %{_libdir}/kde3/kimg_hdr.so
%attr(755,root,root) %{_libdir}/kde3/kimg_ico.so
%attr(755,root,root) %{_libdir}/kde3/kimg_jp2.so
%attr(755,root,root) %{_libdir}/kde3/kimg_pcx.so
%attr(755,root,root) %{_libdir}/kde3/kimg_psd.so
%attr(755,root,root) %{_libdir}/kde3/kimg_rgb.so
%attr(755,root,root) %{_libdir}/kde3/kimg_tga.so
%attr(755,root,root) %{_libdir}/kde3/kimg_tiff.so
%attr(755,root,root) %{_libdir}/kde3/kimg_xcf.so
%attr(755,root,root) %{_libdir}/kde3/kimg_xview.so
%attr(755,root,root) %{_libdir}/kde3/kio_file.so
%attr(755,root,root) %{_libdir}/kde3/kio_ftp.so
%attr(755,root,root) %{_libdir}/kde3/kio_ghelp.so
%attr(755,root,root) %{_libdir}/kde3/kio_help.so
%attr(755,root,root) %{_libdir}/kde3/kio_http.so
%attr(755,root,root) %{_libdir}/kde3/kio_http_cache_cleaner.so
%attr(755,root,root) %{_libdir}/kde3/kio_metainfo.so
%attr(755,root,root) %{_libdir}/kde3/kio_uiserver.so
%attr(755,root,root) %{_libdir}/kde3/kjavaappletviewer.so
%attr(755,root,root) %{_libdir}/kde3/klauncher.so
%attr(755,root,root) %{_libdir}/kde3/knotify.so
%attr(755,root,root) %{_libdir}/kde3/kspell_aspell.so
%attr(755,root,root) %{_libdir}/kde3/kspell_ispell.so
%attr(755,root,root) %{_libdir}/kde3/kspell_hspell.so
%attr(755,root,root) %{_libdir}/kde3/kstyle_highcontrast_config.so
%attr(755,root,root) %{_libdir}/kde3/kstyle_plastik_config.so
%attr(755,root,root) %{_libdir}/kde3/ktexteditor_docwordcompletion.so
%attr(755,root,root) %{_libdir}/kde3/ktexteditor_insertfile.so
%attr(755,root,root) %{_libdir}/kde3/ktexteditor_isearch.so
%attr(755,root,root) %{_libdir}/kde3/ktexteditor_kdatatool.so
%attr(755,root,root) %{_libdir}/kde3/libkatepart.so
%attr(755,root,root) %{_libdir}/kde3/libkcertpart.so
%attr(755,root,root) %{_libdir}/kde3/libkdeprint_management_module.so
%attr(755,root,root) %{_libdir}/kde3/libkhtmlpart.so
%attr(755,root,root) %{_libdir}/kde3/libkmultipart.so
%attr(755,root,root) %{_libdir}/kde3/libshellscript.so
%attr(755,root,root) %{_libdir}/kde3/wmfthumbnail.so
%attr(755,root,root) %{_libdir}/libDCOP.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libDCOP.so.4
%attr(755,root,root) %{_libdir}/libkabc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkabc.so.1
%attr(755,root,root) %{_libdir}/libkabc_dir.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkabc_dir.so.1
%attr(755,root,root) %{_libdir}/libkabc_file.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkabc_file.so.1
%attr(755,root,root) %{_libdir}/libkabc_ldapkio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkabc_ldapkio.so.1
%attr(755,root,root) %{_libdir}/libkatepartinterfaces.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkatepartinterfaces.so.0
%attr(755,root,root) %{_libdir}/libkdecore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdecore.so.4
%attr(755,root,root) %{_libdir}/libkdefakes.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdefakes.so.4
%attr(755,root,root) %{_libdir}/libkdefx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdefx.so.4
%attr(755,root,root) %{_libdir}/libkdeinit_cupsdconf.so
%attr(755,root,root) %{_libdir}/libkdeinit_dcopserver.so
%attr(755,root,root) %{_libdir}/libkdeinit_kaddprinterwizard.so
%attr(755,root,root) %{_libdir}/libkdeinit_kbuildsycoca.so
%attr(755,root,root) %{_libdir}/libkdeinit_kcmshell.so
%attr(755,root,root) %{_libdir}/libkdeinit_kconf_update.so
%attr(755,root,root) %{_libdir}/libkdeinit_kcookiejar.so
%attr(755,root,root) %{_libdir}/libkdeinit_kded.so
%attr(755,root,root) %{_libdir}/libkdeinit_kio_http_cache_cleaner.so
%attr(755,root,root) %{_libdir}/libkdeinit_kio_uiserver.so
%attr(755,root,root) %{_libdir}/libkdeinit_klauncher.so
%attr(755,root,root) %{_libdir}/libkdeprint.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdeprint.so.4
%attr(755,root,root) %{_libdir}/libkdeprint_management.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdeprint_management.so.4
%attr(755,root,root) %{_libdir}/libkdesasl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdesasl.so.1
%attr(755,root,root) %{_libdir}/libkdesu.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdesu.so.4
%attr(755,root,root) %{_libdir}/libkdeui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdeui.so.4
%attr(755,root,root) %{_libdir}/libkdnssd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdnssd.so.1
%attr(755,root,root) %{_libdir}/libkhtml.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkhtml.so.4
%attr(755,root,root) %{_libdir}/libkimproxy.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkimproxy.so.0
%attr(755,root,root) %{_libdir}/libkio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkio.so.4
%attr(755,root,root) %{_libdir}/libkjava.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkjava.so.1
%attr(755,root,root) %{_libdir}/libkjs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkjs.so.1
%attr(755,root,root) %{_libdir}/libkmdi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmdi.so.1
%attr(755,root,root) %{_libdir}/libkmdi2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmdi2.so.1
%attr(755,root,root) %{_libdir}/libkmediaplayer.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmediaplayer.so.0
%attr(755,root,root) %{_libdir}/libkmid.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmid.so.0
%attr(755,root,root) %{_libdir}/libknewstuff.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libknewstuff.so.1
%attr(755,root,root) %{_libdir}/libkntlm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkntlm.so.0
%attr(755,root,root) %{_libdir}/libkparts.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkparts.so.2
%attr(755,root,root) %{_libdir}/libkresources.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkresources.so.1
%attr(755,root,root) %{_libdir}/libkscreensaver.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkscreensaver.so.4
%attr(755,root,root) %{_libdir}/libkscript.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkscript.so.0
%attr(755,root,root) %{_libdir}/libkspell.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkspell.so.4
%attr(755,root,root) %{_libdir}/libkspell2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkspell2.so.1
%attr(755,root,root) %{_libdir}/libktexteditor.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libktexteditor.so.0
%attr(755,root,root) %{_libdir}/libkunittest.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkunittest.so.1
%attr(755,root,root) %{_libdir}/libkutils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkutils.so.1
%attr(755,root,root) %{_libdir}/libkwalletbackend.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkwalletbackend.so.1
%attr(755,root,root) %{_libdir}/libkwalletclient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkwalletclient.so.1
%attr(755,root,root) %{_libdir}/libvcard.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvcard.so.0

# 3rdparty directories
%dir %{_libdir}/kconf_update_bin

# merged kabc files
%attr(755,root,root) %{_libdir}/kde3/kabc_dir.so
%attr(755,root,root) %{_libdir}/kde3/kabc_file.so
%attr(755,root,root) %{_libdir}/kde3/kabc_ldapkio.so
%attr(755,root,root) %{_libdir}/kde3/kabcformat_binary.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kresources.so

%if %{with arts}
%attr(755,root,root) %{_libdir}/libartskde.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libartskde.so.1
%attr(755,root,root) %{_libdir}/kde3/kfileaudiopreview.so
# http://blog.flameeyes.eu/2009/01/02/bundling-libraries-for-despair-and-insecurity
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dcopidl
%attr(755,root,root) %{_bindir}/dcopidl2cpp
%attr(755,root,root) %{_bindir}/kconfig_compiler
%{_includedir}/[!a]*
%{_libdir}/kde3/plugins/designer/kdewidgets.la
%{_libdir}/libDCOP.la
%attr(755,root,root) %{_libdir}/libDCOP.so
%{_libdir}/libkabc.la
%attr(755,root,root) %{_libdir}/libkabc.so
%{_libdir}/libkabc_dir.la
%attr(755,root,root) %{_libdir}/libkabc_dir.so
%{_libdir}/libkabc_file.la
%attr(755,root,root) %{_libdir}/libkabc_file.so
%{_libdir}/libkabc_ldapkio.la
%attr(755,root,root) %{_libdir}/libkabc_ldapkio.so
%{_libdir}/libkatepartinterfaces.la
%attr(755,root,root) %{_libdir}/libkatepartinterfaces.so
%{_libdir}/libkdecore.la
%attr(755,root,root) %{_libdir}/libkdecore.so
%{_libdir}/libkdefakes.la
%attr(755,root,root) %{_libdir}/libkdefakes.so
%{_libdir}/libkdefakes_nonpic.a
%{_libdir}/libkdefx.la
%attr(755,root,root) %{_libdir}/libkdefx.so
%{_libdir}/libkdeprint.la
%attr(755,root,root) %{_libdir}/libkdeprint.so
%{_libdir}/libkdeprint_management.la
%attr(755,root,root) %{_libdir}/libkdeprint_management.so
%{_libdir}/libkdesasl.la
%attr(755,root,root) %{_libdir}/libkdesasl.so
%{_libdir}/libkdesu.la
%attr(755,root,root) %{_libdir}/libkdesu.so
%{_libdir}/libkdeui.la
%attr(755,root,root) %{_libdir}/libkdeui.so
%{_libdir}/libkdnssd.la
%attr(755,root,root) %{_libdir}/libkdnssd.so
%{_libdir}/libkhtml.la
%attr(755,root,root) %{_libdir}/libkhtml.so
%{_libdir}/libkimproxy.la
%attr(755,root,root) %{_libdir}/libkimproxy.so
%{_libdir}/libkio.la
%attr(755,root,root) %{_libdir}/libkio.so
%{_libdir}/libkjava.la
%attr(755,root,root) %{_libdir}/libkjava.so
%{_libdir}/libkjs.la
%attr(755,root,root) %{_libdir}/libkjs.so
%{_libdir}/libkmdi.la
%attr(755,root,root) %{_libdir}/libkmdi.so
%{_libdir}/libkmdi2.la
%attr(755,root,root) %{_libdir}/libkmdi2.so
%{_libdir}/libkmediaplayer.la
%attr(755,root,root) %{_libdir}/libkmediaplayer.so
%{_libdir}/libkmid.la
%attr(755,root,root) %{_libdir}/libkmid.so
%{_libdir}/libknewstuff.la
%attr(755,root,root) %{_libdir}/libknewstuff.so
%{_libdir}/libkntlm.la
%attr(755,root,root) %{_libdir}/libkntlm.so
%{_libdir}/libkparts.la
%attr(755,root,root) %{_libdir}/libkparts.so
%{_libdir}/libkresources.la
%attr(755,root,root) %{_libdir}/libkresources.so
%{_libdir}/libkscreensaver.la
%attr(755,root,root) %{_libdir}/libkscreensaver.so
%{_libdir}/libkscript.la
%attr(755,root,root) %{_libdir}/libkscript.so
%{_libdir}/libkspell.la
%attr(755,root,root) %{_libdir}/libkspell.so
%{_libdir}/libkspell2.la
%attr(755,root,root) %{_libdir}/libkspell2.so
%{_libdir}/libktexteditor.la
%attr(755,root,root) %{_libdir}/libktexteditor.so
%{_libdir}/libkunittest.la
%attr(755,root,root) %{_libdir}/libkunittest.so
%{_libdir}/libkutils.la
%attr(755,root,root) %{_libdir}/libkutils.so
%{_libdir}/libkwalletbackend.la
%attr(755,root,root) %{_libdir}/libkwalletbackend.so
%{_libdir}/libkwalletclient.la
%attr(755,root,root) %{_libdir}/libkwalletclient.so
%{_libdir}/libvcard.la
%attr(755,root,root) %{_libdir}/libvcard.so

%if %{with arts}
%{_libdir}/libartskde.la
%attr(755,root,root) %{_libdir}/libartskde.so
%{_includedir}/arts/*
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_kdedocdir}/en/%{name}*-apidocs
%endif

%if %{with arts}
%files artsmessage
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artsmessage
%endif

%files kgrantpty
%defattr(644,root,root,755)
%attr(4755,root,root) %{_bindir}/kgrantpty
