#
# specfile for node-identity package
#
# Copyright 2019-2020 Hewlett Packard Enterprise Development LP
#

%define namespace cray
%define intranamespace_name node-identity-test-crayctldeploy

%define smokedir /opt/cray/tests/uai-smoke/os/node-identity
%define resourcesdir /opt/cray/tests/uai-resources/os/node-identity

Name: %{namespace}-%{intranamespace_name}
Version: %(cat .version)
Release: %(echo ${BUILD_METADATA})
Source: %{name}-%{version}.tar.bz2
Summary: Cray Node Identity Service Tests
Group: System/Base
Vendor: Hewlett Packard Enterprise Company
License: HPE Proprietary
URL: %url
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Cray Node Identity Service Tests

%prep

%setup

%build

%check

%install
%{__mkdir_p} %{buildroot}%{smokedir}
%{__mkdir_p} %{buildroot}%{resourcesdir}
%{__install} --mode=755 tests/check_xnid.sh %{buildroot}%{resourcesdir}/check_xnid
%{__install} --mode=755 tests/compute_job.sh %{buildroot}%{resourcesdir}/compute_job
%{__install} --mode=755 tests/node_identity_smoke.sh %{buildroot}%{smokedir}/node_identity_smoke

%clean

%pre

%post

%preun

%postun

%files
%{resourcesdir}/check_xnid
%{resourcesdir}/compute_job
%{smokedir}/node_identity_smoke

