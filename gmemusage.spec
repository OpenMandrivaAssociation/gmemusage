%define name gmemusage
%define version 0.2
%define release 10

Summary: 	Graphics memory usage meter
Name: 		%{name}
Version: 	%{version}
Release: 	%mkrel %{release}
Source: 	%{name}-%{version}.tar.bz2
Url: 		http://reality.sgi.com/raju/software/
License: 	GPL
Group: 		Monitoring
Buildrequires:	X11-devel

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

(cd $RPM_BUILD_ROOT
mkdir -p .%{_menudir}
cat > .%{_menudir}/%{name} <<EOF
?package(%{name}):\
command="/usr/X11R6/bin/gmemusage"\
title="Gmemusage"\
longtitle="Memory usage"\
needs="x11"\
icon="monitoring_section.png"\
section="System/Monitoring"
EOF
)
 
%post
%{update_menus}
 
%postun          
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
/usr/X11R6/bin/*
%{_mandir}/man1/*
%{_menudir}/%{name}

