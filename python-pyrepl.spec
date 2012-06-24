
%define 	module	pyrepl

Summary:	pyrepl - a readline-a-like in Python
Summary(pl):	pyrepl - zast�pca readline w Pythonie
Name:		python-%{module}
Version:	0.8.1
Release:	2
License:	Python-style
Group:		Libraries/Python
Source0:	http://codespeak.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	f285e5c0b8d43b86e52fdd1b25e467eb
Patch0:		python-pyrepl-pythoni-first-line-path.patch
URL:		http://codespeak.net/pyrepl/
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

%description -l pl
pyrepl jest modu�em umo�liwiaj�cym zast�pienie modu�u readline modu�em
posiadaj�cym nast�puj�cych cechy:

- rozs�dna obs�uga edycji w wielu liniach,
- historia wraz z jej przeszukiwaniem,
- podpowiadanie wy�wietlaj�ce dost�pne opcje,
- ca�kiem du�y podzbi�r skr�t�w klawiszowych trybu emacsa readline,
  wraz z �atw� metod� rozszerzania tego zbioru,
- liberalna (w stylu Pythona) licencja,
- brak zmiennych globalnych, co umo�liwia uruchomienie dw�ch lub
  wi�cej niezale�nych czytnik�w bez martwienia si� nak�adaniem na siebie
  historii,
- �atwa kontrola umo�liwiaj�ca bezbolesn� integracj� pyrepl w p�tli
  zdarze� aplikacji u�ytkownika,
- og�lnie rzecz bior�c - wi�ksza interakcja z u�ytkownikiem ni� w
  module readline (modu� rozwin�� si� w co� pomi�dzy readline a
  mini-bufferem znanym z emacsa),
- obs�uga uniode (je�li obs�ugiwane przez terminal).

%package utils
Summary:	Utilities for Python pyrepl module
Summary(pl):	Narz�dzia modu�u Pythona pyrepl
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description utils
This package contains pythoni utility - an interactive Python
interpreter with pyrepl module embedded.

%description utils -l pl
Pakiet ten zawiera narz�dzie pythoni - interaktywny interpreter
Pythona z osadzonym we� modu�em pyrepl.

%prep
%setup -q -n %{module}-%{version}
%patch -p0

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{_bindir}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
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
