# TODO: use gtk4-update-icon-cache
Summary:	GNOME Robots game
Summary(pl.UTF-8):	Gra Robots dla GNOME
Name:		gnome-robots
Version:	50.0
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	https://download.gnome.org/sources/gnome-robots/50/%{name}-%{version}.tar.xz
# Source0-md5:	e52ae50ac6585690fb36210b99f094cb
# cargo vendor-filterer --platform='*-unknown-linux-*' --tier=2
Source1:	%{name}-%{version}-vendor.tar.xz
# Source1-md5:	f3c78ba7ef064d82b54006b86814fc73
Patch0:		%{name}-x32.patch
Patch1:		%{name}-no-scripts.patch
URL:		https://wiki.gnome.org/Apps/Robots
# appstreamcli
BuildRequires:	AppStream
BuildRequires:	cargo
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.86
BuildRequires:	glycin-devel >= 2.0
BuildRequires:	glycin-gtk4-devel >= 2.0
BuildRequires:	gtk4-devel >= 4.20.0
BuildRequires:	libadwaita-devel >= 1.8
BuildRequires:	meson >= 0.59
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	rust >= 1.92
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.86
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.86
Requires:	gtk4 >= 4.20.0
Requires:	hicolor-icon-theme
Requires:	libadwaita >= 1.8
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
%setup -q -a1
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
