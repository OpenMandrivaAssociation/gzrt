Name:		gzrt
Summary:	The gzip Recovery Toolkit
Version:	0.5
Release:	%mkrel 4
License:	GPLv2+
Group:		Archiving/Compression
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	zlib-devel
Source:		http://www.urbanophile.com/arenn/hacking/gzrt/gzrt-0.5.tar.gz
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


