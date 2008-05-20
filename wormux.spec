Summary:	A free (libre) clone of Worms from Team17
Summary(de.UTF-8):	Ein kostenloser Team17 Worms-Klon
Summary(pl.UTF-8):	Wolnodostępny klon Worms z Team17
Name:		wormux
Version:	0.8
Release:	0.1
License:	GPL v2+
Group:		Applications/Games
Source0:	http://download.gna.org/wormux/%{name}-%{version}.tar.bz2
# Source0-md5:	79400ddcb2e9fdfcd4145c62940a24d3
Patch0:		%{name}-disable-werror.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.wormux.org/en/index.php
BuildRequires:	SDL-devel >= 1.2.6
BuildRequires:	SDL_gfx-devel >= 2.0.13
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel >= 7.16.4-2
BuildRequires:	gettext-devel
BuildRequires:	libpng-devel
BuildRequires:	libxml++-devel >= 2.6
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free (libre) clone of Worms from Team17.

%description -l de.UTF-8
Ein kostenloser Team17 Worms-Klon.

%description -l pl.UTF-8
Wolnodostępny klon gry Worms z Team17.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# disable building unsupported locale
sed -i -e 's|cpf||g' po/LINGUAS

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--with-datadir-name=%{_datadir}/games/%{name} 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# rename pixmap
mv -f $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}_128x128.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README 
%attr(755,root,root) %{_bindir}/wormux
%{_datadir}/games/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_mandir}/man6/wormux.6*
