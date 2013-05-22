%define	upstream_name	 Convert-UUlib
%define upstream_version 1.4

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4
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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes COPYING doc
%{perl_vendorarch}/auto/Convert
%{perl_vendorarch}/Convert
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2:1.400.0-3mdv2012.0
+ Revision: 765115
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2:1.400.0-2
+ Revision: 763572
- rebuilt for perl-5.14.x

* Tue May 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2:1.400.0-1
+ Revision: 682114
- update to new version 1.4

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2:1.340.0-2
+ Revision: 667056
- mass rebuild

* Fri Dec 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2:1.340.0-1mdv2011.0
+ Revision: 622677
- update to new version 1.34

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 2:1.330.0-3mdv2011.0
+ Revision: 564387
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2:1.330.0-2mdv2011.0
+ Revision: 555704
- rebuild

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 2:1.330.0-1mdv2010.1
+ Revision: 460837
- update to 1.33

* Thu Sep 17 2009 Jérôme Quelin <jquelin@mandriva.org> 2:1.320.0-1mdv2010.0
+ Revision: 443879
- update to 1.32

* Sun Aug 30 2009 Jérôme Quelin <jquelin@mandriva.org> 2:1.300.0-1mdv2010.0
+ Revision: 422561
- update to 1.3

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 2:1.120.0-1mdv2010.0
+ Revision: 408943
- rebuild using %%perl_convert_version

* Fri Oct 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2:1.12-1mdv2009.1
+ Revision: 294622
- update to new version 1.12

* Mon Jun 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2:1.11-1mdv2009.0
+ Revision: 220137
- update to new version 1.11

* Mon Jan 14 2008 Thierry Vignaud <tv@mandriva.org> 2:1.09-2mdv2008.1
+ Revision: 151885
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2:1.09-1mdv2008.0
+ Revision: 46615
- update to new version 1.09


* Sun Jan 28 2007 Buchan Milne <bgmilne@mandriva.org> 1.08-1mdv2007.0
+ Revision: 114647
- New version 1.08

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Convert-UUlib

* Thu Dec 22 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2:1.06-1mdk
- 1.06. Bump epoch.
- more docs

* Tue May 03 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1:1.051-1mdk
- 1.051

* Wed Jan 05 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.04-1mdk
- 1.04
- Update description

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.03-2mdk
- Rebuild for new perl

* Thu Jun 03 2004 Per �yvind Karlsen <peroyvind@linux-mandrake.com> 1.03-1mdk
- 1.03
- cosmetics

* Sat Feb 28 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.3.1-5mdk
- fix DIRM (distlint)
- rebuild

