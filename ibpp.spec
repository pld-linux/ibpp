%define		sver 2-5-3-1
%define		ver %(echo %{sver} | tr -s - .)
Summary:	IBPP - a C++ client interface for Firebird Server & InterBase
Summary(pl.UTF-8):	IBPP - interfejs klienta w C++ do serwerów baz danych Firebird i InterBase
Name:		ibpp
Version:	%{ver}
Release:	1
License:	IBPP License v1.1 (based on Mozilla Public License)
Group:		Libraries
Source0:	http://dl.sourceforge.net/ibpp/%{name}-%{sver}-src.zip
# Source0-md5:	0fec1e010ad272825cb585cd79e68936
Patch0:		%{name}-build.patch
URL:		http://www.ibpp.org/
BuildRequires:	Firebird-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IBPP, where 'PP' stands for '++', is a C++ client interface for
Firebird Server versions 1.0, 1.5 and further. It also works with
InterBase(r) 6.0, though it is expected it might only support Firebird
in the future. It is a class library, free of any specific development
tool dependancies. It is not tied to any 'visual' or 'RAD' tool. It
was indeed developed to add Firebird access in any C++ application.
Those applications using IBPP can be non-visual (CORBA/COM objects,
other libraries of classes and functions, procedural 'legacy' code,
for instance). But it can of course also be used in visual or RAD
environments. IBPP is indeed purely a dynamic SQL interface to
Firebird. In some easy to use C++ classes, you will find nearly all
what is needed to access a Firebird database, and manipulate the data.
IBPP also offers access to most of the administrations tasks :
creating a database, modifying its structure, performing online
backups, administering user accounts on the server and so on.

More background information on %{url} website.

%description -l pl.UTF-8
IBPP, gdzie "PP" oznacza "++", jest interfejsem klienta w C++ do
serwera baz danych Firebird w wersji 1.0, 1.5 i kolejnych. Działa
również z Interbase(R) 6.0, chociaż w przyszłości jest przewidywane
wsparcie jedynie Firebirda. Jest to biblioteka klas, wolna od
jakichkolwiek zależności od narzędzi programistycznych. Nie jest
związana z jakimkolwiek narzędziem "wizualnym" bądź typu "RAD". Został
stworzony aby umożliwić dostęp do Firebirda jakiejkolwiek aplikacji
napisanej w C++. Takie aplikacje, które używają IBPP mogą być bez
interfejsu (np. obiekty CORBA/COM, inne biblioteki klas i funkcji,
procedury "dziedziczące" kod). Ale oczywiście może być również używany
w aplikacjach z interfejsem lub środowiskach RAD. IBPP jest tak
naprawdę czystym interfejsem dynamicznego SQL do Firebirda. W kilku
łatwych do użycia klasach C++ można znaleźć praktycznie wszystko, co
jest potrzebne aby połączyć się z bazą danych Firebird i operować na
jej danych. IBPP oferuje również dostęp do większości zadań
administracyjnych: tworzenie bazy danych, modyfikacja jej struktury,
tworzenie kopii zapasowych z działającej bazy, administrowanie kontami
użytkowników na serwerze, itd.

Więcej informacji na stronie: %{url} .

%package devel
Summary:	IBPP library headers
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki IBPP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Firebird-devel

%description devel
This is the libraries, include files and other resources you can use
to incorporate IBPP into applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do budowania programów korzystających z
IBPP.

%package static
Summary:	IBPP static libraries
Summary(pl.UTF-8):	Statyczne biblioteki IBPP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This is package with static IBPP libraries.

%description static -l pl.UTF-8
Statyczna wersja biblioteki IBPP.

%prep
%setup -q -c
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure

%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags} %{?debug:-g -DDEBUG} -fPIC -Wall -DIBPP_LINUX -DIBPP_GCC"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.txt tests/tests.cpp
%attr(755,root,root) %{_libdir}/libibpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libibpp.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libibpp.so
%{_libdir}/libibpp.la
%{_includedir}/ibpp.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libibpp.a
