# NOTE:	cc1plus takes 136+MB at one time so better prepare a lot of swap space.
#
# Conditional build:
# _without_alsa - without alsa support
# _with_nas	- with NAS support
#

%define		_state		snapshots
%define		_snap		030602
%define		_ver		3.2

Summary:	K Desktop Environment - libraries
Summary(es):	K Desktop Environment - bibliotecas
Summary(ko):	KDE - ¶óÀÌºê·¯¸®
Summary(pl):	K Desktop Environment - biblioteki
Summary(pt_BR):	Bibliotecas de fundação do KDE
Summary(ru):	K Desktop Environment - âÉÂÌÉÏÔÅËÉ
Summary(uk):	K Desktop Environment - â¦ÂÌ¦ÏÔÅËÉ
Name:		kdelibs
Version:	%{_ver}
Release:	0.%{_snap}.1
Epoch:		8
License:	LGPL
Group:		X11/Libraries
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{name}-%{_snap}.tar.bz2
# Source0-md5:	42d33b73b2753bb71d96993945309163
Source0:        http://team.pld.org.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
Patch0:		%{name}-directories.patch
Patch1:		%{name}-resize-icons.patch
Patch2:         %{name}-kcursor.patch
Patch3:         %{name}-defaultfonts.patch
#Patch4:	http://rambo.its.tudelft.nl/~ewald/xine/kdelibs-3.1.1-video-20030314.patch
#Patch5:	http://rambo.its.tudelft.nl/~ewald/xine/kdelibs-3.1.1-streaming-20030317.patch
Icon:		kdelibs.xpm
# Where is gmcop?!!!
BuildRequires:	XFree86-devel >= 4.2.99
%ifnarch sparc sparc64
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
%endif
BuildRequires:	arts-devel >= 1.1-1
BuildRequires:	arts-qt >= 1.1-1
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	cups-devel
BuildRequires:	gettext-devel
BuildRequires:	jasper-devel >= 1.600
BuildRequires:	libart_lgpl-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel >= 2.0
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel >= 2.4.9
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel >= 1.0.7
BuildRequires:	mad-devel
BuildRequires:	openldap-devel
# For Netscape plugin support in Konqueror.
BuildRequires:	openmotif-devel
#
%{?_with_nas:BuildRequires:	nas-devel}
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	pcre-devel >= 3.5
BuildRequires:	qt-devel >= 3.2-0.030428.1
BuildRequires:	zlib-devel
Requires:	XFree86 >= 4.2.99
Requires:	arts >= 1.2
Requires:	qt >= 3.1-3
URL:		http://www.kde.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	kdelibs2
Obsoletes:	kdelibs2-sound
Obsoletes:	kdelibs-sound
Obsoletes:	kdesupport
Obsoletes:	kdesupport-devel
Obsoletes:	kdesupport-static
Obsoletes:	kdesupport-mimelib
Obsoletes:	kdesupport-mimelib-devel
Obsoletes:	kdesupport-mimelib-static

%define		_htmldir	%{_docdir}/kde/HTML

%define		no_install_post_chrpath		1

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
Requires:	%{name} = %{version}
Requires:	arts-devel >= 1.1-1
Requires:	qt-devel >= 3.1
Obsoletes:	kdelibs-sound-devel
Obsoletes:	kdelibs2-devel
Obsoletes:	kdelibs2-sound-devel
Obsoletes:	kdebase-devel <= 3.1.1-0.5.1

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


%package static
Summary:        KDE static libraries
Summary(pl):    Statyczne biblioteki KDE
Group:          X11/Libraries
Requires:       %{name} >= %{version}-%{release}

%description static
KDE static libraries.

%description static -l pl
Statyczne biblioteki KDE.

%package -n arts-kde
Summary:	KDE dependent part of aRts
Summary(pl):	Czê¶æ aRts wymagaj±ca KDE
Group:		X11/Libraries
Requires:	%{name} >= %{version}-%{release}

%description -n arts-kde
KDE dependent part of aRts.

%description -n arts-kde -l pl
Czê¶æ aRts wymagaj±ca KDE.

