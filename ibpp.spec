Summary:	IBPP - a C++ client interface for Firebird Server & InterBase
Summary(pl):	IBPP - interfejs klienta w C++ do serwerów baz danych Firebird i InterBase
Name:		ibpp
Version:	2.3.5.0
Release:	2
License:	IBPP License (based on Mozilla Public License)
Group:		Libraries
Source0:	http://dl.sourceforge.net/ibpp/%{name}-2-3-5-0-src.zip
# Source0-md5:	f96991555dec3c98216e0d78f31b8586
Patch0:		%{name}-types.patch
URL:		http://www.ibpp.org/
BuildRequires:	Firebird-devel
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

%description -l pl
IBPP, gdzie "PP" oznacza "++", jest interfejsem klienta w C++ do
serwera baz danych Firebird w wersji 1.0, 1.5 i kolejnych. Dzia³a
równie¿ z Interbase(R) 6.0, chocia¿ w przysz³o¶ci jest przewidywane
wsparcie jedynie Firebirda. Jest to biblioteka klas, wolna od
jakichkolwiek zale¿no¶ci od narzêdzi programistycznych. Nie jest
zwi±zana z jakimkolwiek narzêdziem "wizualnym" b±d¼ typu "RAD". Zosta³
stworzony aby umo¿liwiæ dostêp do Firebirda jakiejkolwiek aplikacji
napisanej w C++. Takie aplikacje, które u¿ywaj± IBPP mog± byæ bez
interfejsu (np. obiekty CORBA/COM, inne biblioteki klas i funkcji,
procedury "dziedzicz±ce" kod). Ale oczywi¶cie mo¿e byæ równie¿ u¿ywany
w aplikacjach z interfejsem lub ¶rodowiskach RAD. IBPP jest tak
naprawdê czystym interfejsem dynamicznego SQL do Firebirda. W kilku
³atwych do u¿ycia klasach C++ mo¿na znale¼æ praktycznie wszystko, co
jest potrzebne aby po³±czyæ siê z baz± danych Firebird i operowaæ na
jej danych. IBPP oferuje równie¿ dostêp do wiêkszo¶ci zadañ
administracyjnych: tworzenie bazy danych, modyfikacja jej struktury,
tworzenie kopii zapasowych z dzia³aj±cej bazy, administrowanie kontami
u¿ytkowników na serwerze, itd.

Wiêcej informacji na stronie: %{url} .

%package devel
Summary:	IBPP library headers
Summary(pl):	Pliki nag³ówkowe biblioteki IBPP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the libraries, include files and other resources you can use
to incorporate IBPP into applications.

%description devel -l pl
Pliki nag³ówkowe potrzebne do budowania programów korzystaj±cych z
IBPP.

%package static
Summary:	IBPP static libraries
Summary(pl):	Statyczne biblioteki IBPP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This is package with static IBPP libraries.

%description static -l pl
Statyczna wersja biblioteki IBPP.

%prep
%setup -q -c
%patch0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} %{?debug:-DDEBUG} -fPIC -Wall -DIBPP_LINUX -DIBPP_GCC -I." \
	IBPP_GCC=1 \
	%{?debug:DEBUG=1}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

install release/linux/libibpp.so $RPM_BUILD_ROOT%{_libdir}
install release/linux/libibpp.a $RPM_BUILD_ROOT%{_libdir}
install ibpp.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.txt tests/tests.cpp
%attr(755,root,root) %{_libdir}/libibpp.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_includedir}/ibpp.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libibpp.a
