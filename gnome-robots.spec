Summary:	GNOME Robots game
Summary(pl.UTF-8):	Gra Robots dla GNOME
Name:		gnome-robots
Version:	40.0
Release:	2
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	https://download.gnome.org/sources/gnome-robots/40/%{name}-%{version}.tar.xz
# Source0-md5:	041b5df6329df23434edb267bafab3eb
URL:		https://wiki.gnome.org/Apps/Robots
BuildRequires:	appstream-glib
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gsound-devel >= 1.0.2
BuildRequires:	gtk+3-devel >= 3.24.0
BuildRequires:	libgee-devel >= 0.8
BuildRequires:	libgnome-games-support-devel >= 1.7.1
BuildRequires:	librsvg-devel >= 2.36.2
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala
BuildRequires:	vala-gsound >= 1.0.2
BuildRequires:	vala-libgee >= 0.8
BuildRequires:	vala-libgnome-games-support >= 1.7.1
BuildRequires:	vala-librsvg >= 2.36.2
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.32.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.32.0
Requires:	gsound >= 1.0.2
Requires:	gtk+3 >= 3.24.0
Requires:	hicolor-icon-theme
Requires:	libgee >= 0.8
Requires:	libgnome-games-support >= 1.7.1
Requires:	librsvg >= 2.36.2
Provides:	gnome-games-gnobots2 = 1:%{version}-%{release}
Obsoletes:	gnome-games-gnobots2 < 1:3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Robots is the classic robots game where you have to avoid the
robots and make them crash into each other.

%description -l pl.UTF-8
GNOME Robots to klasyczna gra z robotami, polegająca na unikaniu ich i
powodowaniu, żeby zderzały się ze sobą wzajemnie.

%prep
%setup -q

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
%doc NEWS
%attr(755,root,root) %{_bindir}/gnome-robots
%{_datadir}/dbus-1/services/org.gnome.Robots.service
%{_datadir}/glib-2.0/schemas/org.gnome.Robots.gschema.xml
%{_datadir}/gnome-robots
%{_datadir}/metainfo/org.gnome.Robots.appdata.xml
%{_desktopdir}/org.gnome.Robots.desktop
%{_iconsdir}/hicolor/24x24/actions/teleport*.png
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Robots.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Robots-symbolic.svg
%{_mandir}/man6/gnome-robots.6*
