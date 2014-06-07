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
Version:	3.5.13.2
Release:	0.21
Epoch:		9
License:	LGPL v2
Group:		X11/Libraries
Source0:	http://ftp.fau.de/trinity/releases/%{version}/%{name}-trinity-%{version}.tar.xz
# Source0-md5:	0449c1386d15c744b76ba35c227b14a6
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
URL:		http://www.kde.org/
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
BuildRequires:	cups-devel >= 1:1.3.0
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
BuildRequires:	libstdc++-devel >= 5:4.1.0-0.20051206r108118.1
BuildRequires:	libtiff-devel
BuildRequires:	libtqtinterface-devel >= %{version}
%{?with_utempter:BuildRequires:	libutempter-devel}
%{?with_wmf:BuildRequires:	libwmf-devel >= 2:0.2.0}
BuildRequires:	libxml2-devel >= 2.4.9
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel >= 1.0.7
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pcre-devel
BuildRequires:	pcre-devel >= 3.5
BuildRequires:	pkgconfig
BuildRequires:	qt-devel >= 6:3.3.5.051113-1
%{?with_apidocs:BuildRequires:	qt-doc}
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-proto-compositeproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
%{?with_arts:Requires:	arts >= %{artsver}}
Requires:	ca-certificates
Requires:	cups-lib >= 1:1.3.0
Requires:	docbook-dtd412-xml
Requires:	docbook-dtd42-xml
Requires:	docbook-style-xsl
Requires:	hicolor-icon-theme
Requires:	libxml2-progs
Requires:	qt >= 6:3.3.3-4
Requires:	setup >= 2.4.6-7
Requires:	xorg-app-iceauth
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/trinity
%define		_applnkdir	%{_datadir}/applnk

# avoid java dependency
# TODO: split to kjava subpackage
%define		_noautoreqfiles %{_datadir}/apps/kjava/kjava.jar

# unresolved kss_* symbols in libkscreensaver.so.X (by design)
%define		skip_post_check_so libkscreensaver.so.4.2.0

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
Requires:	qt-devel >= 6:3.3.3-4
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
%setup -q -n %{name}-trinity-%{version} %{?with_wmf:-a1}
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
	-DWITH_CUPS=ON \
	-DWITH_LUA=OFF \
	-DWITH_TIFF=ON \
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
		$RPM_BUILD_ROOT%{_datadir}/services/kconfiguredialog \
		$RPM_BUILD_ROOT%{_iconsdir}/crystalsvg/{16x16,22x22,32x32,48x48,64x64,128x128}/apps

	install -d $RPM_BUILD_ROOT%{_kdedocdir}/{ca,cs,da,de,en,en_GB,es,et,fi,fr,hu,it,ja,nb,nl,pl,pt,pt_BR,ro,ru,sk,sl,sv,tr,uk,zh_TW}/common

	# should be hardlinked, not copied
	ln -nf $RPM_BUILD_ROOT%{_bindir}/{kdeinit_wrapper,kdeinit_shutdown}
	ln -nf $RPM_BUILD_ROOT%{_bindir}/{ktelnetservice,filesharelist}

	mv $RPM_BUILD_ROOT/etc/xdg/menus/{,kde-}applications.menu

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
	%{__rm} $RPM_BUILD_ROOT%{_libdir}/libkdeinit_*.la

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
%attr(2755,root,fileshare) %{_bindir}/filesharelist
%attr(2755,root,fileshare) %{_bindir}/fileshareset
%attr(4755,root,root) %{_bindir}/start_kdeinit
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
%attr(755,root,root) %{_bindir}/imagetops
%attr(755,root,root) %{_bindir}/kab2kabc
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
%attr(755,root,root) %{_bindir}/kdetcompmgr
%attr(755,root,root) %{_bindir}/kdontchangethehostname
%attr(755,root,root) %{_bindir}/kdostartupconfig
%attr(755,root,root) %{_bindir}/kfile
%attr(755,root,root) %{_bindir}/kfmexec
%attr(755,root,root) %{_bindir}/khotnewstuff
%attr(755,root,root) %{_bindir}/kinstalltheme
%attr(755,root,root) %{_bindir}/kio_http_cache_cleaner
%attr(755,root,root) %{_bindir}/kio_uiserver
%attr(755,root,root) %{_bindir}/kioexec
%attr(755,root,root) %{_bindir}/kioslave
%attr(755,root,root) %{_bindir}/klauncher
%attr(755,root,root) %{_bindir}/kmailservice
%attr(755,root,root) %{_bindir}/kmimelist
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
%attr(755,root,root) %{_bindir}/networkstatustestservice
%attr(755,root,root) %{_bindir}/preparetips
%attr(755,root,root) %{_bindir}/start_kdeinit_wrapper

