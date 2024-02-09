%global commit 42bd5f597ec8eaa2bdd87392cfc8f854eb1c15ed
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           efistub-hook
Version:        1.0.0
Release:        %autorelease
Summary:        A basic hook to generate efistub entries from rpm packages
BuildArch:      noarch
License:        WTFPL
URL:            https://github.com/randalthor17/efistub-hook
Source0:        %{URL}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

Requires:       efibootmgr
Requires:       coreutils
Requires:       util-linux
Requires:       bash
Requires:       python3-dnf-plugin-post-transaction-actions
Requires:       kernel

%description
This is a basic hook to generate efistub entries from rpm packages. It uses dnf's post-transaction-actions plugin to create and remove EFI boot entries according to kernel package names.

%prep
%autosetup -n efistub-hook-%{commit}

%build

%install
install -Dm0755 efistub.sh %{buildroot}%{_bindir}/efistub
install -Dm0644 efistub.action %{buildroot}%{_sysconfdir}/dnf/plugins/post-transaction-actions.d/efistub.action



%files
%license LICENSE
%{_bindir}/efistub
%{_sysconfdir}/dnf/plugins/post-transaction-actions.d/efistub.action


%changelog
%autochangelog

