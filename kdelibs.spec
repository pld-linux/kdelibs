# NOTE:	cc1plus takes 136+MB at one time so better prepare a lot of swap
# 	space.
Summary:	K Desktop Environment - Libraries
Summary(es):	K Desktop Environment - bibliotecas
Summary(pl):	K Desktop Environment - biblioteki
Summary(pt_BR):	Bibliotecas de fundaÁ„o do KDE
Name:		kdelibs
Version:	2.2.1
Release:	4
Epoch:		6
License:	LGPL
Vendor:		The KDE Team
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/‚…¬Ã…œ‘≈À…
Group(uk):	X11/‚¶¬Ã¶œ‘≈À…
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
Patch0:		%{name}-final.patch
Patch1:		%{name}-nodebug.patch
Patch2:		%{name}-directories.patch
Patch3:		%{name}-klauncher-escape.patch
Patch4:		%{name}-libxml_closecallback.patch
Patch5:		%{name}-libxml_includes.patch
Icon:		kdelibs.xpm
# If you want gmcop you will need *working* pkgconfig --- there is no such
# thing at the moment (2001-08-15) in known universe.
#Requires:	glib2 >= 1.3.3
BuildRequires:	XFree86-devel
%ifnarch sparc sparc64 ppc
BuildRequires:	alsa-lib-devel
%endif
BuildRequires:	audiofile-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel >= 2.0
BuildRequires:	libtiff-devel
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	qt-devel >= 2.3.0
BuildRequires:	gettext-devel
BuildRequires:	zlib-devel
# For Netscape plugin support in Konqueror.
BuildRequires:	motif-devel
BuildRequires:	openssl-devel
BuildRequires:	bzip2-devel
BuildRequires:	libxml2-devel
BuildRequires:	pcre-devel
#BuildRequires:	glib2-devel >= 1.3.3
BuildRequires:	cups-devel
Requires:	qt >= 2.2.4
Requires:	arts = %{version}
%requires_eq	openssl
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
Obsoletes:      kdesupport-mimelib-static

%define         _prefix         /usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML

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
- kdecore - Biblioteka podstawowa,
- KDE kdeui - Biblioteka KDE do interfejsu uøytkownika,
- kfmlib - Biblioteka KDE file manager library,
- khtmlw: Biblioteka KDE z HTML widget,
- mediatool: Biblioteka KDE mediatool.

%description -l pt_BR
Bibliotecas de fundaÁ„o do KDE requeridas por todo e qualquer
aplicativo KDE.

%package devel
Summary:	kdelibs - header files and development documentation
Summary(es):	Header files and documentation for compiling KDE applications
Summary(pl):	kdelibs - pliki nagÛwkowe i dokumentacja do kdelibs
Summary(pt_BR):	Arquivos de inclus„o e documentaÁ„o para compilar aplicativos KDE
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}
Requires:	arts-devel = %{version}
Requires:	qt-devel >= 2.3.0
Obsoletes:	kdelibs-sound-devel
Obsoletes:	kdelibs2-devel
Obsoletes:	kdelibs2-sound-devel

%description devel
This package contains header files and development documentation for
kdelibs.

%description -l es devel
This package includes the header files you will need to compile
applications for KDE. Also included is the KDE API documentation in
HTML format for easy browsing.

%description -l pl devel
Pakiet ten zawiera pliki nag≥Ûwkowe i dokumentacjÍ potrzebn± przy
pisaniu w≥asnych programÛw wykorzystuj±cych kdelibs.

%description -l pt_BR devel
Este pacote contÈm os arquivos de inclus„o que s„o necess·rios para
compilar aplicativos KDE. ContÈm tambÈm a API do KDE documentada no
formato HTML.

%package -n arts
Summary:	aRts sound server
Summary(es):	Sound server used by KDE
Summary(pl):	serwer dºwiÍku
Summary(pt_BR):	Servidor de sons usado pelo KDE
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…

%description -n arts
aRts sound server.

%description -l pl -n arts
Serwer dºwiÍku aRts.

%description -l es -n arts
Sound server and analog analyzer/synthetizer used by KDE.

%description -l pt_BR -n arts
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
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/‚…¬Ã…œ‘≈À…
Group(uk):	X11/‚¶¬Ã¶œ‘≈À…

%description -n arts-X11
X11 dependent part of aRts

%description -n arts-X11
CzÍ∂Ê aRts wymagaj±ca X11

%package -n arts-qt
Summary:	QT dependend part of aRts
Summary(pl):	CzÍ∂Ê aRts wymagaj±ca QT
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/‚…¬Ã…œ‘≈À…
Group(uk):	X11/‚¶¬Ã¶œ‘≈À…

%description -n arts-qt
QT dependend part of aRts

%description -l pl -n arts-qt
CzÍ∂Ê aRts wymagaj±ca QT

%package -n arts-devel
Summary:	sound server - header files
Summary(es):	Header files for compiling aRtsd applications
Summary(pl):	serwer dºwiÍku - pliki nag≥Ûwkowe
Summary(pt_BR):	Arquivos para desenvolvimento com o o aRts
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…

%description -n arts-devel
Header files required to compile programs using arts.

%description -l es -n arts-devel
This package includes the header files you will need to compile
applications for aRtsd.

%description -l pl -n arts-devel
Pliki nag≥Ûwkowe niezbÍdne do budowania aplikacji korzystaj±cych z
arts.

%description -l pt_BR -n arts-devel
Arquivos para desenvolvimento com o o aRts

%package -n arts-message
Summary:	program which can be used to display aRts daemon messages
Summary(pl):	program, do wy∂wietlania komunikatÛw daemona aRts
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/NarzÍdzia

%description -n arts-message
This program can be given as -m option argument to aRts daemon. It
will be called to display messages generated by daemon.

%description -l pl -n arts-message
Ten program moøe byÊ przekazany daemonowi aRts jako parametr opcji -m.
BÍdzie on wywo≥ywany w celu wy∂wietlenia komunikatÛw daemona.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

# Somebody please do this The Right Way (tm)...
cp -p /usr/bin/libtool .

CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcflags}" 
%configure2_13 \
	%{?debug:--enable-debug} \
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

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip arts/doc/{README,NEWS,TODO}

%find_lang %{name} --with-kde --all-name

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   -n arts -p /sbin/ldconfig
%postun -n arts -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kdelibs.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dcop
%attr(755,root,root) %{_bindir}/dcopserver
%attr(755,root,root) %{_bindir}/make*
%attr(755,root,root) %{_bindir}/mein*
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
%attr(755,root,root) %{_libdir}/libksycoca.so.*.*.*
%attr(755,root,root) %{_libdir}/libksycoca.la
%attr(755,root,root) %{_libdir}/mega.so
%attr(755,root,root) %{_libdir}/mega.la
%attr(755,root,root) %{_libdir}/webstyle.so
%attr(755,root,root) %{_libdir}/webstyle.la
%attr(755,root,root) %{_libdir}/kde2
%attr(755,root,root) %dir %{_libdir}/mcop

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
%dir /usr/share/doc/kde
%dir %{_htmldir}
%lang(en) %dir %{_htmldir}/en

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dcopidl*
%{_libdir}/libD*.so
%{_libdir}/libk[dfijpt]*.so
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
%{_libdir}/mcop/*

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
