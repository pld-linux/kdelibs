#
# Conditional build:
%bcond_without	alsa	# build without ALSA support
%bcond_without	apidocs	# do not prepare API documentation
%bcond_with	verbose	# verbose build

%define		_state		unstable
%define		_ver		3.3.89
%define		_snap		041113
%define         artsver         13:1.3.89

Summary:	K Desktop Environment - libraries
Summary(es):	K Desktop Environment - bibliotecas
Summary(ko):	KDE - ¶óÀÌºê·¯¸®
Summary(pl):	K Desktop Environment - biblioteki
Summary(pt_BR):	Bibliotecas de fundação do KDE
Summary(ru):	K Desktop Environment - âÉÂÌÉÏÔÅËÉ
Summary(uk):	K Desktop Environment - â¦ÂÌ¦ÏÔÅËÉ
Name:		kdelibs
Version:	%{_ver}.%{_snap}
Release:	1
Epoch:		9
License:	LGPL
Group:		X11/Libraries
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{_ver}.tar.bz2
Source0:	http://ftp.pld-linux.org/software/kde/%{name}-%{_snap}.tar.bz2
# Source0-md5:	18220e2bb3d0f0aa3ef6da6c27d3c1d9
# Source0-size:	15573765
Source1:	%{name}-wmfplugin.tar.bz2
# Source1-md5:	df0d7c2a13bb68fe25e1d6c009df5b8d
# Source1-size:	3376
Source2:	pnm.protocol
Source3:	x-icq.mimelnk
Patch0:		kde-common-PLD.patch
Patch1:		%{name}-kstandarddirs.patch
Patch2:		%{name}-defaultfonts.patch
Patch3:		%{name}-use_system_sgml.patch
Patch4:		%{name}-fileshareset.patch
Patch5:         %{name}-appicon_themable.patch
Icon:		kdelibs.xpm
URL:		http://www.kde.org/
BuildRequires:	OpenEXR-devel
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	arts-qt-devel >= %{artsver}
BuildRequires:	artsc-devel >= %{artsver}
BuildRequires:	aspell-devel
BuildRequires:	audiofile-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6.1
BuildRequires:	bzip2-devel
BuildRequires:	cups-devel
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-utils
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	ed
BuildRequires:	fam-devel
BuildRequires:	gettext-devel
%{?with_apidocs:BuildRequires:	graphviz}
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
BuildRequires:	libxml2-devel >= 2.4.9
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel >= 1.0.7
BuildRequires:	libwmf-devel >= 2:0.2.0
BuildRequires:	openmotif-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pcre-devel >= 3.5
BuildRequires:	qt-devel >= 6:3.3.3-4
%{?with_apidocs:BuildRequires:	qt-doc}
BuildRequires:	unsermake >= 040511
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	zlib-devel
BuildConflicts:	kdepim-korganizer-libs
BuildConflicts:	kdepim-libkdepim < 3:3.3.0
PreReq:		setup >= 2.4.6-7
Requires:	arts >= %{artsver}
Requires:	docbook-dtd412-xml
Requires:	docbook-dtd42-xml
Requires:	docbook-style-xsl
Requires:	qt >= 6:3.3.3-4
Obsoletes:	arts-kde
Obsoletes:	kde-theme-keramik
Obsoletes:	%{name}-kabc
Obsoletes:	kdelibs2
Obsoletes:	kdelibs2-sound
Obsoletes:	kdelibs-sound
Obsoletes:	kdesupport
Obsoletes:	kdesupport-devel
Obsoletes:	kdesupport-static
Obsoletes:	kdesupport-mimelib
Obsoletes:	kdesupport-mimelib-devel
Obsoletes:	kdesupport-mimelib-static
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
Obsoletes:	kdepim-kaddressbook < 3:3.1.91.030918-1
Obsoletes:	kdepim-kmail < 3:3.1.91.030918-1
Obsoletes:	kdepim-kontact < 3:3.1.91.030918-1
Obsoletes:	kdepim-korganizer < 3:3.1.91.030918-1
Obsoletes:	kdepim-libkcal < 3:3.1.91.030918-1
Obsoletes:	kdepim-libkdenetwork < 3:3.1.91.030918-1
Obsoletes:	kdepim-libkdepim < 3:3.2.90
Obsoletes:	openoffice-mimelinks
Conflicts:	kdepim-devel < 3:3.2.90
Conflicts:	kmplayer < 1:0.83-0.040705.2
Conflicts:	kplayer < 0.5.1-5
Conflicts:	pixieplus < 0.3-4
Conflicts:	sim < 0.9.3-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package includes libraries that are central to the development
and execution of a KDE program, misc HTML documentation and theme
modules.

Included in this package are among others:
- kdecore - KDE core library,
- kdeui - KDE user interface library,
- khtml - KDE HTML widget with javascript and CSS support,
- kwallet - KDE password manager.

%description -l es
Bibliotecas para KDE.

