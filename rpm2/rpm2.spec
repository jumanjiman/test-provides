Name:		rpm2
Version:	1.2.200
Release:	1%{?dist}
Summary:	test with crazy numbering

Group:		System Environment/Base
License:	GPLv3+
URL:		https://github.com/jumanjiman/test-provides
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

obsoletes:	rpm1 < %{version}-%{release}
provides:	rpm1 = %{version}-%{release}


%description
this package is being used to test obsoletes/provides.
in particular, this package hopefully obsoletes a package
having a crazy NVR.


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

