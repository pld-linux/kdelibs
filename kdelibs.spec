# NOTE:	cc1plus takes 136+MB at one time so better prepare a lot of swap
# 	space.
#
# Conditional build:
# _with_nas	- with NAS support
# _without_alsa - disable alsa
# _without_ldap - disable openldap
#

%define		_state		stable
%define		_ver		3.1.3

Summary:	K Desktop Environment - libraries
Summary(es):	K Desktop Environment - bibliotecas
Summary(ko):	KDE - ���̺귯��
Summary(pl):	K Desktop Environment - biblioteki
Summary(pt_BR):	Bibliotecas de funda��o do KDE
Summary(ru):	K Desktop Environment - ����������
Summary(uk):	K Desktop Environment - ��̦�����
Name:		kdelibs
Version:	%{_ver}
Release:	1
Epoch:		8
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	0069e199dd69f27f20afbd5b64449725
#Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Source2:	x-wmv.desktop
Patch0:		%{name}-directories.patch
Patch1:		%{name}-resize-icons.patch
Patch2:         %{name}-kcursor.patch
Patch3:		%{name}-vfolders.patch
Patch4:		%{name}-fonts.patch
Icon:		kdelibs.xpm
URL:		http://www.kde.org/
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
BuildRequires:	esound-devel
BuildRequires:	fam-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
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
# For Netscape plugin support in Konqueror.
BuildRequires:	motif-devel
%{?_with_nas:BuildRequires:	nas-devel}
%{!?_without_ldap:BuildRequires:	openldap-devel}
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	pcre-devel >= 3.5
BuildRequires:	qt-devel >= 3.1-3
BuildRequires: 	sed >= 4.0
BuildRequires:	zlib-devel
Requires:	XFree86-libs >= 4.2.99
Requires:	applnk >= 1.6.2-1
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
Summary(pl):	Nag��wki dla cz�ci aRts wymagaj�ca KDE
Group:		X11/Libraries
Requires:	arts-kde = %{epoch}:%{version}

%description -n arts-kde-devel
Headers for KDE dependent part of aRts.

%description -n arts-kde-devel -l pl
Nag��wki dla z�ci aRts wymagaj�ca KDE.

%package -n arts-message
Summary:	Program which can be used to display aRts daemon messages
Summary(pl):	Program do wy�wietlania komunikat�w daemona aRts
Group:		Development/Tools
Requires:	%{name} >= %{epoch}:%{version}

%description -n arts-message
This program can be given as -m option argument to aRts daemon. It
will be called to display messages generated by daemon.

%description -n arts-message -l pl
Ten program mo�e by� przekazany daemonowi aRts jako parametr opcji -m.
B�dzie on wywo�ywany w celu wy�wietlenia komunikat�w daemona.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
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

for plik in `find ./ -name *.desktop` ; do
	echo $plik
	sed -i -e "s/\[nb\]/\[no\]/g" $plik
done

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
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Settings/KDE,%{_datadir}/apps/khtml/kpartplugins} \
	$RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/{16x16,22x22,32x32,48x48,64x64}/{actions,apps,mimetypes} \
	$RPM_BUILD_ROOT%{_pixmapsdir}/crystalsvg/{16x16,22x22,32x32,48x48,64x64,128x128}/apps

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/mimelnk/video
mv $RPM_BUILD_ROOT%{_applnkdir}/{Settings/[!K]*,Settings/KDE}
rm -rf $RPM_BUILD_ROOT%{_htmldir}/en/kdelibs-apidocs/kspell

# this is provided by openoffice:
rm -f $RPM_BUILD_ROOT%{_datadir}/mimielnk/application/vnd.sun.xml.{calc,impress,writer}

#bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

#find_lang kdelibs --with-kde --all-name > %{name}.lang
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
%{_datadir}/config
# Contains Components/kabc.desktop only
%{_applnkdir}/Settings/KDE
%{_pixmapsdir}/*
%{_datadir}/apps
%{_datadir}/autostart
%{_datadir}/locale/all_languages
%{_datadir}/mimelnk
%{_datadir}/services
%{_datadir}/servicetypes
%dir %{_docdir}/kde
%dir %{_htmldir}
%lang(en) %dir %{_htmldir}/en

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
