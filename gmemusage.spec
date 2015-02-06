Summary: 	Graphics memory usage meter
Name: 		gmemusage
Version: 	0.2
Release: 	15
Source: 	%{name}-%{version}.tar.bz2
Url: 		http://reality.sgi.com/raju/software/
License: 	GPL
Group: 		Monitoring
Buildrequires:	pkgconfig(x11)

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


%changelog
* Fri Feb 04 2011 Funda Wang <fwang@mandriva.org> 0.2-13mdv2011.0
+ Revision: 635854
- tighten BR

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-12mdv2011.0
+ Revision: 618966
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.2-11mdv2010.0
+ Revision: 429221
- rebuild

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.2-10mdv2009.0
+ Revision: 218423
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.2-10mdv2008.1
+ Revision: 131581
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- import gmemusage


* Fri Dec 23 2005 Anssi Hannula <anssi@mandriva.org> 0.2-10mdk
- %%mkrel
- fix menudir
- fix lib64 build

* Thu Jul 22 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.2-9mdk
- rebuild

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.2-7mdk
- rebuild

* Sat Jan 19 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 0.2-6mdk
- Fix menu entry

* Wed Jul 18 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.2-5mdk
- rebuild

* Wed Jan 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.2-4mdk
- rebuild

* Tue Aug 31 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.2-3mdk
- BM
- macros 
- menu

* Thu Apr 27 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.2-2mdk
- fix  group

* Thu Feb 24 2000 Lenny Cartier <lenny@mandrakesoft.com>
- mandrake build
