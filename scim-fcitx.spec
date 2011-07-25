Summary:	FCITX Input Method Engine for SCIM
Name:		scim-fcitx
Version:	3.1.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/scim/%{name}.%{version}.tar.bz2
# Source0-md5:	781dc96ebce31e2949ecb0c3c1c769f6
Patch0:		%{name}-gcc43.patch
URL:		http://www.scim-im.org/projects/imengines/
BuildRequires:	scim-devel
Requires:	scim
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
scim-fcitx is a port of the fcitx Chinese input method for the SCIM
input method platform. It provides Wubi, Erbi, Cangjie, and Pinyin
styles of input.

%package tools
Summary:	Fcitx tables tools
Group:		Development/Libraries

%description tools
This package contains input table tools from fcitx.

%prep
%setup -q -n fcitx
%patch0 -p1

%build
%configure

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT/%{_libdir}/scim-1.0/*/IMEngine/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_libdir}/scim-1.0/*/IMEngine/fcitx.so
%{_datadir}/scim/fcitx
%{_datadir}/scim/icons/fcitx

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
