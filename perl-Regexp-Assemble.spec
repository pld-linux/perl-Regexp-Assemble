#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Regexp
%define	pnam	Assemble
Summary:	Regexp::Assemble - Assemble multiple Regular Expressions into a single RE
#Summary(pl.UTF-8):	
Name:		perl-Regexp-Assemble
Version:	0.38
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/R/RS/RSAVAGE/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	75905c73b33c123ce085fd7d194dd95e
URL:		http://search.cpan.org/dist/Regexp-Assemble/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Regexp::Assemble takes an arbitrary number of regular expressions
and assembles them into a single regular expression (or RE) that
matches all that the individual REs match.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes TODO
%{perl_vendorlib}/Regexp/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
