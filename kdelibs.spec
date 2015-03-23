#
# Conditional build:
%bcond_without	alsa			# ALSA support
%bcond_with	arts			# Build with aRts
%bcond_with	apidocs			# don't prepare API documentation
%bcond_without	kerberos5		# disable kerberos
%bcond_without	openexr			# Enable OpenEXR support
%bcond_without	jasper		# Enable jasper (jpeg2k) support
%bcond_without	avahi		# Enable AVAHI support
%bcond_without	pcre		# Enable pcre regex support for kjs
%bcond_without	inotify		# Enable inotify support for kio
%bcond_without	gamin		# Enable FAM/GAMIN support
%bcond_without	lzma		# Enable support for LZMA/XZ
%bcond_without	aspell		# Enable aspell support
%bcond_without	hspell		# Enable hspell support
%bcond_without	utempter	# Use utempter for utmp management
%bcond_without	libart		# Enable libart support (for SVG icons)
%bcond_without	libidn		# Enable support for libidn
%bcond_without	ssl		# Enable support for SSL
%bcond_without	cups		# Enable CUPS support
%bcond_without	lua		# Enable LUA support
%bcond_without	tiff		# Enable tiff support
%bcond_without	sudo		# Use sudo as backend for kdesu (default is su)
%bcond_without	elficon		# with ELF Icon support
%bcond_with	wmf		# with wmfplugin (needs porting to CMake)
%bcond_without	lib_loader		# use lib_loader patch

%define		artsver		13:1.5.10
Summary:	K Desktop Environment 3 libraries
Summary(es.UTF-8):	K Desktop Environment 3 - bibliotecas
Summary(ko.UTF-8):	KDE 3 - 라이브러리
Summary(pl.UTF-8):	Biblioteki K Desktop Environment 3
Summary(pt_BR.UTF-8):	Bibliotecas de fundação do KDE 3
Summary(ru.UTF-8):	K Desktop Environment 3 - Библиотеки
Summary(uk.UTF-8):	K Desktop Environment 3 - Бібліотеки
Name:		kdelibs
Version:	R14.0.0
Release:	0.23
Epoch:		9
License:	LGPL v2
Group:		X11/Libraries
Source0:	http://tde-mirror.yosemite.net/trinity/releases/%{version}/tdelibs-%{version}.tar.bz2
# Source0-md5:	64b4550fb22ba700f38027379eab246e
Source1:	%{name}-wmfplugin.tar.bz2
# Source1-md5:	df0d7c2a13bb68fe25e1d6c009df5b8d
Source2:	pnm.protocol
Source3:	x-icq.mimelnk
Source4:	x-mplayer2.desktop
Patch0:		kde-common-PLD.patch
Patch1:		%{name}-kstandarddirs.patch
Patch3:		%{name}-use_system_sgml.patch
Patch4:		%{name}-fileshareset.patch
Patch5:		%{name}-appicon_themable.patch
Patch7:		%{name}-xgl.patch
Patch9:		%{name}-lib_loader.patch
# http://kate-editor.org/downloads/syntax_highlighting?kateversion=2.5
Patch10:	%{name}-kate-syntax.patch
Patch12:	%{name}-konqueror-agent.patch
Patch15:	dcopobject-destruct-crash.patch
Patch17:	%{name}-3.5.10-LDFLAG_fix-1.patch
Patch19:	%{name}-gcc4.patch
Patch20:	xdg-menu-prefix.patch
URL:		https://www.trinitydesktop.org/
%{?with_openexr:BuildRequires:	OpenEXR-devel >= 1.4.0.a}
BuildRequires:	acl-devel
BuildRequires:	alsa-lib-devel
%{?with_alsa:BuildRequires:	alsa-lib-devel}
%{?with_arts:BuildRequires:	arts-qt-devel >= %{artsver}}
%{?with_arts:BuildRequires:	artsc-devel >= %{artsver}}
%{?with_aspell:BuildRequires:	aspell-devel}
%{?with_aspell:BuildRequires:	aspell}
%{?with_avahi:BuildRequires:	avahi-devel}
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.8
%{?with_cups:BuildRequires:	cups-devel >= 1:1.3.0}
BuildRequires:	dbus-1-tqt-devel >= 0.9
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	fam-devel
BuildRequires:	gamin-devel
BuildRequires:	glib2-devel
BuildRequires:	glibc-devel >= 6:2.4
%{?with_kerberos5:BuildRequires:	heimdal-devel}
BuildRequires:	hspell-devel
BuildRequires:	jasper-devel >= 1.600
%{?with_jasper:BuildRequires:	jasper-devel}
BuildRequires:	libart_lgpl-devel
BuildRequires:	libidn-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel
BuildRequires:	libpng-devel
%{?with_elficon:BuildRequires:	libr-devel >= 0.6.0}
BuildRequires:	libstdc++-devel >= 5:4.1.0-0.20051206r108118.1
BuildRequires:	libtiff-devel
BuildRequires:	libtqt3-mt-devel >= 3.5.0
BuildRequires:	libtqtinterface-devel >= 4.2.0
%{?with_utempter:BuildRequires:	libutempter-devel}
%{?with_wmf:BuildRequires:	libwmf-devel >= 2:0.2.0}
BuildRequires:	libxml2-devel >= 2.4.9
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel >= 1.0.7
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pcre-devel >= 3.5
BuildRequires:	pkgconfig
#BuildRequires:	qt-devel >= 6:3.3.5.051113-1
%{?with_apidocs:BuildRequires:	qt-doc}
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	tar >= 1:1.22
BuildRequires:	tqt3-dev-tools >= 3.5.0
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-proto-compositeproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
%{?with_arts:Requires:	arts >= %{artsver}}
Requires:	ca-certificates
%{?with_cups:Requires:	cups-lib >= 1:1.3.0}
Requires:	docbook-dtd412-xml
Requires:	docbook-dtd42-xml
Requires:	docbook-style-xsl
Requires:	hicolor-icon-theme
Requires:	libxml2-progs
#Requires:	qt >= 6:3.3.3-4
Requires:	setup >= 2.4.6-7
Requires:	xorg-app-iceauth
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/trinity
%define		_applnkdir	%{_datadir}/applnk

