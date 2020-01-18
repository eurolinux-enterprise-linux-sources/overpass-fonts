%global fontname overpass
%global fontconf 60-%{fontname}.conf

Name:		%{fontname}-fonts
Version:	1.01
Release:	4%{?dist}
Summary:	Typeface based on the U.S. interstate highway road signage type system
License:	OFL or ASL 2.0 
URL:		https://fedorahosted.org/overpass-fonts/
Source0:	https://fedorahosted.org/releases/o/v/overpass-fonts/Overpass-Fonts-%{version}.tar.gz
Source1:	%{name}-fontconfig.conf
Source2:	http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	fontpackages-filesystem

%description
Free & open source typeface based on the U.S. interstate highway road signage 
type system; it is sans-serif and suitable for both body and titling text.

%prep
%setup -q -c
cp %{SOURCE2} .

%build
# Nothing to do here.

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
		%{buildroot}%{_fontconfig_confdir}/%{fontconf}

%_font_pkg -f %{fontconf} *.ttf
%doc Overpass-OFL.txt LICENSE-2.0.txt

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 11 2012 Tom Callaway <spot@fedoraproject.org>
- License is now OFL or ASL 2.0

* Mon Sep 24 2012 Tom Callaway <spot@fedoraproject.org> - 1.01-2
- fix spaces vs tabs issue

* Mon Aug 27 2012 Tom Callaway <spot@fedoraproject.org> - 1.01-1
- initial package
