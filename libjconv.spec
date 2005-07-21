Summary:	Japanese (and not only) code conversion library
Summary(pl):	Biblioteka do konwersji tekstów japoñskich (i nie tylko)
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

%description -l pl
Pakiet ten pozwala na konwersjê tekstu w kodowaniu Japoñskim, mo¿e
jednak s³u¿yæ do konwersji z innych zbiorów znaków.

%package devel
Summary:	Header files for Japanese code conversion library
Summary(pl):	Pliki nag³ówkowe do biblioteki jconv
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for jconv library.

%description devel -l pl
Pliki nag³ówkowe dla biblioteki jconv.

%package static
Summary:	Static jconv libraries
Summary(pl):	Biblioteki statyczne jconv
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of jconv libraries.

%description static -l pl
Wersja statyczna biblioteki jconv.

%package -n jconv
Summary:	Japanese code conversion tool
Summary(pl):	Narzêdzie do konwersji kodowania tekstów japoñskich
Group:		Applications/Text
Requires:	%{name} = %{version}

%description -n jconv
Japanese code conversion tool.

%description -n jconv -l pl
Program do konwersji kodowania Japoñskich tekstów.

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
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/%{name}/default.conf
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
