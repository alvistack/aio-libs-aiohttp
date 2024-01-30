# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-aiohttp
Epoch: 100
Version: 3.11.7
Release: 1%{?dist}
Summary: Asynchronous HTTP client/server framework for asyncio and Python
License: Apache-2.0
URL: https://github.com/aio-libs/aiohttp/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python3-Cython3
BuildRequires: python3-devel
BuildRequires: python3-multidict >= 4.5
BuildRequires: python3-pip
BuildRequires: python3-setuptools
BuildRequires: python-rpm-macros

%description
Python HTTP client/server for asyncio which supports both the client and
the server side of the HTTP protocol, client and server websocket, and
webservers with middlewares and pluggable routing.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
mkdir -p .git
make cythonize
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
    .

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-aiohttp
Summary: Asynchronous HTTP client/server framework for asyncio and Python
Requires: python3
Requires: python3-aiohappyeyeballs >= 2.3.0
Requires: python3-aiosignal >= 1.1.2
Requires: python3-async-timeout >= 4.0
Requires: python3-attrs >= 17.3.0
Requires: python3-frozenlist >= 1.1.1
Requires: python3-multidict >= 4.5
Requires: python3-propcache >= 0.2.0
Requires: python3-yarl >= 1.17.0
Provides: python3-aiohttp = %{epoch}:%{version}-%{release}
Provides: python3dist(aiohttp) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-aiohttp = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(aiohttp) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-aiohttp = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(aiohttp) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-aiohttp
Python HTTP client/server for asyncio which supports both the client and
the server side of the HTTP protocol, client and server websocket, and
webservers with middlewares and pluggable routing.

%files -n python%{python3_version_nodots}-aiohttp
%license LICENSE.txt
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-aiohttp
Summary: Asynchronous HTTP client/server framework for asyncio and Python
Requires: python3
Requires: python3-aiohappyeyeballs >= 2.3.0
Requires: python3-aiosignal >= 1.1.2
Requires: python3-async-timeout >= 4.0
Requires: python3-attrs >= 17.3.0
Requires: python3-frozenlist >= 1.1.1
Requires: python3-multidict >= 4.5
Requires: python3-propcache >= 0.2.0
Requires: python3-yarl >= 1.17.0
Provides: python3-aiohttp = %{epoch}:%{version}-%{release}
Provides: python3dist(aiohttp) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-aiohttp = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(aiohttp) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-aiohttp = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(aiohttp) = %{epoch}:%{version}-%{release}

%description -n python3-aiohttp
Python HTTP client/server for asyncio which supports both the client and
the server side of the HTTP protocol, client and server websocket, and
webservers with middlewares and pluggable routing.

%files -n python3-aiohttp
%license LICENSE.txt
%{python3_sitearch}/*
%endif

%changelog
