# NOTE:	cc1plus takes 136+MB at one time so better prepare a lot of swap
# 	space.
#
# Conditional build:
# _with_pixmapsubdirs - leave different depth/resolution icons
#
%define		_with_pixmapsubdirs	1
Summary:	K Desktop Environment - libraries
Summary(es):	K Desktop Environment - bibliotecas
Summary(ko):	KDE - ∂Û¿Ã∫Í∑Ø∏Æ.
Summary(pl):	K Desktop Environment - biblioteki
Summary(pt_BR):	Bibliotecas de fundaÁ„o do KDE
Summary(ru):	K Desktop Environment - ‚…¬Ã…œ‘≈À…
Summary(uk):	K Desktop Environment - ‚¶¬Ã¶œ‘≈À…
Name:		kdelibs
Version:	3.0.4
Release:	7
Epoch:		7
License:	LGPL
Vendor:		The KDE Team
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Source2:	%{name}-extra_icons.tar.bz2
Patch0:		%{name}-directories.patch
Patch1:		%{name}-libxml_closecallback.patch
Patch2:		%{name}-am.patch
Patch3:		%{name}-resize-icons.patch
Patch4:		%{name}-ksyscoca.patch
Patch5:		%{name}-dtfix.patch
Patch6:		%{name}-lang.patch
Patch7:		%{name}-alignment.patch
Patch8:  	%{name}-katetextbuffermultibyte.patch
Patch9:		%{name}-dock.patch
#The following two are security patches from 3.0.5
Patch10:	%{name}-khtml.patch
Patch11:	%{name}-kio.patch
#End security patches
Icon:		kdelibs.xpm
# If you want gmcop you will need *working* pkgconfig --- there is no such
# thing at the moment (2001-08-15) in known universe.
#Requires:	glib2 >= 1.3.3
BuildRequires:	XFree86-devel
%ifnarch sparc sparc64
BuildRequires:	alsa-lib-devel
%endif
BuildRequires:	arts-devel >= 1.0.0
BuildRequires:	arts-qt >= 1.0.0
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	awk
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
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	pcre-devel >= 3.5
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	zlib-devel
BuildRequires:	libxml2-progs
Requires:	arts >= 1.0.0
Requires:	qt >= 3.0.5
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
Obsoletes:      kde-i18n-Affrikaans kde-i18n-Arabic kde-i18n-Azerbaijani
Obsoletes:      kde-i18n-Bulgarian kde-i18n-Bosnian kde-i18n-Catalan
Obsoletes:      kde-i18n-Czech kde-i18n-Danish kde-i18n-German kde-i18n-Greek
Obsoletes:      kde-i18n-English_UK kde-i18n-Esperanto kde-i18n-Spanish
Obsoletes:      kde-i18n-Estonian kde-i18n-Finnish kde-i18n-French
Obsoletes:      kde-i18n-Hebrew kde-i18n-Croatian kde-i18n-Hungarian
Obsoletes:      kde-i18n-Indonesian kde-i18n-Icelandic kde-i18n-Italian
Obsoletes:      kde-i18n-Japanese kde-i18n-Korean kde-i18n-Lithuanian
Obsoletes:      kde-i18n-Latvian kde-i18n-Maltese kde-i18n-Dutch
Obsoletes:      kde-i18n-Norwegian kde-i18n-Norwegian_Bokmaal
Obsoletes:      kde-i18n-Norwegian_Nynorsk kde-i18n-Polish kde-i18n-Portugnese
Obsoletes:      kde-i18n-Brazil_Portugnese kde-i18n-Romanian kde-i18n-Russian
Obsoletes:      kde-i18n-Slovak kde-i18n-Slovenian kde-i18n-Serbian
Obsoletes:      kde-i18n-Swedish kde-i18n-Tamil kde-i18n-Thai kde-i18n-Turkish
Obsoletes:      kde-i18n-Ukrainian kde-i18n-Venda kde-i18n-Vietnamese
Obsoletes:      kde-i18n-Xhosa kde-i18n-Simplified_Chinese kde-i18n-Chinese
Obsoletes:      kde-i18n-Zulu

