%define	modname	DateTime
%define modver 1.52

# Disabled by default to avoid circular dependency between
# perl-DateTime and perl-DateTime-TimeZone
%bcond_with tests

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
Epoch:		2

Summary:	A date and time object in Perl
License:	Artistic
Group:		Development/Perl
URL:		http://metacpan.org/release/DateTime/
# Also: https://github.com/houseabsolute/DateTime.pm
Source0:	https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-%{modver}.tar.gz

BuildRequires:	perl(DateTime::Locale) >= 0.21
BuildRequires:	perl(Params::Validate) >= 0.76
BuildRequires:	perl(Pod::Man) >= 1.14
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Time::Local) >= 1.04
BuildRequires:	perl(Math::Round)
%if %{with tests}
BuildRequires:	perl(DateTime::TimeZone)
BuildRequires:	perl(CPAN::Meta::Requirements)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::Warnings)
BuildRequires:	perl(Test::More) >= 0.34
%endif
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
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%if %{with tests}
%check
%make test
%endif

%install
%make_install

%files
%doc Changes CREDITS
%{perl_vendorarch}/DateTime*
%{perl_vendorarch}/auto/*
%{_mandir}/*/*