# avoid java dependency
# TODO: split to kjava subpackage
%define		_noautoreqfiles %{_datadir}/apps/kjava/kjava.jar

# unresolved kss_* symbols in libtdescreensaver.so.X (by design)
%define		skip_post_check_so libtdescreensaver.so.14.0.0

# ssp flags, fix this later
%undefine	_ssp_cflags

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
#Requires:	qt-devel >= 6:3.3.3-4
Requires:	xorg-lib-libXmu-devel
Requires:	xorg-lib-libXt-devel

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

%prep
%setup -q -c %{?with_wmf:-a1}
mv tdelibs/* .
%patch0 -p1
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1
%{?with_lib_loader:%patch9 -p1}
#%patch10 -p1 does not apply, drop
%patch12 -p1
%patch15 -p1
%patch17 -p1
%patch19 -p1
%patch20 -p1

%build
install -d build
cd build

%cmake \
	-Wno-dev \
	-DPLUGIN_INSTALL_DIR=%{_libexecdir} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DAPPS_INSTALL_DIR=%{_applnkdir} \
	-DWITH_ALL_OPTIONS=ON \
	-DWITH_ARTS=O%{!?with_arts:FF}%{?with_arts:N} \
	%{?with_alsa:-DWITH_ALSA=ON} \
	-DWITH_LIBART=ON \
	-DWITH_LIBIDN=ON \
	-DWITH_SSL=ON \
	-DWITH_CUPS=O%{!?with_cups:FF}%{?with_cups:N} \
	-DWITH_LUA=OFF \
	-DWITH_TIFF=ON \
	-DWITH_GCC_VISIBILITY=ON \
	-DWITH_SUDO_KDESU_BACKEND=%{!?with_sudo:OFF}%{?with_sudo:ON} \
	%{?with_jasper:-DWITH_JASPER=ON} \
	%{?with_openexr:-DWITH_OPENEXR=ON} \
	-DWITH_UTEMPTER=O%{!?with_utempter:FF}%{?with_utempter:N} \
	%{?with_avahi:-DWITH_AVAHI=ON} \
	%{!?with_pcre:-DWITH_PCRE=OFF} \
	%{!?with_inotify:-DWITH_INOTIFY=OFF} \
	%{!?with_gamin:-DWITH_GAMIN=OFF} \
	%{!?with_lzma:-DWITH_LZMA=OFF} \
	-DWITH_ASPELL=O%{!?with_aspell:FF}%{?with_aspell:N} \
	-DWITH_ELFICON=O%{!?with_elficon:FF}%{?with_elficon:N} \
	%{!?with_hspell:-DWITH_HSPELL=OFF} \
	..

%{__make}
rm -f makeinstall.stamp

%install
test -f makeinstall.stamp -a %{_specdir}/%{name}.spec -nt makeinstall.stamp && rm -f makeinstall.stamp

if [ ! -f makeinstall.stamp -o ! -d $RPM_BUILD_ROOT ]; then
	rm -rf makeinstall.stamp installed.stamp $RPM_BUILD_ROOT

	%{__make} install -C build \
		DESTDIR=$RPM_BUILD_ROOT \
		kde_htmldir=%{_kdedocdir}
		kde_libs_htmldir=%{_kdedocdir}

	touch makeinstall.stamp
fi

if [ ! -f installed.stamp ]; then
	cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/services
	cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/mimelnk/application/x-icq.desktop
	cp -p %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/mimelnk/application

	install -d \
		$RPM_BUILD_ROOT/etc/security \
		$RPM_BUILD_ROOT%{_libdir}/kconf_update_bin \
		$RPM_BUILD_ROOT%{_applnkdir}/.hidden \
		$RPM_BUILD_ROOT%{_datadir}/services/.hidden \
		$RPM_BUILD_ROOT%{_datadir}/apps/khtml/kpartplugins \
		$RPM_BUILD_ROOT%{_datadir}/apps/profiles \
		$RPM_BUILD_ROOT%{_datadir}/apps/remotes \
		$RPM_BUILD_ROOT%{_datadir}/config/magic \
		$RPM_BUILD_ROOT%{_datadir}/services/tdeconfiguredialog \
		$RPM_BUILD_ROOT%{_iconsdir}/crystalsvg/{16x16,22x22,32x32,48x48,64x64,128x128}/apps

	install -d $RPM_BUILD_ROOT%{_kdedocdir}/{ca,cs,da,de,en,en_GB,es,et,fi,fr,hu,it,ja,nb,nl,pl,pt,pt_BR,ro,ru,sk,sl,sv,tr,uk,zh_TW}/common

	# should be hardlinked, not copied
	ln -nf $RPM_BUILD_ROOT%{_bindir}/{tdeinit_wrapper,tdeinit_shutdown}
	ln -nf $RPM_BUILD_ROOT%{_bindir}/{tdetelnetservice,filesharelist}

	# use ca-certificates' ca-bundle.crt, symlink as what most other
	# distros do these days (http://bugzilla.redhat.com/521902)
	ln -sf /etc/certs/ca-certificates.crt $RPM_BUILD_ROOT%{_datadir}/apps/kssl/ca-bundle.crt
	%{__rm} $RPM_BUILD_ROOT%{_datadir}/config/ksslcalist

	# For fileshare
	touch $RPM_BUILD_ROOT/etc/security/fileshare.conf
	%{__sed} -i -e 's|/etc/init.d|/etc/rc.d/init.d|g' $RPM_BUILD_ROOT%{_bindir}/fileshare*

	if [ -d $RPM_BUILD_ROOT%{_kdedocdir}/en/%{name}-%{version}-apidocs ] ; then
		mv -f $RPM_BUILD_ROOT%{_kdedocdir}/en/%{name}-{%{version}-,}apidocs
	fi

	# packaged by hicolor-icon-theme
	%{__rm} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/index.theme

	# remove *.la for dynamic plugins. kde lib loader handles .so now.
%if %{with lib_loader}
	%{__rm} $RPM_BUILD_ROOT%{_libexecdir}/*.la
	# keep $RPM_BUILD_ROOT%{_libexecdir}/plugins/designer/kdewidget.la for kdebase and others.
	%{__rm} $RPM_BUILD_ROOT%{_libexecdir}/plugins/styles/*.la
	%{__rm} $RPM_BUILD_ROOT%{_libdir}/libtdeinit_*.la

	# remove unwanted boost deps from .la
	sed -i 's:-lboost_filesystem -lboost_regex::' $RPM_BUILD_ROOT%{_libexecdir}/plugins/designer/kdewidgets.la
	sed -i 's:-lboost_filesystem -lboost_regex::' $RPM_BUILD_ROOT%{_libdir}/*.la
%endif

	touch installed.stamp
fi

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%ghost /etc/security/fileshare.conf
/etc/dbus-1/system.d/org.trinitydesktop.hardwarecontrol.conf
%{_datadir}/dbus-1/system-services/org.trinitydesktop.hardwarecontrol.service
%attr(2755,root,fileshare) %{_bindir}/filesharelist
%attr(2755,root,fileshare) %{_bindir}/fileshareset
%attr(4755,root,root) %{_bindir}/start_tdeinit
%attr(755,root,root) %{_bindir}/checkXML
%{?with_cups:%attr(755,root,root) %{_bindir}/cupsdconf}
%{?with_cups:%attr(755,root,root) %{_bindir}/cupsdoprint}
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
%attr(755,root,root) %{_bindir}/imagetops
%attr(755,root,root) %{_bindir}/tdeab2tdeabc
%attr(755,root,root) %{_bindir}/kaddprinterwizard
%attr(755,root,root) %{_bindir}/tdebuildsycoca
%attr(755,root,root) %{_bindir}/tdecmshell
%attr(755,root,root) %{_bindir}/tdeconf_update
%attr(755,root,root) %{_bindir}/kcookiejar
%attr(755,root,root) %{_bindir}/tde-config
%attr(755,root,root) %{_bindir}/tde-menu
%attr(755,root,root) %{_bindir}/kded
%attr(755,root,root) %{_bindir}/tdeinit
%attr(755,root,root) %{_bindir}/tdeinit_shutdown
%attr(755,root,root) %{_bindir}/tdeinit_wrapper
%attr(755,root,root) %{_bindir}/tdesu_stub
%attr(755,root,root) %{_bindir}/kdetcompmgr
%attr(755,root,root) %{_bindir}/kdontchangethehostname
%attr(755,root,root) %{_bindir}/tdedostartupconfig
%attr(755,root,root) %{_bindir}/tdefile
%attr(755,root,root) %{_bindir}/kfmexec
%attr(755,root,root) %{_bindir}/tdehotnewstuff
%attr(755,root,root) %{_bindir}/kinstalltheme
%attr(755,root,root) %{_bindir}/tdeio_http_cache_cleaner
%attr(755,root,root) %{_bindir}/tdeio_uiserver
%attr(755,root,root) %{_bindir}/tdeioexec
%attr(755,root,root) %{_bindir}/tdeioslave
%attr(755,root,root) %{_bindir}/tdelauncher
%attr(755,root,root) %{_bindir}/tdemailservice
%attr(755,root,root) %{_bindir}/tdemimelist
%attr(755,root,root) %{_bindir}/kpac_dhcp_helper
%attr(755,root,root) %{_bindir}/tdesendbugmail
%attr(755,root,root) %{_bindir}/kshell
%attr(755,root,root) %{_bindir}/tdestartupconfig
%attr(755,root,root) %{_bindir}/ksvgtopng
%attr(755,root,root) %{_bindir}/tdetelnetservice
%attr(755,root,root) %{_bindir}/tdetradertest
%attr(755,root,root) %{_bindir}/tdeunittestmodrunner
%attr(755,root,root) %{_bindir}/kwrapper
%attr(755,root,root) %{_bindir}/lnusertemp
%{?with_cups:%attr(755,root,root) %{_bindir}/make_driver_db_cups}
%attr(755,root,root) %{_bindir}/make_driver_db_lpr
%attr(755,root,root) %{_bindir}/maketdewidgets
%attr(755,root,root) %{_bindir}/meinproc
%attr(755,root,root) %{_bindir}/networkstatustestservice
%attr(755,root,root) %{_bindir}/preparetips
%attr(755,root,root) %{_bindir}/start_tdeinit_wrapper
%attr(755,root,root) %{_bindir}/tde_dbus_hardwarecontrol
%attr(755,root,root) %{_bindir}/tdeiso_info
%attr(755,root,root) %{_bindir}/tdelfeditor

%dir %{_datadir}/apps
%{_datadir}/apps/LICENSES
%attr(755,root,root) %{_datadir}/apps/dcopidlng/kalyptus
%dir %{_datadir}/apps/tdeconf_update
%attr(755,root,root) %{_datadir}/apps/tdeconf_update/*.pl
%attr(755,root,root) %{_datadir}/apps/tdeconf_update/*.sh
%dir %{_datadir}/apps/dcopidlng
%dir %{_datadir}/emoticons
%dir %{_datadir}/autostart
%{_datadir}/apps/dcopidlng/*.pm
%{_datadir}/apps/tdeabc
%{_datadir}/apps/katepart
%{_datadir}/apps/tdecertpart
%{_datadir}/apps/kcm_componentchooser
%{_datadir}/apps/tdeconf_update/*.upd
%{_datadir}/apps/tdeprint
%{_datadir}/apps/tdeui
%{_datadir}/apps/tdewidgets
%{_datadir}/apps/tdehtml
%{_datadir}/apps/tdeio_uiserver
%{_datadir}/apps/kjava
%{_datadir}/apps/tdenewstuff
%{_datadir}/apps/knotify
%{_datadir}/apps/ksgmltools2
%{_datadir}/apps/kssl
%{_datadir}/apps/tdestyle
%{_datadir}/apps/tdetexteditor_docwordcompletion
%{_datadir}/apps/tdetexteditor_insertfile
%{_datadir}/apps/tdetexteditor_isearch
%{_datadir}/apps/tdetexteditor_kdatatool
%{_datadir}/apps/proxyscout
%{_datadir}/apps/tdehwlib

%dir %{_datadir}/apps/konqueror
%dir %{_datadir}/apps/konqueror/servicemenus
%{_datadir}/apps/konqueror/servicemenus/isoservice.desktop

%{_datadir}/autostart/tdeab2tdeabc.desktop

%{_datadir}/config
%{_datadir}/emoticons/Default
%{_datadir}/mimelnk

%dir %{_datadir}/services
%dir %{_datadir}/services/.hidden
#%dir %{_datadir}/services/tdeconfiguredialog
%dir %{_datadir}/services/tderesources
%{_datadir}/services/tderesources/tdeabc
%{_datadir}/services/bmp.kimgio
%{_datadir}/services/data.protocol
%{_datadir}/services/dds.kimgio
%{_datadir}/services/eps.kimgio
%{?with_openexr:%{_datadir}/services/exr.kimgio}
%{_datadir}/services/file.protocol
%{_datadir}/services/ftp.protocol
%{_datadir}/services/ghelp.protocol
%{_datadir}/services/gif.kimgio
%{_datadir}/services/hdr.kimgio
%{_datadir}/services/help.protocol
%{_datadir}/services/http.protocol
%{_datadir}/services/http_cache_cleaner.desktop
%{_datadir}/services/https.protocol
%{_datadir}/services/ico.kimgio
%{_datadir}/services/jp2.kimgio
%{_datadir}/services/jpeg.kimgio
%{_datadir}/services/katepart.desktop
%{_datadir}/services/kbzip2filter.desktop
%{_datadir}/services/tdecertpart.desktop
%{_datadir}/services/kded
%{_datadir}/services/kgzipfilter.desktop
%{_datadir}/services/tdehtml.desktop
%{_datadir}/services/tdehtmlimage.desktop
%{_datadir}/services/tdeio_uiserver.desktop
%{_datadir}/services/kjavaappletviewer.desktop
%{_datadir}/services/tdemailservice.protocol
%{_datadir}/services/tdemultipart.desktop
%{_datadir}/services/knotify.desktop
%{_datadir}/services/tderesources/tdeabc_manager.desktop
%{?with_aspell:%{_datadir}/services/tdespell_aspell.desktop}
%{_datadir}/services/tdespell_hspell.desktop
%{_datadir}/services/tdespell_ispell.desktop
%{_datadir}/services/tdetexteditor_docwordcompletion.desktop
%{_datadir}/services/tdetexteditor_insertfile.desktop
%{_datadir}/services/tdetexteditor_isearch.desktop
%{_datadir}/services/tdetexteditor_kdatatool.desktop
%{_datadir}/services/kxzfilter.desktop
%{_datadir}/services/metainfo.protocol
%{_datadir}/services/mms.protocol
%{_datadir}/services/mmst.protocol
%{_datadir}/services/mmsu.protocol
%{_datadir}/services/mng.kimgio
%{_datadir}/services/pbm.kimgio
%{_datadir}/services/pcx.kimgio
%{_datadir}/services/pgm.kimgio
%{_datadir}/services/png.kimgio
%{_datadir}/services/pnm.protocol
%{_datadir}/services/ppm.kimgio
%{_datadir}/services/psd.kimgio
%{_datadir}/services/rgb.kimgio
%{_datadir}/services/rlogin.protocol
%{_datadir}/services/rtsp.protocol
%{_datadir}/services/rtspt.protocol
%{_datadir}/services/rtspu.protocol
%{_datadir}/services/shellscript.desktop
%{_datadir}/services/ssh.protocol
%{_datadir}/services/telnet.protocol
%{_datadir}/services/tga.kimgio
%{_datadir}/services/tiff.kimgio
%{_datadir}/services/webdav.protocol
%{_datadir}/services/webdavs.protocol
#%{?with_wmf:%{_datadir}/services/wmfthumbnail.desktop}
%{_datadir}/services/xbm.kimgio
%{_datadir}/services/xcf.kimgio
%{_datadir}/services/xpm.kimgio
%{_datadir}/services/xv.kimgio
%{_datadir}/services/iso.protocol
%{_datadir}/services/tdefile_elf.desktop
%{_datadir}/servicetypes
%{_iconsdir}/crystalsvg
%{_iconsdir}/default.tde
%{_localedir}/all_languages

%dir %{_desktopdir}/tde
%{_desktopdir}/tde/tderesources.desktop
%dir %{_applnkdir}
%dir %{_applnkdir}/.hidden
%{_applnkdir}/tdeio_iso.desktop
/etc/xdg/menus/tde-applications.menu

%{?with_cups:%attr(755,root,root) %{_libdir}/libtdeinit_cupsdconf.so}
%attr(755,root,root) %{_libdir}/libtdeinit_dcopserver.so
%attr(755,root,root) %{_libdir}/libtdeinit_kaddprinterwizard.so
%attr(755,root,root) %{_libdir}/libtdeinit_tdebuildsycoca.so
%attr(755,root,root) %{_libdir}/libtdeinit_tdecmshell.so
%attr(755,root,root) %{_libdir}/libtdeinit_tdeconf_update.so
%attr(755,root,root) %{_libdir}/libtdeinit_kcookiejar.so
%attr(755,root,root) %{_libdir}/libtdeinit_kded.so
%attr(755,root,root) %{_libdir}/libtdeinit_tdeio_http_cache_cleaner.so
%attr(755,root,root) %{_libdir}/libtdeinit_tdeio_uiserver.so
%attr(755,root,root) %{_libdir}/libtdeinit_tdelauncher.so

%attr(755,root,root) %{_libdir}/libDCOP.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libDCOP.so.14
%attr(755,root,root) %{_libdir}/libconnectionmanager.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libconnectionmanager.so.0
%attr(755,root,root) %{_libdir}/libtdeabc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdeabc.so.1
%attr(755,root,root) %{_libdir}/libtdeabc_dir.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdeabc_dir.so.1
%attr(755,root,root) %{_libdir}/libtdeabc_file.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdeabc_file.so.1
%attr(755,root,root) %{_libdir}/libtdeabc_ldaptdeio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdeabc_ldaptdeio.so.1
%attr(755,root,root) %{_libdir}/libtdeabc_net.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdeabc_net.so.1
%attr(755,root,root) %{_libdir}/libkatepartinterfaces.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkatepartinterfaces.so.0
%attr(755,root,root) %{_libdir}/libtdecore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdecore.so.14
%attr(755,root,root) %{_libdir}/libtdefakes.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdefakes.so.14
%attr(755,root,root) %{_libdir}/libtdefx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdefx.so.14
%attr(755,root,root) %{_libdir}/libtdeprint.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdeprint.so.14
%attr(755,root,root) %{_libdir}/libtdeprint_management.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdeprint_management.so.14
%attr(755,root,root) %{_libdir}/libtdesasl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdesasl.so.1
%attr(755,root,root) %{_libdir}/libtdesu.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdesu.so.14
%attr(755,root,root) %{_libdir}/libtdeui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdeui.so.14
%attr(755,root,root) %{_libdir}/libtdednssd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdednssd.so.1
%attr(755,root,root) %{_libdir}/libkglib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkglib.so.0
%attr(755,root,root) %{_libdir}/libtdehtml.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdehtml.so.14
%attr(755,root,root) %{_libdir}/libtdeimproxy.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdeimproxy.so.0
%attr(755,root,root) %{_libdir}/libtdeio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdeio.so.14
%attr(755,root,root) %{_libdir}/libkjava.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkjava.so.1
%attr(755,root,root) %{_libdir}/libkjs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkjs.so.1
%attr(755,root,root) %{_libdir}/libtdemdi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdemdi.so.1
%attr(755,root,root) %{_libdir}/libtdemdi2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdemdi2.so.1
%attr(755,root,root) %{_libdir}/libtdemediaplayer.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdemediaplayer.so.0
%attr(755,root,root) %{_libdir}/libtdemid.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdemid.so.0
%attr(755,root,root) %{_libdir}/libtdenewstuff.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdenewstuff.so.1
%attr(755,root,root) %{_libdir}/libtdentlm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdentlm.so.0
%attr(755,root,root) %{_libdir}/libtdeparts.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdeparts.so.2
%attr(755,root,root) %{_libdir}/libtderandr.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtderandr.so.0
%attr(755,root,root) %{_libdir}/libtderesources.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtderesources.so.1
%attr(755,root,root) %{_libdir}/libtdersync.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdersync.so.0
%attr(755,root,root) %{_libdir}/libtdescreensaver.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdescreensaver.so.14
%attr(755,root,root) %{_libdir}/libtdescript.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdescript.so.0
%attr(755,root,root) %{_libdir}/libtdespell.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdespell.so.14
%attr(755,root,root) %{_libdir}/libtdespell2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdespell2.so.1
%attr(755,root,root) %{_libdir}/libtdetexteditor.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdetexteditor.so.0
%attr(755,root,root) %{_libdir}/libtdeunittest.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdeunittest.so.1
%attr(755,root,root) %{_libdir}/libtdeutils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdeutils.so.1
%attr(755,root,root) %{_libdir}/libtdewalletbackend.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdewalletbackend.so.1
%attr(755,root,root) %{_libdir}/libtdewalletclient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdewalletclient.so.1
%attr(755,root,root) %{_libdir}/libnetworkstatus.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnetworkstatus.so.0
%attr(755,root,root) %{_libdir}/libvcard.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvcard.so.0

%if %{with arts}
%attr(755,root,root) %{_libdir}/libartskde.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libartskde.so.1
%attr(755,root,root) %{_libexecdir}/kfileaudiopreview.so
%endif

%if %{without lib_loader}
%{?with_cups:%{_libdir}/libtdeinit_cupsdconf.la}
%{_libdir}/libtdeinit_dcopserver.la
%{_libdir}/libtdeinit_kaddprinterwizard.la
%{_libdir}/libtdeinit_tdebuildsycoca.la
%{_libdir}/libtdeinit_tdecmshell.la
%{_libdir}/libtdeinit_tdeconf_update.la
%{_libdir}/libtdeinit_kcookiejar.la
%{_libdir}/libtdeinit_kded.la
%{_libdir}/libtdeinit_tdeio_http_cache_cleaner.la
%{_libdir}/libtdeinit_tdeio_uiserver.la
%{_libdir}/libtdeinit_tdelauncher.la
%{?with_cups:%{_libexecdir}/cupsdconf.la}
%{_libexecdir}/dcopserver.la
%{_libexecdir}/tdeabc_dir.la
%{_libexecdir}/tdeabc_file.la
%{_libexecdir}/tdeabc_ldaptdeio.la
%{_libexecdir}/tdeabc_net.la
%{_libexecdir}/tdeabcformat_binary.la
%{_libexecdir}/kaddprinterwizard.la
%{_libexecdir}/tdebuildsycoca.la
%{_libexecdir}/kbzip2filter.la
%{_libexecdir}/kcm_tderesources.la
%{_libexecdir}/tdecmshell.la
%{_libexecdir}/tdeconf_update.la
%{_libexecdir}/kcookiejar.la
%{_libexecdir}/kded.la
%{_libexecdir}/kded_kcookiejar.la
%{_libexecdir}/kded_tdeprintd.la
%{_libexecdir}/kded_kdetrayproxy.la
%{_libexecdir}/kded_kpasswdserver.la
%{_libexecdir}/kded_kssld.la
%{_libexecdir}/kded_tdewalletd.la
%{_libexecdir}/kded_networkstatus.la
%{_libexecdir}/kded_proxyscout.la
%{?with_cups:%{_libexecdir}/tdeprint_cups.la}
%{_libexecdir}/tdeprint_ext.la
%{_libexecdir}/tdeprint_lpdunix.la
%{_libexecdir}/tdeprint_lpr.la
%{_libexecdir}/tdeprint_rlpr.la
%{_libexecdir}/tdeprint_tool_escputil.la
%{_libexecdir}/kgzipfilter.la
%{_libexecdir}/tdehtmlimagepart.la
%{_libexecdir}/kimg_dds.la
%{_libexecdir}/kimg_eps.la
%{_libexecdir}/kimg_exr.la
%{_libexecdir}/kimg_hdr.la
%{_libexecdir}/kimg_ico.la
%{_libexecdir}/kimg_jp2.la
%{_libexecdir}/kimg_pcx.la
%{_libexecdir}/kimg_psd.la
%{_libexecdir}/kimg_rgb.la
%{_libexecdir}/kimg_tga.la
%{_libexecdir}/kimg_tiff.la
%{_libexecdir}/kimg_xcf.la
%{_libexecdir}/kimg_xview.la
%{_libexecdir}/tdeio_file.la
%{_libexecdir}/tdeio_ftp.la
%{_libexecdir}/tdeio_ghelp.la
%{_libexecdir}/tdeio_help.la
%{_libexecdir}/tdeio_http.la
%{_libexecdir}/tdeio_http_cache_cleaner.la
%{_libexecdir}/tdeio_iso.la
%{_libexecdir}/tdeio_metainfo.la
%{_libexecdir}/tdeio_uiserver.la
%{_libexecdir}/kjavaappletviewer.la
%{_libexecdir}/tdelauncher.la
%{_libexecdir}/knotify.la
%{_libexecdir}/tdespell_aspell.la
%{_libexecdir}/tdespell_hspell.la
%{_libexecdir}/tdespell_ispell.la
%{_libexecdir}/tdestyle_highcontrast_config.la
%{_libexecdir}/tdestyle_plastik_config.la
%{_libexecdir}/tdetexteditor_docwordcompletion.la
%{_libexecdir}/tdetexteditor_insertfile.la
%{_libexecdir}/tdetexteditor_isearch.la
%{_libexecdir}/tdetexteditor_kdatatool.la
%{_libexecdir}/kxzfilter.la
%{_libexecdir}/libkatepart.la
%{_libexecdir}/libtdecertpart.la
%{_libexecdir}/libtdeprint_management_module.la
%{_libexecdir}/libtdehtmlpart.la
%{_libexecdir}/libtdemultipart.la
%{_libexecdir}/libshellscript.la
%{_libexecdir}/tdefile_elf.la
%{_libexecdir}/plugins/styles/asteroid.la
%{_libexecdir}/plugins/styles/highcolor.la
%{_libexecdir}/plugins/styles/highcontrast.la
%{_libexecdir}/plugins/styles/keramik.la
%{_libexecdir}/plugins/styles/kthemestyle.la
%{_libexecdir}/plugins/styles/light.la
%{_libexecdir}/plugins/styles/plastik.la
%endif

%dir %{_libdir}/kconf_update_bin

%dir %{_libexecdir}
%{?with_cups:%attr(755,root,root) %{_libexecdir}/cupsdconf.so}
%attr(755,root,root) %{_libexecdir}/dcopserver.so
%attr(755,root,root) %{_libexecdir}/tdeabc_dir.so
%attr(755,root,root) %{_libexecdir}/tdeabc_file.so
%attr(755,root,root) %{_libexecdir}/tdeabc_ldaptdeio.so
%attr(755,root,root) %{_libexecdir}/tdeabc_net.so
%attr(755,root,root) %{_libexecdir}/tdeabcformat_binary.so
%attr(755,root,root) %{_libexecdir}/kaddprinterwizard.so
%attr(755,root,root) %{_libexecdir}/tdebuildsycoca.so
%attr(755,root,root) %{_libexecdir}/kbzip2filter.so
%attr(755,root,root) %{_libexecdir}/kcm_tderesources.so
%attr(755,root,root) %{_libexecdir}/tdecmshell.so
%attr(755,root,root) %{_libexecdir}/tdeconf_update.so
%attr(755,root,root) %{_libexecdir}/kcookiejar.so
%attr(755,root,root) %{_libexecdir}/kded.so
%attr(755,root,root) %{_libexecdir}/kded_kcookiejar.so
%attr(755,root,root) %{_libexecdir}/kded_tdeprintd.so
%attr(755,root,root) %{_libexecdir}/kded_kdetrayproxy.so
%attr(755,root,root) %{_libexecdir}/kded_kpasswdserver.so
%attr(755,root,root) %{_libexecdir}/kded_kssld.so
%attr(755,root,root) %{_libexecdir}/kded_tdewalletd.so
%attr(755,root,root) %{_libexecdir}/kded_networkstatus.so
%attr(755,root,root) %{_libexecdir}/kded_proxyscout.so
%{?with_cups:%attr(755,root,root) %{_libexecdir}/tdeprint_cups.so}
%attr(755,root,root) %{_libexecdir}/tdeprint_ext.so
%attr(755,root,root) %{_libexecdir}/tdeprint_lpdunix.so
%attr(755,root,root) %{_libexecdir}/tdeprint_lpr.so
%attr(755,root,root) %{_libexecdir}/tdeprint_rlpr.so
%attr(755,root,root) %{_libexecdir}/tdeprint_tool_escputil.so
%attr(755,root,root) %{_libexecdir}/kgzipfilter.so
%attr(755,root,root) %{_libexecdir}/tdehtmlimagepart.so
%attr(755,root,root) %{_libexecdir}/kimg_dds.so
%attr(755,root,root) %{_libexecdir}/kimg_eps.so
%{?with_openexr:%attr(755,root,root) %{_libexecdir}/kimg_exr.so}
%attr(755,root,root) %{_libexecdir}/kimg_hdr.so
%attr(755,root,root) %{_libexecdir}/kimg_ico.so
%attr(755,root,root) %{_libexecdir}/kimg_jp2.so
%attr(755,root,root) %{_libexecdir}/kimg_pcx.so
%attr(755,root,root) %{_libexecdir}/kimg_psd.so
%attr(755,root,root) %{_libexecdir}/kimg_rgb.so
%attr(755,root,root) %{_libexecdir}/kimg_tga.so
%attr(755,root,root) %{_libexecdir}/kimg_tiff.so
%attr(755,root,root) %{_libexecdir}/kimg_xcf.so
%attr(755,root,root) %{_libexecdir}/kimg_xview.so
%attr(755,root,root) %{_libexecdir}/tdeio_file.so
%attr(755,root,root) %{_libexecdir}/tdeio_ftp.so
%attr(755,root,root) %{_libexecdir}/tdeio_ghelp.so
%attr(755,root,root) %{_libexecdir}/tdeio_help.so
%attr(755,root,root) %{_libexecdir}/tdeio_http.so
%attr(755,root,root) %{_libexecdir}/tdeio_http_cache_cleaner.so
%attr(755,root,root) %{_libexecdir}/tdeio_iso.so
%attr(755,root,root) %{_libexecdir}/tdeio_metainfo.so
%attr(755,root,root) %{_libexecdir}/tdeio_uiserver.so
%attr(755,root,root) %{_libexecdir}/kjavaappletviewer.so
%attr(755,root,root) %{_libexecdir}/tdelauncher.so
%attr(755,root,root) %{_libexecdir}/knotify.so
%{?with_aspell:%attr(755,root,root) %{_libexecdir}/tdespell_aspell.so}
%attr(755,root,root) %{_libexecdir}/tdespell_hspell.so
%attr(755,root,root) %{_libexecdir}/tdespell_ispell.so
%attr(755,root,root) %{_libexecdir}/tdestyle_highcontrast_config.so
%attr(755,root,root) %{_libexecdir}/tdestyle_plastik_config.so
%attr(755,root,root) %{_libexecdir}/tdetexteditor_docwordcompletion.so
%attr(755,root,root) %{_libexecdir}/tdetexteditor_insertfile.so
%attr(755,root,root) %{_libexecdir}/tdetexteditor_isearch.so
%attr(755,root,root) %{_libexecdir}/tdetexteditor_kdatatool.so
%attr(755,root,root) %{_libexecdir}/kxzfilter.so
%attr(755,root,root) %{_libexecdir}/libkatepart.so
%attr(755,root,root) %{_libexecdir}/libtdecertpart.so
%attr(755,root,root) %{_libexecdir}/libtdeprint_management_module.so
%attr(755,root,root) %{_libexecdir}/libtdehtmlpart.so
%attr(755,root,root) %{_libexecdir}/libtdemultipart.so
%attr(755,root,root) %{_libexecdir}/libshellscript.so
%{?with_wmf:%attr(755,root,root) %{_libexecdir}/wmfthumbnail.so}
%attr(755,root,root) %{_libexecdir}/tdefile_elf.so

%dir %{_libexecdir}/plugins
%dir %{_libexecdir}/plugins/designer
%attr(755,root,root) %{_libexecdir}/plugins/designer/tdewidgets.so
%dir %{_libexecdir}/plugins/styles
%attr(755,root,root) %{_libexecdir}/plugins/styles/asteroid.so
%attr(755,root,root) %{_libexecdir}/plugins/styles/highcolor.so
%attr(755,root,root) %{_libexecdir}/plugins/styles/highcontrast.so
%attr(755,root,root) %{_libexecdir}/plugins/styles/keramik.so
%attr(755,root,root) %{_libexecdir}/plugins/styles/kthemestyle.so
%attr(755,root,root) %{_libexecdir}/plugins/styles/light.so
%attr(755,root,root) %{_libexecdir}/plugins/styles/plastik.so

%dir %{dirname:%{_kdedocdir}}
%dir %{_kdedocdir}
%dir %{_kdedocdir}/en
%lang(en) %{_kdedocdir}/en/common
%lang(en) %{_kdedocdir}/en/tdespell

%lang(ca) %dir %{_kdedocdir}/ca
%lang(ca) %dir %{_kdedocdir}/ca/common
%lang(cs) %dir %{_kdedocdir}/cs
%lang(cs) %dir %{_kdedocdir}/cs/common
%lang(da) %dir %{_kdedocdir}/da
%lang(da) %dir %{_kdedocdir}/da/common
%lang(de) %dir %{_kdedocdir}/de
%lang(de) %dir %{_kdedocdir}/de/common
%lang(en_GB) %dir %{_kdedocdir}/en_GB
%lang(en_GB) %dir %{_kdedocdir}/en_GB/common
%lang(es) %dir %{_kdedocdir}/es
%lang(es) %dir %{_kdedocdir}/es/common
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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dcopidl
%attr(755,root,root) %{_bindir}/dcopidl2cpp
%attr(755,root,root) %{_bindir}/tdeconfig_compiler
%{_includedir}/[!a]*
%{_pkgconfigdir}/tdelibs.pc
%{_datadir}/cmake/tdelibs.cmake
%{_libexecdir}/plugins/designer/tdewidgets.la

%{_libdir}/libtdefakes_pic.a
%{_libdir}/libtdefakes_nonpic.a

%{_libdir}/libDCOP.la
%attr(755,root,root) %{_libdir}/libDCOP.so
%{_libdir}/libconnectionmanager.la
%attr(755,root,root) %{_libdir}/libconnectionmanager.so
%{_libdir}/libtdeabc.la
%attr(755,root,root) %{_libdir}/libtdeabc.so
%{_libdir}/libtdeabc_dir.la
%attr(755,root,root) %{_libdir}/libtdeabc_dir.so
%{_libdir}/libtdeabc_file.la
%attr(755,root,root) %{_libdir}/libtdeabc_file.so
%{_libdir}/libtdeabc_ldaptdeio.la
%attr(755,root,root) %{_libdir}/libtdeabc_ldaptdeio.so
%{_libdir}/libtdeabc_net.la
%attr(755,root,root) %{_libdir}/libtdeabc_net.so
%{_libdir}/libkatepartinterfaces.la
%attr(755,root,root) %{_libdir}/libkatepartinterfaces.so
%{_libdir}/libtdecore.la
%attr(755,root,root) %{_libdir}/libtdecore.so
%{_libdir}/libtdefakes.la
%attr(755,root,root) %{_libdir}/libtdefakes.so
%{_libdir}/libtdefx.la
%attr(755,root,root) %{_libdir}/libtdefx.so
%{_libdir}/libtdeprint.la
%attr(755,root,root) %{_libdir}/libtdeprint.so
%{_libdir}/libtdeprint_management.la
%attr(755,root,root) %{_libdir}/libtdeprint_management.so
%{_libdir}/libtdesasl.la
%attr(755,root,root) %{_libdir}/libtdesasl.so
%{_libdir}/libtdesu.la
%attr(755,root,root) %{_libdir}/libtdesu.so
%{_libdir}/libtdeui.la
%attr(755,root,root) %{_libdir}/libtdeui.so
%{_libdir}/libtdednssd.la
%attr(755,root,root) %{_libdir}/libtdednssd.so
%{_libdir}/libkglib.la
%attr(755,root,root) %{_libdir}/libkglib.so
%{_libdir}/libtdehtml.la
%attr(755,root,root) %{_libdir}/libtdehtml.so
%{_libdir}/libtdeimproxy.la
%attr(755,root,root) %{_libdir}/libtdeimproxy.so
%{_libdir}/libtdeio.la
%attr(755,root,root) %{_libdir}/libtdeio.so
%{_libdir}/libkjava.la
%attr(755,root,root) %{_libdir}/libkjava.so
%{_libdir}/libkjs.la
%attr(755,root,root) %{_libdir}/libkjs.so
%{_libdir}/libtdemdi.la
%attr(755,root,root) %{_libdir}/libtdemdi.so
%{_libdir}/libtdemdi2.la
%attr(755,root,root) %{_libdir}/libtdemdi2.so
%{_libdir}/libtdemediaplayer.la
%attr(755,root,root) %{_libdir}/libtdemediaplayer.so
%{_libdir}/libtdemid.la
%attr(755,root,root) %{_libdir}/libtdemid.so
%{_libdir}/libtdenewstuff.la
%attr(755,root,root) %{_libdir}/libtdenewstuff.so
%{_libdir}/libtdentlm.la
%attr(755,root,root) %{_libdir}/libtdentlm.so
%{_libdir}/libtdeparts.la
%attr(755,root,root) %{_libdir}/libtdeparts.so
%{_libdir}/libtderandr.la
%attr(755,root,root) %{_libdir}/libtderandr.so
%{_libdir}/libtderesources.la
%attr(755,root,root) %{_libdir}/libtderesources.so
%{_libdir}/libtdersync.la
%attr(755,root,root) %{_libdir}/libtdersync.so
%{_libdir}/libtdescreensaver.la
%attr(755,root,root) %{_libdir}/libtdescreensaver.so
%{_libdir}/libtdescript.la
%attr(755,root,root) %{_libdir}/libtdescript.so
%{_libdir}/libtdespell.la
%attr(755,root,root) %{_libdir}/libtdespell.so
%{_libdir}/libtdespell2.la
%attr(755,root,root) %{_libdir}/libtdespell2.so
%{_libdir}/libtdetexteditor.la
%attr(755,root,root) %{_libdir}/libtdetexteditor.so
%{_libdir}/libtdeunittest.la
%attr(755,root,root) %{_libdir}/libtdeunittest.so
%{_libdir}/libtdeutils.la
%attr(755,root,root) %{_libdir}/libtdeutils.so
%{_libdir}/libtdewalletbackend.la
%attr(755,root,root) %{_libdir}/libtdewalletbackend.so
%{_libdir}/libtdewalletclient.la
%attr(755,root,root) %{_libdir}/libtdewalletclient.so
%{_libdir}/libnetworkstatus.la
%attr(755,root,root) %{_libdir}/libnetworkstatus.so
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
