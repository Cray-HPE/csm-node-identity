# Copyright 2020-2021 Hewlett Packard Enterprise Development LP
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# (MIT License)
%define namespace csm
%define intranamespace_name node-identity

Name: %{namespace}-%{intranamespace_name}
Version: %(cat .version)
Release: %(echo ${BUILD_METADATA})
Source: %{name}-%{version}.tar.bz2
Summary: CSM Node Identity Service
Group: System/Management
Vendor: Hewlett Packard Enterprise Company
License: MIT
URL: %url
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Requires: iproute2

%systemd_requires

%description
Cray System Management (CSM) systemd Node Identity Service 

%prep

%setup

%build

%check

%install
%{__mkdir_p} %{buildroot}%{_unitdir}
%{__mkdir_p} %{buildroot}%{_sbindir}
%{__install} -m 0644 src/csm-node-identity.service %{buildroot}%{_unitdir}/csm-node-identity.service
%{__install} -m 0755 src/csm-node-identity.sh %{buildroot}%{_sbindir}/csm-node-identity.sh

%files
%defattr(-,root,root)
%if 0%{?prefixdirs:1}
%{prefixdirs}
%dir %{_sbindir}
%endif
%{_unitdir}/csm-node-identity.service
%{_sbindir}/csm-node-identity.sh

%clean

%pre
%if 0%{?suse_version}
%service_add_pre csm-node-identity.service
%endif

%post
%if 0%{?suse_version}
%service_add_post csm-node-identity.service
%else
%systemd_post csm-node-identity.service
%endif

%preun
%if 0%{?suse_version}
%service_del_preun csm-node-identity.service
%else
%systemd_preun csm-node-identity.service
%endif

%postun
%if 0%{?suse_version}
%service_del_postun csm-node-identity.service
%else
%systemd_postun_with_restart csm-node-identity.service
%endif