%dir %{_datadir}/apps
%{_datadir}/apps/LICENSES
%attr(755,root,root) %{_datadir}/apps/dcopidlng/kalyptus
%dir %{_datadir}/apps/kconf_update
%attr(755,root,root) %{_datadir}/apps/kconf_update/*.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/*.sh
%dir %{_datadir}/apps/dcopidlng
%dir %{_datadir}/emoticons
%dir %{_datadir}/autostart
%{_datadir}/apps/dcopidlng/*.pm
%{_datadir}/apps/kabc
%{_datadir}/apps/katepart
%{_datadir}/apps/kcertpart
%{_datadir}/apps/kcm_componentchooser
%{_datadir}/apps/kconf_update/*.upd
%{_datadir}/apps/kdeprint
%{_datadir}/apps/kdeui
%{_datadir}/apps/kdewidgets
%{_datadir}/apps/khtml
%{_datadir}/apps/kio_uiserver
%{_datadir}/apps/kjava
%{_datadir}/apps/knewstuff
%{_datadir}/apps/knotify
%{_datadir}/apps/ksgmltools2
%{_datadir}/apps/kssl
%{_datadir}/apps/kstyle
%{_datadir}/apps/ktexteditor_docwordcompletion
%{_datadir}/apps/ktexteditor_insertfile
%{_datadir}/apps/ktexteditor_isearch
%{_datadir}/apps/ktexteditor_kdatatool
%{_datadir}/apps/proxyscout

%dir %{_datadir}/apps/konqueror
%dir %{_datadir}/apps/konqueror/servicemenus
%{_datadir}/apps/konqueror/servicemenus/isoservice.desktop

%{_datadir}/autostart/kab2kabc.desktop

%{_datadir}/config
%{_datadir}/emoticons/Default
%{_datadir}/mimelnk

%dir %{_datadir}/services
%dir %{_datadir}/services/.hidden
%dir %{_datadir}/services/kconfiguredialog
%dir %{_datadir}/services/kresources
%{_datadir}/services/kresources/kabc
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
%{_datadir}/services/kcertpart.desktop
%{_datadir}/services/kded
%{_datadir}/services/kgzipfilter.desktop
%{_datadir}/services/khtml.desktop
%{_datadir}/services/khtmlimage.desktop
%{_datadir}/services/kio_uiserver.desktop
%{_datadir}/services/kjavaappletviewer.desktop
%{_datadir}/services/kmailservice.protocol
%{_datadir}/services/kmultipart.desktop
%{_datadir}/services/knotify.desktop
%{_datadir}/services/kresources/kabc_manager.desktop
%{?with_aspell:%{_datadir}/services/kspell_aspell.desktop}
%{_datadir}/services/kspell_hspell.desktop
%{_datadir}/services/kspell_ispell.desktop
%{_datadir}/services/ktexteditor_docwordcompletion.desktop
%{_datadir}/services/ktexteditor_insertfile.desktop
%{_datadir}/services/ktexteditor_isearch.desktop
%{_datadir}/services/ktexteditor_kdatatool.desktop
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
%{?with_wmf:%{_datadir}/services/wmfthumbnail.desktop}
%{_datadir}/services/xbm.kimgio
%{_datadir}/services/xcf.kimgio
%{_datadir}/services/xpm.kimgio
%{_datadir}/services/xv.kimgio
%{_datadir}/services/iso.protocol
%{_datadir}/servicetypes
%{_iconsdir}/crystalsvg
%{_iconsdir}/default.kde
%{_localedir}/all_languages

%dir %{_desktopdir}/kde
%{_desktopdir}/kde/kresources.desktop
%dir %{_applnkdir}
%dir %{_applnkdir}/.hidden
%{_applnkdir}/kio_iso.desktop
/etc/xdg/menus/kde-applications.menu

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

%attr(755,root,root) %{_libdir}/libDCOP.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libDCOP.so.4
%attr(755,root,root) %{_libdir}/libconnectionmanager.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libconnectionmanager.so.0
%attr(755,root,root) %{_libdir}/libkabc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkabc.so.1
%attr(755,root,root) %{_libdir}/libkabc_dir.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkabc_dir.so.1
%attr(755,root,root) %{_libdir}/libkabc_file.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkabc_file.so.1
%attr(755,root,root) %{_libdir}/libkabc_ldapkio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkabc_ldapkio.so.1
%attr(755,root,root) %{_libdir}/libkabc_net.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkabc_net.so.1
%attr(755,root,root) %{_libdir}/libkatepartinterfaces.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkatepartinterfaces.so.0
%attr(755,root,root) %{_libdir}/libkdecore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdecore.so.4
%attr(755,root,root) %{_libdir}/libkdefakes.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdefakes.so.4
%attr(755,root,root) %{_libdir}/libkdefx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdefx.so.4
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
%attr(755,root,root) %{_libdir}/libkglib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkglib.so.0
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
%attr(755,root,root) %{_libdir}/libkrandr.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkrandr.so.0
%attr(755,root,root) %{_libdir}/libkresources.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkresources.so.1
%attr(755,root,root) %{_libdir}/libkrsync.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkrsync.so.0
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
%{_libdir}/libkdeinit_cupsdconf.la
%{_libdir}/libkdeinit_dcopserver.la
%{_libdir}/libkdeinit_kaddprinterwizard.la
%{_libdir}/libkdeinit_kbuildsycoca.la
%{_libdir}/libkdeinit_kcmshell.la
%{_libdir}/libkdeinit_kconf_update.la
%{_libdir}/libkdeinit_kcookiejar.la
%{_libdir}/libkdeinit_kded.la
%{_libdir}/libkdeinit_kio_http_cache_cleaner.la
%{_libdir}/libkdeinit_kio_uiserver.la
%{_libdir}/libkdeinit_klauncher.la
%{_libexecdir}/cupsdconf.la
%{_libexecdir}/dcopserver.la
%{_libexecdir}/kabc_dir.la
%{_libexecdir}/kabc_file.la
%{_libexecdir}/kabc_ldapkio.la
%{_libexecdir}/kabc_net.la
%{_libexecdir}/kabcformat_binary.la
%{_libexecdir}/kaddprinterwizard.la
%{_libexecdir}/kbuildsycoca.la
%{_libexecdir}/kbzip2filter.la
%{_libexecdir}/kcm_kresources.la
%{_libexecdir}/kcmshell.la
%{_libexecdir}/kconf_update.la
%{_libexecdir}/kcookiejar.la
%{_libexecdir}/kded.la
%{_libexecdir}/kded_kcookiejar.la
%{_libexecdir}/kded_kdeprintd.la
%{_libexecdir}/kded_kdetrayproxy.la
%{_libexecdir}/kded_kpasswdserver.la
%{_libexecdir}/kded_kssld.la
%{_libexecdir}/kded_kwalletd.la
%{_libexecdir}/kded_networkstatus.la
%{_libexecdir}/kded_proxyscout.la
%{_libexecdir}/kdeprint_cups.la
%{_libexecdir}/kdeprint_ext.la
%{_libexecdir}/kdeprint_lpdunix.la
%{_libexecdir}/kdeprint_lpr.la
%{_libexecdir}/kdeprint_rlpr.la
%{_libexecdir}/kdeprint_tool_escputil.la
%{_libexecdir}/kgzipfilter.la
%{_libexecdir}/khtmlimagepart.la
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
%{_libexecdir}/kio_file.la
%{_libexecdir}/kio_ftp.la
%{_libexecdir}/kio_ghelp.la
%{_libexecdir}/kio_help.la
%{_libexecdir}/kio_http.la
%{_libexecdir}/kio_http_cache_cleaner.la
%{_libexecdir}/kio_iso.la
%{_libexecdir}/kio_metainfo.la
%{_libexecdir}/kio_uiserver.la
%{_libexecdir}/kjavaappletviewer.la
%{_libexecdir}/klauncher.la
%{_libexecdir}/knotify.la
%{_libexecdir}/kspell_aspell.la
%{_libexecdir}/kspell_hspell.la
%{_libexecdir}/kspell_ispell.la
%{_libexecdir}/kstyle_highcontrast_config.la
%{_libexecdir}/kstyle_plastik_config.la
%{_libexecdir}/ktexteditor_docwordcompletion.la
%{_libexecdir}/ktexteditor_insertfile.la
%{_libexecdir}/ktexteditor_isearch.la
%{_libexecdir}/ktexteditor_kdatatool.la
%{_libexecdir}/kxzfilter.la
%{_libexecdir}/libkatepart.la
%{_libexecdir}/libkcertpart.la
%{_libexecdir}/libkdeprint_management_module.la
%{_libexecdir}/libkhtmlpart.la
%{_libexecdir}/libkmultipart.la
%{_libexecdir}/libshellscript.la
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
%attr(755,root,root) %{_libexecdir}/cupsdconf.so
%attr(755,root,root) %{_libexecdir}/dcopserver.so
%attr(755,root,root) %{_libexecdir}/kabc_dir.so
%attr(755,root,root) %{_libexecdir}/kabc_file.so
%attr(755,root,root) %{_libexecdir}/kabc_ldapkio.so
%attr(755,root,root) %{_libexecdir}/kabc_net.so
%attr(755,root,root) %{_libexecdir}/kabcformat_binary.so
%attr(755,root,root) %{_libexecdir}/kaddprinterwizard.so
%attr(755,root,root) %{_libexecdir}/kbuildsycoca.so
%attr(755,root,root) %{_libexecdir}/kbzip2filter.so
%attr(755,root,root) %{_libexecdir}/kcm_kresources.so
%attr(755,root,root) %{_libexecdir}/kcmshell.so
%attr(755,root,root) %{_libexecdir}/kconf_update.so
%attr(755,root,root) %{_libexecdir}/kcookiejar.so
%attr(755,root,root) %{_libexecdir}/kded.so
%attr(755,root,root) %{_libexecdir}/kded_kcookiejar.so
%attr(755,root,root) %{_libexecdir}/kded_kdeprintd.so
%attr(755,root,root) %{_libexecdir}/kded_kdetrayproxy.so
%attr(755,root,root) %{_libexecdir}/kded_kpasswdserver.so
%attr(755,root,root) %{_libexecdir}/kded_kssld.so
%attr(755,root,root) %{_libexecdir}/kded_kwalletd.so
%attr(755,root,root) %{_libexecdir}/kded_networkstatus.so
%attr(755,root,root) %{_libexecdir}/kded_proxyscout.so
%attr(755,root,root) %{_libexecdir}/kdeprint_cups.so
%attr(755,root,root) %{_libexecdir}/kdeprint_ext.so
%attr(755,root,root) %{_libexecdir}/kdeprint_lpdunix.so
%attr(755,root,root) %{_libexecdir}/kdeprint_lpr.so
%attr(755,root,root) %{_libexecdir}/kdeprint_rlpr.so
%attr(755,root,root) %{_libexecdir}/kdeprint_tool_escputil.so
%attr(755,root,root) %{_libexecdir}/kgzipfilter.so
%attr(755,root,root) %{_libexecdir}/khtmlimagepart.so
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
%attr(755,root,root) %{_libexecdir}/kio_file.so
%attr(755,root,root) %{_libexecdir}/kio_ftp.so
%attr(755,root,root) %{_libexecdir}/kio_ghelp.so
%attr(755,root,root) %{_libexecdir}/kio_help.so
%attr(755,root,root) %{_libexecdir}/kio_http.so
%attr(755,root,root) %{_libexecdir}/kio_http_cache_cleaner.so
%attr(755,root,root) %{_libexecdir}/kio_iso.so
%attr(755,root,root) %{_libexecdir}/kio_metainfo.so
%attr(755,root,root) %{_libexecdir}/kio_uiserver.so
%attr(755,root,root) %{_libexecdir}/kjavaappletviewer.so
%attr(755,root,root) %{_libexecdir}/klauncher.so
%attr(755,root,root) %{_libexecdir}/knotify.so
%{?with_aspell:%attr(755,root,root) %{_libexecdir}/kspell_aspell.so}
%attr(755,root,root) %{_libexecdir}/kspell_hspell.so
%attr(755,root,root) %{_libexecdir}/kspell_ispell.so
%attr(755,root,root) %{_libexecdir}/kstyle_highcontrast_config.so
%attr(755,root,root) %{_libexecdir}/kstyle_plastik_config.so
%attr(755,root,root) %{_libexecdir}/ktexteditor_docwordcompletion.so
%attr(755,root,root) %{_libexecdir}/ktexteditor_insertfile.so
%attr(755,root,root) %{_libexecdir}/ktexteditor_isearch.so
%attr(755,root,root) %{_libexecdir}/ktexteditor_kdatatool.so
%attr(755,root,root) %{_libexecdir}/kxzfilter.so
%attr(755,root,root) %{_libexecdir}/libkatepart.so
%attr(755,root,root) %{_libexecdir}/libkcertpart.so
%attr(755,root,root) %{_libexecdir}/libkdeprint_management_module.so
%attr(755,root,root) %{_libexecdir}/libkhtmlpart.so
%attr(755,root,root) %{_libexecdir}/libkmultipart.so
%attr(755,root,root) %{_libexecdir}/libshellscript.so
%{?with_wmf:%attr(755,root,root) %{_libexecdir}/wmfthumbnail.so}

%dir %{_libexecdir}/plugins
%dir %{_libexecdir}/plugins/designer
%attr(755,root,root) %{_libexecdir}/plugins/designer/kdewidgets.so
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
%lang(en) %{_kdedocdir}/en/kspell

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
%attr(755,root,root) %{_bindir}/kconfig_compiler
%{_includedir}/[!a]*
%{_datadir}/cmake/kdelibs.cmake
%{_libexecdir}/plugins/designer/kdewidgets.la

%{_libdir}/libkdefakes_pic.a
%{_libdir}/libkdefakes_nonpic.a

%{_libdir}/libDCOP.la
%attr(755,root,root) %{_libdir}/libDCOP.so
%{_libdir}/libconnectionmanager.la
%attr(755,root,root) %{_libdir}/libconnectionmanager.so
%{_libdir}/libkabc.la
%attr(755,root,root) %{_libdir}/libkabc.so
%{_libdir}/libkabc_dir.la
%attr(755,root,root) %{_libdir}/libkabc_dir.so
%{_libdir}/libkabc_file.la
%attr(755,root,root) %{_libdir}/libkabc_file.so
%{_libdir}/libkabc_ldapkio.la
%attr(755,root,root) %{_libdir}/libkabc_ldapkio.so
%{_libdir}/libkabc_net.la
%attr(755,root,root) %{_libdir}/libkabc_net.so
%{_libdir}/libkatepartinterfaces.la
%attr(755,root,root) %{_libdir}/libkatepartinterfaces.so
%{_libdir}/libkdecore.la
%attr(755,root,root) %{_libdir}/libkdecore.so
%{_libdir}/libkdefakes.la
%attr(755,root,root) %{_libdir}/libkdefakes.so
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
%{_libdir}/libkglib.la
%attr(755,root,root) %{_libdir}/libkglib.so
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
%{_libdir}/libkrandr.la
%attr(755,root,root) %{_libdir}/libkrandr.so
%{_libdir}/libkresources.la
%attr(755,root,root) %{_libdir}/libkresources.so
%{_libdir}/libkrsync.la
%attr(755,root,root) %{_libdir}/libkrsync.so
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
