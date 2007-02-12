Summary:	Japanese (and not only) code conversion library
Summary(pl.UTF-8):   Biblioteka do konwersji tekstów japońskich (i nie tylko)
Name:		libjconv
Version:	2.8
Release:	3
License:	GPL v2
Group:		Libraries
Source0:	http://www.jaist.ac.jp/~amatsus/linux/src/net/%{name}-%{version}.tar.bz2
# Source0-md5:	dbc0b977ded88ffa524fca4ea237af51
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides Japanese code translation based on iconv, it may
be used also to convert from other character sets.

%description -l pl.UTF-8
Pakiet ten pozwala na konwersję tekstu w kodowaniu japońskim, może
jednak służyć do konwersji z innych zbiorów znaków.

%package devel
Summary:	Header files for Japanese code conversion library
Summary(pl.UTF-8):   Pliki nagłówkowe do biblioteki jconv
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for jconv library.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki jconv.

%package static
Summary:	Static jconv libraries
Summary(pl.UTF-8):   Biblioteki statyczne jconv
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of jconv libraries.

%description static -l pl.UTF-8
Wersja statyczna biblioteki jconv.

%package -n jconv
Summary:	Japanese code conversion tool
Summary(pl.UTF-8):   Narzędzie do konwersji kodowania tekstów japońskich
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}

%description -n jconv
Japanese code conversion tool.

%description -n jconv -l pl.UTF-8
Program do konwersji kodowania japońskich tekstów.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC -Wall -DHAVE_CODESET"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_bindir}} \
	$RPM_BUILD_ROOT%{_sysconfdir}/%{name}

install default.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install %{name}.so $RPM_BUILD_ROOT%{_libdir}
install jconv.h $RPM_BUILD_ROOT%{_includedir}
install jconv $RPM_BUILD_ROOT%{_bindir}
install %{name}.a $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/default.conf
%attr(755,root,root) %{_libdir}/*.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files -n jconv
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jconv