%description -l pl
Ten pakiet zawiera biblioteki potrzebne do rozwijania i uruchamiania
aplikacji KDE, ró¿n± dokumentacjê oraz modu³y z motywami wygl±du KDE.

Pakiet ten zawiera miêdzy innymi:
- kdecore - podstawow± bibliotekê KDE,
- kdeui - interfejs u¿ytkownika KDE,
- khtml - obs³ugê HTML, javascript oraz CSS dla KDE,
- kwallet - system zarz±dzania has³ami w KDE.

%description -l pt_BR
Bibliotecas de fundação do KDE requeridas por todo e qualquer
aplicativo KDE.

%description -l ru
âÉÂÌÉÏÔÅËÉ ÄÌÑ K Desktop Environment.

÷ËÌÀÞÅÎÙ ÂÉÂÌÉÏÔÅËÉ KDE:
- jscript (javascript),
- kdecore (ÑÄÒÏ KDE),
- kdeui (ÉÎÔÅÒÆÅÊÓ ÐÏÌØÚÏ×ÁÔÅÌÑ),
- khtmlw (ÒÁÂÏÔÁ Ó HTML),
- kimgio (ÏÂÒÁÂÏÔËÁ ÉÚÏÂÒÁÖÅÎÉÊ).
- kspell (ÐÒÏ×ÅÒËÁ ÏÒÆÏÇÒÁÆÉÉ),

%description -l uk
â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ K Desktop Environment.

÷ËÌÀÞÅÎ¦ ÔÁË¦ Â¦ÂÌ¦ÏÔÅËÉ KDE:
- jscript (javascript),
- kdecore (ÑÄÒÏ KDE),
- kdeui (¦ÎÔÅÒÆÅÊÓ ËÏÒÉÓÔÕ×ÁÞÁ),
- khtmlw (ÒÏÂÏÔÁ Ú HTML),
- kimgio (ÏÂÒÏÂËÁ ÚÏÂÒÁÖÅÎØ).
- kspell (ÐÅÒÅ×¦ÒËÁ ÏÒÆÏÇÒÁÆ¦§),

%package devel
Summary:	kdelibs - header files and development documentation
Summary(pl):	kdelibs - pliki nag³ówkowe i dokumentacja do kdelibs
Summary(pt_BR):	Arquivos de inclusão e documentação para compilar aplicativos KDE
Summary(ru):	èÅÄÅÒÙ É ÄÏËÕÍÅÎÔÁÃÉÑ ÄÌÑ ËÏÍÐÉÌÌÑÃÉÉ ÐÒÏÇÒÁÍÍ KDE
Summary(uk):	èÅÄÅÒÉ ÔÁ ÄÏËÕÍÅÎÔÁÃ¦Ñ ÄÌÑ ËÏÍÐ¦ÌÑÃ¦§ ÐÒÏÇÒÁÍ KDE
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	arts-qt-devel >= %{artsver}
Requires:	artsc-devel >= %{artsver}
Requires:	fam-devel
Requires:	libart_lgpl-devel
Requires:	libidn-devel
Requires:	pcre-devel
Requires:	qt-devel >= 6:3.3.3-4
Obsoletes:	arts-kde-devel
Obsoletes:	kdelibs-sound-devel
Obsoletes:	kdelibs2-devel
Obsoletes:	kdelibs2-sound-devel
Obsoletes:	kdelibs-static
Conflicts:	kdebase-devel <= 9:3.1.90

%description devel
This package contains header files and development documentation for
kdelibs.

%description devel -l pl
Pakiet ten zawiera pliki nag³ówkowe i dokumentacjê potrzebn± przy
pisaniu w³asnych programów wykorzystuj±cych kdelibs.

%description devel -l pt_BR
Este pacote contém os arquivos de inclusão que são necessários para
compilar aplicativos KDE. 

%description devel -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÈÅÄÅÒÙ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ËÏÍÐÉÌÑÃÉÉ ÐÒÏÇÒÁÍÍ ÄÌÑ
KDE. 

%description devel -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÈÅÄÅÒÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ËÏÍÐ¦ÌÑÃ¦§ ÐÒÏÇÒÁÍ ÄÌÑ KDE.

%package apidocs
Summary:	API documentation
Summary(pl):	Dokumentacja API
Group:		Documentation
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description apidocs
Annotated reference of KDE libraries programming interface including:
- class lists
- class members
- namespaces

%description apidocs -l pl
Dokumentacja interfejsu programowania bibliotek KDE z przypisami.
Zawiera:
- listy klas i ich sk³adników
- listê przestrzeni nazw (namespace)

%package artsmessage
Summary:	Program used to display aRts daemon messages
Summary(pl):	Program do wy¶wietlania komunikatów demona aRts
Group:		Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	arts-message

%description artsmessage
This program is run when a -m option argument is passed to aRts
daemon. It displays messages generated by daemon.

%description artsmessage -l pl
Ten program jest uruchamiany, gdy do demona aRts zostanie przekazana
opcja z parametrem -m. Bêdzie on u¿ywany do wy¶wietlenia komunikatów
demona.

