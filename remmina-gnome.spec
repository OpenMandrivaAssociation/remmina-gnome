Summary:	GNOME desktop applet for remmina
Name:		remmina-gnome
Version:	0.8.1
Release:	%mkrel 1
License:	GPLv2
Group:		Graphical desktop/GNOME
Url:		https://remmina.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/remmina/%{version}/%{name}-%{version}.tar.gz
Requires:	remmina >= %{version}-%{release}
BuildRequires:	gnome-panel-devel >= 2.20
BuildRequires:	avahi-client-devel
Buildrequires:	intltool >= 0.35.0
BuildRequires:  perl(XML::Parser)
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Remmina is a remote desktop client written in GTK+, aiming to be
useful for system administrators and travellers, who need to work with
lots of remote computers in front of either large monitors or tiny
netbooks. Remmina supports multiple network protocols in an integrated
and consistant user interface. Currently RDP, VNC, XDMCP and SSH are
supported.

This package contains a GNOME desktop applet for remmina.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%_bindir/remmina-applet
%_libdir/bonobo/servers/Remmina_Applet.server
%_datadir/locale/*/*/remmina-gnome.mo
