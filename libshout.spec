Summary:	libshout - icecast source streaming library
Summary(pl):	Biblioteka ºrÛde≥ strumieni icecast
Name:		libshout
Version:	1.0.5
Release:	2
License:	LGPL
Vendor:		Icecast <team@icecast.org>
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
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
libshout to biblioteka do komunikowania siÍ z i wysy≥ania danych do
serwera icecast. Obs≥uguje po≥±czenia, czasy danych i zapobiega
dotarciu wiÍkszo∂ci z≥ych danych do serwera icecast.

%package devel
Summary:	Icecast source streaming library development package
Summary(pl):	Pakiet dla programistÛw uøywaj±cych libshout
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
The libshout-devel package contains the header files needed for
developing applications that send data to an icecast server. Install
libshout-devel if you want to develop applications using libshout.

%description devel -l pl
Ten pakiet zawiera pliki nag≥Ûwkowe potrzebne do tworzenia aplikacji
wysy≥aj±cych dane do serwera icecast.

%package static
Summary:	Icecast source streaming static library
Summary(pl):	Statyczna biblioteka libshout
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Icecast source streaming static library.

%description static -l pl
Statyczna biblioteka libshout - ºrÛde≥ strumieni icecast.

%prep
%setup -q
%patch -p1

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c
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
