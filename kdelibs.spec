# NOTE:	cc1plus takes 136+MB at one time so better prepare a lot of swap
# 	space.
Summary:	K Desktop Environment - libraries
Summary(es):	K Desktop Environment - bibliotecas
Summary(pl):	K Desktop Environment - biblioteki
Summary(pt_BR):	Bibliotecas de fundaÁ„o do KDE
Summary(ru):	K Desktop Environment - ‚…¬Ã…œ‘≈À…
Summary(uk):	K Desktop Environment - ‚¶¬Ã¶œ‘≈À…
Name:		kdelibs
Version:	2.2.2
Release:	8
Epoch:		6
License:	LGPL
Vendor:		The KDE Team
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
Patch0:		%{name}-final.patch
Patch1:		%{name}-nodebug.patch
Patch2:		%{name}-directories.patch
Patch3:		%{name}-klauncher-escape.patch
Patch4:		%{name}-libxml_closecallback.patch
Patch5:		%{name}-cookieperms.patch
Patch6:		%{name}-qt_docdir.patch
Patch7:		%{name}-selectedicons.patch
Patch8:		%{name}-ktoolbarbutton-fix-enable-disable-text.patch
Patch9:		%{name}-kstddirs-symlinks.patch
Patch10:	%{name}-kssl-wrongwarnings.patch
Patch11:	%{name}-kicondialog.cpp.patch
Patch12:	%{name}-kdeprint-PPD-O-Matic.patch
Patch13:	%{name}-fix-cups-config-dialogbox-use-kintvalidator.patch
Patch14:	%{name}-fix-cupsdconf.patch
Patch15:	%{name}-fix-file-dialogbox-dont-add-separator-in-bookmaks-when-bookmarks-is-empty.patch
Patch16:	%{name}-fix-filter-dlg.patch
Patch17:	%{name}-fix-kdeprint-preview-button.patch
Patch18:	%{name}-fix-kintvalidator.patch
Patch19:	%{name}-fix-kjs-mem-leak.patch
Patch20:	%{name}-fix-special-printer.patch
Patch21:	%{name}-fix-popupmenu-image.patch
Patch22:	%{name}-disable-ok-button-in-properties-dialogbox-when-filename-is-empty.patch
Patch23:	%{name}-artswrapper-priority_fix.patch
Icon:		kdelibs.xpm
# If you want gmcop you will need *working* pkgconfig --- there is no such
# thing at the moment (2001-08-15) in known universe.
#Requires:	glib2 >= 1.3.3
BuildRequires:	XFree86-devel
%ifnarch sparc sparc64
BuildRequires:	alsa-lib-devel
%endif
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
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	pcre-devel >= 3.5
BuildRequires:	qt-devel >= 2.3.0
BuildRequires:	zlib-devel
Requires:	arts = %{version}
Requires:	qt >= 2.2.4
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

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML

%description
Libraries for the K Desktop Environment.

KDE Libraries included:
- kdecore (KDE core library),
- kdeui (user interface),
- khtml (HTML widget),
- kfile (file access),
- kspell (spelling checker),
- kssl (secure web browsing),
- kab (addressbook),
- kimgio (image manipulation),
- arts (sound, mixing and animation),
- kstyles, kparts, kjs (JavaScript),
- kio, kdesu and ksgmltools.

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
- kab (¡ƒ“≈”Œ¡— ÀŒ…«¡),
- kdecore (—ƒ“œ KDE),
- kdeui (…Œ‘≈“∆≈ ” –œÃÿ⁄œ◊¡‘≈Ã—),
- kfile (ƒœ”‘’– À ∆¡ Ã¡Õ),
- kfm (∆¡ Ãœ◊Ÿ  Õ≈Œ≈ƒ÷≈“),
- khtmlw (“¡¬œ‘¡ ” HTML),
- kimgio (œ¬“¡¬œ‘À¡ …⁄œ¬“¡÷≈Œ… ).
- kspell (–“œ◊≈“À¡ œ“∆œ«“¡∆……),

%description -l uk
‚¶¬Ã¶œ‘≈À… ƒÃ— K Desktop Environment.

˜ÀÃ¿ﬁ≈Œ¶ ‘¡À¶ ¬¶¬Ã¶œ‘≈À… KDE:
- jscript (javascript),
- kab (¡ƒ“≈”Œ¡ ÀŒ…«¡),
- kdecore (—ƒ“œ KDE),
- kdeui (¶Œ‘≈“∆≈ ” Àœ“…”‘’◊¡ﬁ¡),
- kfile (ƒœ”‘’– ƒœ ∆¡ Ã¶◊),
- kfm (∆¡ Ãœ◊…  Õ≈Œ≈ƒ÷≈“),
- khtmlw (“œ¬œ‘¡ ⁄ HTML),
- kimgio (œ¬“œ¬À¡ ⁄œ¬“¡÷≈Œÿ).
- kspell (–≈“≈◊¶“À¡ œ“∆œ«“¡∆¶ß),

