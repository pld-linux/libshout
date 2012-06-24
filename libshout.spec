Summary:	libshout - icecast source streaming library
Summary(pl):	Biblioteka �r�de� strumieni icecast
Name:		libshout
Version:	2.1
Release:	1
License:	LGPL
Vendor:		Icecast <team@icecast.org>
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/libshout/%{name}-%{version}.tar.gz
# Source0-md5:	ca6e98af87fd17c709821d9be82b37d5
#Patch0:		%{name}-ac_am_fixes.patch
URL:		http://www.icecast.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libshout is a library for communicating with and sending data to an
icecast server. It handles the socket connection, the timing of the
data, and prevents most bad data from getting to the icecast server.

%description -l pl
libshout to biblioteka do komunikowania si� z i wysy�ania danych do
serwera icecast. Obs�uguje po��czenia, czasy danych i zapobiega
dotarciu wi�kszo�ci z�ych danych do serwera icecast.

%package devel
Summary:	Icecast source streaming library development package
Summary(pl):	Pakiet dla programist�w u�ywaj�cych libshout
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The libshout-devel package contains the header files needed for
developing applications that send data to an icecast server. Install
libshout-devel if you want to develop applications using libshout.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe potrzebne do tworzenia aplikacji
wysy�aj�cych dane do serwera icecast.

%package static
Summary:	Icecast source streaming static library
Summary(pl):	Statyczna biblioteka libshout
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Icecast source streaming static library.

%description static -l pl
Statyczna biblioteka libshout - �r�de� strumieni icecast.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -rf examples/*.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/* 
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/shout
%{_pkgconfigdir}/shout.pc
%{_aclocaldir}/shout.m4
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
 %{_libdir}/lib*.a
