%define debug_package  %{nil}

Name:           mgaextra
Version:        5.0
Release:        %mkrel 1
Summary:        Skrypt wstępnej konfiguracji Magei
License:        GPL
Group:          System/Configuration/Other
URL:            http://www.mageia.org.pl/
Source0:        %{name}.tar.xz
BuildArch:      noarch
Requires:       python-vte
Requires:       wget
Requires:       pygtk2.0-libglade
Requires:       zenity

%description
Skrypt wstępnej konfiguracji dla Magei.

%prep
%setup -q -n %{name}
# DEPRECATED: swapped="no"
# libglade-WARNING **: unknown attribute `swapped' for <signal>.
sed -i "s/swapped=\"no\"//g" skrypt.glade

%build


%install
rm -rf %{buildroot}

#executable
install -d %{buildroot}%{_bindir}
install -m0755 %{name} %{buildroot}%{_bindir}

#desktop
#install -d %%{buildroot}%%{_desktopdir}
install -d -p %{buildroot}%{_datadir}/applications
install -m0755 *.desktop %{buildroot}%{_datadir}/applications/

#data
install -d %{buildroot}/%{_datadir}/%{name}
install -d %{buildroot}/%{_datadir}/%{name}/images
install -d %{buildroot}/%{_datadir}/%{name}/scripts
install -m0755 skrypt %{buildroot}/%{_datadir}/%{name}
install -m0644 copyright splash.py skrypt.glade categories.ini categories_en.ini %{buildroot}/%{_datadir}/%{name}
install -m0644 images/*.png %{buildroot}/%{_datadir}/%{name}/images
install -m0744 scripts/* %{buildroot}/%{_datadir}/%{name}/scripts


%files
%defattr(-,root,root,0755)
%{_bindir}/%{name}
%{_datadir}/%{name}/categories.ini
%{_datadir}/%{name}/categories_en.ini
%{_datadir}/%{name}/copyright
%{_datadir}/%{name}/skrypt
%{_datadir}/%{name}/skrypt.glade
%{_datadir}/%{name}/splash.py
%{_datadir}/%{name}/images/*
%{_datadir}/%{name}/scripts/*
%{_datadir}/applications/*.desktop


%changelog
* Fri Apr 18 2014 napcok <napcok@gmail.com> 4.0-1
- MGA 4

* Fri May 31 2013 m123456 <m123456> 3.0-9
- Repo Cauldron -> 3

* Tue Mar 19 2013 napcok <napcok@gmail.com> 3.0-8
- mozilla-thunderbird -> thunderbird
- dodno gry xonotic, warsow, ut, supertux, openarena
- zmiana obramowanie splasha

* Sat Mar 16 2013 m123456 <m123456> 3.0-7
- poprawienie wykrywania Steama
- małe czyszczenie categories.ini
- up 3.0-6 -> 3.0-7 :)

* Sat Mar 16 2013 m123456 <m123456> 3.0-6
- drobne poprawki i uaktualnienie wersji Adobe Reader

* Fri Mar 15 2013 napcok <napcok@gmail.com> 3.0-5
- MOPL2 -> MOPL3
- usunięcie qnapi (nierozwijane), smplayer daje radę

* Tue Mar 12 2013 napcok <napcok@gmail.com> 3.0-4
- rawstudio removed, darktable added 

* Tue Mar 12 2013 napcok <napcok@gmail.com> 3.0-3
- nowy tymczasowy splash
- dodane TeamViewer, Ubuntu One
- gry usunięto niedostępne, dodano Steam, Playonlinux, 0 A.D.

* Mon Feb 11 2013 m123456 <m123456> 3.0-1
- naprawa unknown attribute `swapped'
- dodanie środowiska graficznego RazorQt
- poprawa gnome-desktop -> gnome-desktop3
  - wyświetlenie zainstalowanego środ. gnome 3
- mirrory Cauldron-a
- inne drobne poprawki

* Thu Oct 18 2012 m123456 <m123456> 2.0-5
- dodanie zależności 32-bitowych do Adobe Reader dla arch. 64
- skrypty -> urpmi/urpme dla java-sun

* Mon Jun 04 2012 m123456 <m123456> 2.0-4
- poprawiono skrypty dla Tlen-u
- dodano wymaganą zależność:
  libopenssl0.9.8/lib64openssl0.9.8

* Fri May 25 2012 m123456 <m123456> 2.0-3
- zmiana repo Cauldron na oficjalne Mga 2

* Sun May 20 2012 m123456 <m123456> 2.0-2
gnome 2 -> gnome 3
  Cauldron -> Official
    - nazwy w menu
    - oficjalne repozytoria nadal ustawione na Cauldron
  Java skrypt- wersja testowa
    oracle-java-installer-1.7.0_04-2.mga2.src.rpm
  Poprawa linku do repo. MOPL

* Wed Mar 21 2012 m123456 <m123456> 2.0-1
- mod. scripts
- add cauldron repo for 32 and 64bit
- repo. 64bit include 32bit mirrors (get-skype)
- change tar.gz to tar.xz

* Fri Dec 02 2011 m123456 <m123456> 1.0-6
- add: Adobe Reader v9.4.6, XFdrake and drak3d

* Wed Oct 19 2011 m123456 <m123456> 1.0-5.mga1
- change logo and icons
- change links to repo MOPL
- add repo MOPL testing

* Thu Oct  6 2011 m123456 <m123456> 1.0-4.mga1
- Some cleanup needed in the spec file by ryoshu
- accees to program from gui LXDE, GNOME, XFCE
- add flash-player-plugin11
- add repository BlogDRAKE
- add fotoxx, rawstudio, megaglest, ultimatestunts, qnapi

* Tue Sep 27 2011 m123456 <m123456> 1.0-3.mga1
- chaneg group (System/Configuration/Other)
- add pygtk2.0-libglade, zenity to requires

* Thu Sep 22 2011 m123456 <m123456> 1.0-2.mopl1
- change name mageia-skrypt -> mgaextra
- changes icons, add programs etc.

* Thu Sep 22 2011 Daniel Napora <napcok@gmail.com> 1.0-1.mopl1
- first build for Mageia 1