%package kgrantpty
Summary:	Helper program to fix terminal permissions
Summary(pl):	Program pomocniczy do ustawiania uprawnieñ terminala
Group:		Applications/Terminal
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description kgrantpty
This suid root program fixes the permissions of pseudo-terminal device
files so that they cannot be eavesdropped by other local users. Systems
that support /dev/pts (typical PLD installations do) don't require an
extra program to do it, in that case this package is useless.

Install this package if you're running a custom system that lacks
Unix98 pts support and privacy from other local users is a concern for
you.

%description kgrantpty -l pl
Ten program, dzia³aj±cy z uprawnieniami roota, poprawia uprawnienia
plików pseudo-terminali, ¿eby unikn±æ ich pods³uchiwania przez innych
lokalnych u¿ytkowników. Systemy obs³uguj±ce /dev/pts (typowe instalacje
PLD go obs³uguj±) nie wymagaj± do tego dodatkowego programu, w tym
przypadku ten pakiet jest bezu¿yteczny.

Zainstaluj ten pakiet je¿eli korzystasz z nietypowej konfiguracji
nieobs³uguj±cej pts-ów typu Unix98 i obawiasz siê inwigilacji ze strony
innych u¿ytkowników lokalnych.

%prep
%setup -q -n %{name}-%{_snap} -a1
#%patch100 -p1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1 
%patch5 -p1 

#echo "KDE_OPTIONS = nofinal" >> kdeui/Makefile.am
#echo "KDE_OPTIONS = nofinal" >> kjs/Makefile.am

%{__sed} -i -e 's/Terminal=0/Terminal=false/' \
	kresources/kresources.desktop

%build

cp %{_datadir}/automake/config.sub admin

export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}

#export UNSERMAKE=%{_datadir}/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	%{!?debug:--disable-rpath} \
	--enable-final \
	--enable-mitshm \
	--with-ldap=no \
	--with%{!?with_alsa:out}-alsa \
	--with-qt-libraries=%{_libdir}

%{__make} %{?with_verbose:VERBOSE=1}

%{?with_apidocs:%{__make} apidox}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}
	kde_libs_htmldir=%{_kdedocdir}

install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/services
install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/mimelnk/application

#{__make} install \
#	DESTDIR=$RPM_BUILD_ROOT

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
	$RPM_BUILD_ROOT%{_datadir}/wallpapers \
	$RPM_BUILD_ROOT%{_iconsdir}/crystalsvg/{16x16,22x22,32x32,48x48,64x64,128x128}/apps

# Debian manpages
install -d $RPM_BUILD_ROOT%{_mandir}/man1
cd debian/man
%{__perl} -pi -e 's/ksendbugemail/ksendbugmail/;s/KSENDBUGEMAIL/KSENDBUGMAIL/' \
    ksendbugmail.sgml

for f in *.sgml ; do
	base="$(basename $f .sgml)"
	upper="$(echo ${base} | tr a-z A-Z)"
	db2man $f
	install ${upper}.1 $RPM_BUILD_ROOT%{_mandir}/man1/${base}.1
done
cd -

