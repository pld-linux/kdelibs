# NOTE:	cc1plus takes 136+MB at one time so better prepare a lot of swap
# 	space.
#
# Conditional build:
# _with_ra		- use it if You're building for Ra dist 
# _without_alsa - disable alsa
#

%define		_state		stable
%define		_ver		3.1

Summary:	K Desktop Environment - libraries
Summary(es):	K Desktop Environment - bibliotecas
Summary(ko):	KDE - ¶óÀÌºê·¯¸®
Summary(pl):	K Desktop Environment - biblioteki
Summary(pt_BR):	Bibliotecas de fundação do KDE
Summary(ru):	K Desktop Environment - âÉÂÌÉÏÔÅËÉ
Summary(uk):	K Desktop Environment - â¦ÂÌ¦ÏÔÅËÉ
Name:		kdelibs
Version:	%{_ver}
Release:	9
Epoch:		8
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
#Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Source2:	x-wmv.desktop
Patch0:		%{name}-directories.patch
Patch1:		%{name}-resize-icons.patch
Patch2:         %{name}-kcursor.patch
Patch3:         %{name}-kdefx.patch
Icon:		kdelibs.xpm
# Where is gmcop?!!!
BuildRequires:	XFree86-devel
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
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel >= 2.0
BuildRequires:	libtiff-devel
# For Netscape plugin support in Konqueror.
BuildRequires:	motif-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.9
BuildRequires:	libxslt-devel >= 1.0.7
%if %{?_with_ra:1}0
BuildRequires:	openssl-devel = 0.9.6i
%else
BuildRequires:	openssl-devel >= 0.9.7
%endif
BuildRequires:	pcre-devel >= 3.5
BuildRequires:	qt-devel >= 3.1
BuildRequires:	zlib-devel
BuildRequires:	libxml2-progs
BuildRequires:	libvorbis-devel
BuildRequires:	mad-devel
Requires:	applnk
Requires:	arts >= 1.1-1
Requires:	qt >= 3.1
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
Obsoletes:	kde-i18n-Affrikaans kde-i18n-Arabic kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian kde-i18n-Bosnian kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech kde-i18n-Danish kde-i18n-German kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK kde-i18n-Esperanto kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian kde-i18n-Finnish kde-i18n-French
Obsoletes:	kde-i18n-Hebrew kde-i18n-Croatian kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian kde-i18n-Icelandic kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese kde-i18n-Korean kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian kde-i18n-Maltese kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Nynorsk kde-i18n-Polish kde-i18n-Portugnese
Obsoletes:	kde-i18n-Brazil_Portugnese kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil_Portuguese kde-i18n-Romanian kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak kde-i18n-Slovenian kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish kde-i18n-Tamil kde-i18n-Thai kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian kde-i18n-Venda kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa kde-i18n-Simplified_Chinese kde-i18n-Chinese
Obsoletes:	kde-i18n-Zulu

%define		_htmldir	/usr/share/doc/kde/HTML

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
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

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

CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcflags}"
%configure \
	--%{?debug:en}%{!?debug:dis}able-debug \
	--enable-final \
%ifarch %{ix86}
	--enable-fast-malloc=full \
%endif
	--disable-mysql \
	--disable-informix \
	--enable-mitshm \
	--with%{?_without_alsa:out}-alsa

# Cannot patch configure.in because it does not rebuild correctly on ac25
sed -e 's@#define HAVE_LIBAUDIONAS 1@/* #undef HAVE_LIBAUDIONAS */@' \
	< config.h \
	> config.h.tmp
mv -f config.h{.tmp,}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/mimelnk/video

install -d \
	$RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/{16x16,22x22,32x32,48x48,64x64}/{actions,apps,mimetypes}

mv $RPM_BUILD_ROOT%{_applnkdir}/{Settings/[!K]*,Settings/KDE}

rm -rf $RPM_BUILD_ROOT%{_htmldir}/en/kdelibs-apidocs/kspell

install -d $RPM_BUILD_ROOT%{_datadir}/apps/khtml/kpartplugins

#bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

#%find_lang kdelibs --with-kde --all-name

> %{name}.lang
topics="common kdelibs-apidocs kspell"
for i in $topics; do
	%find_lang $i --with-kde
	cat $i.lang >> %{name}.lang
done

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   -n arts-kde -p /sbin/ldconfig
%postun -n arts-kde -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kdelibs.lang
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
%{_libdir}/libkcertpart.la
%attr(755,root,root) %{_libdir}/libkcertpart.so
%dir %{_libdir}/kde3
%dir %{_libdir}/kde3/plugins
%dir %{_libdir}/kde3/plugins/designer
%dir %{_libdir}/kde3/plugins/styles
%{_libdir}/kde3/*.la
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/plugins/designer/*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/designer/*.so
%{_libdir}/kde3/plugins/styles/*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so

%config %{_datadir}/config
# Contains Components/kabc.desktop only
%{_applnkdir}/Settings/KDE
%{_pixmapsdir}/*
%{_datadir}/apps
%{_datadir}/autostart
%{_datadir}/locale/all_languages
%{_datadir}/mimelnk
%{_datadir}/services
%{_datadir}/servicetypes
%dir /usr/share/doc/kde
%dir %{_htmldir}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dcopidl*
%{_libdir}/lib[!ack]*.so
%{_libdir}/libk[!c]*.so
# All subdirs and headers not starting with 'a'.
%{_includedir}/[!a]*

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
