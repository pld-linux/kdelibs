# NOTE:	cc1plus takes 136+MB at one time so better prepare a lot of swap
#	space.
#
# Conditional build:
%bcond_without	alsa	# build without ALSA support
%bcond_with	i18n	# with i18n stuff - not used in DEVEL branch
#
%define		_state		snapshots
%define		_ver		3.2.90
%define		_snap		040206
%define         artsver         13:1.2.0

Summary:	K Desktop Environment - libraries
Summary(es):	K Desktop Environment - bibliotecas
Summary(ko):	KDE - ¶óÀÌºê·¯¸®
Summary(pl):	K Desktop Environment - biblioteki
Summary(pt_BR):	Bibliotecas de fundação do KDE
Summary(ru):	K Desktop Environment - âÉÂÌÉÏÔÅËÉ
Summary(uk):	K Desktop Environment - â¦ÂÌ¦ÏÔÅËÉ
Name:		kdelibs
Version:	%{_ver}.%{_snap}
Release:	2
Epoch:		9
License:	LGPL
Group:		X11/Libraries
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{name}-%{_ver}.tar.bz2
Source0:	http://ep09.pld-linux.org/~adgor/kde/%{name}-%{_snap}.tar.bz2
##%% Source0-md5:	24be0d558725f4d3441fb9d580129720	
#Source1:	http://ep09.pld-linux.org/~djurban/kde/i18n/kde-i18n-%{name}-%{version}.tar.bz2
##%% Source1-md5: 	1b484133af8a53b761c7bc9fcb6c1814 
Patch0:		%{name}-kstandarddirs.patch
Patch1:		%{name}-defaultfonts.patch
Patch2:		%{name}-use_system_sgml.patch
Icon:		kdelibs.xpm
URL:		http://www.kde.org/
BuildRequires:	XFree86-devel >= 4.2.99
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	arts-qt-devel >= %{artsver}
BuildRequires:	artsc-devel >= %{artsver}
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
BuildRequires:	ed
BuildRequires:	fam-devel
BuildRequires:	gettext-devel
BuildRequires:	jasper-devel >= 1.600
BuildRequires:	libart_lgpl-devel
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
BuildRequires:	openldap-devel
BuildRequires:	openmotif-devel
BuildRequires:	openssl-devel >= 0.9.7c
BuildRequires:	pcre-devel >= 3.5
BuildRequires:	qt-devel >= 6:3.2.1-4
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	xrender-devel
BuildRequires:	zlib-devel
BuildRequires:	libidn-devel
BuildRequires:	unsermake
Requires:	XFree86 >= 4.2.99
Requires:	arts >= %{_artsver}
Requires:	docbook-dtd412-xml
Requires:	docbook-dtd42-xml
Requires:	docbook-style-xsl
Requires:	qt >= 6:3.2.1-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
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
Obsoletes:	kdeedu-kgeo
Obsoletes:	kdegames-megami
Obsoletes:	kdenetwork-kmail
Obsoletes:	kdenetwork-knode
Obsoletes:	kdenetwork-kxmlrpcd
Obsoletes:	kdepim-commonlibs
Obsoletes:	kdepim-kaplan
# More
Obsoletes:	kdepim-kaddressbook < 3:3.1.91.030918-1
Obsoletes:	kdepim-kmail < 3:3.1.91.030918-1
Obsoletes:	kdepim-kontact < 3:3.1.91.030918-1
Obsoletes:	kdepim-korganizer < 3:3.1.91.030918-1
Obsoletes:	kdepim-libkcal < 3:3.1.91.030918-1
Obsoletes:	kdepim-libkdenetwork < 3:3.1.91.030918-1
Obsoletes:	kdepim-libkdepim < 3:3.1.91.030918-1
Conflicts:	pixieplus < 0.3-4

%description
Libraries for the K Desktop Environment.

Included with this package are:
- jscript - KDE javascript library,
- kdecore - KDE core library,
- kdeui - KDE user interface library,
- kfmlib - KDE file manager library,
- khtmlw - KDE HTML widget,
- mediatool - KDE mediatool library.

%description -l es
Bibliotecas para KDE.

%description -l pl
Biblioteki do K Desktop Environment.