%package devel
Summary:	kdelibs - header files and development documentation
Summary(es):	Header files and documentation for compiling KDE applications
Summary(pl):	kdelibs - pliki nag≥Ûwkowe i dokumentacja do kdelibs
Summary(pt_BR):	Arquivos de inclus„o e documentaÁ„o para compilar aplicativos KDE
Summary(ru):	Ë≈ƒ≈“Ÿ … ƒœÀ’Õ≈Œ‘¡√…— ƒÃ— ÀœÕ–…ÃÃ—√…… –“œ«“¡ÕÕ KDE
Summary(uk):	Ë≈ƒ≈“… ‘¡ ƒœÀ’Õ≈Œ‘¡√¶— ƒÃ— ÀœÕ–¶Ã—√¶ß –“œ«“¡Õ KDE
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	arts-devel = %{version}
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	qt-devel >= 2.3.0
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

%package -n arts
Summary:	aRts sound server
Summary(es):	Sound server used by KDE
Summary(pl):	Serwer dºwiÍku
Summary(pt_BR):	Servidor de sons usado pelo KDE
Group:		Libraries

%description -n arts
aRts sound server.

%description -n arts -l es
Sound server and analog analyzer/synthetizer used by KDE.

%description -n arts -l pl
Serwer dºwiÍku aRts.

%description -n arts -l pt_BR
O aRts È um sintetizador analÛgico em tempo real que È completamente
modular. VocÍ pode criar sons e m˙sicas (sÌntese em tempo real de
midi) usando pequenos mÛdulos como oscilador para criar waveforms,
v·rios filtros, mixers, faders, etc. VocÍ pode configurar tudo atravÈs
de uma interface no KDE. O Servidor aRts È controlado via CORBA. Este
design foi escolhido para permitir que outras aplicaÁıes usem o aRts
como um sintetizador (ou fornecedor de filtros). Usado pelo KDE, entre
outros.

%package -n arts-X11
Summary:	X11 dependent part of aRts
Summary(pl):	CzÍ∂Ê aRts wymagaj±ca X11
Group:		X11/Libraries

%description -n arts-X11
X11 dependent part of aRts.

%description -n arts-X11 -l pl
CzÍ∂Ê aRts wymagaj±ca X11.

%package -n arts-qt
Summary:	QT dependend part of aRts
Summary(pl):	CzÍ∂Ê aRts wymagaj±ca QT
Group:		X11/Libraries

%description -n arts-qt
QT dependend part of aRts.

%description -n arts-qt -l pl
CzÍ∂Ê aRts wymagaj±ca QT.

%package -n arts-devel
Summary:	Sound server - header files
Summary(es):	Header files for compiling aRtsd applications
Summary(pl):	Serwer dºwiÍku - pliki nag≥Ûwkowe
Summary(pt_BR):	Arquivos para desenvolvimento com o o aRts
Group:		Development/Libraries

%description -n arts-devel
Header files required to compile programs using arts.

%description -n arts-devel -l es
This package includes the header files you will need to compile
applications for aRtsd.

%description -n arts-devel -l pl
Pliki nag≥Ûwkowe niezbÍdne do budowania aplikacji korzystaj±cych z
arts.

%description -n arts-devel -l pt_BR
Arquivos para desenvolvimento com o o aRts.

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
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%{__make} -f Makefile.cvs

CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcflags}"
%configure \
	--%{?debug:en}%{!?debug:dis}able-debug \
	--enable-final \
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
install -d $RPM_BUILD_ROOT%{_datadir}/templates/.source

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip arts/doc/{README,NEWS,TODO}

