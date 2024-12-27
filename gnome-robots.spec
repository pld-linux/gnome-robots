# TODO: use gtk4-update-icon-cache
Summary:	GNOME Robots game
Summary(pl.UTF-8):	Gra Robots dla GNOME
Name:		gnome-robots
Version:	41.1
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	https://download.gnome.org/sources/gnome-robots/41/%{name}-%{version}.tar.xz
# Source0-md5:	150d940aa6f8d8267ed62144dbe5b899
Source1:	%{name}-%{version}-vendor.tar.xz
# Source1-md5:	9ca0e4a67c0646ba3c759438218327bd
URL:		https://wiki.gnome.org/Apps/Robots
BuildRequires:	appstream-glib
BuildRequires:	cargo
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.36
BuildRequires:	gtk4-devel >= 4.10.0
BuildRequires:	libadwaita-devel >= 1.2
BuildRequires:	librsvg-devel >= 2.36.2
BuildRequires:	meson >= 0.59
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	rust
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala
BuildRequires:	vala-librsvg >= 2.36.2
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.36
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.36
Requires:	gtk4 >= 4.10.0
Requires:	hicolor-icon-theme
Requires:	libadwaita >= 1.2
Requires:	librsvg >= 2.36.2
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

# use offline registry
CARGO_HOME="$(pwd)/.cargo"

mkdir -p "$CARGO_HOME"
cat >$CARGO_HOME/config <<EOF
[source.crates-io]
replace-with = 'vendored-sources'

[source.vendored-sources]
directory = '$PWD/vendor'
EOF

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