Pakiet ten zawiera:
- jscript - biblioteka KDE do javascript,
- kdecore - biblioteka podstawowa,
- kdeui - biblioteka KDE do interfejsu u¿ytkownika,
- kfmlib - biblioteka KDE file manager library,
- khtmlw - biblioteka KDE z HTML widget,
- mediatool - biblioteka KDE mediatool.

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
Requires:	arts-devel >= %{artsver}
Requires:	artsc-devel >= %{artsver}
Requires:	fam-devel
Requires:	libart_lgpl-devel
Requires:	qt-devel >= 6:3.2.1-4
Requires:	xrender-devel
Obsoletes:	arts-kde-devel
Obsoletes:	kdelibs-sound-devel
Obsoletes:	kdelibs2-devel
Obsoletes:	kdelibs2-sound-devel
Obsoletes:	kdelibs-static
Conflicts:	kdebase-devel <= 9:3.1.90

%description devel
This package contains header files and development documentation for
kdelibs.

%description devel -l es
This package includes the header files you will need to compile
applications for KDE. Also included is the KDE API documentation in
HTML format for easy browsing.

%description devel -l pl
Pakiet ten zawiera pliki nag³ówkowe i dokumentacjê potrzebn± przy
pisaniu w³asnych programów wykorzystuj±cych kdelibs.

%description devel -l pt_BR
Este pacote contém os arquivos de inclusão que são necessários para
compilar aplicativos KDE. Contém também a API do KDE documentada no
formato HTML.

%description devel -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÈÅÄÅÒÙ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ËÏÍÐÉÌÑÃÉÉ ÐÒÏÇÒÁÍÍ ÄÌÑ
KDE. ôÁËÖÅ ×ËÌÀÞÅÎÁ ÄÏËÕÍÅÎÔÁÃÉÑ × ÆÏÒÍÁÔÅ HTML.

%description devel -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÈÅÄÅÒÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ËÏÍÐ¦ÌÑÃ¦§ ÐÒÏÇÒÁÍ ÄÌÑ KDE.
ôÁËÏÖ ÄÏ ÎØÏÇÏ ×ÈÏÄÉÔØ ÄÏËÕÍÅÎÔÁÃ¦Ñ Õ ÆÏÒÍÁÔ¦ HTML.

%package artsmessage
Summary:	Program which can be used to display aRts daemon messages
Summary(pl):	Program do wy¶wietlania komunikatów demona aRts
Group:		Development/Tools
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	arts-message

%description artsmessage
This program can be given as -m option argument to aRts daemon. It
will be called to display messages generated by daemon.

%description artsmessage -l pl
Ten program mo¿e byæ przekazany demonowi aRts jako parametr opcji -m.
Bêdzie on wywo³ywany w celu wy¶wietlenia komunikatów demona.

#%package kabc
#Summary:	Adressbook converter
#Summary(pl):	Konwerter ksi±¿ki adresowej
#Group:		X11/Applications
#Requires:	%{name} = %{epoch}:%{version}-%{release}
#Conflicts:	%{name} < 8:3.1.4
#
#%description kabc
#Adressbook can be shared between various applications. This package
#can be used to determine the adressbook location and it can convert
#between diferent adressbook formats.
#
#%description kabc -l pl
#Ksi±¿ka adresowa mo¿e byæ wspó³dzielona przez ró¿ne aplikacje. Ten
#pakiet umo¿liwia okre¶lenie miejsca przechowywania ksi±¿ki adresowej
#oraz jej konwersjê.

