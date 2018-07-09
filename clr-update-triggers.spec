Name     : clr-update-triggers
Version  : 10
Release  : 24
URL      : http://localhost/cgit/projects/clr-update-triggers/snapshot/clr-update-triggers-10.tar.gz
Source0  : http://localhost/cgit/projects/clr-update-triggers/snapshot/clr-update-triggers-10.tar.gz
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
install -D -m 0755 update-helper.sh %{buildroot}/usr/bin/update-helper
install -D -m 0755 10-glib-schemas-hook.sh %{buildroot}/usr/libexec/updater/10-glib-schemas-hook.sh
install -D -m 0755 10-ldconfig-hook.sh %{buildroot}/usr/libexec/updater/10-ldconfig-hook.sh
install -D -m 0755 10-mandb-hook.sh %{buildroot}/usr/libexec/updater/10-mandb-hook.sh
install -D -m 0755 10-fc-cache-hook.sh %{buildroot}/usr/libexec/updater/10-fc-cache-hook.sh
install -D -m 0755 10-motd-hook.sh %{buildroot}/usr/libexec/updater/10-motd-hook.sh
install -D -m 0755 10-tmpfiles-hook.sh %{buildroot}/usr/libexec/updater/10-tmpfiles-hook.sh
install -D -m 0755 10-trust-store-hook.sh %{buildroot}/usr/libexec/updater/10-trust-store-hook.sh
install -D -m 0755 20-graphviz-dot-hook.sh %{buildroot}/usr/libexec/updater/20-graphviz-dot-hook.sh
install -D -m 0755 update-trigger.sh %{buildroot}/usr/libexec/updater/update-trigger.sh

%files
%defattr(-,root,root,-)
/usr/bin/update-helper
/usr/libexec/updater/10-glib-schemas-hook.sh
/usr/libexec/updater/10-ldconfig-hook.sh
/usr/libexec/updater/10-mandb-hook.sh
/usr/libexec/updater/10-fc-cache-hook.sh
/usr/libexec/updater/10-motd-hook.sh
/usr/libexec/updater/10-tmpfiles-hook.sh
/usr/libexec/updater/10-trust-store-hook.sh
/usr/libexec/updater/20-graphviz-dot-hook.sh
/usr/libexec/updater/update-trigger.sh
