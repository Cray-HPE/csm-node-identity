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
wall "install 0%{?suse_version} suse"
%else
%if 0%{?sle_version}
wall "install 0%{?suse_version} sle"
%else
wall "install 0%{?suse_version} non-suse"
%endif
%endif

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
wall "clean pre 0%{?suse_version} 0%{?sle_version} suse"
%service_add_pre csm-node-identity.service
%else
%if 0%{?sle_version}
wall "clean pre 0%{?suse_version} 0%{?sle_version} sle"
%service_add_pre csm-node-identity.service
%endif
%endif

%post
%if 0%{?suse_version}
wall "clean post 0%{?suse_version} 0%{?sle_version} suse"
%service_add_post csm-node-identity.service
%else
%if 0%{?sle_version}
wall "clean post 0%{?suse_version} 0%{?sle_version} sle"
%service_add_post csm-node-identity.service
%else
wall "clean post 0%{?suse_version} 0%{?sle_version} non-suse"
%systemd_post csm-node-identity.service
%endif
%endif

%preun
%if 0%{?suse_version}
wall "clean preun 0%{?suse_version} 0%{?sle_version} suse"
%service_del_preun csm-node-identity.service
%else
%if 0%{?sle_version}
wall "clean preun 0%{?suse_version} 0%{?sle_version} sle"
%service_del_preun csm-node-identity.service
%else
wall "clean preun 0%{?suse_version} 0%{?sle_version} non-sue"
%systemd_preun csm-node-identity.service
%endif
%endif

%postun
%if 0%{?suse_version}
wall "clean postun 0%{?suse_version} 0%{?sle_version} suse"
%service_del_postun csm-node-identity.service
%else
%if 0%{?sle_version}
wall "clean postun 0%{?suse_version} 0%{?sle_version} sle"
%service_del_postun csm-node-identity.service
%else
wall "clean postun 0%{?suse_version} 0%{?sle_version} non-suse"
%systemd_postun_with_restart csm-node-identity.service
%endif
%endif
