AutoReqProv: no
%global debug_package %{nil}

%global realname libudev0

Name: libudev0-shim
Version: 181
Release: 1%{?dist}
Summary: Shared library to access udev device information
License: LGPLv2.1+
Group: System Environment/Libraries
Url: http://kernel.org/pub/linux/utils/kernel/hotplug/
Patch: uint.patch
Source: https://github.com/systemd/systemd/archive/%{version}.tar.gz
Source1: usbutils.pc
Source2: gtk-doc.pc

BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  gperf
BuildRequires:  libselinux-devel 
BuildRequires:  libsepol-devel 
BuildRequires:  gtk-doc 
BuildRequires:  usbutils 
BuildRequires:  clang llvm
BuildRequires:  glib2-devel
BuildRequires:  hwdata
BuildRequires:  gobject-introspection-devel >= 0.6.2
BuildRequires:  usbutils >= 0.82
BuildRequires:  kmod-devel >= 5
BuildRequires:  libblkid-devel >= 2.20
Provides: libudev0 = %{version}-%{release}

%description
This package provides shared library to access udev device information

%prep
%autosetup -n systemd-%{version} -p1

%build

NOCONFIGURE=1 ./autogen.sh

  # Event codes have been moved out of input.h
  #sed -i 's:input.h:input-event-codes.h:' Makefile.in
  # stdin.h is needed for uint32_t and uint8_t typedefs
  #sed -i '20a#include <stdint.h>' src/mtd_probe/mtd_probe.h

PKG_CONFIG_PATH=%{_libdir}/pkgconfig/:%{_sourcedir}

export CC=clang 
export CXX=clang++

./configure \
    --disable-gudev \
    --disable-introspection \
    --sysconfdir=/etc \
    --bindir=/usr/bin \
    --sbindir=/usr/bin \
    --libdir=%{_libdir} \
    --disable-gtk-doc \
    --disable-umockdev \
    --libexecdir=/usr/libexec \
    --disable-keymap \
    --disable-static \
    --disable-silent-rules

#    --disable-mtd_probe  \

sed -i 's/ -shared / -Wl,-O1,--as-needed\0/g' -i libtool
make LIBS="-lrt"

%install
install -Dm755 src/.libs/libudev.so.0.13.1 %{buildroot}/%{_libdir}/libudev.so.0.13.1
ln -sf %{_libdir}/libudev.so.0.13.1 %{buildroot}/%{_libdir}/libudev.so.0

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/libudev.so.*

%changelog

* Tue Oct 24 2017 David Vásquez <davidjeremias82 AT gmail DOT com> 182-1
- Initial build