# For fileshare
touch $RPM_BUILD_ROOT/etc/security/fileshare.conf
%{__sed} -i -e  "s|/etc/init.d|/etc/rc.d/init.d|g" $RPM_BUILD_ROOT%{_bindir}/fileshare*

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
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
%attr(755,root,root) %{_bindir}/ghns
%ghost /etc/security/fileshare.conf
%attr(2755,root,fileshare) %{_bindir}/filesharelist
%attr(2755,root,fileshare) %{_bindir}/fileshareset
%attr(755,root,root) %{_bindir}/imagetops
%attr(755,root,root) %{_bindir}/kaddprinterwizard
%attr(755,root,root) %{_bindir}/kbuildsycoca
%attr(755,root,root) %{_bindir}/kconf_update
%attr(755,root,root) %{_bindir}/kcookiejar
#%%attr(755,root,root) %{_bindir}/kdb2html
%attr(755,root,root) %{_bindir}/kde-config
%attr(755,root,root) %{_bindir}/kde-menu
%attr(755,root,root) %{_bindir}/kded
%attr(755,root,root) %{_bindir}/kdeinit
%attr(755,root,root) %{_bindir}/kdeinit_shutdown
%attr(755,root,root) %{_bindir}/kdeinit_wrapper
%attr(755,root,root) %{_bindir}/kdesu_stub
%attr(755,root,root) %{_bindir}/kdontchangethehostname
%attr(755,root,root) %{_bindir}/kfile
%attr(755,root,root) %{_bindir}/khotnewstuff
%attr(755,root,root) %{_bindir}/kimage_concat
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
%attr(755,root,root) %{_bindir}/ksvgtopng
%attr(755,root,root) %{_bindir}/ktelnetservice
%attr(755,root,root) %{_bindir}/ktradertest
%attr(755,root,root) %{_bindir}/kwrapper
%attr(755,root,root) %{_bindir}/lnusertemp
%attr(755,root,root) %{_bindir}/make_driver_db_cups
%attr(755,root,root) %{_bindir}/make_driver_db_lpr
%attr(755,root,root) %{_bindir}/makekdewidgets
%attr(755,root,root) %{_bindir}/meinproc
%attr(755,root,root) %{_bindir}/preparetips
#%attr(755,root,root) %{_bindir}/xml2man
%{_libdir}/libDCOP.la
%attr(755,root,root) %{_libdir}/libDCOP.so.*.*.*
%{_libdir}/libartskde.la
%attr(755,root,root) %{_libdir}/libartskde.so.*.*.*
%{_libdir}/libkabc.la
%attr(755,root,root) %{_libdir}/libkabc.so.*.*.*
%{_libdir}/libkabc_dir.la
%attr(755,root,root) %{_libdir}/libkabc_dir.so.*.*.*
%{_libdir}/libkabc_file.la
%attr(755,root,root) %{_libdir}/libkabc_file.so.*.*.*
%{_libdir}/libkabc_ldapkio.la
%attr(755,root,root) %{_libdir}/libkabc_ldapkio.so.*.*.*
%{_libdir}/libkabc_net.la
%attr(755,root,root) %{_libdir}/libkabc_net.so.*.*.*
%{_libdir}/libkatepartinterfaces.la
%attr(755,root,root) %{_libdir}/libkatepartinterfaces.so.*.*.*
%{_libdir}/libkdecore.la
%attr(755,root,root) %{_libdir}/libkdecore.so.*.*.*
%{_libdir}/libkdefakes.la
%attr(755,root,root) %{_libdir}/libkdefakes.so.*.*.*
%{_libdir}/libkdefx.la
%attr(755,root,root) %{_libdir}/libkdefx.so.*.*.*
%{_libdir}/libkdeinit_cupsdconf.la
%attr(755,root,root) %{_libdir}/libkdeinit_cupsdconf.so
%{_libdir}/libkdeinit_dcopserver.la
%attr(755,root,root) %{_libdir}/libkdeinit_dcopserver.so
%{_libdir}/libkdeinit_kaddprinterwizard.la
%attr(755,root,root) %{_libdir}/libkdeinit_kaddprinterwizard.so
%{_libdir}/libkdeinit_kbuildsycoca.la
%attr(755,root,root) %{_libdir}/libkdeinit_kbuildsycoca.so
%{_libdir}/libkdeinit_kconf_update.la
%attr(755,root,root) %{_libdir}/libkdeinit_kconf_update.so
%{_libdir}/libkdeinit_kcookiejar.la
%attr(755,root,root) %{_libdir}/libkdeinit_kcookiejar.so
%{_libdir}/libkdeinit_kded.la
%attr(755,root,root) %{_libdir}/libkdeinit_kded.so
%{_libdir}/libkdeinit_kio_http_cache_cleaner.la
%attr(755,root,root) %{_libdir}/libkdeinit_kio_http_cache_cleaner.so
%{_libdir}/libkdeinit_kio_uiserver.la
%attr(755,root,root) %{_libdir}/libkdeinit_kio_uiserver.so
%{_libdir}/libkdeinit_klauncher.la
%attr(755,root,root) %{_libdir}/libkdeinit_klauncher.so
%{_libdir}/libkdeprint.la
%attr(755,root,root) %{_libdir}/libkdeprint.so.*.*.*
%{_libdir}/libkdeprint_management.la
%attr(755,root,root) %{_libdir}/libkdeprint_management.so.*.*.*
%{_libdir}/libkdesasl.la
%attr(755,root,root) %{_libdir}/libkdesasl.so.*.*.*
%{_libdir}/libkdesu.la
%attr(755,root,root) %{_libdir}/libkdesu.so.*.*.*
%{_libdir}/libkdeui.la
%attr(755,root,root) %{_libdir}/libkdeui.so.*.*.*
%{_libdir}/libkhtml.la
%attr(755,root,root) %{_libdir}/libkhtml.so.*.*.*
%{_libdir}/libkimproxy.la
%attr(755,root,root) %{_libdir}/libkimproxy.so.*.*.*
%{_libdir}/libkio.la
%attr(755,root,root) %{_libdir}/libkio.so.*.*.*
%{_libdir}/libkjava.la
%attr(755,root,root) %{_libdir}/libkjava.so.*.*.*
%{_libdir}/libkjs.la
%attr(755,root,root) %{_libdir}/libkjs.so.*.*.*
%{_libdir}/libkmdi.la
%attr(755,root,root) %{_libdir}/libkmdi.so.*.*.*
%{_libdir}/libkmdi2.la
%attr(755,root,root) %{_libdir}/libkmdi2.so.*.*.*
%{_libdir}/libkmediaplayer.la
%attr(755,root,root) %{_libdir}/libkmediaplayer.so.*.*.*
%{_libdir}/libkmid.la
%attr(755,root,root) %{_libdir}/libkmid.so.*.*.*
%{_libdir}/libknewstuff.la
%attr(755,root,root) %{_libdir}/libknewstuff.so.*.*.*
%{_libdir}/libkntlm.la
%attr(755,root,root) %{_libdir}/libkntlm.so.*.*.*
%{_libdir}/libkparts.la
%attr(755,root,root) %{_libdir}/libkparts.so.*.*.*
%{_libdir}/libkresources.la
%attr(755,root,root) %{_libdir}/libkresources.so.*.*.*
%{_libdir}/libkscreensaver.la
%attr(755,root,root) %{_libdir}/libkscreensaver.so.*.*.*
%{_libdir}/libkscript.la
%attr(755,root,root) %{_libdir}/libkscript.so.*.*.*
%{_libdir}/libkspell.la
%attr(755,root,root) %{_libdir}/libkspell.so.*.*.*
%{_libdir}/libkspell2.la
%attr(755,root,root) %{_libdir}/libkspell2.so.*.*.*
%{_libdir}/libktexteditor.la
%attr(755,root,root) %{_libdir}/libktexteditor.so.*.*.*
%{_libdir}/libkutils.la
%attr(755,root,root) %{_libdir}/libkutils.so.*.*.*
%{_libdir}/libkwalletbackend.la
%attr(755,root,root) %{_libdir}/libkwalletbackend.so.*.*.*
%{_libdir}/libkwalletclient.la
%attr(755,root,root) %{_libdir}/libkwalletclient.so.*.*.*
#%{_libdir}/libqt-addon.la
#%attr(755,root,root) %{_libdir}/libqt-addon.so.*.*.*
%{_libdir}/libvcard.la
%attr(755,root,root) %{_libdir}/libvcard.so.*.*.*
%dir %{_libdir}/kde3
%{_libdir}/kde3/cupsdconf.la
%attr(755,root,root) %{_libdir}/kde3/cupsdconf.so
%{_libdir}/kde3/dcopserver.la
%attr(755,root,root) %{_libdir}/kde3/dcopserver.so
%{_libdir}/kde3/kaddprinterwizard.la
%attr(755,root,root) %{_libdir}/kde3/kaddprinterwizard.so
%{_libdir}/kde3/kbuildsycoca.la
%attr(755,root,root) %{_libdir}/kde3/kbuildsycoca.so
%{_libdir}/kde3/kbzip2filter.la
%attr(755,root,root) %{_libdir}/kde3/kbzip2filter.so
%{_libdir}/kde3/kconf_update.la
%attr(755,root,root) %{_libdir}/kde3/kconf_update.so
%{_libdir}/kde3/kcookiejar.la
%attr(755,root,root) %{_libdir}/kde3/kcookiejar.so
%{_libdir}/kde3/kded.la
%attr(755,root,root) %{_libdir}/kde3/kded.so
%{_libdir}/kde3/kded_kcookiejar.la
%attr(755,root,root) %{_libdir}/kde3/kded_kcookiejar.so
%{_libdir}/kde3/kded_kdeprintd.la
%attr(755,root,root) %{_libdir}/kde3/kded_kdeprintd.so
%{_libdir}/kde3/kded_kdetrayproxy.la
%attr(755,root,root) %{_libdir}/kde3/kded_kdetrayproxy.so
%{_libdir}/kde3/kded_kpasswdserver.la
%attr(755,root,root) %{_libdir}/kde3/kded_kpasswdserver.so
%{_libdir}/kde3/kded_kssld.la
%attr(755,root,root) %{_libdir}/kde3/kded_kssld.so
%{_libdir}/kde3/kded_kwalletd.la
%attr(755,root,root) %{_libdir}/kde3/kded_kwalletd.so
%{_libdir}/kde3/kded_proxyscout.la
%attr(755,root,root) %{_libdir}/kde3/kded_proxyscout.so
%{_libdir}/kde3/kdeprint_cups.la
%attr(755,root,root) %{_libdir}/kde3/kdeprint_cups.so
%{_libdir}/kde3/kdeprint_ext.la
%attr(755,root,root) %{_libdir}/kde3/kdeprint_ext.so
%{_libdir}/kde3/kdeprint_lpdunix.la
%attr(755,root,root) %{_libdir}/kde3/kdeprint_lpdunix.so
%{_libdir}/kde3/kdeprint_lpr.la
%attr(755,root,root) %{_libdir}/kde3/kdeprint_lpr.so
%{_libdir}/kde3/kdeprint_rlpr.la
%attr(755,root,root) %{_libdir}/kde3/kdeprint_rlpr.so
%{_libdir}/kde3/kdeprint_tool_escputil.la
%attr(755,root,root) %{_libdir}/kde3/kdeprint_tool_escputil.so
%{_libdir}/kde3/kfileaudiopreview.la
%attr(755,root,root) %{_libdir}/kde3/kfileaudiopreview.so
%{_libdir}/kde3/kgzipfilter.la
%attr(755,root,root) %{_libdir}/kde3/kgzipfilter.so
%{_libdir}/kde3/khtmlimagepart.la
%attr(755,root,root) %{_libdir}/kde3/khtmlimagepart.so
%{_libdir}/kde3/kimg_dds.la
%attr(755,root,root) %{_libdir}/kde3/kimg_dds.so
%{_libdir}/kde3/kimg_eps.la
%attr(755,root,root) %{_libdir}/kde3/kimg_eps.so
%{_libdir}/kde3/kimg_exr.la
%attr(755,root,root) %{_libdir}/kde3/kimg_exr.so
%{_libdir}/kde3/kimg_ico.la
%attr(755,root,root) %{_libdir}/kde3/kimg_ico.so
%{_libdir}/kde3/kimg_jp2.la
%attr(755,root,root) %{_libdir}/kde3/kimg_jp2.so
%{_libdir}/kde3/kimg_pcx.la
%attr(755,root,root) %{_libdir}/kde3/kimg_pcx.so
%{_libdir}/kde3/kimg_rgb.la
%attr(755,root,root) %{_libdir}/kde3/kimg_rgb.so
%{_libdir}/kde3/kimg_tga.la
%attr(755,root,root) %{_libdir}/kde3/kimg_tga.so
%{_libdir}/kde3/kimg_tiff.la
%attr(755,root,root) %{_libdir}/kde3/kimg_tiff.so
%{_libdir}/kde3/kimg_xcf.la
%attr(755,root,root) %{_libdir}/kde3/kimg_xcf.so
%{_libdir}/kde3/kimg_xview.la
%attr(755,root,root) %{_libdir}/kde3/kimg_xview.so
%{_libdir}/kde3/kio_file.la
%attr(755,root,root) %{_libdir}/kde3/kio_file.so
%{_libdir}/kde3/kio_ftp.la
%attr(755,root,root) %{_libdir}/kde3/kio_ftp.so
%{_libdir}/kde3/kio_ghelp.la
%attr(755,root,root) %{_libdir}/kde3/kio_ghelp.so
%{_libdir}/kde3/kio_help.la
%attr(755,root,root) %{_libdir}/kde3/kio_help.so
%{_libdir}/kde3/kio_http.la
%attr(755,root,root) %{_libdir}/kde3/kio_http.so
%{_libdir}/kde3/kio_http_cache_cleaner.la
%attr(755,root,root) %{_libdir}/kde3/kio_http_cache_cleaner.so
%{_libdir}/kde3/kio_metainfo.la
%attr(755,root,root) %{_libdir}/kde3/kio_metainfo.so
%{_libdir}/kde3/kio_uiserver.la
%attr(755,root,root) %{_libdir}/kde3/kio_uiserver.so
%{_libdir}/kde3/kjavaappletviewer.la
%attr(755,root,root) %{_libdir}/kde3/kjavaappletviewer.so
%{_libdir}/kde3/klauncher.la
%attr(755,root,root) %{_libdir}/kde3/klauncher.so
%{_libdir}/kde3/knotify.la
%attr(755,root,root) %{_libdir}/kde3/knotify.so
%{_libdir}/kde3/kspell_aspell.la
%attr(755,root,root) %{_libdir}/kde3/kspell_aspell.so
%{_libdir}/kde3/kspell_ispell.la
%attr(755,root,root) %{_libdir}/kde3/kspell_ispell.so
%{_libdir}/kde3/kstyle_plastik_config.la
%attr(755,root,root) %{_libdir}/kde3/kstyle_plastik_config.so
%{_libdir}/kde3/ktexteditor_autobookmarker.la
%attr(755,root,root) %{_libdir}/kde3/ktexteditor_autobookmarker.so
%{_libdir}/kde3/ktexteditor_docwordcompletion.la
%attr(755,root,root) %{_libdir}/kde3/ktexteditor_docwordcompletion.so
%{_libdir}/kde3/ktexteditor_insertfile.la
%attr(755,root,root) %{_libdir}/kde3/ktexteditor_insertfile.so
%{_libdir}/kde3/ktexteditor_isearch.la
%attr(755,root,root) %{_libdir}/kde3/ktexteditor_isearch.so
%{_libdir}/kde3/ktexteditor_kdatatool.la
%attr(755,root,root) %{_libdir}/kde3/ktexteditor_kdatatool.so
%{_libdir}/kde3/libkatepart.la
%attr(755,root,root) %{_libdir}/kde3/libkatepart.so
%{_libdir}/kde3/libkcertpart.la
%attr(755,root,root) %{_libdir}/kde3/libkcertpart.so
%{_libdir}/kde3/libkdeprint_management_module.la
%attr(755,root,root) %{_libdir}/kde3/libkdeprint_management_module.so
%{_libdir}/kde3/libkhtmlpart.la
%attr(755,root,root) %{_libdir}/kde3/libkhtmlpart.so
%{_libdir}/kde3/libkmultipart.la
%attr(755,root,root) %{_libdir}/kde3/libkmultipart.so
%{_libdir}/kde3/libshellscript.la
%attr(755,root,root) %{_libdir}/kde3/libshellscript.so
%{_libdir}/kde3/wmfthumbnail.la
%attr(755,root,root) %{_libdir}/kde3/wmfthumbnail.so
%dir %{_libdir}/kde3/plugins
%dir %{_libdir}/kde3/plugins/designer
%{_libdir}/kde3/plugins/designer/kdewidgets.la
%attr(755,root,root) %{_libdir}/kde3/plugins/designer/kdewidgets.so
%dir %{_libdir}/kde3/plugins/styles
%{_libdir}/kde3/plugins/styles/highcolor.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/highcolor.so
%{_libdir}/kde3/plugins/styles/keramik.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/keramik.so
%{_libdir}/kde3/plugins/styles/kthemestyle.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/kthemestyle.so
%{_libdir}/kde3/plugins/styles/light.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/light.so
%{_libdir}/kde3/plugins/styles/plastik.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/plastik.so

