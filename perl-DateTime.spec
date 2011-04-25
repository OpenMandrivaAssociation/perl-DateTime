%define upstream_name	 DateTime
%define upstream_version 0.68

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1
Epoch:		2

Summary:	A date and time object in Perl
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://datetime.perl.org/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tar.gz

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
BuildRequires:	perl-devel


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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README CREDITS
%{perl_vendorarch}/DateTime*
%{perl_vendorarch}/auto/*
%{_mandir}/*/*
