Summary:	FCITX Input Method Engine for SCIM
Summary(pl.UTF-8):	Silnik metody wprowadzania znaków FCITX dla SCIM-a
Name:		scim-fcitx
Version:	3.1.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/scim/%{name}.%{version}.tar.bz2
# Source0-md5:	781dc96ebce31e2949ecb0c3c1c769f6
Patch0:		%{name}-gcc43.patch
URL:		http://www.scim-im.org/projects/imengines/
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	scim-devel >= 1.2.0
Requires:	scim >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
scim-fcitx is a port of the fcitx Chinese input method for the SCIM
input method platform. It provides Wubi, Erbi, Cangjie, and Pinyin
styles of input.

%description -l pl.UTF-8
scim-fcitx to port metody wprowadzania znaków chińskich fcitx dla
platformy wprowadzania znaków SCIM. Obsługuje metody Wubi, Erbi,
Cangjie i Pinyin.

%package tools
Summary:	Fcitx tables tools
Summary(pl.UTF-8):	Narzędzia do obsługi tablic fcitx
Group:		Development/Tools

%description tools
This package contains input table tools from fcitx.

%description tools -l pl.UTF-8
Ten pakiet zawiera narzędzia do obsługi tablic wejściowych fcitx.

%prep
%setup -q -n fcitx
%patch0 -p1

%build
%configure \
	--disable-static

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT/%{_libdir}/scim-1.0/*/IMEngine/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS
%attr(755,root,root) %{_libdir}/scim-1.0/*/IMEngine/fcitx.so
%{_datadir}/scim/fcitx
%{_datadir}/scim/icons/fcitx

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/createPYMB
%attr(755,root,root) %{_bindir}/mb2txt
%attr(755,root,root) %{_bindir}/txt2mb
