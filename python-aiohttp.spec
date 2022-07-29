%global debug_package %{nil}

Name: python-aiohttp
Epoch: 100
Version: 3.8.0
Release: 1%{?dist}
Summary: Asynchronous HTTP client/server framework for asyncio and Python
License: Apache-2.0
URL: https://github.com/aio-libs/aiohttp/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-cython
BuildRequires: python3-devel
BuildRequires: python3-idna-ssl >= 1.0
BuildRequires: python3-setuptools

%description
Python HTTP client/server for asyncio which supports both the client and
the server side of the HTTP protocol, client and server websocket, and
webservers with middlewares and pluggable routing.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-aiohttp
Summary: Asynchronous HTTP client/server framework for asyncio and Python
Requires: python3
Requires: python3-aiosignal >= 1.1.2
Requires: python3-async-timeout >= 4.0
Requires: python3-asynctest >= 0.13.0
Requires: python3-attrs >= 17.3.0
Requires: python3-charset-normalizer >= 2.0
Requires: python3-frozenlist >= 1.1.1
Requires: python3-idna-ssl >= 1.0
Requires: python3-multidict >= 4.5
Requires: python3-typing-extensions >= 3.7.4
Requires: python3-yarl >= 1.0
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
Requires: python3-aiosignal >= 1.1.2
Requires: python3-async-timeout >= 4.0
Requires: python3-asynctest >= 0.13.0
Requires: python3-attrs >= 17.3.0
Requires: python3-charset-normalizer >= 2.0
Requires: python3-frozenlist >= 1.1.1
Requires: python3-idna-ssl >= 1.0
Requires: python3-multidict >= 4.5
Requires: python3-typing-extensions >= 3.7.4
Requires: python3-yarl >= 1.0
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
