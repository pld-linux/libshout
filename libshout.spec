#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	libshout - icecast source streaming library
Summary(pl.UTF-8):	Biblioteka źródeł strumieni icecast
Name:		libshout
Version:	2.4.3
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://downloads.xiph.org/releases/libshout/%{name}-%{version}.tar.gz
# Source0-md5:	2623ebf5bdf00517d2a7fd17d70c31aa
URL:		http://www.icecast.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libogg-devel
BuildRequires:	libtheora-devel
BuildRequires:	libvorbis-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	speex-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libshout is a library for communicating with and sending data to an
icecast server. It handles the socket connection, the timing of the
data, and prevents most bad data from getting to the icecast server.

%description -l pl.UTF-8
libshout to biblioteka do komunikowania się z i wysyłania danych do
serwera icecast. Obsługuje połączenia, czasy danych i zapobiega
dotarciu większości złych danych do serwera icecast.

%package devel
Summary:	Icecast source streaming library development package
Summary(pl.UTF-8):	Pakiet dla programistów używających libshout
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libogg-devel
Requires:	libtheora-devel
Requires:	libvorbis-devel
Requires:	speex-devel

%description devel
The libshout-devel package contains the header files needed for
developing applications that send data to an icecast server. Install
libshout-devel if you want to develop applications using libshout.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do tworzenia aplikacji
wysyłających dane do serwera icecast.

%package static
Summary:	Icecast source streaming static library
Summary(pl.UTF-8):	Statyczna biblioteka libshout
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Icecast source streaming static library.

%description static -l pl.UTF-8
Statyczna biblioteka libshout - źródeł strumieni icecast.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# ckport support is not maintained in PLD
%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/ckport

cp -rf examples/*.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/libshout.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libshout.so.3

%files devel
%defattr(644,root,root,755)
%doc doc/* 
%attr(755,root,root) %{_libdir}/libshout.so
%{_libdir}/libshout.la
%{_includedir}/shout
%{_pkgconfigdir}/shout.pc
%{_aclocaldir}/shout.m4
%{_examplesdir}/%{name}-%{version}

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libshout.a
%endif
