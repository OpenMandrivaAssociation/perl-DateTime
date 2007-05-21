%define module	DateTime
%define name	perl-%{module}
%define	modprefix DateTime
%define version	0.37
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		1
Summary:	A date and time object in Perl
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
Url:		http://datetime.perl.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires:	perl(DateTime::Locale) >= 0.21
BuildRequires:	perl(DateTime::TimeZone) >= 0.38
BuildRequires:	perl(Params::Validate) >= 0.76
BuildRequires:	perl(Pod::Man) >= 1.14
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More) >= 0.34
BuildRequires:	perl(Time::Local) >= 1.04
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
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%__make CFLAGS="%{optflags}"

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README CREDITS
%{perl_vendorarch}/%{modprefix}*
%{perl_vendorarch}/auto/*
%{_mandir}/*/*



