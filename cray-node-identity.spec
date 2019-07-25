#
# specfile for node-identity package
#
# Copyright 2019 Cray Inc. All Rights Reserved.
#

%define namespace cray
%define intranamespace_name node-identity

Name: %{namespace}-%{intranamespace_name}
Version: 0.2.%(echo $BUILD_NUMBER)
Release: 1 
Source: %{name}-%{version}.tar.bz2
Summary: Cray Node Identity Script 
Group: System/Base
License: Cray Software License Agreement
URL: %url
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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

%{__mkdir_p} %{buildroot}/opt/cray/tests/uai-smoke/os/node_identity
%{__mkdir_p} %{buildroot}/opt/cray/tests/uai-resources/os/node_identity
%{__install} --mode=755 tests/check_xnid.sh %{buildroot}/opt/cray/tests/uai-resources/os/node_identity/check_xnid
%{__install} --mode=755 tests/compute_job.sh %{buildroot}/opt/cray/tests/uai-resources/os/node_identity/compute_job
%{__install} --mode=755 tests/node_identity_smoke.sh %{buildroot}/opt/cray/tests/uai-smoke/os/node_identity/node_identity_smoke

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

# The package ends with the name "crayctldeploy" because the SMS installer
# will automatically install it. Otherwise an ansible role has to be written
# to install it.
%package test-crayctldeploy

Summary: Basic Functionality Tests of the Node Identity Service

%description test-crayctldeploy
Cray Node Identity Service Tests

%files test-crayctldeploy
/opt/cray/tests/uai-resources/os/node_identity/check_xnid
/opt/cray/tests/uai-resources/os/node_identity/compute_job
/opt/cray/tests/uai-smoke/os/node_identity/node_identity_smoke

