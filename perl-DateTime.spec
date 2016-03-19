%define	modname	DateTime
%define modver 1.12

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	6
Epoch:		2

Summary:	A date and time object in Perl
License:	Artistic
Group:		Development/Perl
URL:		http://datetime.perl.org/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/%{modname}/%{modname}-%{modver}.tar.gz

BuildRequires:	perl(DateTime::Locale) >= 0.21
BuildRequires:	perl(Test::Warnings)
#BuildRequires:	perl(DateTime::TimeZone) >= 0.38
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
%doc Changes CREDITS
%{perl_vendorarch}/DateTime*
%{perl_vendorarch}/auto/*
%{_mandir}/*/*
