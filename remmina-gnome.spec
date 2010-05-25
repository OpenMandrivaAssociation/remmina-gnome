%define name	remmina-gnome
%define version	0.7.3
%define release %mkrel 1

Summary:	GNOME desktop applet for remmina
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.gz
License:	GPLv2
Group:		Graphical desktop/GNOME
Url:		http://remmina.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	remmina >= %{version}-%{release}
BuildRequires:	gnome-panel-devel >= 2.20
BuildRequires:	avahi-client-devel

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
%configure
%make

%install
%__rm -rf %{buildroot}
%makeinstall

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%_bindir/remmina-applet
%_libdir/bonobo/servers/Remmina_Applet.server
%_datadir/locale/*/*/remmina-gnome.mo
