%define	modname	DateTime

# Disabled by default to avoid circular dependency between
# perl-DateTime and perl-DateTime-TimeZone
%bcond_with tests

Name:		perl-%{modname}
Version:	1.65
Release:	1

Summary:	A date and time object in Perl
License:	Artistic
Group:		Development/Perl
URL:		https://metacpan.org/release/DateTime/
# Also: https://github.com/houseabsolute/DateTime.pm
Source0:	https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-%{version}.tar.gz

BuildRequires:	perl(DateTime::Locale)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Pod::Man)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Time::Local)
BuildRequires:	perl(Math::Round)
%if %{with tests}
BuildRequires:	perl(DateTime::TimeZone)
BuildRequires:	perl(CPAN::Meta::Requirements)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::Warnings)
BuildRequires:	perl(Test::More)
%endif
BuildRequires:	perl-devel
BuildRequires:	perl(List::MoreUtils)


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
%autosetup -p1 -n %{modname}-%{version}

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
