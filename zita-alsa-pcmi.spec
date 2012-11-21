Summary:	Library providing easy access to ALSA PCM devices
Name:		zita-alsa-pcmi
Version:	0.2.0
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://www.kokkinizita.net/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	caffc4f9bb0872e8e431581472891522
BuildRequires:	alsa-lib-devel
BuildRequires:	libstdc++-devel
Patch0:		%{name}-make.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library providing easy access to ALSA PCM devices.

%package devel
Summary:	Header files for zita-alsa-pcmi library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for zita-alsa-pcmi
library.

%prep
%setup -q
%patch0 -p1

%build
export CXXFLAGS="%{rpmcxxflags}"
export LDFLAGS="%{rpmldflags}"

%{__make} -C libs \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C libs install \
	DESTDIR=$RPM_BUILD_ROOT

chmod +x $RPM_BUILD_ROOT%{_libdir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %ghost %{_libdir}/libzita-alsa-pcmi.so.?
%attr(755,root,root) %{_libdir}/libzita-alsa-pcmi.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libzita-alsa-pcmi.so
%{_includedir}/zita-alsa-pcmi.h

