# NOTE:	cc1plus takes 136+MB at one time so better prepare a lot of swap
# 	space.
#
# Conditional build:
# _with_nas	- with NAS support
# _without_alsa - disable alsa
# _without_ldap - disable openldap
#

%define		_state		stable
%define		_ver		3.1.4

Summary:	K Desktop Environment - libraries
Summary(es):	K Desktop Environment - bibliotecas
Summary(ko):	KDE - ���̺귯��
Summary(pl):	K Desktop Environment - biblioteki
Summary(pt_BR):	Bibliotecas de funda��o do KDE
Summary(ru):	K Desktop Environment - ����������
Summary(uk):	K Desktop Environment - ��̦�����
Name:		kdelibs
Version:	%{_ver}
Release:	0.91
Epoch:		8
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	82c265de78d53c7060a09c5cb1a78942
Source1:	ftp://blysk.ds.pg.gda.pl/linux/kde-i18n-package/%{version}/kde-i18n-%{name}-%{version}.tar.bz2
# Source1-md5:	96a06b72e19e48f1c43dabe8147556ba
Source2:	%{name}-extra_icons.tar.bz2
# Source2-md5:	13e68a0ac0e9724c9b4a74e6bc729087
Source3:	x-wmv.desktop
Patch0:		%{name}-directories.patch
Patch1:		%{name}-resize-icons.patch
Patch2:		%{name}-kcursor.patch
#Patch3:		%{name}-vfolders.patch
Patch4:		%{name}-fonts.patch
Icon:		kdelibs.xpm
URL:		http://www.kde.org/
# Where is gmcop?!!!
BuildRequires:	XFree86-devel
%ifnarch sparc sparc64
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
%endif
BuildRequires:	arts-devel >= 1.1-1
BuildRequires:	arts-qt >= 1.1-1
BuildRequires:	audiofile-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
BuildRequires:	bzip2-devel
BuildRequires:	cups-devel
BuildRequires:	ed
BuildRequires:	esound-devel
BuildRequires:	fam-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	libart_lgpl-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel >= 2.0
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:1.5-2
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel >= 2.4.9
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel >= 1.0.7
BuildRequires:	mad-devel
# For Netscape plugin support in Konqueror.
BuildRequires:	motif-devel
%{?_with_nas:BuildRequires:	nas-devel}
%{!?_without_ldap:BuildRequires:	openldap-devel}
BuildRequires:	openssl-devel >= 0.9.6k
BuildRequires:	pcre-devel >= 3.5
BuildRequires:	qt-devel >= 3.1-3
BuildRequires:	zlib-devel
Requires:	XFree86-libs
Requires:	applnk
Requires:	arts >= 1.1-1
Requires:	qt >= 3.1-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	kde-theme-keramik
Obsoletes:	kdelibs2
Obsoletes:	kdelibs2-sound
Obsoletes:	kdelibs-sound
Obsoletes:	kdesupport
Obsoletes:	kdesupport-devel
Obsoletes:	kdesupport-static
Obsoletes:	kdesupport-mimelib
Obsoletes:	kdesupport-mimelib-devel
Obsoletes:	kdesupport-mimelib-static
Conflicts:	pixieplus < 0.3-4

%define		_prefix		/usr/X11R6
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
- kdeui - biblioteka KDE do interfejsu u�ytkownika,
- kfmlib - biblioteka KDE file manager library,
- khtmlw - biblioteka KDE z HTML widget,
- mediatool - biblioteka KDE mediatool.

%description -l pt_BR
Bibliotecas de funda��o do KDE requeridas por todo e qualquer
aplicativo KDE.

%description -l ru
���������� ��� K Desktop Environment.

�������� ���������� KDE:
- jscript (javascript),
- kdecore (���� KDE),
- kdeui (��������� ������������),
- khtmlw (������ � HTML),
- kimgio (��������� �����������).
- kspell (�������� ����������),

%description -l uk
��̦����� ��� K Desktop Environment.