%define		_prefix		/usr/X11R6
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
- kdeui - biblioteka KDE do interfejsu uøytkownika,
- kfmlib - biblioteka KDE file manager library,
- khtmlw - biblioteka KDE z HTML widget,
- mediatool - biblioteka KDE mediatool.

%description -l pt_BR
Bibliotecas de fundaÁ„o do KDE requeridas por todo e qualquer
aplicativo KDE.

%description -l ru
‚…¬Ã…œ‘≈À… ƒÃ— K Desktop Environment.

˜ÀÃ¿ﬁ≈ŒŸ ¬…¬Ã…œ‘≈À… KDE:
- jscript (javascript),
- kdecore (—ƒ“œ KDE),
- kdeui (…Œ‘≈“∆≈ ” –œÃÿ⁄œ◊¡‘≈Ã—),
- khtmlw (“¡¬œ‘¡ ” HTML),
- kimgio (œ¬“¡¬œ‘À¡ …⁄œ¬“¡÷≈Œ… ).
- kspell (–“œ◊≈“À¡ œ“∆œ«“¡∆……),

%description -l uk
‚¶¬Ã¶œ‘≈À… ƒÃ— K Desktop Environment.

˜ÀÃ¿ﬁ≈Œ¶ ‘¡À¶ ¬¶¬Ã¶œ‘≈À… KDE:
- jscript (javascript),
- kdecore (—ƒ“œ KDE),
- kdeui (¶Œ‘≈“∆≈ ” Àœ“…”‘’◊¡ﬁ¡),
- khtmlw (“œ¬œ‘¡ ⁄ HTML),
- kimgio (œ¬“œ¬À¡ ⁄œ¬“¡÷≈Œÿ).
- kspell (–≈“≈◊¶“À¡ œ“∆œ«“¡∆¶ß),

%package devel
Summary:	kdelibs - header files and development documentation
Summary(pl):	kdelibs - pliki nag≥Ûwkowe i dokumentacja do kdelibs
Summary(pt_BR):	Arquivos de inclus„o e documentaÁ„o para compilar aplicativos KDE
Summary(ru):	Ë≈ƒ≈“Ÿ … ƒœÀ’Õ≈Œ‘¡√…— ƒÃ— ÀœÕ–…ÃÃ—√…… –“œ«“¡ÕÕ KDE
Summary(uk):	Ë≈ƒ≈“… ‘¡ ƒœÀ’Õ≈Œ‘¡√¶— ƒÃ— ÀœÕ–¶Ã—√¶ß –“œ«“¡Õ KDE
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	arts-devel >= 1.0.0
Requires:	qt-devel >= 3.0.3
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
Pakiet ten zawiera pliki nag≥Ûwkowe i dokumentacjÍ potrzebn± przy
pisaniu w≥asnych programÛw wykorzystuj±cych kdelibs.

%description devel -l pt_BR
Este pacote contÈm os arquivos de inclus„o que s„o necess·rios para
compilar aplicativos KDE. ContÈm tambÈm a API do KDE documentada no
formato HTML.

%description devel -l ru
¸‘œ‘ –¡À≈‘ ”œƒ≈“÷…‘ »≈ƒ≈“Ÿ, Œ≈œ¬»œƒ…ÕŸ≈ ƒÃ— ÀœÕ–…Ã—√…… –“œ«“¡ÕÕ ƒÃ—
KDE. Ù¡À÷≈ ◊ÀÃ¿ﬁ≈Œ¡ ƒœÀ’Õ≈Œ‘¡√…— ◊ ∆œ“Õ¡‘≈ HTML.

%description devel -l uk
„≈  –¡À≈‘ Õ¶”‘…‘ÿ »≈ƒ≈“…, Œ≈œ¬»¶ƒŒ¶ ƒÃ— ÀœÕ–¶Ã—√¶ß –“œ«“¡Õ ƒÃ— KDE.
Ù¡Àœ÷ ƒœ Œÿœ«œ ◊»œƒ…‘ÿ ƒœÀ’Õ≈Œ‘¡√¶— ’ ∆œ“Õ¡‘¶ HTML.

