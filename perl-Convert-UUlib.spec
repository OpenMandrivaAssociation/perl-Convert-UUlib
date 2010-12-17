%define	upstream_name	 Convert-UUlib
%define upstream_version 1.34

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Epoch:		2

Summary:	%{upstream_name} module for perl
License: 	GPL
Group: 		Development/Perl
Url: 		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Convert/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description
Convert::UUlib is a Perl interface to the uulib library (a.k.a.
uudeview/uuenview).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%doc README Changes COPYING doc
%{perl_vendorarch}/auto/Convert
%{perl_vendorarch}/Convert
%{_mandir}/*/*