%package i18n
Summary:	Internationalization and localization files for kdelibs.
Summary(pl):	Pliki umiêdzynarodawiaj±ce kdelibs.
Requires:       %{name} = %{epoch}:%{version}-%{release}
Group:		X11/Applications
Obsoletes:      kde-i18n-Affrikaans
Obsoletes:      kde-i18n-Afrikaans
Obsoletes:      kde-i18n-Arabic
Obsoletes:      kde-i18n-Azerbaijani
Obsoletes:      kde-i18n-Bulgarian
Obsoletes:      kde-i18n-Bosnian
Obsoletes:      kde-i18n-Catalan
Obsoletes:      kde-i18n-Czech
Obsoletes:      kde-i18n-Danish
Obsoletes:      kde-i18n-German
Obsoletes:      kde-i18n-Greek
Obsoletes:      kde-i18n-English_UK
Obsoletes:      kde-i18n-British
Obsoletes:      kde-i18n-Esperanto
Obsoletes:      kde-i18n-Spanish
Obsoletes:      kde-i18n-Estonian
Obsoletes:      kde-i18n-Finnish
Obsoletes:      kde-i18n-French
Obsoletes:      kde-i18n-Hebrew
Obsoletes:      kde-i18n-Hindi
Obsoletes:      kde-i18n-Croatian
Obsoletes:      kde-i18n-Hungarian
Obsoletes:      kde-i18n-Indonesian
Obsoletes:      kde-i18n-Icelandic
Obsoletes:      kde-i18n-Italian
Obsoletes:      kde-i18n-Japanese
Obsoletes:      kde-i18n-Korean
Obsoletes:      kde-i18n-Lithuanian
Obsoletes:      kde-i18n-Latvian
Obsoletes:      kde-i18n-Maltese
Obsoletes:      kde-i18n-Malay
Obsoletes:      kde-i18n-Mongolian
Obsoletes:      kde-i18n-Dutch
Obsoletes:      kde-i18n-Norwegian
Obsoletes:      kde-i18n-Norwegian_Bokmaal
Obsoletes:      kde-i18n-Norwegian_Bookmal
Obsoletes:      kde-i18n-Norwegian_Nynorsk
Obsoletes:      kde-i18n-Polish
Obsoletes:      kde-i18n-Portugnese
Obsoletes:      kde-i18n-Portuguese
Obsoletes:      kde-i18n-Brazil
Obsoletes:      kde-i18n-Brazil_Portugnese
Obsoletes:      kde-i18n-Brazil_Portuguese
Obsoletes:      kde-i18n-Romanian
Obsoletes:      kde-i18n-Russian
Obsoletes:      kde-i18n-Slovak
Obsoletes:      kde-i18n-Slovenian
Obsoletes:      kde-i18n-Serbian
Obsoletes:      kde-i18n-Swedish
Obsoletes:      kde-i18n-Tamil
Obsoletes:      kde-i18n-Thai
Obsoletes:      kde-i18n-Turkish
Obsoletes:      kde-i18n-Ukrainian
Obsoletes:      kde-i18n-Uzbek
Obsoletes:      kde-i18n-Venda
Obsoletes:      kde-i18n-Vietnamese
Obsoletes:      kde-i18n-Xhosa
Obsoletes:      kde-i18n-Simplified_Chinese
Obsoletes:      kde-i18n-Chinese
Obsoletes:      kde-i18n-Chinese-Big5
Obsoletes:      kde-i18n-Zulu
Obsoletes:      kde-i18n-kdelibs
Obsoletes:      kde-i18n

%description i18n 
Internationalization and localization files for kdelibs.

%description i18n -l pl
Pliki umiêdzynarodawiaj±ce kdelibs.


%prep 
%setup -q -n %{name}-%{_snap}
%patch0 -p1
%patch1 -p1
%patch2 -p1

# unwanted manpages (no binaries)
rm -f debian/{kdb2html.sgml,knotify.sgml,xml2man.sgml}
# typo
%{__perl} -pi -e 's/ksendbugemail/ksendbugmail/;s/KSENDBUGEMAIL/KSENDBUGMAIL/' \
	debian/ksendbugmail.sgml

%build
cp /usr/share/automake/config.sub admin

export UNSERMAKE=/usr/share/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

%configure \
	--%{?debug:en}%{!?debug:dis}able-debug \
	--disable-rpath \
	--with-qt-libraries=%{_libdir} \
%ifarch %{ix86}
	--enable-fast-malloc=full \
%endif
	--enable-mitshm \
	--with%{!?with_alsa:out}-alsa

%{__make}

#%%{__make} apidox

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d \
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
cd debian
for f in *.sgml ; do
	base="$(basename $f .sgml)"
	upper="$(echo ${base} | tr a-z A-Z)"
	db2man $f
	install ${upper}.1 $RPM_BUILD_ROOT%{_mandir}/man1/${base}.1
done

cd -