%package -n arts-kde
Summary:	KDE dependent part of aRts
Summary(pl):	CzÍ∂Ê aRts wymagaj±ca KDE
Group:		X11/Libraries
Requires:	%{name} = %{version}

%description -n arts-kde
KDE dependent part of aRts.

%description -n arts-kde -l pl
CzÍ∂Ê aRts wymagaj±ca KDE.

%package -n arts-kde-devel
Summary:	Headers for KDE dependent part of aRts
Summary(pl):	Nag≥Ûwki dla czÍ∂ci aRts wymagaj±ca KDE
Group:		X11/Libraries
Requires:	arts-kde = %{version}

%description -n arts-kde-devel
Headers for KDE dependent part of aRts.

%description -n arts-kde-devel -l pl
Nag≥Ûwki dla zÍ∂ci aRts wymagaj±ca KDE.

%package -n arts-message
Summary:	Program which can be used to display aRts daemon messages
Summary(pl):	Program do wy∂wietlania komunikatÛw daemona aRts
Group:		Development/Tools

%description -n arts-message
This program can be given as -m option argument to aRts daemon. It
will be called to display messages generated by daemon.

%description -n arts-message -l pl
Ten program moøe byÊ przekazany daemonowi aRts jako parametr opcji -m.
BÍdzie on wywo≥ywany w celu wy∂wietlenia komunikatÛw daemona.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
#%patch2 -p0
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
#%{__make} -f Makefile.cvs
CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcflags}"
%configure \
	--%{?debug:en}%{!?debug:dis}able-debug \
	--enable-final \
	--disable-rpath \
%ifarch %{ix86}
	--enable-fast-malloc=full \
%endif
	--disable-mysql \
	--disable-informix \
	--with-alsa \
	--enable-mitshm

# Cannot patch configure.in because it does not rebuild correctly on ac25
sed -e 's@#define HAVE_LIBAUDIONAS 1@/* #undef HAVE_LIBAUDIONAS */@' \
	< config.h \
	> config.h.tmp
mv -f config.h{.tmp,}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}/{hicolor,locolor}/{16x16,22x22,32x32,48x48}/{actions,apps,devices,filesystems,mimetypes}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

# create in toplevel %%{_pixmapsdir} links to icons
for i in $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/48x48/filesystems/{desktop,network,socket}.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/48x48/devices/{cdaudio_unmount,scanner}.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/48x48/mimetypes/{cdtrack,html,image,sound}.png
do
%if %{?_with_pixmapsubdirs:1}%{!?_with_pixmapsubdirs:0}
	ln -sf `echo $i | sed "s:^$RPM_BUILD_ROOT%{_pixmapsdir}/::"` $RPM_BUILD_ROOT%{_pixmapsdir}	
%else
	cp -af $i $RPM_BUILD_ROOT%{_pixmapsdir}
%endif
done

bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_pixmapsdir}

