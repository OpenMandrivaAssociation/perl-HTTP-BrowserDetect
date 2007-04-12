%define module	HTTP-BrowserDetect
%define name	perl-%{module}
%define version 0.98
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Summary:	Determine the Web browser, version, and platform from an HTTP user agent string
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTTP/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The HTTP::BrowserDetect object does a number of tests on an HTTP user agent
string. The results of these tests are available via methods of the object.

This module is based upon the JavaScript browser detection code available at
http://www.mozilla.org/docs/web-developer/sniffer/browser_type.html.

%prep
%setup -q -n %{module}-%{version}
perl -pi -e 's/\015$//' README

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/HTTP
%{_mandir}/*/*

