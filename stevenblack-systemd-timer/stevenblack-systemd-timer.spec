Name:           stevenblack-systemd-timer
Version:        1.0.0
Release:        1%{?dist}
Summary:        Just a test timer to update StevenBlack's hosts using podman.

License:        MIT
URL:            https://github.com/randalthor17/misc-copr-repos
Source0:        stevenblack-systemd-timer.service
Source1:        stevenblack-systemd-timer.timer

BuildRequires:  systemd-rpm-macros
Requires:       podman

%description
This is just a systemd service to update StevenBlack's hosts on a timer.

%prep
%autosetup


%install
install -Dm0644 stevenblack-systemd-timer.service %{buildroot}/%{_unitdir}
install -Dm0644 stevenblack-systemd-timer.timer %{buildroot}/%{_unitdir}

%files
%{_unitdir}/stevenblack-systemd-timer.*

%post
%systemd_post stevenblack-systemd-timer.service

%preun
%systemd_preun stevenblack-systemd-timer.service

%postun
%systemd_postun_with_reload stevenblack-systemd-timer.service

%changelog
* Tue Jan 30 2024 randalthor17 <itsmehauhon@gmail.com>
- Initial COmmit