%package -n arts-kde-devel
Summary:	Headers for KDE dependent part of aRts
Summary(pl):	Nag³ówki dla czê¶ci aRts wymagaj±ca KDE
Group:		X11/Libraries
Requires:	arts-kde = %{version}-%{release}

%description -n arts-kde-devel
Headers for KDE dependent part of aRts.

%description -n arts-kde-devel -l pl
Nag³ówki dla zê¶ci aRts wymagaj±ca KDE.

%package -n arts-message
Summary:	Program which can be used to display aRts daemon messages
Summary(pl):	Program do wy¶wietlania komunikatów daemona aRts
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description -n arts-message
This program can be given as -m option argument to aRts daemon. It
will be called to display messages generated by daemon.

%description -n arts-message -l pl
Ten program mo¿e byæ przekazany daemonowi aRts jako parametr opcji -m.
Bêdzie on wywo³ywany w celu wy¶wietlenia komunikatów daemona.

%package kabc
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Applications
Requires:	kdebase-core
Requires:	%{name} = %{version}-%{release}

%description kabc
TODO.

%description kabc
TODO.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
#%patch4 -p1
#%patch5 -p1

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

cd kdecore
> plddirs.h
echo "#define kde_appsdir \"%{_applnkdir}\"" >> plddirs.h
echo "#define kde_htmldir \"%{_htmldir}\"" >> plddirs.h
echo "#define kde_icondir \"%{_pixmapsdir}\"" >> plddirs.h
cd -

for plik in `find ./ -name *.desktop` ; do
	echo $plik
	sed -i -e "s/\[nb\]/\[no\]/g" $plik
done

%configure \
	--%{?debug:en}%{!?debug:dis}able-debug \
%ifarch %{ix86}
	--enable-fast-malloc=full \
%endif
	--enable-mitshm \
	--with%{?_without_alsa:out}-alsa

%if %{!?_with_nas:1}0
# Cannot patch configure.in because it does not rebuild correctly on ac25
sed -e 's@#define HAVE_LIBAUDIONAS 1@/* #undef HAVE_LIBAUDIONAS */@' \
	< config.h \
	> config.h.tmp
mv -f config.h{.tmp,}
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d \
	$RPM_BUILD_ROOT%{_datadir}/apps/khtml/kpartplugins \
	$RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/{16x16,22x22,32x32,48x48,64x64}/{actions,apps,mimetypes} \
	$RPM_BUILD_ROOT%{_pixmapsdir}/crystalsvg/{16x16,22x22,32x32,48x48,64x64,128x128}/apps

mv $RPM_BUILD_ROOT%{_applnkdir}/{Settings,KDE-Settings}

%clean
rm -rf $RPM_BUILD_ROOT

%post			-p /sbin/ldconfig
%postun			-p /sbin/ldconfig

