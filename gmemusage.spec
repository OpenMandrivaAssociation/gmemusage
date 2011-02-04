Summary: 	Graphics memory usage meter
Name: 		gmemusage
Version: 	0.2
Release: 	%mkrel 13
Source: 	%{name}-%{version}.tar.bz2
Url: 		http://reality.sgi.com/raju/software/
License: 	GPL
Group: 		Monitoring
Buildrequires:	libx11-devel
BuildRoot: 	%{_tmppath}/%{name}-buildroot

%description
This tool displays the bar graph describing a memory usage of processes
on the Linux box. Uses /proc filesystem.

%prep
%setup

%build
%make OPTIM="%optflags" LIBX11DIR=-L%{_libdir} LDFLAGS="%ldflags"

%install
rm -fr %buildroot
install -D -m 755 gmemusage $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -m 644 gmemusage.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/gmemusage
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
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop
