#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Lingua
%define	pnam	Stem-It
Summary:	Lingua::Stem::It - Porter's stemming algorithm for Italian
Summary(pl):	Lingua::Stem::It - algorytm Portera okre¶laj±cy rdzenie s³ów dla jêzyka w³oskiego
Name:		perl-Lingua-Stem-It
Version:	0.01
Release:	2
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b06d70d6ce3763bb33b4d9f3c04b996f
BuildRequires:	perl >= 5.8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module applies the Porter Stemming Algorithm to its parameters,
returning the stemmed words.

The algorithm is implemented exactly as described in:
http://snowball.tartarus.org/italian/stemmer.html .

%description -l pl
Ten modu³ stosuje do swoich parametrów algorytm Portera okre¶laj±cy
rdzenie s³ów, zwracaj±c te rdzenie.

Zaimplementowany zosta³ algorytm opisany na stronie:
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

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Lingua/Stem/*.pm
%{_mandir}/man3/*
