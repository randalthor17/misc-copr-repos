Name:           neovide
Version:        0.12.2
Release:        1%{?dist}
Summary:        No Nonsense Neovim Client in Rust
License:        MIT
URL:            https://github.com/neovide/neovide
Source0:        %{URL}/archive/refs/tags/%{version}.tar.gz


# Tools
BuildRequires:  cargo
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++

# Libraries
BuildRequires:  SDL2-devel
BuildRequires:  expat-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  libXext-devel
BuildRequires:  openssl-devel
BuildRequires:  vulkan-devel

# Base
Requires:       google-noto-sans-mono-fonts
Requires:       neovim >= 0.6.0

# Libraries
Requires:       SDL2
Requires:       expat
Requires:       fontconfig
Requires:       freetype
Requires:       libXext
Requires:       openssl
Requires:       vulkan

%description

This is a simple graphical user interface for Neovim. Where possible there are
some graphical improvements, but it should act functionally like the terminal
UI.

%prep
%autosetup


%build
cargo build --release --verbose


%install
install -Dm0755 'target/release/neovide' "%{buildroot}%{_bindir}/neovide"
install -Dm0644 'assets/neovide.svg' "%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/neovide.svg"
desktop-file-install --dir="%{buildroot}%{_datadir}/applications" 'assets/neovide.desktop'
desktop-file-validate "%{buildroot}%{_datadir}/applications/neovide.desktop"


%files
%license LICENSE
%{_bindir}/neovide
%{_datadir}/icons/hicolor/scalable/apps/neovide.svg
%{_datadir}/applications/neovide.desktop


%changelog