������Φ ��˦ ¦�̦����� KDE:
- jscript (javascript),
- kdecore (���� KDE),
- kdeui (��������� �����������),
- khtmlw (������ � HTML),
- kimgio (������� ���������).
- kspell (����צ��� �������Ʀ�),

%package devel
Summary:	kdelibs - header files and development documentation
Summary(pl):	kdelibs - pliki nag��wkowe i dokumentacja do kdelibs
Summary(pt_BR):	Arquivos de inclus�o e documenta��o para compilar aplicativos KDE
Summary(ru):	������ � ������������ ��� ����������� �������� KDE
Summary(uk):	������ �� ���������æ� ��� ���Ц��æ� ������� KDE
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}
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
Pakiet ten zawiera pliki nag��wkowe i dokumentacj� potrzebn� przy
pisaniu w�asnych program�w wykorzystuj�cych kdelibs.

%description devel -l pt_BR
Este pacote cont�m os arquivos de inclus�o que s�o necess�rios para
compilar aplicativos KDE. Cont�m tamb�m a API do KDE documentada no
formato HTML.

%description devel -l ru
���� ����� �������� ������, ����������� ��� ���������� �������� ���
KDE. ����� �������� ������������ � ������� HTML.

%description devel -l uk
��� ����� ͦ����� ������, ����Ȧ�Φ ��� ���Ц��æ� ������� ��� KDE.
����� �� ����� ������� ���������æ� � �����Ԧ HTML.

%package -n arts-kde
Summary:	KDE dependent part of aRts
Summary(pl):	Cz�� aRts wymagaj�ca KDE
Group:		X11/Libraries
Requires:	%{name} >= %{epoch}:%{version}

%description -n arts-kde
KDE dependent part of aRts.

%description -n arts-kde -l pl
Cz�� aRts wymagaj�ca KDE.

%package -n arts-kde-devel
Summary:	Headers for KDE dependent part of aRts
Summary(pl):	Nag��wki dla cz�ci aRts wymagaj�cej KDE
Group:		X11/Libraries
Requires:	arts-kde = %{epoch}:%{version}
Requires:	%{name}-devel = %{epoch}:%{version}
%{!?_without_alsa:Requires:	alsa-lib-devel}
Requires:	audiofile-devel
Requires:	fam-devel
Requires:	libart_lgpl-devel
Requires:	mad-devel
Requires:	libvorbis-devel

%description -n arts-kde-devel
Headers for KDE dependent part of aRts.

%description -n arts-kde-devel -l pl
Nag��wki dla cz�ci aRts wymagaj�cej KDE.

%package -n arts-message
Summary:	Program which can be used to display aRts daemon messages
Summary(pl):	Program do wy�wietlania komunikat�w demona aRts
Group:		Development/Tools
Requires:	%{name} >= %{epoch}:%{version}

%description -n arts-message
This program can be given as -m option argument to aRts daemon. It
will be called to display messages generated by daemon.

%description -n arts-message -l pl
Ten program mo�e by� przekazany demonowi aRts jako parametr opcji -m.
B�dzie on wywo�ywany w celu wy�wietlenia komunikat�w demona.

%package kabc
Summary:	Adressbook converter
Summary(pl):	Konwerter ksi��ki adresowej
Group:		X11/Applications
Requires:	kdebase-core = 8:%{version}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	%{name} < 8:3.1.4

%description kabc
Adressbook can be shared between various applications. This package
can be used to determine the adressbook location and it can convert
between diferent adressbook formats.

%description kabc -l pl
Ksi��ka adresowa mo�e by� wsp�dzielona przez r�ne aplikacje. Ten
pakiet umo�liwia okre�lenie miejsca przechowywania ksi��ki adresowej
oraz jej konwersj�.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
#%%patch3 -p1
%patch4 -p1

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

for plik in `find ./ -name *.desktop | grep -l '\[nb\]'` ; do
	echo $plik
	echo -e ',s/\[nb\]/[no]/\n,w' | ed $plik
