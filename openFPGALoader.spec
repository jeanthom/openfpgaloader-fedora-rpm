Name:        openFPGALoader
Version:     0.4.0
%define uver 0.4.0
Release:     2%{?dist}
Summary:     Universal utility for programming FPGA
License:     ASL 2.0
URL:         https://github.com/trabucayre/openFPGALoader
Source0:     https://github.com/trabucayre/openFPGALoader/archive/v%{version}/openFPGALoader-v%{version}.tar.gz
Requires:    libftdi
Requires:    libgudev
BuildRequires: cmake
BuildRequires: gcc-c++
%if 0%{?fedora} >= 1 || 0%{rhel} >= 8
BuildRequires: libgudev-devel
%endif
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(libftdi1)
BuildRequires: pkgconfig(hidapi-libusb)
 
%description
Universal utility for programming FPGA

%prep
%setup -n openFPGALoader-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install
 
%files
%license LICENSE
%{_bindir}/openFPGALoader
%{_datadir}/*
 
%changelog
* Fri Jul 2 2021 Jean THOMAS <git0@pub.jeanthomas.me> - v0.4.0-2
- Add support for older CentOS/RHEL

* Thu Jul 1 2021 Jean Thomas <git0@pub.jeanthomas.me> - v0.4.0-1
- Initial release
