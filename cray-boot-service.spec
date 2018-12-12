#
# specfile for boot-service package
#
# Copyright 2018 Cray Inc. All Rights Reserved.
#

%define namespace cray
%define intranamespace_name boot-service

Name: %{namespace}-%{intranamespace_name}
Version: 0.1.0 
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
%{__mkdir_p} %{buildroot}%{_presetdir}
%{__mkdir_p} %{buildroot}%{_sbindir}
%{__install} -m 0644 src/cray-boot.service %{buildroot}%{_unitdir}/cray-boot.service
%{__install} -m 0644 src/80-crayboot.preset %{buildroot}%{_presetdir}/80-crayboot.preset
%{__install} -m 0755 src/cray-boot.sh %{buildroot}%{_sbindir}/cray-boot.sh

%files
%defattr(-,root,root)
%if 0%{?prefixdirs:1}
%{prefixdirs}
%dir %{_sbindir}
%endif
%{_unitdir}/cray-boot.service
%{_presetdir}/80-crayboot.preset
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

