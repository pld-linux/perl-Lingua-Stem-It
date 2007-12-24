#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Lingua
%define		pnam	Stem-It
Summary:	Lingua::Stem::It - Porter's stemming algorithm for Italian
Summary(pl.UTF-8):	Lingua::Stem::It - algorytm Portera określający rdzenie słów dla języka włoskiego
Name:		perl-Lingua-Stem-It
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Lingua/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	611ec6d600f1280aa6c510c83b7bc4a2
URL:		http://search.cpan.org/dist/Lingua-Stem-It/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module applies the Porter Stemming Algorithm to its parameters,
returning the stemmed words.

The algorithm is implemented exactly as described in:
http://snowball.tartarus.org/italian/stemmer.html .

%description -l pl.UTF-8
Ten moduł stosuje do swoich parametrów algorytm Portera określający
rdzenie słów, zwracając te rdzenie.

Zaimplementowany został algorytm opisany na stronie:
http://snowball.tartarus.org/italian/stemmer.html .

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Lingua/Stem/*.pm
%{_mandir}/man3/*