%if %{with i18n}
bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT
for f in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/*.mo; do
	[ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] && rm -f $f
done

%endif

%find_lang %{name} --with-kde --all-name

files=%{name}

for i in $files; do
echo "%defattr(644,root,root,755)" > ${i}_en.lang
grep en\/ ${i}.lang | grep -Ev '\-apidocs|en\/common' >> ${i}_en.lang
grep -Ev '\-apidocs|en\/' ${i}.lang > ${i}.lang.1
mv ${i}.lang.1 ${i}.lang
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%if %{with i18n}
%files i18n -f %{name}.lang
%endif

%files -f %{name}_en.lang
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
%attr(755,root,root) %{_bindir}/kgrantpty
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
#%{_libdir}/libkabc_ldap.la
#%attr(755,root,root) %{_libdir}/libkabc_ldap.so.*.*.*
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
%{_libdir}/libkio.la
%attr(755,root,root) %{_libdir}/libkio.so.*.*.*
%{_libdir}/libkjava.la
%attr(755,root,root) %{_libdir}/libkjava.so.*.*.*
%{_libdir}/libkjs.la
%attr(755,root,root) %{_libdir}/libkjs.so.*.*.*
%{_libdir}/libkmdi.la
%attr(755,root,root) %{_libdir}/libkmdi.so.*.*.*
%{_libdir}/libkmediaplayer.la
%attr(755,root,root) %{_libdir}/libkmediaplayer.so.*.*.*
%{_libdir}/libkmid.la
%attr(755,root,root) %{_libdir}/libkmid.so.*.*.*
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
%{_libdir}/libktexteditor.la
%attr(755,root,root) %{_libdir}/libktexteditor.so.*.*.*
%{_libdir}/libkutils.la
%attr(755,root,root) %{_libdir}/libkutils.so.*.*.*
%{_libdir}/libkwalletbackend.la
%attr(755,root,root) %{_libdir}/libkwalletbackend.so.*.*.*
%{_libdir}/libkwalletclient.la
%attr(755,root,root) %{_libdir}/libkwalletclient.so.*.*.*
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
%{_libdir}/kde3/kimg_eps.la
%attr(755,root,root) %{_libdir}/kde3/kimg_eps.so
%{_libdir}/kde3/kimg_ico.la
%attr(755,root,root) %{_libdir}/kde3/kimg_ico.so
%{_libdir}/kde3/kimg_jp2.la
%attr(755,root,root) %{_libdir}/kde3/kimg_jp2.so
#%{_libdir}/kde3/kimg_krl.la
#%attr(755,root,root) %{_libdir}/kde3/kimg_krl.so
%{_libdir}/kde3/kimg_pcx.la
%attr(755,root,root) %{_libdir}/kde3/kimg_pcx.so
%{_libdir}/kde3/kimg_tga.la
%attr(755,root,root) %{_libdir}/kde3/kimg_tga.so
%{_libdir}/kde3/kimg_tiff.la
%attr(755,root,root) %{_libdir}/kde3/kimg_tiff.so
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
%{_libdir}/kde3/libkhtmlpart.la
%attr(755,root,root) %{_libdir}/kde3/libkhtmlpart.so
%{_libdir}/kde3/libkmultipart.la
%attr(755,root,root) %{_libdir}/kde3/libkmultipart.so
%{_libdir}/kde3/libshellscript.la
%attr(755,root,root) %{_libdir}/kde3/libshellscript.so
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

%dir %{_datadir}/apps
%{_datadir}/apps/LICENSES
%{_datadir}/apps/dcopidlng
%{_datadir}/apps/katepart
%{_datadir}/apps/kcertpart
%{_datadir}/apps/kcm_componentchooser
%{_datadir}/apps/kconf_update
%{_datadir}/apps/kdeprint
%{_datadir}/apps/kdeui
%{_datadir}/apps/kdewidgets
# also contains 3rdparty kpartplugins dir
%{_datadir}/apps/khtml
%{_datadir}/apps/kio_uiserver
%{_datadir}/apps/kjava
%{_datadir}/apps/knotify
%{_datadir}/apps/ksgmltools2
%{_datadir}/apps/kssl
%{_datadir}/apps/kstyle
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
%{_datadir}/services/ktexteditor_insertfile.desktop
%{_datadir}/services/ktexteditor_isearch.desktop
%{_datadir}/services/ktexteditor_kdatatool.desktop
%{_datadir}/services/bmp.kimgio
%{_datadir}/services/eps.kimgio
%{_datadir}/services/gif.kimgio
%{_datadir}/services/ico.kimgio
%{_datadir}/services/jp2.kimgio
%{_datadir}/services/jpeg.kimgio
#%{_datadir}/services/krl.kimgio
%{_datadir}/services/pbm.kimgio
%{_datadir}/services/pcx.kimgio
%{_datadir}/services/pgm.kimgio
%{_datadir}/services/png.kimgio
%{_datadir}/services/ppm.kimgio
%{_datadir}/services/tga.kimgio
%{_datadir}/services/tiff.kimgio
%{_datadir}/services/xbm.kimgio
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
%{_datadir}/services/rlogin.protocol
%{_datadir}/services/rtsp.protocol
%{_datadir}/services/shellscript.desktop
%{_datadir}/services/telnet.protocol
%{_datadir}/services/webdav.protocol
%{_datadir}/services/webdavs.protocol
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
#%{_libdir}/kde3/kabc_ldap.la
#%attr(755,root,root) %{_libdir}/kde3/kabc_ldap.so
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
%lang(en) %{_kdedocdir}/en/%{name}-%{_snap}-apidocs
%attr(755,root,root) %{_bindir}/dcopidl
%attr(755,root,root) %{_bindir}/dcopidl2cpp
%attr(755,root,root) %{_bindir}/kconfig_compiler
%attr(755,root,root) %{_libdir}/libDCOP.so
%attr(755,root,root) %{_libdir}/libartskde.so
%attr(755,root,root) %{_libdir}/libkabc.so
%attr(755,root,root) %{_libdir}/libkabc_dir.so
%attr(755,root,root) %{_libdir}/libkabc_file.so
#%attr(755,root,root) %{_libdir}/libkabc_ldap.so
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
%attr(755,root,root) %{_libdir}/libkio.so
%attr(755,root,root) %{_libdir}/libkjava.so
%attr(755,root,root) %{_libdir}/libkjs.so
%attr(755,root,root) %{_libdir}/libkmdi.so
%attr(755,root,root) %{_libdir}/libkmediaplayer.so
%attr(755,root,root) %{_libdir}/libkmid.so
%attr(755,root,root) %{_libdir}/libkparts.so
%attr(755,root,root) %{_libdir}/libkresources.so
%attr(755,root,root) %{_libdir}/libkscreensaver.so
%attr(755,root,root) %{_libdir}/libkscript.so
%attr(755,root,root) %{_libdir}/libkspell.so
%attr(755,root,root) %{_libdir}/libktexteditor.so
%attr(755,root,root) %{_libdir}/libkutils.so
%attr(755,root,root) %{_libdir}/libkwalletbackend.so
%attr(755,root,root) %{_libdir}/libkwalletclient.so
%attr(755,root,root) %{_libdir}/libvcard.so
%{_libdir}/libkdefakes_nonpic.a
%{_includedir}/[!a]*
%{_includedir}/arts/*
%{_mandir}/man1/dcopidl.1*
%{_mandir}/man1/dcopidl2cpp.1*
#%%lang(en) %{_docdir}/kde/HTML/en/kde-%{_snap}-apidocs

%files artsmessage
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artsmessage
%{_mandir}/man1/artsmessage.1*

#%files kabc
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kab2kabc
#%{_libdir}/kde3/kabc_dir.la
#%attr(755,root,root) %{_libdir}/kde3/kabc_dir.so
#%{_libdir}/kde3/kabc_file.la
#%attr(755,root,root) %{_libdir}/kde3/kabc_file.so
#%{_libdir}/kde3/kabc_ldap.la
#%attr(755,root,root) %{_libdir}/kde3/kabc_ldap.so
#%{_libdir}/kde3/kabc_ldapkio.la
#%attr(755,root,root) %{_libdir}/kde3/kabc_ldapkio.so
#%{_libdir}/kde3/kabc_net.la
#%attr(755,root,root) %{_libdir}/kde3/kabc_net.so
#%{_libdir}/kde3/kabcformat_binary.la
#%attr(755,root,root) %{_libdir}/kde3/kabcformat_binary.so
#%{_libdir}/kde3/kcm_kresources.la
#%attr(755,root,root) %{_libdir}/kde3/kcm_kresources.so
#%{_datadir}/apps/kabc
#%{_datadir}/autostart/kab2kabc.desktop
#%{_datadir}/services/kresources/kabc
#%{_desktopdir}/kde/kresources.desktop
