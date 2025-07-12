# TODO: use gtk4-update-icon-cache
Summary:	GNOME Robots game
Summary(pl.UTF-8):	Gra Robots dla GNOME
Name:		gnome-robots
Version:	41.2
Release:	2
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	https://download.gnome.org/sources/gnome-robots/41/%{name}-%{version}.tar.xz
# Source0-md5:	8ec5ea7ebbf13d5d979a45374c3146f1
# cargo vendor-filterer --platform='*-unknown-linux-*' --tier=2
Source1:	%{name}-%{version}-vendor.tar.xz
# Source1-md5:	a8363d25faeba46f227d474ef6154234
Patch0:		%{name}-x32.patch
Patch1:		%{name}-no-scripts.patch
URL:		https://wiki.gnome.org/Apps/Robots
BuildRequires:	appstream-glib
BuildRequires:	cargo
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.82
BuildRequires:	gtk4-devel >= 4.16.1
BuildRequires:	libadwaita-devel >= 1.6
BuildRequires:	librsvg-devel >= 2.59.2
BuildRequires:	meson >= 0.59
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	rust
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala
BuildRequires:	vala-librsvg >= 2.59.2
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.82
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.82
Requires:	gtk4 >= 4.16.1
Requires:	hicolor-icon-theme
Requires:	libadwaita >= 1.6
Requires:	librsvg >= 2.59.2
Provides:	gnome-games-gnobots2 = 1:%{version}-%{release}
Obsoletes:	gnome-games-gnobots2 < 1:3.8.0
ExclusiveArch:	%{x8664} %{ix86} x32 aarch64 armv6hl armv7hl armv7hnl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Robots is the classic robots game where you have to avoid the
robots and make them crash into each other.

%description -l pl.UTF-8
GNOME Robots to klasyczna gra z robotami, polegająca na unikaniu ich i
powodowaniu, żeby zderzały się ze sobą wzajemnie.

%prep
%setup -q -b1
%ifarch x32
%patch -P0 -p1
%endif
%patch -P1 -p1

# use offline registry
CARGO_HOME="$(pwd)/.cargo"

mkdir -p "$CARGO_HOME"
cat >$CARGO_HOME/config.toml <<EOF
[source.crates-io]
replace-with = 'vendored-sources'

[source.vendored-sources]
directory = '$PWD/vendor'
EOF

%build
%ifarch x32
export PKG_CONFIG_ALLOW_CROSS=1
%endif
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%ifarch x32
export PKG_CONFIG_ALLOW_CROSS=1
%endif
%meson_install

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-robots
%{_datadir}/dbus-1/services/org.gnome.Robots.service
%{_datadir}/glib-2.0/schemas/org.gnome.Robots.gschema.xml
%{_datadir}/gnome-robots
%{_datadir}/metainfo/org.gnome.Robots.metainfo.xml
%{_desktopdir}/org.gnome.Robots.desktop
%{_iconsdir}/hicolor/24x24/actions/teleport*.png
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Robots.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Robots-symbolic.svg
%{_mandir}/man6/gnome-robots.6*
