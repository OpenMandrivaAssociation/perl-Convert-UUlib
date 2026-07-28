%define	modname	 Convert-UUlib
%define modver 1.8

Summary:	%{modname} module for perl
Name:		perl-%{modname}
Epoch:		2
Version:	%{modver}
Release:	3
License:	GPLv2
Group:		Development/Perl
Url:		https://metacpan.org/dist/Convert-UUlib
Source0:	https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Convert-UUlib-%{modver}.tar.gz
BuildRequires:	make
BuildRequires: perl(Canary::Stability)
BuildRequires:	perl-devel
BuildRequires:	perl(common::sense)

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

