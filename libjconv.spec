Summary:	Japanese (and not only) code conversion library
Summary(pl):	Biblioteka do konwersji tekstÛw japoÒskich (i nie tylko)
Name:		libjconv
Version:	2.8
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	http://www.jaist.ac.jp/~amatsus/linux/src/net/%{name}-%{version}.tar.bz2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides Japanese code translation based on iconv, it may
be used also to convert from other character sets.

%description -l pl
Pakiet ten pozwala na konwersjÍ tekstu w kodowaniu JapoÒskim, moøe
jednak s≥uøyÊ do konwersji z innych zbiorÛw znakÛw.

%package devel
Summary:	Header files for Japanese code conversion library
Summary(pl):	Pliki nag≥Ûwkowe do biblioteki jconv
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Header files for jconv library.

%description devel -l pl
Pliki nag≥Ûwkowe dla biblioteki jconv.

%package static
Summary:	Static jconv libraries
Summary(pl):	Biblioteki statyczne jconv
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Static version of jconv libraries.

%description static -l pl
Wersja statyczna biblioteki jconv.

%package -n jconv
Summary:	Japanese code conversion tool
Summary(pl):	NarzÍdzie do konwersji kodowania tekstÛw japoÒskich
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst
Requires:	%{name} = %{version}

%description -n jconv
Japanese code conversion tool.

%description -n jconv -l pl
Program do konwersji kodowania JapoÒskich tekstÛw.

%prep
%setup  -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_bindir}} \
	$RPM_BUILD_ROOT%{_sysconfdir}/%{name}

install default.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install %{name}.so $RPM_BUILD_ROOT%{_libdir}
install jconv.h $RPM_BUILD_ROOT%{_includedir}
install jconv $RPM_BUILD_ROOT%{_bindir}
install %{name}.a $RPM_BUILD_ROOT%{_libdir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%config %verify(not md5 size mtime) %{_sysconfdir}/%{name}/default.conf
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
