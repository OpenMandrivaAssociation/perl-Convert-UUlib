%define	module	Convert-UUlib
%define	name	perl-%{module}
%define	version	1.09
%define	release	%mkrel 1

Name: 		%{name}
Version: 	%{version}
Epoch:		2
Release: 	%{release}
License: 	GPL
Group: 		Development/Perl
Source: 	%{module}-%{version}.tar.gz
URL: 		http://search.cpan.org/dist/%{module}/
BuildRequires:	perl-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: 	perl
Summary:	%{module} module for perl

%description
Convert::UUlib is a Perl interface to the uulib library (a.k.a.
uudeview/uuenview).

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
%make

%check
%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{perl_vendorarch}/auto/Convert
%{perl_vendorarch}/Convert
%{_mandir}/*/*
%doc README Changes COPYING doc


