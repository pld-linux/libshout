%define name	libshout
%define version	1.0.5
%define release 1

Summary:	libshout - icecast source streaming library
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Libraries/Multimedia
Copyright:	LGPL
URL:		http://www.icecast.org
Vendor:		Icecast <team@icecast.org>
Source:		ftp://ftp.icecast.org/pub/libshout/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-root

%description
Libshout is a library for communicating with and sending data to an
icecast server.  It handles the socket connection, the timing of the
data, and prevents most bad data from getting to the icecast server.

%package devel
Summary: icecast source streaming library development package
Group: Development/Libraries

%description devel
The libshout-devel package contains the header files needed for developing
applications that send data to an icecast server.  Install libshout-devel if
you want to develop applications using libshout.

%prep
%setup -q -n libshout-%{version}

%build
if [ ! -f configure ]; then
  CFLAGS="$RPM_FLAGS" ./autogen.sh --prefix=/usr
else
  CFLAGS="$RPM_FLAGS" ./configure --prefix=/usr
fi
make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root)
%doc AUTHORS
%doc CHANGES
%doc COPYING
%doc README
/usr/lib/libshout.so.*

%files devel
%doc doc/shout_connect.html
%doc doc/shout_disconnect.html
%doc doc/shout_init_connection.html
%doc doc/shout_send_data.html
%doc doc/shout_sleep.html
%doc doc/shout_update_metadata.html
%doc doc/shout_strerror.html
%doc doc/errorhandling.html
%doc doc/overview.html
%doc doc/style.css
%doc doc/reference.html
%doc doc/example.html
%doc doc/example_c.html
%doc doc/connection.html
%doc doc/datastreaming.html
%doc doc/datastructures.html
%doc doc/index.html
%doc doc/initialization.html
%doc doc/metadata.html
%doc doc/shout_conn_t.html
%doc example/Makefile
%doc example/example.c
/usr/include/shout/shout.h

%clean 
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%changelog
* Tue Mar 21 2000 Jeremy Katz <katzj@icecast.org>
- split into libshout and libshout-devel packages

* Tue Mar 21 2000 Jack Moffitt <jack@icecast.org>
- new version

* Wed Mar 15 2000 Jack Moffitt <jack@icecast.org>
- More files to get installed

* Wed Mar 15 2000 Jeremy Katz <katzj@icecast.org>
- Clean up the spec file a tad
- Do an ldconfig after installing the lib

* Tue Mar 14 2000 Jack Moffitt <jack@icecast.org>
- First official rpm build, using 1.0.0