%dir %{_datadir}/apps
%{_datadir}/apps/LICENSES
%dir %{_datadir}/apps/dcopidlng
%attr(755,root,root) %{_datadir}/apps/dcopidlng/kalyptus
%{_datadir}/apps/dcopidlng/*.pm
%{_datadir}/apps/katepart
%{_datadir}/apps/kcertpart
%{_datadir}/apps/kcm_componentchooser
%dir %{_datadir}/apps/kconf_update
%attr(755,root,root) %{_datadir}/apps/kconf_update/*.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/*.sh
%{_datadir}/apps/kconf_update/*.upd
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
%{_datadir}/locale/all_languages
%{_datadir}/mimelnk
%dir %{_datadir}/services
%dir %{_datadir}/services/kresources
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
%{_datadir}/services/ktexteditor_autobookmarker.desktop
%{_datadir}/services/ktexteditor_docwordcompletion.desktop
%{_datadir}/services/ktexteditor_insertfile.desktop
%{_datadir}/services/ktexteditor_isearch.desktop
%{_datadir}/services/ktexteditor_kdatatool.desktop
%{_datadir}/services/bmp.kimgio
%{_datadir}/services/dds.kimgio
%{_datadir}/services/eps.kimgio
%{_datadir}/services/exr.kimgio
%{_datadir}/services/gif.kimgio
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
%{_datadir}/services/wmfthumbnail.desktop
%{_datadir}/servicetypes
%dir %{_desktopdir}/kde
# contains also 3rdparty hicolor & crystalsvg/apps trees
%{_iconsdir}/crystalsvg
%{_iconsdir}/default.kde
%{_mandir}/man1/checkXML.1*
%{_mandir}/man1/cupsdconf.1*
%{_mandir}/man1/cupsdoprint.1*
%{_mandir}/man1/dcop.1*
%{_mandir}/man1/dcopclient.1*
%{_mandir}/man1/dcopfind.1*
%{_mandir}/man1/dcopobject.1*
%{_mandir}/man1/dcopref.1*
%{_mandir}/man1/dcopserver.1*
%{_mandir}/man1/dcopserver_shutdown.1*
%{_mandir}/man1/dcopstart.1*
%{_mandir}/man1/imagetops.1*
%{_mandir}/man1/kaddprinterwizard.1*
%{_mandir}/man1/kbuildsycoca.1*
%{_mandir}/man1/kconf_update.1*
%{_mandir}/man1/kcookiejar.1*
%{_mandir}/man1/kde-config.1*
%{_mandir}/man1/kded.1*
%{_mandir}/man1/kdeinit.1*
%{_mandir}/man1/kdeinit_shutdown.1*
%{_mandir}/man1/kdeinit_wrapper.1*
%{_mandir}/man1/kdesu_stub.1*
%{_mandir}/man1/kdontchangethehostname.1*
%{_mandir}/man1/kfile.1*
%{_mandir}/man1/kimage_concat.1*
%{_mandir}/man1/kinstalltheme.1*
%{_mandir}/man1/kio_http_cache_cleaner.1*
%{_mandir}/man1/kio_uiserver.1*
%{_mandir}/man1/kioslave.1*
%{_mandir}/man1/klauncher.1*
%{_mandir}/man1/kmailservice.1*
%{_mandir}/man1/kpac_dhcp_helper.1*
%{_mandir}/man1/ksendbugmail.1*
%{_mandir}/man1/kshell.1*
%{_mandir}/man1/ksvgtopng.1*
%{_mandir}/man1/ktelnetservice.1*
%{_mandir}/man1/kwrapper.1*
%{_mandir}/man1/lnusertemp.1*
%{_mandir}/man1/make_driver_db_cups.1*
%{_mandir}/man1/make_driver_db_lpr.1*
%{_mandir}/man1/meinproc.1*
%{_mandir}/man1/preparetips.1*
%dir %{_docdir}/kde
%dir %{_kdedocdir}
%dir %{_kdedocdir}/en
%{_kdedocdir}/en/common
%lang(en) %{_kdedocdir}/en/kspell

# 3rdparty directories
%dir %{_libdir}/kconf_update_bin
%dir %{_datadir}/applnk
%dir %{_datadir}/applnk/.hidden
%dir %{_datadir}/apps/profiles
%dir %{_datadir}/apps/remotes
%dir %{_datadir}/config.kcfg
%dir %{_datadir}/services/kconfiguredialog
%dir %{_datadir}/wallpapers

# merged kabc files
%attr(755,root,root) %{_bindir}/kab2kabc
%{_libdir}/kde3/kabc_dir.la
%attr(755,root,root) %{_libdir}/kde3/kabc_dir.so
%{_libdir}/kde3/kabc_file.la
%attr(755,root,root) %{_libdir}/kde3/kabc_file.so
%{_libdir}/kde3/kabc_ldapkio.la
%attr(755,root,root) %{_libdir}/kde3/kabc_ldapkio.so
%{_libdir}/kde3/kabc_net.la
%attr(755,root,root) %{_libdir}/kde3/kabc_net.so
%{_libdir}/kde3/kabcformat_binary.la
%attr(755,root,root) %{_libdir}/kde3/kabcformat_binary.so
%{_libdir}/kde3/kcm_kresources.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kresources.so
%{_datadir}/apps/kabc
%{_datadir}/autostart/kab2kabc.desktop
%{_datadir}/services/kresources/kabc
%{_desktopdir}/kde/kresources.desktop
%{_mandir}/man1/kab2kabc.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dcopidl
%attr(755,root,root) %{_bindir}/dcopidl2cpp
%attr(755,root,root) %{_bindir}/kconfig_compiler
%attr(755,root,root) %{_libdir}/libDCOP.so
%attr(755,root,root) %{_libdir}/libartskde.so
%attr(755,root,root) %{_libdir}/libkabc.so
%attr(755,root,root) %{_libdir}/libkabc_dir.so
%attr(755,root,root) %{_libdir}/libkabc_file.so
%attr(755,root,root) %{_libdir}/libkabc_ldapkio.so
%attr(755,root,root) %{_libdir}/libkabc_net.so
%attr(755,root,root) %{_libdir}/libkatepartinterfaces.so
%attr(755,root,root) %{_libdir}/libkdecore.so
%attr(755,root,root) %{_libdir}/libkdefakes.so
%attr(755,root,root) %{_libdir}/libkdefx.so
%attr(755,root,root) %{_libdir}/libkdeprint.so
%attr(755,root,root) %{_libdir}/libkdeprint_management.so
%attr(755,root,root) %{_libdir}/libkdesasl.so
%attr(755,root,root) %{_libdir}/libkdesu.so
%attr(755,root,root) %{_libdir}/libkdeui.so
%attr(755,root,root) %{_libdir}/libkhtml.so
%attr(755,root,root) %{_libdir}/libkimproxy.so
%attr(755,root,root) %{_libdir}/libkio.so
%attr(755,root,root) %{_libdir}/libkjava.so
%attr(755,root,root) %{_libdir}/libkjs.so
%attr(755,root,root) %{_libdir}/libkmdi.so
%attr(755,root,root) %{_libdir}/libkmdi2.so
%attr(755,root,root) %{_libdir}/libkmediaplayer.so
%attr(755,root,root) %{_libdir}/libkmid.so
%attr(755,root,root) %{_libdir}/libknewstuff.so
%attr(755,root,root) %{_libdir}/libkntlm.so
%attr(755,root,root) %{_libdir}/libkparts.so
%attr(755,root,root) %{_libdir}/libkresources.so
%attr(755,root,root) %{_libdir}/libkscreensaver.so
%attr(755,root,root) %{_libdir}/libkscript.so
%attr(755,root,root) %{_libdir}/libkspell.so
%attr(755,root,root) %{_libdir}/libkspell2.so
%attr(755,root,root) %{_libdir}/libktexteditor.so
%attr(755,root,root) %{_libdir}/libkutils.so
%attr(755,root,root) %{_libdir}/libkwalletbackend.so
%attr(755,root,root) %{_libdir}/libkwalletclient.so
#%attr(755,root,root) %{_libdir}/libqt-addon.so
%attr(755,root,root) %{_libdir}/libvcard.so
%{_libdir}/libkdefakes_nonpic.a
%{_includedir}/[!a]*
%{_includedir}/arts/*
%{_mandir}/man1/dcopidl.1*
%{_mandir}/man1/dcopidl2cpp.1*

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_kdedocdir}/en/%{name}-apidocs
%endif

%files artsmessage
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artsmessage
%{_mandir}/man1/artsmessage.1*

%files kgrantpty
%defattr(644,root,root,755)
%attr(4755,root,root) %{_bindir}/kgrantpty
