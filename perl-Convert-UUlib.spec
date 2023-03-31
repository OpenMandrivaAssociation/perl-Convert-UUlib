%define	modname	 Convert-UUlib
%define modver 1.4

Summary:	%{modname} module for perl
Name:		perl-%{modname}
Epoch:		2
Version:	%perl_convert_version %{modver}
Release:	17
License:	GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/Convert/%{modname}-%{modver}.tar.gz
BuildRequires:	perl-devel

%description
Convert::UUlib is a Perl interface to the uulib library (a.k.a.
uudeview/uuenview).

%prep
%setup -qn %{modname}-%{modver}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes COPYING doc
%{perl_vendorarch}/auto/Convert
%{perl_vendorarch}/Convert
%{_mandir}/man3/*

