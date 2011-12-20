%define	version		1.1.0
%define	release		%mkrel 1
%define abi		0
%define libname		%mklibname cuneiform %{abi}
%define develname	%mklibname cuneiform -d

Name:		cuneiform-linux
Summary:	An OCR system
Version:	%{version}
Release:	%{release}
License:	BSD
URL:		https://launchpad.net/cuneiform-linux
Group:		Text tools
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	ImageMagick-devel
Suggests:	cuneiform-qt yagf

%description
Cuneiform is an multi-language OCR system originally developed
and open sourced by Cognitive Technologies. Cuneiform was
originally a Windows program, which was ported to Linux
by Jussi Pakkanen.

%package -n %{libname}
Summary:	Cuneiform OCR system shared libraries
Group:		System/Libraries

%description -n %{libname}
Cuneiform is an multi-language OCR system originally developed
and open sourced by Cognitive Technologies. Cuneiform was
originally a Windows program, which was ported to Linux
by Jussi Pakkanen.

%package -n %{develname}
Summary:	Cuneiform development files
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Requires:	ImageMagick-devel

%description -n %{develname}
Cuneiform is an multi-language OCR system originally developed
and open sourced by Cognitive Technologies. Cuneiform was
originally a Windows program, which was ported to Linux
by Jussi Pakkanen.

This package contains files required only for development purpose.

%prep

%setup -q -n %{name}-%{version}

%build
%cmake
%make

%install
rm -rf %{buildroot}
cd build
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc issues.txt *readme.rtf readme.txt
%{_bindir}/cuneiform
%{_datadir}/cuneiform/*.dat

%files -n %{libname}
%{_libdir}/*.so.%{abi}*
%{_libdir}/*.so.%{version}

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/cuneiform.h