done

%{__libtoolize}
%{__make} -f admin/Makefile.common cvs

%configure \
	--%{?debug:en}%{!?debug:dis}able-debug \
	--disable-informix \
	--disable-mysql \
%ifarch %{ix86}
	--enable-fast-malloc=full \
%endif
	--enable-final \
	--enable-mitshm \
	%{?_without_ldap:--without-ldap} \
	%{!?_without_ldap:--with-ldap} \
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
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Settings/KDE/System,%{_datadir}/apps/khtml/kpartplugins} \
	$RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/{16x16,22x22,32x32,48x48,64x64}/{actions,apps,mimetypes} \
	$RPM_BUILD_ROOT%{_pixmapsdir}/crystalsvg/{16x16,22x22,32x32,48x48,64x64,128x128}/apps

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/mimelnk/video
mv $RPM_BUILD_ROOT%{_applnkdir}/{Settings/[!K]*,Settings/KDE}
rm -rf $RPM_BUILD_ROOT%{_htmldir}/en/kdelibs-apidocs/kspell

echo -e "Accessibility\nComponents\nDesktop\nInformation\nLookNFeel\n"\
"Network\nPeripherals\nPersonalization\nPowerControl\nSecurity\nSound\n"\
"System\nWebBrowsing" > $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE/.order

cat > $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE/.directory << EOF
[Desktop Entry]
Name=KDE
Icon=kcontrol
X-KDE-BaseGroup=settings
EOF

# these are provided by openoffice:
rm -f $RPM_BUILD_ROOT%{_datadir}/mimielnk/application/vnd.sun.xml.{calc,impress,writer}

bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_pixmapsdir}
for i in {actions/misc,devices/{cdaudio_unmount,mouse,scanner}}.png \
	 filesystems/{desktop,folder_home,network,socket}.png; do
	ln -s crystalsvg/48x48/$i $RPM_BUILD_ROOT%{_pixmapsdir}/`basename $i`
done

for i in `find $RPM_BUILD_ROOT%{_applnkdir} -type f`; do
	if grep '^Icon=.[^.]*$' $i >/dev/null; then
		echo -e ',s/\(^Icon=.*$\)/\\1.png/\n,w' | ed $i
	fi
