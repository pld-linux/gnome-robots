Summary:	GNOME Robots
Summary(pl.UTF-8):	Robots dla GNOME
Name:		gnome-robots
Version:	3.12.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-robots/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	effb662c3476131ac543b563febbdcd0
URL:		https://wiki.gnome.org/Apps/Robots
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.4.0
BuildRequires:	intltool >= 0.50.0
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	librsvg-devel >= 2.32.0
BuildRequires:	pkgconfig
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	gtk+3 >= 3.4.0
Requires:	hicolor-icon-theme
Requires:	libcanberra-gtk3 >= 0.26
Requires:	librsvg >= 2.32.0
Provides:	gnome-games-gnobots2 = 1:%{version}-%{release}
Obsoletes:	gnome-games-gnobots2 < 1:3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Avoid the robots and make them crash into each other.

%description -l pl.UTF-8
Gra polegająca na zapobieganiu zderzeniom robotów.

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
%update_icon_cache HighContrast
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache HighContrast
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/gnome-robots
%{_datadir}/appdata/gnome-robots.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.robots.gschema.xml
%{_datadir}/gnome-robots
%{_desktopdir}/gnome-robots.desktop
%{_iconsdir}/HighContrast/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man6/gnome-robots.6*
