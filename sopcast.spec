Name:           sopcast
Version:        3.2.6
Release:        6.R
Summary:        A P2P Stream program

License:        Redistributable
URL:            http://www.sopcast.org
Group:          Applications/Internet
Source0:        http://download.easetuner.com/download/sp-auth.tgz
Source1:        sopcast
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#Requires:       mplayer
AutoReqProv:    no
Requires:       /bin/sh
Requires:       ld-linux.so.2
Requires:       libc.so.6
Requires:       libgcc_s.so.1
Requires:       libm.so.6
Requires:       libpthread.so.0
Requires:       libstdc++.so.5

BuildArch:      i686


%description
A P2P Stream program and playing script


%prep
%setup -q -n sp-auth


%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
%{__install} -pD -m755 sp-sc-auth %{buildroot}%{_bindir}
# File install
%{__install} -pD -m755 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_bindir}/sopcast

%clean
rm -rf %{buildroot}


%files
%doc Readme
%defattr(-,root,root)
%{_bindir}/*


%changelog
* Mon Oct 24 2011 Vasiliy N. Glazov <vascom2@gmail.com> 3.2.6-6.R
- Removed auto requires, added it manual

* Tue Aug 03 2011 Vasiliy N. Glazov <vascom2@gmail.com> 3.2.6-5.R
- Removed mplayer requires

* Wed Jul 13 2011 Arkady L. Shane <ashejn@russianfedora.ru> 3.2.6-4.R
- added BuildArch: i686
- cleanup spec
- remove %%{?dist}

* Tue Jul 12 2011 Vasiliy N. Glazov <vascom2@gmail.com> 3.2.6-3.R
- updated to 3.2.6
- added playing script

* Mon May 19 2008 Arkady L. Shane <ashejn@yandex-team.ru> 1.1.1-2
- fixed bug #12

* Sun May 18 2008 Arkady L. Shane <ashejn@yandex-team.ru> 1.1.1-1
- initial build for Fedora
