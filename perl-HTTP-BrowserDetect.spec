%define upstream_name	 HTTP-BrowserDetect
%define upstream_version 1.26

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Determine the Web browser, version, and platform from an HTTP user agent string
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTTP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Data::Dump)
BuildRequires:	perl(YAML::Tiny)
BuildRequires:	perl(JSON::PP)
BuildArch:	noarch

%description
The HTTP::BrowserDetect object does a number of tests on an HTTP user agent
string. The results of these tests are available via methods of the object.

This module is based upon the JavaScript browser detection code available at
http://www.mozilla.org/docs/web-developer/sniffer/browser_type.html.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
perl -pi -e 's/\015$//' README

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/HTTP
%{_mandir}/*/*

%changelog
* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.260.0-1mdv2011
+ Revision: 690266
- update to new version 1.26

* Sat May 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.240.0-1
+ Revision: 674662
- update to new version 1.24

* Sat May 14 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.230.0-1
+ Revision: 674628
- workaround buildrequires issue breaking check suite..

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 1.23

* Mon Mar 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.220.0-1
+ Revision: 644751
- update to new version 1.22

* Sun Dec 26 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.210.0-1mdv2011.0
+ Revision: 625271
- update to new version 1.21

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.200.0-1mdv2011.0
+ Revision: 601875
- update to new version 1.20
- update to new version 1.19

* Tue Aug 31 2010 Jérôme Quelin <jquelin@mandriva.org> 1.170.0-1mdv2011.0
+ Revision: 574788
- update to 1.17

* Sun Aug 22 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.160.0-1mdv2011.0
+ Revision: 572058
- new version

* Fri Aug 13 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.130.0-1mdv2011.0
+ Revision: 569458
- new version

* Sun Aug 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.120.0-1mdv2011.0
+ Revision: 567735
- new version

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.110.0-1mdv2011.0
+ Revision: 552319
- update to 1.11

* Tue Apr 06 2010 Jérôme Quelin <jquelin@mandriva.org> 1.90.0-1mdv2010.1
+ Revision: 532149
- update to 1.09

* Sun Mar 21 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.80.0-1mdv2010.1
+ Revision: 526036
- new version

* Thu Feb 11 2010 Jérôme Quelin <jquelin@mandriva.org> 1.70.0-1mdv2010.1
+ Revision: 504072
- update to 1.07

* Fri Nov 27 2009 Jérôme Quelin <jquelin@mandriva.org> 1.60.0-1mdv2010.1
+ Revision: 470468
- adding missing buildrequires:
- update to 1.06

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-1mdv2010.1
+ Revision: 461385
- adding missing buildrequires:
- update to 1.03

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.990.0-1mdv2010.0
+ Revision: 403266
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.99-3mdv2009.0
+ Revision: 268525
- rebuild early 2009.0 package (before pixel changes)

* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.99-2mdv2009.0
+ Revision: 210958
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 0.99-1mdv2008.0
+ Revision: 20185
- 0.99


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.98-3mdv2007.0
- Rebuild

* Mon Apr 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.98-2mdk
- Rebuild
- better sources URL
- better buildrequires syntax

* Mon Apr 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.98-1mdk 
- first mandriva release

