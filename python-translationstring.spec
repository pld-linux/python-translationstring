#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	translationstring
Summary:	Utility library for i18n relied on by various Repoze and Pyramid packages
Name:		python-%{module}
Version:	1.1
Release:	3
License:	BSD-like (http://repoze.org/license.html)
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/t/translationstring/%{module}-%{version}.tar.gz
# Source0-md5:	0979b46d8f0f852810c8ec4be5c26cf2
URL:		http://pypi.python.org/pypi/translationstring
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
library used by various Pylons Project packages for
internationalization (i18n) duties related to translation.

This package provides a translation string class, a translation string
factory class, translation and pluralization primitives, and a utility
that helps Chameleon templates use translation facilities of this
package. It does not depend on Babel, but its translation and
pluralization services are meant to work best when provided with an
instance of the babel.support.Translations class.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/tests

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt README.txt
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
