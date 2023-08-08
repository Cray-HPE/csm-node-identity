#
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
Name: %(echo $NAME)
Version: %(echo $VERSION)
Release: 1
Source: %{name}-%{version}.tar.bz2
Summary: CSM Node Identity Service
Group: System/Management
Vendor: Hewlett Packard Enterprise Company
License: MIT
BuildArchitectures: noarch
BuildRequires: systemd
Requires: iproute2
Obsoletes: cray-node-identity
Conflicts: cray-node-identity
Provides: cray-node-identity

%{!?_unitdir:
%define _unitdir /usr/lib/systemd/system
 }

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
%if 0%{?suse_version}
echo "install suse" >> %{buildroot}/rpms.txt
%else
echo "install non-suse" >> %{buildroot}/rpms.txt
%endif

%files
%defattr(-,root,root)
%if 0%{?prefixdirs:1}
%{prefixdirs}
%dir %{_sbindir}
%endif
%{_unitdir}/csm-node-identity.service
%{_sbindir}/csm-node-identity.sh
rpms.txt

%clean

%pre
%if 0%{?suse_version}
echo "clean pre suse" >> %{buildroot}/rpms.txt
%service_add_pre csm-node-identity.service
%endif

%post
%if 0%{?suse_version}
echo "clean post suse" >> %{buildroot}/rpms.txt
%service_add_post csm-node-identity.service
%else
echo "clean post non-suse" >> %{buildroot}/rpms.txt
%systemd_post csm-node-identity.service
%endif

%preun
%if 0%{?suse_version}
echo "clean preun suse" >> %{buildroot}/rpms.txt
%service_del_preun csm-node-identity.service
%else
echo "clean preun non-suse" >> %{buildroot}/rpms.txt
%systemd_preun csm-node-identity.service
%endif

%postun
%if 0%{?suse_version}
echo "clean postun suse" >> %{buildroot}/rpms.txt
%service_del_postun csm-node-identity.service
%else
echo "clean postun non-suse" >> %{buildroot}/rpms.txt
%systemd_postun_with_restart csm-node-identity.service
%endif

