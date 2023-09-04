Name:		python-pygdbmi
Version:	0.11.0.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pygdbmi/pygdbmi-%{version}.tar.gz
Summary:	Parse gdb machine interface output with Python
URL:		https://pypi.org/project/pygdbmi/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Parse gdb machine interface output with Python

%prep
%autosetup -p1 -n pygdbmi-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/pygdbmi
%{py_sitedir}/pygdbmi-*.*-info
