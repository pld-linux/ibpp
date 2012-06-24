#
# Conditional build:
%bcond_with	debug	#builds debug version of library
#
Summary:	IBPP, a C++ client interface for Firebird Server & InterBase
Summary(pl):	IBPP, interfejs klienta w C++ do Firebird Server & Interbase
Name:		ibpp
Version:	2.3.5.0
Release:	1
License:	IBPP License (based on Mozilla Public License)
Group:		Libraries
Source0:	http://dl.sourceforge.net/ibpp/%{name}-2-3-5-0-src.zip
# Source0-md5:	f96991555dec3c98216e0d78f31b8586
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

More background information on http://www.ibpp.org website.

%description -l pl
IBPP, gdzie "PP" oznacza "++", jest interfejsem klienta w C++ do
Firebird Server w wersji 1.0, 1.5 i kolejnych. Dzia�a r�wnie� z
Interbase(r) 6.0, chocia� w przysz�o�ci jest przewidywane wsparcie
jedynie Firebirda. Jest to biblioteka klas, wolna od jakichkolwiek
zale�no�ci od narz�dzi programistycznych. Nie jest zwi�zana z
jakimkolwiek narz�dziem "wizualnym" b�d� typu "RAD". Zosta� stworzony
aby umo�liwi� dost�p do Firebirda jakiejkolwiek aplikacji napisanej w
C++. Takie aplikacje, kt�re u�ywaj� IBPP mog� by� bez interfejsu (np.
obiekty CORBA/COM, inne biblioteki klas i funkcji, procedury
"dziedzicz�ce" kod). Ale oczywi�cie mo�e by� r�wnie� u�ywany w
aplikacjach z interfejsem lub �rodowiskach RAD. IBPP jest tak naprawd�
czystym interfejsem dynamicznego SQL do Firebirda. W kilku �atwych do
u�ycia klasach C++ znajdziesz praktycznie wszytko czego potrzebujesz
aby po�aczy� si� z baz� danych Firebird i operowa� na jej danych. IBPP
r�wnie� oferuje dost�p do wi�kszo�ci zada� administracyjnych:
towrzenie bazy danych, modyfikacja jej struktur, tworzenie kopii
zapasowych z dzia�aj�cej bazy, administrowanie kontami u�ytkownik�w na
serwerze, itd.

Wi�cej informacji na stronie: http://www.ibpp.org.

%package devel
Summary:	IBPP library headers
Summary(pl):	Pliki nag��wkowe biblioteki IBPP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the libraries, include files and other resources you can use
to incorporate IBPP into applications.

%description devel -l pl
Pliki nag��wkowe potrzebne do budowania program�w korzystaj�cych z
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
%setup -q -c %{name}-%{version}

%build
%if %{with debug}
%{__make} IBPP_GCC=1 DEBUG=1
%else
%{__make} IBPP_GCC=1
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_docdir}/%{name}-%{version}}
mv -f release/linux/libibpp.so $RPM_BUILD_ROOT%{_libdir}
mv -f release/linux/libibpp.a $RPM_BUILD_ROOT%{_libdir}
mv -f ibpp.h $RPM_BUILD_ROOT%{_includedir}
mv -f *.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
mv -f tests/tests.cpp $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libibpp.so
%doc %{_docdir}/%{name}-%{version}/*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_includedir}/ibpp.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libibpp.a
