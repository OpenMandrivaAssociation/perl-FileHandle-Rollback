%define real_name FileHandle-Rollback

Summary:	FileHandle-Rollback module for perl 
Name:		perl-%{real_name}
Version:	1.06
Release:	%mkrel 4
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


