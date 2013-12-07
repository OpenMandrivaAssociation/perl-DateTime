%define	modname	DateTime
%define	modver	1.03

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	5
Epoch:		2

Summary:	A date and time object in Perl
License:	Artistic
Group:		Development/Perl
URL:		http://datetime.perl.org/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/DateTime/%{modname}-%{modver}.tar.gz

BuildRequires:	perl(DateTime::Locale) >= 0.21
BuildRequires:	perl(DateTime::TimeZone) >= 0.38
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Params::Validate) >= 0.76
BuildRequires:	perl(Pod::Man) >= 1.14
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More) >= 0.34
BuildRequires:	perl(Time::Local) >= 1.04
BuildRequires:	perl(Math::Round)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl-devel >= 2:5.14
BuildRequires:	perl-List-MoreUtils >= 0.320.0-3


Provides:	perl(DateTimePP)
Provides:	perl(DateTimePPExtra)

%description
DateTime is a class for the representation of date/time combinations, and is
part of the Perl DateTime project.

It represents the Gregorian calendar, extended backwards in time before its
creation (in 1582). This is sometimes known as the "proleptic Gregorian
calendar". In this calendar, the first day of the calendar (the epoch), is the
first day of year 1, which corresponds to the date which was (incorrectly)
believed to be the birth of Jesus Christ.

%prep
%setup -q -n %{modname}-%{modver}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes README CREDITS
%{perl_vendorarch}/DateTime*
%{perl_vendorarch}/auto/*
%{_mandir}/*/*

%changelog
* Fri Dec 28 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.720.0-2
- cleanups
- rebuild for new perl-5.16.2

* Fri Jan 20 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.720.0-1
+ Revision: 762889
- Build for perl 5.14.x
- Update to 0.72

* Thu Jun 16 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.700.0-1
+ Revision: 685622
- update to new version 0.70

* Mon Apr 25 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.680.0-1
+ Revision: 659055
- new version 0.68

* Sun Apr 24 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.670.0-1
+ Revision: 658373
- new version 0.67
- add a BR on Math::Round

* Thu Dec 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.660.0-1mdv2011.0
+ Revision: 624081
- update to new version 0.66

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.650.0-1mdv2011.0
+ Revision: 596608
- update to 0.65

* Sat Oct 16 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.630.0-1mdv2011.0
+ Revision: 585985
- new upstream release

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.610.0-1mdv2011.0
+ Revision: 561030
- update to 0.61

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.600.0-3mdv2011.0
+ Revision: 555786
- rebuild for perl 5.12

  + Sandro Cazzaniga <kharec@mandriva.org>
    - rebuild

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.600.0-1mdv2011.0
+ Revision: 551989
- update to 0.60

* Wed Mar 17 2010 Jérôme Quelin <jquelin@mandriva.org> 0.550.0-1mdv2010.1
+ Revision: 523432
- update to 0.55

* Mon Mar 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.540.0-1mdv2010.1
+ Revision: 519949
- update to 0.54

* Tue Dec 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.530.0-1mdv2010.1
+ Revision: 474661
- update to 0.53

* Sun Dec 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.520.0-1mdv2010.1
+ Revision: 474101
- adding missing buildrequires:
- update to 0.52

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.510.0-1mdv2010.1
+ Revision: 460717
- update to 0.51

* Mon Jul 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.500.0-1mdv2010.0
+ Revision: 392733
- bumping epoch to make sure %%perl_convert_version works
- update to 0.50
- using %%perl_convert_version
- fixed license field

* Tue Dec 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.4501-1mdv2009.1
+ Revision: 309297
- update to new version 0.4501

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.4305-1mdv2009.1
+ Revision: 292117
- update to new version 0.4305

* Mon Sep 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4304-1mdv2009.0
+ Revision: 289459
- 0.4304

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sat Mar 01 2008 Michael Scherer <misc@mandriva.org> 0.42-1mdv2008.1
+ Revision: 177287
- update to new version 0.42

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.41-3mdv2008.1
+ Revision: 152051
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Oct 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.41-1mdv2008.1
+ Revision: 100854
- update to new version 0.41

* Sun Sep 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.40-1mdv2008.0
+ Revision: 78095
- update to new version 0.40

* Fri Jul 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.39-1mdv2008.0
+ Revision: 56248
- update to new version 0.39
- update to new version 0.38

* Mon May 21 2007 Michael Scherer <misc@mandriva.org> 0.37-1mdv2008.0
+ Revision: 29068
- Update to new version 0.37


* Sat Aug 12 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-12 14:39:36 (55729)
- Version 0.34

* Wed Aug 09 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-09 17:35:26 (54815)
- Version 0.33

* Sun Aug 06 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-06 17:00:07 (53482)
- Version 0.32

* Sun Aug 06 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-06 16:54:28 (53479)
- import perl-DateTime-0.31-1mdk

* Sun May 21 2006 Scott Karns <scottk@mandriva.org> 0.31-1mdk
- 0.31
- Added BuildRequires perl(Scalar::Util) for 0.31

* Sat May 06 2006 Scott Karns <scottk@mandriva.org> 0.30-3mdk
- Remove mdkversion conditional surrounding BuildRequires perl-devel.
  (Needed for arch specific perl packages.)

* Fri May 05 2006 Scott Karns <scottk@mandriva.org> 0.30-2mdk
- Added CFLAGS="-O2 -g -pipe -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fomit-frame-pointer -march=i586 -mtune=pentiumpro -fasynchronous-unwind-tables"
- Updated BuildRequires
- Updated to comply with Mandriva perl packaging policies

* Mon Jan 16 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.30-1mdk
- 0.30

* Tue Aug 23 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.2901-2mdk
- buildrequires perl-Class-Singleton 
- use standard syntax for manual dependencies
- fix sources url for rpmbuildupdate

* Fri Jul 15 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.2901-1mdk
- 0.2901

* Sat Jun 04 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.29-1mdk
- 0.29

* Fri Apr 22 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.28-1mdk
- 0.28

* Wed Feb 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.27-1mdk
- 0.27

* Mon Jan 31 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.26-1mdk
- 0.26

* Tue Jan 11 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.25-1mdk
- 0.25

* Tue Dec 14 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.24-1mdk
- 0.24

* Fri Dec 10 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.23-1mdk
- 0.23
- test during build

* Mon Nov 15 2004 Michael Scherer <misc@mandrake.org> 0.22-3mdk
- Rebuild for new perl

* Mon Aug 30 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.22-2mdk
- Add manually needed provides.

* Thu Aug 26 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.22-1mdk
- Initial MDK release.

