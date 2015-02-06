%define real_name FileHandle-Rollback

Summary:	FileHandle-Rollback module for perl 
Name:		perl-%{real_name}
Version:	1.06
Release:	6
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
FileHandle::Rollback allows you to open a filehandle, write data to that
handle, read the data back exactly as if it were already in the file,
then cancel the whole transaction if you choose.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/FileHandle/Rollback.pm
%{_mandir}/*/*




%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.06-4mdv2010.0
+ Revision: 430456
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.06-3mdv2009.0
+ Revision: 256938
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.06-1mdv2008.1
+ Revision: 135841
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-1mdv2008.0
+ Revision: 63956
- update to new version 1.06


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 1.05-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.05-1mdk
- initial Mandriva package

