Summary:	libshout - icecast source streaming library
Summary(pl):	Biblioteka ¼róde³ strumieni icecast
Name:		libshout
Version:	1.0.5
Release:	2
License:	LGPL
Vendor:		Icecast <team@icecast.org>
Group:		Libraries
Source0:	ftp://ftp.icecast.org/pub/libshout/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_am_fixes.patch
URL:		http://www.icecast.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libshout is a library for communicating with and sending data to an
icecast server. It handles the socket connection, the timing of the
data, and prevents most bad data from getting to the icecast server.

%description -l pl
libshout to biblioteka do komunikowania siê z i wysy³ania danych do
serwera icecast. Obs³uguje po³±czenia, czasy danych i zapobiega
dotarciu wiêkszo¶ci z³ych danych do serwera icecast.

%package devel
Summary:	Icecast source streaming library development package
Summary(pl):	Pakiet dla programistów u¿ywaj±cych libshout
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
The libshout-devel package contains the header files needed for
developing applications that send data to an icecast server. Install
libshout-devel if you want to develop applications using libshout.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe potrzebne do tworzenia aplikacji
wysy³aj±cych dane do serwera icecast.

%package static
Summary:	Icecast source streaming static library
Summary(pl):	Statyczna biblioteka libshout
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Icecast source streaming static library.

%description static -l pl
Statyczna biblioteka libshout - ¼róde³ strumieni icecast.

%prep
%setup -q
%patch -p1

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*.{html,css}
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/shout

%files static
%defattr(644,root,root,755)
 %{_libdir}/lib*.a
