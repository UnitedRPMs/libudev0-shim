AutoReqProv: no
%global debug_package %{nil}

Name: libudev0-shim
Version: 1
Release: 1%{?dist}
Summary: libudev.so.0 compatibility library for systems with newer udev versions
License: LGPLv2.1+
Group: System Environment/Libraries
Url: https://github.com/archlinux/libudev0-shim

Provides: libudev0 = %{version}-%{release}
Requires: systemd

Source: https://github.com/archlinux/libudev0-shim/archive/v%{version}.tar.gz

BuildRequires: make

%description
libudev.so.0 compatibility library for systems with newer udev versions

%prep
%autosetup -n %{name}-%{version}


%build
unset LDFLAGS
make

%install
install -Dm 755 libudev.so.0.0.9999 -t "$RPM_BUILD_ROOT/%{_libdir}"
ln -sf libudev.so.0.0.9999 "$RPM_BUILD_ROOT/%{_libdir}/libudev.so.0"

%files
%{_libdir}/libudev.so.*

%changelog

* Tue Oct 24 2017 David Vásquez <davidjeremias82 AT gmail DOT com> 175-1
- Initial build