%find_lang %{name} --with-kde --all-name

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post -n arts -p /sbin/ldconfig
%postun -n arts -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kdelibs.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dcop
%attr(755,root,root) %{_bindir}/dcopserver
%attr(755,root,root) %{_bindir}/make*
%attr(755,root,root) %{_bindir}/meinproc
%attr(755,root,root) %{_bindir}/[cilkpsx]*
%attr(755,root,root) %{_libdir}/[bdhk]*.??
%attr(755,root,root) %{_libdir}/libc*.??
%attr(755,root,root) %{_libdir}/libartskde.so
%attr(755,root,root) %{_libdir}/libk[afhjpt]*.so.*.*
%attr(755,root,root) %{_libdir}/libk[afjpt]*.la
%attr(755,root,root) %{_libdir}/libkdeprint*.so.*.*
%attr(755,root,root) %{_libdir}/libkdeprint*.la
%attr(755,root,root) %{_libdir}/libkhtml.la
%attr(755,root,root) %{_libdir}/libkscreensaver.la
%attr(755,root,root) %{_libdir}/libkspell.la
%attr(755,root,root) %{_libdir}/libkmid.so.*.*
%attr(755,root,root) %{_libdir}/libkmid.la
%attr(755,root,root) %{_libdir}/libkhtmli*.??
%attr(755,root,root) %{_libdir}/libks[!ys]*.so.*.*.*
%attr(755,root,root) %{_libdir}/libD*.so.*.*
%attr(755,root,root) %{_libdir}/libD*.la
%attr(755,root,root) %{_libdir}/libkdefakes.so.*.*
%attr(755,root,root) %{_libdir}/libkdefakes.la
%attr(755,root,root) %{_libdir}/libkdecore.so.*.*
%attr(755,root,root) %{_libdir}/libkdecore.la
%attr(755,root,root) %{_libdir}/libkdeui.so.*.*
%attr(755,root,root) %{_libdir}/libkdeui.la
%attr(755,root,root) %{_libdir}/libkdesu*.so.*.*
%attr(755,root,root) %{_libdir}/libkdesu*.la
%attr(755,root,root) %{_libdir}/libkio.la
%attr(755,root,root) %{_libdir}/libkio.so.*.*.*
%attr(755,root,root) %{_libdir}/libkssl.so.*.*.*
%attr(755,root,root) %{_libdir}/libkssl.la
%attr(755,root,root) %{_libdir}/libkded_kssld.la
%attr(755,root,root) %{_libdir}/libkded_kssld.so
%attr(755,root,root) %{_libdir}/libksycoca.so.*.*.*
%attr(755,root,root) %{_libdir}/libksycoca.la
%attr(755,root,root) %{_libdir}/mega.so
%attr(755,root,root) %{_libdir}/mega.la
%attr(755,root,root) %{_libdir}/webstyle.so
%attr(755,root,root) %{_libdir}/webstyle.la
%attr(755,root,root) %{_libdir}/kde2

%config %{_datadir}/config
%dir %{_pixmapsdir}/hicolor
%dir %{_pixmapsdir}/locolor
%dir %{_pixmapsdir}/*/[1-9]*
%dir %{_pixmapsdir}/*/[1-9]*/*
%{_pixmapsdir}/*/[1-9]*/*/*
# I'm not sure what this file is for.
%{_pixmapsdir}/hicolor/index.desktop
%{_datadir}/apps
%{_datadir}/mimelnk
%{_datadir}/services
%{_datadir}/servicetypes
%{_datadir}/templates
%dir /usr/share/doc/kde
%dir %{_htmldir}
%lang(en) %dir %{_htmldir}/en

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dcopidl*
%{_libdir}/libD*.so
%{_libdir}/libk[fijpt]*.so
%{_libdir}/libkde[!d]*.so
%{_libdir}/libks[cpsy]*.so
%{_libdir}/libkhtml.so
%{_libdir}/libkmid.so
%{_libdir}/libkab.so
# All subdirs and headers not starting with 'a'.
%{_includedir}/[!a]*
%{_includedir}/addressbook.h

%files -n arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artscat
%attr(755,root,root) %{_bindir}/artsd
%attr(755,root,root) %{_bindir}/artsdsp
%attr(755,root,root) %{_bindir}/artsplay
%attr(755,root,root) %{_bindir}/artsshell
%attr(755,root,root) %{_bindir}/artswrapper
%attr(755,root,root) %{_libdir}/lib[ams]*.so.*.*
%attr(755,root,root) %{_libdir}/lib[ams]*.la
%attr(755,root,root) %{_libdir}/libkmedia*.so.*.*
%attr(755,root,root) %{_libdir}/libkmedia*.la
%{_libdir}/mcop

%files -n arts-X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libx11globalcomm.so.*.*.*
%attr(755,root,root) %{_libdir}/libx11globalcomm.la

%files -n arts-qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqtmcop.so.*.*.*
%attr(755,root,root) %{_libdir}/libqtmcop.la

%files -n arts-devel
%defattr(644,root,root,755)
%doc arts/doc/*.gz
%attr(755,root,root) %{_bindir}/artsc-config
%attr(755,root,root) %{_bindir}/mcopidl
%{_libdir}/lib[mqsx]*.so
%{_libdir}/libarts[!k]*.so
%{_libdir}/libkmedia*.so
%{_includedir}/arts
%{_includedir}/artsc

%files -n arts-message
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artsmessage
