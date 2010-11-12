%define upstream_name	 HTTP-BrowserDetect
%define upstream_version 1.19

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Determine the Web browser, version, and platform from an HTTP user agent string
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTTP/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires: perl(Data::Dump)
BuildRequires: perl(YAML::Tiny)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
The HTTP::BrowserDetect object does a number of tests on an HTTP user agent
string. The results of these tests are available via methods of the object.

This module is based upon the JavaScript browser detection code available at
http://www.mozilla.org/docs/web-developer/sniffer/browser_type.html.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
