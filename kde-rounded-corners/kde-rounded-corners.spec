Name:           kde-rounded-corners
Version:        0.6.0
Release:        1%{?dist}
Summary:        Rounds the corners of your windows in KDE Plasma 5 and 6.

License:        GPL-3.0
URL:            https://github.com/matinlotfali/KDE-Rounded-Corners
Source0:        %{URL}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kwin-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  libepoxy-devel
Requires:       kwin
Requires:       libepoxy
Requires:       kf5-kconfigwidgets

%description
This effect rounds the corners of your windows and adds an outline around them without much affecting the performance of the KDE Plasma desktop.

%prep
%autosetup


%build
%cmake
%cmake_build


%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%{_libdir}/plugins/kwin/effects/*
%{_datadir}/kwin/shaders/*


%changelog
* Wed Feb 07 2024 randalthor17 <itsmehauhon@gmail.com>
- Initial commit
