Name:           genhosts
Version:        1.0.0
Release:        %autorelease
Summary:        A simple program to generate hosts file from specified blocklist URLs

License:        MIT
URL:            https://github.com/randalthor17/genhosts
Source0:        %{URL}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  libcurl-devel
Buildrequires:  gcc-c++
BuildRequires:  cxxopts-devel
Requires:       libcurl

%description
%{summary}.

%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install


%files
%license LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog

