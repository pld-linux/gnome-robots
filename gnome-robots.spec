Summary:	GNOME Robots game
Summary(pl.UTF-8):	Gra Robots dla GNOME
Name:		gnome-robots
Version:	3.22.1
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-robots/3.22/%{name}-%{version}.tar.xz
# Source0-md5:	adc8b1ddfff21e344eb461db0785eb08
URL:		https://wiki.gnome.org/Apps/Robots
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gtk+3-devel >= 3.15.0
BuildRequires:	intltool >= 0.50.0
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	libgnome-games-support-devel >= 1.0
BuildRequires:	librsvg-devel >= 2.36.2
BuildRequires:	pkgconfig
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.32.0
Requires:	glib2 >= 1:2.32.0
Requires:	gtk+3 >= 3.15.0
Requires:	hicolor-icon-theme
Requires:	libcanberra-gtk3 >= 0.26
Requires:	libgnome-games-support >= 1.0
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
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_datadir}/appdata/gnome-robots.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.robots.gschema.xml
%{_datadir}/gnome-robots
%{_desktopdir}/gnome-robots.desktop
%{_iconsdir}/hicolor/24x24/actions/teleport*.png
%{_iconsdir}/hicolor/*x*/apps/gnome-robots.png
%{_iconsdir}/hicolor/scalable/apps/gnome-robots.svg
%{_iconsdir}/hicolor/scalable/apps/gnome-robots-symbolic.svg
%{_mandir}/man6/gnome-robots.6*
