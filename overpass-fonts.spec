%global fontname overpass
%global archivename %{fontname}-fonts-ttf
%global fontconf 60-%{fontname}.conf

Name:		%{fontname}-fonts
Version:	2.1
Release:	1%{?dist}
Summary:	Typeface based on the U.S. interstate highway road signage type system
License:	OFL
URL:		https://github.com/RedHatBrand/overpass/
#Source0:	https://github.com/RedHatBrand/overpass/releases/download/2.0/overpass-fonts-ttf-2.zip
Source0:	https://pravins.fedorapeople.org/overpass-fonts/%{archivename}-%{version}.zip
Source1:	%{name}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	fontpackages-filesystem

%description
Free and open source typeface based on the U.S. interstate highway road signage
type system; it is sans-serif and suitable for both body and titling text.

%prep
%setup -c -q

%build
# Nothing to do here.

%install
mv %{archivename}-%{version}/Overpass\ Specimen\ 8-20-15.pdf %{archivename}-%{version}/Overpass-Specimen-8-20-15.pdf
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{archivename}-%{version}/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
		%{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
	%{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%doc %{archivename}-%{version}/README.md %{archivename}-%{version}/Overpass-Specimen-8-20-15.pdf
%license %{archivename}-%{version}/LICENSE.md
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Thu May 05 2016 Pravin Satute <psatute AT redhat DOT com> - 2.1-1
- Resolves: rhbz#1284772 - Upstream new release with ttfautohint
- Changed url to https://github.com/RedHatBrand/overpass/, https://overpassfont.org looks dead.
- Add Light variant font.
- Add metainfo file to show this font in gnome-software.

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.01-5
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 11 2012 Tom Callaway <spot@fedoraproject.org>
- License is now OFL or ASL 2.0

* Mon Sep 24 2012 Tom Callaway <spot@fedoraproject.org> - 1.01-2
- fix spaces vs tabs issue

* Mon Aug 27 2012 Tom Callaway <spot@fedoraproject.org> - 1.01-1
- initial package
