
%define 	module	pyrepl

Summary:	pyrepl - a readline-a-like in Python
Summary(pl.UTF-8):	pyrepl - zastępca readline w Pythonie
Name:		python-%{module}
Version:	0.8.1
Release:	2
License:	Python-style
Group:		Libraries/Python
Source0:	http://codespeak.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	f285e5c0b8d43b86e52fdd1b25e467eb
Patch0:		python-pyrepl-pythoni-first-line-path.patch
URL:		http://codespeak.net/pyrepl/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
%pyrequires_eq	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyrepl - a readline-a-like in Python. Its key features are:

- sane multi-line editing,
- history, with incremental search,
- completion, including displaying of available options,
- a fairly large subset of the readline emacs-mode keybindings (adding
  more is mostly just a matter of typing),
- a liberal, Python-style, license,
- a new python top-level,
- no global variables, so you can run two or more independent readers
  without having their histories interfering,
- no hogging of control -- it should be easy to integrate pyrepl into
  YOUR application's event loop,
- generally speaking, a much more interactive experience than readline
  (it's a bit like a cross between readline and emacs's mini-buffer),
- unicode support (given terminal support).

%description -l pl.UTF-8
pyrepl jest modułem umożliwiającym zastąpienie modułu readline modułem
posiadającym następujących cechy:

- rozsądna obsługa edycji w wielu liniach,
- historia wraz z jej przeszukiwaniem,
- podpowiadanie wyświetlające dostępne opcje,
- całkiem duży podzbiór skrótów klawiszowych trybu emacsa readline,
  wraz z łatwą metodą rozszerzania tego zbioru,
- liberalna (w stylu Pythona) licencja,
- brak zmiennych globalnych, co umożliwia uruchomienie dwóch lub
  więcej niezależnych czytników bez martwienia się nakładaniem na siebie
  historii,
- łatwa kontrola umożliwiająca bezbolesną integrację pyrepl w pętli
  zdarzeń aplikacji użytkownika,
- ogólnie rzecz biorąc - większa interakcja z użytkownikiem niż w
  module readline (moduł rozwinął się w coś pomiędzy readline a
  mini-bufferem znanym z emacsa),
- obsługa uniode (jeśli obsługiwane przez terminal).

%package utils
Summary:	Utilities for Python pyrepl module
Summary(pl.UTF-8):	Narzędzia modułu Pythona pyrepl
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description utils
This package contains pythoni utility - an interactive Python
interpreter with pyrepl module embedded.

%description utils -l pl.UTF-8
Pakiet ten zawiera narzędzie pythoni - interaktywny interpreter
Pythona z osadzonym weń modułem pyrepl.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{_bindir}}

%py_install \
	--install-lib=%{py_sitescriptdir} \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

install pythoni $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO CHANGES CREDITS
%{py_sitescriptdir}/pyrepl

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pythoni
