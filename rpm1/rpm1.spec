Name:		rpm1
Version:	001.002.000
Release:	4%{?dist}
Summary:	test with crazy numbering

Group:		System Environment/Base
License:	GPLv3+
URL:		https://github.com/jumanjiman/test-provides
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch


%description
this package is being used to test obsoletes/provides.
in particular, this package has a crazy NVR.


%prep
%setup -q


%build


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)



%changelog
* Mon Feb 28 2011 Paul Morgan <jumanjiman@gmail.com> 001.002.000-4
- new package built with tito


