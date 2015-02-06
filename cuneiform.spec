%define	version		1.1.0
%define release		3
%define abi		0
%define libname		%mklibname cuneiform %{abi}
%define develname	%mklibname cuneiform -d

# datafiles must have DOS-style EOL
%define dont_fix_eol	1

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
#Suggests:	cuneiform-qt yagf

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


%changelog
* Sun Jan 15 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.1.0-2mdv2011.0
+ Revision: 761431
- don't suggest frontends to avoid dependency hell
- don't fix EOL in data files

* Tue Dec 20 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.1.0-1
+ Revision: 743893
- devel package reqs fixed
- new version 1.1.0, separate lib package

* Fri Dec 31 2010 Александр Казанцев <kazancas@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 626895
- initial release
- import cuneiform-linux


* Sat Jul 03 2010 Alexander Kazancev <kazancas@mandriva.ru> 1.0.0-1edm2010.0
- New version

* Sat Apr 03 2010 Doktor5000 <rpm@mandrivauser.de> 0.9.0-3mud2010.0
- added Suggests for the GUIs cuneiform-qt and yagf

* Mon Mar 29 2010 Doktor5000 <rpm@mandrivauser.de> 0.9.0-2mud2010.0
- switch to trunk revision 471
- try to fix "PUMA_XFinalrecognition failed" error

* Mon Mar 29 2010 Doktor5000 <rpm@mandrivauser.de> 0.9.0-1mud2010.0
- new version 0.9.0
- added spec-helper fix from MadMax aka MaxiPunkt
- rebuild for 2010.0

* Thu Jan 22 2009 Oliver Burger <rpm@mandrivauser.de> 0.5-1mud2009.0
- new version 0.5

* Wed Oct 20 2008 Oliver Burger <rpm@mandrivauser.de> 0.4-1.1mud2009.0
- Rebuild for 2009.0-final

* Sat Sep 20 2008 Oliver Burger <rpm@mandrivauser.de> 0.4-1mud2009.0
- Rebuild for MUde

* Sat Sep 20 2008 MaxiPunkt <email@domain.de> 0.4-1max
- First built for Mandriva