%post	-n arts-kde	-p /sbin/ldconfig
%postun	-n arts-kde	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/checkXML
%attr(755,root,root) %{_bindir}/cupsdconf
%attr(755,root,root) %{_bindir}/cupsdoprint
%attr(755,root,root) %{_bindir}/dcop
%attr(755,root,root) %{_bindir}/dcopclient
%attr(755,root,root) %{_bindir}/dcopfind
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
%attr(755,root,root) %{_bindir}/kdb2html
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
%attr(755,root,root) %{_bindir}/kioslave
%attr(755,root,root) %{_bindir}/klauncher
%attr(755,root,root) %{_bindir}/kmailservice
%attr(755,root,root) %{_bindir}/knotify
%attr(755,root,root) %{_bindir}/kpac_dhcp_helper
%attr(755,root,root) %{_bindir}/ksendbugmail
%attr(755,root,root) %{_bindir}/kshell
%attr(755,root,root) %{_bindir}/ksvgtopng
%attr(755,root,root) %{_bindir}/ktelnetservice
%attr(755,root,root) %{_bindir}/kwrapper
%attr(755,root,root) %{_bindir}/lnusertemp
%attr(755,root,root) %{_bindir}/make_driver_db_cups
%attr(755,root,root) %{_bindir}/make_driver_db_lpr
%attr(755,root,root) %{_bindir}/meinproc
%attr(755,root,root) %{_bindir}/preparetips
%attr(755,root,root) %{_bindir}/xml2man
%{_libdir}/dcopserver.la
%attr(755,root,root) %{_libdir}/dcopserver.so
%{_libdir}/kaddprinterwizard.la
%attr(755,root,root) %{_libdir}/kaddprinterwizard.so
%{_libdir}/kbuildsycoca.la
%attr(755,root,root) %{_libdir}/kbuildsycoca.so
%{_libdir}/kconf_update.la
%attr(755,root,root) %{_libdir}/kconf_update.so
%{_libdir}/kcookiejar.la
%attr(755,root,root) %{_libdir}/kcookiejar.so
%{_libdir}/kded.la
%attr(755,root,root) %{_libdir}/kded.so
%{_libdir}/kio_http_cache_cleaner.la
%attr(755,root,root) %{_libdir}/kio_http_cache_cleaner.so
%{_libdir}/kio_uiserver.la
%attr(755,root,root) %{_libdir}/kio_uiserver.so
%{_libdir}/klauncher.la
%attr(755,root,root) %{_libdir}/klauncher.so
%{_libdir}/knotify.la
%attr(755,root,root) %{_libdir}/knotify.so
%{_libdir}/libDCOP.la
%attr(755,root,root) %{_libdir}/libDCOP.so.*.*.*
%{_libdir}/libcupsdconf.la
%attr(755,root,root) %{_libdir}/libcupsdconf.so
%{_libdir}/libkabc.la
%attr(755,root,root) %{_libdir}/libkabc.so.*.*.*
%{_libdir}/libkatepartinterfaces.la
%attr(755,root,root) %{_libdir}/libkatepartinterfaces.so.*.*.*
%{_libdir}/libkdecore.la
%attr(755,root,root) %{_libdir}/libkdecore.so.*.*.*
%{_libdir}/libkdefakes.la
%attr(755,root,root) %{_libdir}/libkdefakes.so.*.*.*
%{_libdir}/libkdefx.la
%attr(755,root,root) %{_libdir}/libkdefx.so.*.*.*
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
%{_libdir}/libshellscript.la
%attr(755,root,root) %{_libdir}/libshellscript.so.*.*.*
%{_libdir}/libvcard.la
%attr(755,root,root) %{_libdir}/libvcard.so.*.*.*
%dir %{_libdir}/kde3
%{_libdir}/kde3/kbzip2filter.la
%attr(755,root,root) %{_libdir}/kde3/kbzip2filter.so
%{_libdir}/kde3/kded_kcookiejar.la
%attr(755,root,root) %{_libdir}/kde3/kded_kcookiejar.so
%{_libdir}/kde3/kded_kdeprintd.la
%attr(755,root,root) %{_libdir}/kde3/kded_kdeprintd.so
%{_libdir}/kde3/kded_kpasswdserver.la
%attr(755,root,root) %{_libdir}/kde3/kded_kpasswdserver.so
%{_libdir}/kde3/kded_kssld.la
%attr(755,root,root) %{_libdir}/kde3/kded_kssld.so
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
%{_libdir}/kde3/kimg_krl.la
%attr(755,root,root) %{_libdir}/kde3/kimg_krl.so
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
%{_libdir}/kde3/kio_metainfo.la
%attr(755,root,root) %{_libdir}/kde3/kio_metainfo.so
%{_libdir}/kde3/kjavaappletviewer.la
%attr(755,root,root) %{_libdir}/kde3/kjavaappletviewer.so
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
%{_libdir}/kde3/libkmultipart.la
%attr(755,root,root) %{_libdir}/kde3/libkmultipart.so
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
%{_datadir}/apps/katepart
%{_datadir}/apps/kcertpart
%{_datadir}/apps/kcm_componentchooser
%{_datadir}/apps/kconf_update
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
%{_datadir}/services/krl.kimgio
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
%{_datadir}/services/rlogin.protocol
%{_datadir}/services/rtsp.protocol
%{_datadir}/services/shellscript.desktop
%{_datadir}/services/telnet.protocol
%{_datadir}/services/webdav.protocol
%{_datadir}/services/webdavs.protocol
%{_datadir}/servicetypes
%{_pixmapsdir}/*
%dir %{_docdir}/kde
%dir %{_htmldir}
%lang(en) %dir %{_htmldir}/en
%lang(en) %{_htmldir}/en/common
%lang(en) %dir %{_htmldir}/en/kdelibs-apidocs
%lang(en) %{_htmldir}/en/kdelibs-apidocs/common
%lang(en) %{_htmldir}/en/kdelibs-apidocs/dcop
%lang(en) %{_htmldir}/en/kdelibs-apidocs/interfaces
%lang(en) %{_htmldir}/en/kdelibs-apidocs/kdecore
%lang(en) %{_htmldir}/en/kdelibs-apidocs/kdefx
%lang(en) %{_htmldir}/en/kdelibs-apidocs/kdeui
%lang(en) %{_htmldir}/en/kdelibs-apidocs/khtml
%lang(en) %{_htmldir}/en/kdelibs-apidocs/kio
%lang(en) %{_htmldir}/en/kdelibs-apidocs/kjs
%lang(en) %{_htmldir}/en/kdelibs-apidocs/kparts
%lang(en) %{_htmldir}/en/kdelibs-apidocs/kutils
%lang(en) %{_htmldir}/en/kdelibs-apidocs/libkmid
%lang(en) %{_htmldir}/en/kspell

%files devel
%attr(755,root,root) %{_bindir}/dcopidl
%attr(755,root,root) %{_bindir}/dcopidl2cpp
%attr(755,root,root) %{_bindir}/kde-config
%{_includedir}/[!a]*
%{_libdir}/libDCOP.so
%{_libdir}/libkabc.so
%{_libdir}/libkatepartinterfaces.so
%{_libdir}/libkdecore.so
%{_libdir}/libkdefakes.so
%{_libdir}/libkdefx.so
%{_libdir}/libkdeprint.so
%{_libdir}/libkdeprint_management.so
%{_libdir}/libkdesasl.so
%{_libdir}/libkdesu.so
%{_libdir}/libkdeui.so
%{_libdir}/libkhtml.so
%{_libdir}/libkio.so
%{_libdir}/libkjava.so
%{_libdir}/libkjs.so
%{_libdir}/libkmdi.so
%{_libdir}/libkmediaplayer.so
%{_libdir}/libkmid.so
%{_libdir}/libkparts.so
%{_libdir}/libkresources.so
%{_libdir}/libkscreensaver.so
%{_libdir}/libkscript.so
%{_libdir}/libkspell.so
%{_libdir}/libktexteditor.so
%{_libdir}/libkutils.so
%{_libdir}/libshellscript.so
%{_libdir}/libvcard.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libkdefakes_nonpic.a

%files -n arts-kde
%defattr(644,root,root,755)
%{_libdir}/libartskde.la
%attr(755,root,root) %{_libdir}/libartskde.so.*.*.*

%files -n arts-kde-devel
%defattr(644,root,root,755)
%{_includedir}/arts/*
%{_libdir}/libartskde.so

%files -n arts-message
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artsmessage

%files kabc
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kab2kabc
%{_libdir}/kde3/kabc_dir.la
%attr(0755,root,root) %{_libdir}/kde3/kabc_dir.so
%{_libdir}/kde3/kabc_file.la
%attr(0755,root,root) %{_libdir}/kde3/kabc_file.so
%{_libdir}/kde3/kabc_ldap.la
%attr(0755,root,root) %{_libdir}/kde3/kabc_ldap.so
%{_libdir}/kde3/kabc_net.la
%attr(0755,root,root) %{_libdir}/kde3/kabc_net.so
%{_libdir}/kde3/kabcformat_binary.la
%attr(0755,root,root) %{_libdir}/kde3/kabcformat_binary.so
%{_libdir}/kde3/kabcformat_vcard2.la
%attr(0755,root,root) %{_libdir}/kde3/kabcformat_vcard2.so
%{_libdir}/kde3/kcm_kresources.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_kresources.so
%{_datadir}/apps/kabc
%{_datadir}/autostart/kab2kabc.desktop
%{_datadir}/services/kresources/kabc
%{_applnkdir}/KDE-Settings/Components/kresources.desktop
#%lang(en) %{_htmldir}/en/kdelibs-apidocs/kabc
