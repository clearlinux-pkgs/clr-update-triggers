Name     : clr-update-triggers
Version  : 15
Release  : 31
URL      : http://localhost/cgit/projects/clr-update-triggers/snapshot/clr-update-triggers-15.tar.gz
Source0  : http://localhost/cgit/projects/clr-update-triggers/snapshot/clr-update-triggers-15.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1

%description
No detailed description available

%prep
%setup -q -n clr-update-triggers-%{version}

%build

%install
rm -rf %{buildroot}
install -D -p -m 0755 update-helper.sh %{buildroot}/usr/bin/update-helper
install -D -p -t %{buildroot}/usr/libexec/updater -m 0755 *-hook.sh update-trigger.sh

%files
%defattr(-,root,root,-)
/usr/bin/update-helper
/usr/libexec/updater/10-fc-cache-hook.sh
/usr/libexec/updater/10-glib-schemas-hook.sh
/usr/libexec/updater/10-ldconfig-hook.sh
/usr/libexec/updater/10-locale-archive-hook.sh
/usr/libexec/updater/10-mandb-hook.sh
/usr/libexec/updater/10-motd-hook.sh
/usr/libexec/updater/10-tmpfiles-hook.sh
/usr/libexec/updater/10-trust-store-hook.sh
/usr/libexec/updater/20-graphviz-dot-hook.sh
/usr/libexec/updater/20-xdg-hook.sh
/usr/libexec/updater/update-trigger.sh
