Summary:	Japanese (and not only) code conversion library
Summary(pl):	Biblioteka do konwersji tekstów japoñskich (i nie tylko)
Name:		libjconv
Version:	2.8
Release:	1
License:	GPL
Group:		Libraries
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides Japanese code translation based on iconv,
it may be used also to convert from other character sets.

%description -l pl
Pakiet ten pozwala na konwersjê tekstu w kodowaniu Japoñskim,
mo¿e jednak s³u¿yæ do konwersji z innych zbiorów znaków.

%package devel
Summary: header files for Japanese code conversion library
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
Header files for jconv library.

%description devel -l pl
Pliki nag³ówkowe dla biblioteki jconv.

%package static
Summary: header files
Group: Development/Libraries
Requires: %{name}-devel = %{version}

%description static
Static version of jconv libraries.

%description static -l pl
Wersja statyczna biblioteki jconv.

%prep
%setup  -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__install} -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}
%{__install} -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
%{__install} default.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
%{__install} %{name}.so $RPM_BUILD_ROOT%{_libdir}
%{__install} jconv.h $RPM_BUILD_ROOT%{_includedir}
%{__install} %{name}.a $RPM_BUILD_ROOT%{_libdir}

gzip -9nf README

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/*.so
%config %verify(not md5 size mtime) %{_sysconfdir}/%{name}/default.conf

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