done

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT
for f in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/*.mo; do
	[ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] && rm -f $f
done

#%find_lang kdelibs --with-kde --all-name > %{name}.lang

%find_lang	kabc_dir		--with-kde
%find_lang	kabc_ldap		--with-kde
%find_lang	kabcformat_binary	--with-kde
cat kabc{_dir,_ldap,format_binary}.lang > kabc.lang

# do not compile
#%find_lang	kabc_net		--with-kde
#%find_lang	kabc_sql		--with-kde

topics="common cupsdconf desktop_kde-i18n katepart kdelibs-apidocs kmcop \
	knotify kspell ktexteditor_insertfile ktexteditor_isearch \
	ktexteditor_kdatatool libkscreensaver ppdtranslations timezones"
%find_lang	kdelibs			--with-kde
for i in $topics; do
	%find_lang $i --with-kde
	cat $i.lang >> kdelibs.lang
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n arts-kde -p /sbin/ldconfig
%postun	-n arts-kde -p /sbin/ldconfig

%files -f kdelibs.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/[!adk]*
%attr(755,root,root) %{_bindir}/dcop
%attr(755,root,root) %{_bindir}/dcop[!i]*
%attr(755,root,root) %{_bindir}/k[!a]*
%attr(755,root,root) %{_bindir}/ka[!b]*
# shared libraries
%attr(755,root,root) %{_libdir}/libDCOP.so.*.*.*
%attr(755,root,root) %{_libdir}/libkatepartinterfaces.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdecore.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdefakes.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdefx.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdeprint.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdeprint_management.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdesasl.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdesu.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdeui.so.*.*.*
%attr(755,root,root) %{_libdir}/libkjava.so.*.*.*
%attr(755,root,root) %{_libdir}/libkio.so.*.*.*
%attr(755,root,root) %{_libdir}/libkjs.so.*.*.*
%attr(755,root,root) %{_libdir}/libkmediaplayer.so.*.*.*
%attr(755,root,root) %{_libdir}/libkmid.so.*.*.*
%attr(755,root,root) %{_libdir}/libkparts.so.*.*.*
%attr(755,root,root) %{_libdir}/libkscreensaver.so.*.*.*
%attr(755,root,root) %{_libdir}/libkscript.so.*.*.*
%attr(755,root,root) %{_libdir}/libkspell.so.*.*.*
%attr(755,root,root) %{_libdir}/libktexteditor.so.*.*.*
%attr(755,root,root) %{_libdir}/libkutils.so.*.*.*
%attr(755,root,root) %{_libdir}/libshellscript.so.*.*.*
%attr(755,root,root) %{_libdir}/libvcard.so.*.*.*
# shared, possibly (lt_)dlopened libraries (.la possibly needed here)
%attr(755,root,root) %{_libdir}/libkabc.so.*.*.*
%{_libdir}/libkabc.la
%attr(755,root,root) %{_libdir}/libkhtml.so.*.*.*
%{_libdir}/libkhtml.la
# actual KDE-style binaries, but ugh, possibly (lt_)dlopened (.la should be here)
%attr(755,root,root) %{_libdir}/dcopserver.so
%{_libdir}/dcopserver.la
%attr(755,root,root) %{_libdir}/kaddprinterwizard.so
%{_libdir}/kaddprinterwizard.la
%attr(755,root,root) %{_libdir}/kbuildsycoca.so
%{_libdir}/kbuildsycoca.la
%attr(755,root,root) %{_libdir}/kconf_update.so
%{_libdir}/kconf_update.la
%attr(755,root,root) %{_libdir}/kcookiejar.so
%{_libdir}/kcookiejar.la
%attr(755,root,root) %{_libdir}/kded.so
%{_libdir}/kded.la
%attr(755,root,root) %{_libdir}/kio_http_cache_cleaner.so
%{_libdir}/kio_http_cache_cleaner.la
%attr(755,root,root) %{_libdir}/kio_uiserver.so
%{_libdir}/kio_uiserver.la
%attr(755,root,root) %{_libdir}/klauncher.so
%{_libdir}/klauncher.la
%attr(755,root,root) %{_libdir}/knotify.so
%{_libdir}/knotify.la
# plugins (possibly lt_dlopened - .la needed here)
%attr(755,root,root) %{_libdir}/libcupsdconf.so
%{_libdir}/libcupsdconf.la
%attr(755,root,root) %{_libdir}/libkcertpart.so
%{_libdir}/libkcertpart.la
%dir %{_libdir}/kde3
%attr(755,root,root) %{_libdir}/kde3/[!k]*.so
%attr(755,root,root) %{_libdir}/kde3/k[!ac]*.so
%{_libdir}/kde3/[!k]*.la
%{_libdir}/kde3/k[!ac]*.la
%dir %{_libdir}/kde3/plugins
%dir %{_libdir}/kde3/plugins/designer
%attr(755,root,root) %{_libdir}/kde3/plugins/designer/*.so
%{_libdir}/kde3/plugins/designer/*.la
%dir %{_libdir}/kde3/plugins/styles
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_libdir}/kde3/plugins/styles/*.la

%{_datadir}/config
%{_pixmapsdir}/*
%dir %{_datadir}/apps
%{_datadir}/apps/[!k]*
%{_datadir}/apps/k[!a]*
%{_datadir}/apps/ka[!b]*
%dir %{_datadir}/autostart
%{_datadir}/locale/all_languages
%{_datadir}/mimelnk
%{_datadir}/services
%{_datadir}/servicetypes
%dir %{_applnkdir}/Settings/KDE
%dir %{_applnkdir}/Settings/KDE/.directory
%dir %{_applnkdir}/Settings/KDE/.order
%dir %{_applnkdir}/Settings/KDE/System
%dir %{_docdir}/kde
%dir %{_htmldir}
# this should not be %%lang: other language resources refer to it
%dir %{_htmldir}/en

%files kabc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kab2kabc
%{_libdir}/kde3/kabc_dir.la
%attr(755,root,root) %{_libdir}/kde3/kabc_dir.so
%{_libdir}/kde3/kabc_ldap.la
%attr(755,root,root) %{_libdir}/kde3/kabc_ldap.so
%{_libdir}/kde3/kabcformat_binary.la
%attr(755,root,root) %{_libdir}/kde3/kabcformat_binary.so
%{_libdir}/kde3/kcm_kabc.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kabc.so
%{_datadir}/apps/kabc
%{_datadir}/autostart/kab2kabc.desktop
%{_applnkdir}/Settings/KDE/Components/kabc.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dcopidl*
# shared libraries - .la here
%attr(755,root,root) %{_libdir}/libDCOP.so
%{_libdir}/libDCOP.la
%attr(755,root,root) %{_libdir}/libkatepartinterfaces.so
%{_libdir}/libkatepartinterfaces.la
%attr(755,root,root) %{_libdir}/libkdecore.so
%{_libdir}/libkdecore.la
%attr(755,root,root) %{_libdir}/libkdefakes.so
%{_libdir}/libkdefakes.la
%attr(755,root,root) %{_libdir}/libkdefx.so
%{_libdir}/libkdefx.la
%attr(755,root,root) %{_libdir}/libkdeprint.so
%{_libdir}/libkdeprint.la
%attr(755,root,root) %{_libdir}/libkdeprint_management.so
%{_libdir}/libkdeprint_management.la
%attr(755,root,root) %{_libdir}/libkdesasl.so
%{_libdir}/libkdesasl.la
%attr(755,root,root) %{_libdir}/libkdesu.so
%{_libdir}/libkdesu.la
%attr(755,root,root) %{_libdir}/libkdeui.so
%{_libdir}/libkdeui.la
%attr(755,root,root) %{_libdir}/libkjava.so
%{_libdir}/libkjava.la
%attr(755,root,root) %{_libdir}/libkio.so
%{_libdir}/libkio.la
%attr(755,root,root) %{_libdir}/libkjs.so
%{_libdir}/libkjs.la
%attr(755,root,root) %{_libdir}/libkmediaplayer.so
%{_libdir}/libkmediaplayer.la
%attr(755,root,root) %{_libdir}/libkmid.so
%{_libdir}/libkmid.la
%attr(755,root,root) %{_libdir}/libkparts.so
%{_libdir}/libkparts.la
%attr(755,root,root) %{_libdir}/libkscreensaver.so
%{_libdir}/libkscreensaver.la
%attr(755,root,root) %{_libdir}/libkscript.so
%{_libdir}/libkscript.la
%attr(755,root,root) %{_libdir}/libkspell.so
%{_libdir}/libkspell.la
%attr(755,root,root) %{_libdir}/libktexteditor.so
%{_libdir}/libktexteditor.la
%attr(755,root,root) %{_libdir}/libkutils.so
%{_libdir}/libkutils.la
%attr(755,root,root) %{_libdir}/libshellscript.so
%{_libdir}/libshellscript.la
%attr(755,root,root) %{_libdir}/libvcard.so
%{_libdir}/libvcard.la
# shared, possibly (lt_)dlopened libraries - .la in main package
%attr(755,root,root) %{_libdir}/libkabc.so
%attr(755,root,root) %{_libdir}/libkhtml.so
# All subdirs and headers not starting with 'a'.
%{_includedir}/[!a]*

%files -n arts-kde
%defattr(644,root,root,755)
# shared library
%attr(755,root,root) %{_libdir}/libartskde.so.*.*.*

%files -n arts-kde-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libartskde.so
%{_libdir}/libartskde.la
%{_includedir}/arts/*

%files -n arts-message
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artsmessage