%if %{!?_with_pixmapsubdirs:1}%{?_with_pixmapsubdirs:0}
# moved
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/*color/??x??/*/{cdaudio_unmount,cdtrack,desktop,html,image,network,scanner,socket,sound}.png
# resized
# Note: arts is moved from kdebase, encrypted should be removed only from actions
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/*color/??x??/*/{editcopy,history,launch,spellcheck}.png
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/*color/??x??/actions/encrypted.png
%endif

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

for f in `find $RPM_BUILD_ROOT%{_applnkdir} -name '.directory' -o -name '*.desktop'` ; do
	awk -v F=$f '/^Icon=/ && !/\.xpm$/ && !/\.png$/ { $0 = $0 ".png";} { print $0; } END { if(F == ".directory") print "Type=Directory"; }' < $f > $f.tmp
	mv -f $f{.tmp,}
done

%find_lang kdelibs --with-kde --all-name

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   -n arts-kde -p /sbin/ldconfig
%postun -n arts-kde -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kdelibs.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dcop
%attr(755,root,root) %{_bindir}/dcop[cfors]*
%attr(755,root,root) %{_bindir}/make*
%attr(755,root,root) %{_bindir}/meinproc
%attr(755,root,root) %{_bindir}/[ciklpsx]*
%attr(755,root,root) %{_libdir}/[bdhk]*.??
%attr(755,root,root) %{_libdir}/libc*.??
%attr(755,root,root) %{_libdir}/libk[afhijmpt]*.so.*.*
%attr(755,root,root) %{_libdir}/libk[afhijmpt]*.la
%attr(755,root,root) %{_libdir}/libkcertpart.??
%attr(755,root,root) %{_libdir}/libkscreensaver.la
%attr(755,root,root) %{_libdir}/libkscript.la
%attr(755,root,root) %{_libdir}/libkspell.la
%attr(755,root,root) %{_libdir}/libks[cp]*.so.*.*
%attr(755,root,root) %{_libdir}/libD*.so.*.*
%attr(755,root,root) %{_libdir}/libD*.la
%attr(755,root,root) %{_libdir}/libkatepart.so
%attr(755,root,root) %{_libdir}/libkdecore.so.*.*
%attr(755,root,root) %{_libdir}/libkdecore.la
%attr(755,root,root) %{_libdir}/libkdefakes.so.*.*
%attr(755,root,root) %{_libdir}/libkdefakes.la
%attr(755,root,root) %{_libdir}/libkdefx.la
%attr(755,root,root) %{_libdir}/libkdefx.so.*.*
%attr(755,root,root) %{_libdir}/libkdeprint*.so.*.*
%attr(755,root,root) %{_libdir}/libkdeprint*.la
%attr(755,root,root) %{_libdir}/libkdesasl.so.*.*
%attr(755,root,root) %{_libdir}/libkdesasl.la
%attr(755,root,root) %{_libdir}/libkdesu*.so.*.*
%attr(755,root,root) %{_libdir}/libkdesu*.la
%attr(755,root,root) %{_libdir}/libkdeui.so.*.*
%attr(755,root,root) %{_libdir}/libkdeui.la
%attr(755,root,root) %{_libdir}/libshellscript.la
%attr(755,root,root) %{_libdir}/libshellscript.so.*.*
%attr(755,root,root) %{_libdir}/libvcard.so.*.*
%attr(755,root,root) %{_libdir}/libvcard.la
%attr(755,root,root) %{_libdir}/kde3

%config %{_datadir}/config
%dir %{_pixmapsdir}/hicolor
%dir %{_pixmapsdir}/locolor
%dir %{_pixmapsdir}/*/[1-9]*
%dir %{_pixmapsdir}/*/[1-9]*/*
%{_pixmapsdir}/*/[1-9]*/*/*
%{_pixmapsdir}/*.png
# I'm not sure what this file is for.
%{_pixmapsdir}/hicolor/index.desktop
%{_datadir}/apps
%{_datadir}/autostart
%{_datadir}/mimelnk
%{_datadir}/services
%{_datadir}/servicetypes
%dir /usr/share/doc/kde
%dir %{_htmldir}
%dir %{_htmldir}/en

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dcopidl*
%{_libdir}/libD*.so
%{_libdir}/libkabc.so
%{_libdir}/libkatepartinterfaces.so
%{_libdir}/libk[dfhijmpt]*.so
%{_libdir}/libks[cpsy]*.so
%{_libdir}/libshellscript.so
%{_libdir}/libvcard.so
# All subdirs and headers not starting with 'a'.
%{_includedir}/[!a]*

%files -n arts-kde
%defattr(644,root,root,755)
%{_libdir}/libartskde.la
%{_libdir}/libartskde.so.*.*

%files -n arts-kde-devel
%defattr(644,root,root,755)
%{_includedir}/arts/*
%{_libdir}/libartskde.so

%files -n arts-message
%defattr(644,root,root,755)
%{_bindir}/artsmessage
