%global fontname oldschool-pc
%global fontconf 62-%{fontname}
%global zip_timestamp .20160116

%global common_desc \
The Ultimate Oldschool PC Font Pack is a font collection which brings you \
pixel-perfect remakes of various type styles from text-mode era PCs - in \
modern, multi-platform, Unicode-compatible TrueType form.

Name:           %{fontname}-fonts
Version:        1.0
Release:        1%{zip_timestamp}%{?dist}
Summary:        A collection of classic text mode fonts

License:        CC BY-SA 4.0
URL:            http://int10h.org/oldschool-pc-fonts
Source0:        http://int10h.org/oldschool-pc-fonts/download/ultimate_oldschool_pc_font_pack_v%{version}.zip
Source2:        px437.conf
Source3:        pxplus.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel

%description
%common_desc


%package common
Summary:        Common files of The Ultimate Oldschool PC Font Pack
Requires:       fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.


%package -n %{fontname}-px437-fonts
Summary:        Oldschool PC fonts supporting Codepage 437 character set
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-px437-fonts
%common_desc

These fonts feature the classic set of 256 characters established by the
original PC, also known as Code Page 437 (or PC ASCII, Latin-US DOS/OEM, and
other catchy names).  They are exact duplicates of the original pixel fonts in
outline form, and characters are Unicode-mapped for maximum compatibility.

%_font_pkg -n px437 -f %{fontconf}-px437.conf "Px437_*.ttf"


%package -n %{fontname}-pxplus-fonts
Summary:        Oldschool PC fonts supporting some Unicode ranges
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-pxplus-fonts
%common_desc

On top of the CP437 range, these fonts support extended Latin, Greek, Cyrillic
and Hebrew scripts plus a bunch of additional glyphs and Unicode symbols.  The
extra characters were taken from international versions of the original
hardware (if available), or designed to closely follow the existing ones.

%_font_pkg -n pxplus -f %{fontconf}-pxplus.conf "PxPlus_*.ttf"


%prep
%setup -q -c


%build


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p "Px437 (TrueType - DOS charset)"/*.ttf %{buildroot}%{_fontdir}
install -m 0644 -p "PxPlus (TrueType - extended charset)"/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-px437.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pxplus.conf

for fconf in %{fontconf}-px437.conf \
             %{fontconf}-pxplus.conf; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done


%clean
rm -fr %{buildroot}


%files common
%license LICENSE.TXT
%doc README.NFO


%changelog
* Sun Nov 06 2016 Jajauma's Packages <jajauma@yandex.ru> - 1.0-1.20160116
- Public release
