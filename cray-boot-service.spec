#
# specfile for boot-service package
#
# Copyright 2018 Cray Inc. All Rights Reserved.
#

%define namespace cray
%define intranamespace_name boot-service

Name: %{namespace}-%{intranamespace_name}
Version: 0.1.1
Release: 1 
Source: %{name}-%{version}.tar.bz2
Summary: Cray Boot Service Script 
Group: System/Base
License: Cray Software License Agreement
URL: %url
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%systemd_requires

%description
Cray Systemd Boot Service 

%prep

%setup

%build

%check

%install
%{__mkdir_p} %{buildroot}%{_unitdir}
%{__mkdir_p} %{buildroot}%{_sbindir}
%{__install} -m 0644 src/cray-boot.service %{buildroot}%{_unitdir}/cray-boot.service
%{__install} -m 0755 src/cray-boot.sh %{buildroot}%{_sbindir}/cray-boot.sh

%{__mkdir_p} %{buildroot}/opt/cray/tests/uai-smoke/os/boot_service
%{__mkdir_p} %{buildroot}/opt/cray/tests/uai-resources/os/boot_service
%{__install} --mode=755 tests/check_xnid.sh %{buildroot}/opt/cray/tests/uai-resources/os/boot_service/check_xnid
%{__install} --mode=755 tests/compute_job.sh %{buildroot}/opt/cray/tests/uai-resources/os/boot_service/compute_job
%{__install} --mode=755 tests/boot_service_smoke.sh %{buildroot}/opt/cray/tests/uai-smoke/os/boot_service/boot_service_smoke

%files
%defattr(-,root,root)
%if 0%{?prefixdirs:1}
%{prefixdirs}
%dir %{_sbindir}
%endif
%{_unitdir}/cray-boot.service
%{_sbindir}/cray-boot.sh

%clean

%pre
%if 0%{?suse_version}
%service_add_pre cray-boot.service
%endif

%post
%if 0%{?suse_version}
%service_add_post cray-boot.service
%else
%systemd_post cray-boot.service
%endif

%preun
%if 0%{?suse_version}
%service_del_preun cray-boot.service
%else
%systemd_preun cray-boot.service
%endif

%postun
%if 0%{?suse_version}
%service_del_postun cray-boot.service
%else
%systemd_postun_with_restart cray-boot.service
%endif

# The package ends with the name "crayctldeploy" because the SMS installer
# will automatically install it. Otherwise an ansible role has to be written
# to install it.
%package test-crayctldeploy

Summary: Basic Functionality Tests of the Boot Service

%description test-crayctldeploy
Cray Boot Service Tests

%files test-crayctldeploy
/opt/cray/tests/uai-resources/os/boot_service/check_xnid
/opt/cray/tests/uai-resources/os/boot_service/compute_job
/opt/cray/tests/uai-smoke/os/boot_service/boot_service_smoke

