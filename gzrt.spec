Name:		gzrt
Summary:	The gzip Recovery Toolkit
Version:	0.6
Release:	1
License:	GPLv2+
Group:		Archiving/Compression
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	zlib-devel
Source:		http://www.urbanophile.com/arenn/hacking/gzrt/%{name}-%{version}.tar.gz
URL:		http://www.urbanophile.com/arenn/hacking/gzrt/gzrt.html
%description
The gzip Recovery Toolkit attempts to automate the recovery of data
from corrupted gzip files (including tarballs) through a program called
gzrecover.

%prep
%setup -q

%build
%{__make}

%install
%{__mkdir_p} %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
%{__cp} -p gzrecover %{buildroot}%{_bindir}
%{__cp} -p gzrecover.1 %{buildroot}%{_mandir}/man1

%files
%doc ChangeLog README
%{_bindir}/gzrecover
%{_mandir}/man1/gzrecover.1*




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5-5mdv2011.0
+ Revision: 619323
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.5-4mdv2010.0
+ Revision: 429371
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.5-3mdv2009.0
+ Revision: 246782
- rebuild

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 0.5-1mdv2008.1
+ Revision: 167903
- fix no-buildroot-tag

* Mon Sep 17 2007 Nicolas Vigier <nvigier@mandriva.com> 0.5-1mdv2008.0
+ Revision: 89180
- Import gzrt


