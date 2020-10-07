#
# specfile for node-identity package
#
# Copyright 2019-2020 Hewlett Packard Enterprise Development LP
#

%define namespace cray
%define intranamespace_name node-identity

Name: %{namespace}-%{intranamespace_name}
Version: %(cat .version)
Release: %(echo ${BUILD_METADATA})
Source: %{name}-%{version}.tar.bz2
Summary: Cray Node Identity Script 
Group: System/Base
Vendor: Hewlett Packard Enterprise Company
License: HPE Proprietary
URL: %url
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Requires: iproute2

%systemd_requires

%description
Cray Systemd Node Identity Service 

%prep

%setup

%build

%check

%install
%{__mkdir_p} %{buildroot}%{_unitdir}
%{__mkdir_p} %{buildroot}%{_sbindir}
%{__install} -m 0644 src/cray-node-identity.service %{buildroot}%{_unitdir}/cray-node-identity.service
%{__install} -m 0755 src/cray-node-identity.sh %{buildroot}%{_sbindir}/cray-node-identity.sh

%files
%defattr(-,root,root)
%if 0%{?prefixdirs:1}
%{prefixdirs}
%dir %{_sbindir}
%endif
%{_unitdir}/cray-node-identity.service
%{_sbindir}/cray-node-identity.sh

%clean

%pre
%if 0%{?suse_version}
%service_add_pre cray-node-identity.service
%endif

%post
%if 0%{?suse_version}
%service_add_post cray-node-identity.service
%else
%systemd_post cray-node-identity.service
%endif

%preun
%if 0%{?suse_version}
%service_del_preun cray-node-identity.service
%else
%systemd_preun cray-node-identity.service
%endif

%postun
%if 0%{?suse_version}
%service_del_postun cray-node-identity.service
%else
%systemd_postun_with_restart cray-node-identity.service
%endif

