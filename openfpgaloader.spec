Name:        openfpgaloader
Version:     0.4.0
%define uver 0.4.0
Release:     1%{?dist}
Summary:     Universal utility for programming FPGA
License:     ASL 2.0
URL:         https://github.com/trabucayre/openFPGALoader
Source0:     https://github.com/trabucayre/openFPGALoader/archive/v%{version}/%{name}-v%{version}.tar.gz
Requires:    libftdi
Requires:    libgudev
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libgudev-devel
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(libftdi1)
BuildRequires: pkgconfig(hidapi-libusb)
 
%description
Universal utility for programming FPGA

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest
 
%files
%{_bindir}/*
%{_datadir}/*.bit
 
%changelog
* Wed Jun 30 2021 Jean Thomas <git0@pub.jeanthomas.me> - v0.4.0-1
- Initial release
