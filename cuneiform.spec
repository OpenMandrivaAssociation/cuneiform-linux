%define Werror_cflags %nil

%define	version	1.0.0
%define	release	%mkrel 1

Name:		cuneiform-linux
Summary:	An OCR system
Version:	%{version}
Release:	%{release}
License:	BSD
URL:		https://launchpad.net/cuneiform-linux
Group:		Text tools
Source0:	%{name}-%{version}.tar.bz2.tar
BuildRequires:	cmake
BuildRequires:	ImageMagick
Suggests:	cuneiform-qt yagf

%description
Cuneiform is an multi-language OCR system originally developed
and open sourced by Cognitive Technologies. Cuneiform was
originally a Windows program, which was ported to Linux
by Jussi Pakkanen.


%prep

%setup -q -n %{name}-%{version}

%build
%cmake
%make

%install
rm -rf %{buildroot}
cd build
%makeinstall_std
export DONT_FIX_EOL=1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc issues.txt *readme.rtf readme.txt
%{_bindir}/cuneiform
%{_datadir}/cuneiform/*.dat
%{_includedir}/cuneiform.h
%{_libdir}/*.so
%{_libdir}/*.so.%{version}
