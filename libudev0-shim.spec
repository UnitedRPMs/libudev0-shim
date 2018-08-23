AutoReqProv: no
%global debug_package %{nil}

%global realname libudev0

Name: libudev0-shim
Version: 181
Release: 2%{?dist}
Summary: Shared library to access udev device information
License: LGPLv2.1+
Group: System Environment/Libraries
Url: http://kernel.org/pub/linux/utils/kernel/hotplug/
Source: https://github.com/archlinux/libudev0-shim/archive/v1.tar.gz

BuildRequires:  gcc-c++ systemd-devel
Provides: libudev0 = %{version}-%{release}

%description
This package provides shared library to access udev device information

%prep
%autosetup -n libudev0-shim-1 

%build


  make

%install

  install -Dm 755 libudev.so.0.0.9999 -t "%{buildroot}/%{_libdir}"
  ln -sf %{_libdir}/libudev.so.0.0.9999 "%{buildroot}/%{_libdir}/libudev.so.0"

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/libudev.so.*

%changelog

* Wed Aug 22 2018 David Va <davidva AT tuta DOT io> 181-2
- Rebuilt

* Tue Oct 24 2017 David Vásquez <davidjeremias82 AT gmail DOT com> 181-1
- Initial build
