%define name gmemusage
%define version 0.2
%define release 11

Summary: 	Graphics memory usage meter
Name: 		%{name}
Version: 	%{version}
Release: 	%mkrel %{release}
Source: 	%{name}-%{version}.tar.bz2
Url: 		http://reality.sgi.com/raju/software/
License: 	GPL
Group: 		Monitoring
Buildrequires:	X11-devel
BuildRoot: 	%{_tmppath}/%{name}-buildroot

%description
This tool displays the bar graph describing a memory usage of processes
on the Linux box. Uses /proc filesystem.

%prep
rm -rf $RPM_BUILD_ROOT

%setup

%build

%make OPTIM="$RPM_OPT_FLAGS" LIBX11DIR=-L%{_prefix}/X11R6/%{_lib}

%install
install -m 755 -d $RPM_BUILD_ROOT/usr/X11R6/bin
install -m 755 -d $RPM_BUILD_ROOT%{_mandir}/man1
install -m 755 gmemusage $RPM_BUILD_ROOT/usr/X11R6/bin/
install -m 644 gmemusage.1 $RPM_BUILD_ROOT%{_mandir}/man1/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=/usr/X11R6/bin/gmemusage
Name=Gmemusage
Comment=Memory usage
Icon=monitoring_section
Categories=System;Monitor;
EOF
 
%if %mdkversion < 200900
%post
%{update_menus}
%endif
 
%if %mdkversion < 200900
%postun          
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
/usr/X11R6/bin/*
%{_mandir}/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop

