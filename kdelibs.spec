# NOTE:	cc1plus takes 136+MB at one time so better prepare a lot of swap space.
#
# Conditional build:
# _without_alsa - without alsa support
# _with_nas	- with NAS support
#

%define		_state		snapshots
%define		_snap		030501
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
Source0:        http://team.pld.org.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
Source2:	x-wmv.desktop
Source3:	%{name}-default_applications.menu
Patch0:		%{name}-directories.patch
Patch1:		%{name}-resize-icons.patch
Patch2:         %{name}-kcursor.patch
Patch3:		%{name}-vmenu_location.patch
#Patch4:		http://rambo.its.tudelft.nl/~ewald/xine/kdelibs-3.1.1-video-20030314.patch
#Patch5:		http://rambo.its.tudelft.nl/~ewald/xine/kdelibs-3.1.1-streaming-20030317.patch
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
# For Netscape plugin support in Konqueror.
BuildRequires:	motif-devel
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
Requires:       %{name} >= %{version}

%description static
KDE static libraries.

%description static -l pl
Statyczne biblioteki KDE. 

%package -n arts-kde
Summary:	KDE dependent part of aRts
Summary(pl):	Czê¶æ aRts wymagaj±ca KDE
Group:		X11/Libraries
Requires:	%{name} >= %{version}

%description -n arts-kde
KDE dependent part of aRts.

%description -n arts-kde -l pl
Czê¶æ aRts wymagaj±ca KDE.

%package -n arts-kde-devel
Summary:	Headers for KDE dependent part of aRts
Summary(pl):	Nag³ówki dla czê¶ci aRts wymagaj±ca KDE
Group:		X11/Libraries
Requires:	arts-kde = %{version}

%description -n arts-kde-devel
Headers for KDE dependent part of aRts.

%description -n arts-kde-devel -l pl
Nag³ówki dla zê¶ci aRts wymagaj±ca KDE.

%package -n arts-message
Summary:	Program which can be used to display aRts daemon messages
Summary(pl):	Program do wy¶wietlania komunikatów daemona aRts
Group:		Development/Tools
Requires:	%{name} >= %{version}

%description -n arts-message
This program can be given as -m option argument to aRts daemon. It
will be called to display messages generated by daemon.

%description -n arts-message -l pl
Ten program mo¿e byæ przekazany daemonowi aRts jako parametr opcji -m.
Bêdzie on wywo³ywany w celu wy¶wietlenia komunikatów daemona.

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

%if %{?_with_nas:0}1
# Cannot patch configure.in because it does not rebuild correctly on ac25
sed -e 's@#define HAVE_LIBAUDIONAS 1@/* #undef HAVE_LIBAUDIONAS */@' \
	< config.h \
	> config.h.tmp
mv -f config.h{.tmp,}
%endif

cd khtml/css 
%{__make} parser
cd ../../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/mimelnk/video

install -d \
	$RPM_BUILD_ROOT%{_datadir}/apps/khtml/kpartplugins \
	$RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/{16x16,22x22,32x32,48x48,64x64}/{actions,apps,mimetypes} \
	$RPM_BUILD_ROOT%{_pixmapsdir}/crystalsvg/{16x16,22x22,32x32,48x48,64x64,128x128}/apps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/[!ad]*
%attr(755,root,root) %{_bindir}/dcop
%attr(755,root,root) %{_bindir}/dcop[!i]*
%{_libdir}/[dk]*.la
%attr(755,root,root) %{_libdir}/[dk]*.so
%{_libdir}/lib[!ack]*.la
%attr(755,root,root) %{_libdir}/lib[!ack]*.so.*
%{_libdir}/libc*.la
%attr(755,root,root) %{_libdir}/libc*.so
%{_libdir}/libk[!c]*.la
%attr(755,root,root) %{_libdir}/libk[!c]*.so.*
%dir %{_libdir}/kde3
%dir %{_libdir}/kde3/plugins
%dir %{_libdir}/kde3/plugins/designer
%dir %{_libdir}/kde3/plugins/styles
%{_libdir}/kde3/*.la
%attr(755,root,root) %{_libdir}/kde3/*.so*
%{_libdir}/kde3/plugins/designer/*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/designer/*.so
%{_libdir}/kde3/plugins/styles/*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_datadir}/apps
%{_datadir}/autostart
%{_datadir}/config
%{_datadir}/locale/all_languages
%{_datadir}/mimelnk
%{_datadir}/services
%{_datadir}/servicetypes
%{_pixmapsdir}/*
%{_docdir}/kde

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dcopidl*
%{_libdir}/lib[!ack]*.so
%{_libdir}/libk[!c]*.so
# All subdirs and headers not starting with 'a'.
%{_includedir}/[!a]*

%files static
%defattr(644,root,root,755)
%{_libdir}/libkdefakes_nonpic.a

%files -n arts-kde
%defattr(644,root,root,755)
%{_libdir}/libartskde.la
%attr(755,root,root) %{_libdir}/libartskde.so.*

%files -n arts-kde-devel
%defattr(644,root,root,755)
%{_includedir}/arts/*
%{_libdir}/libartskde.so

%files -n arts-message
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artsmessage
