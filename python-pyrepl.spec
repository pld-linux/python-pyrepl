
%define 	module	pyrepl

Summary:	pyrepl - a readline-a-like in Python
Summary(pl):	pyrepl - zastêpca readline w Pythonie
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
pyrepl jest modu³em umo¿liwiaj±cym zast±pienie modu³u readline modu³em
posiadaj±cym nastêpuj±cych cechy:

- rozs±dna obs³uga edycji w wielu liniach,
- historia wraz z jej przeszukiwaniem,
- podpowiadanie wy¶wietlaj±ce dostêpne opcje,
- ca³kiem du¿y podzbiór skrótów klawiszowych trybu emacsa readline,
  wraz z ³atw± metod± rozszerzania tego zbioru,
- liberalna (w stylu Pythona) licencja,
- brak zmiennych globalnych, co umo¿liwia uruchomienie dwóch lub
  wiêcej niezale¿nych czytników bez martwienia siê nak³adaniem na siebie
  historii,
- ³atwa kontrola umo¿liwiaj±ca bezbolesn± integracjê pyrepl w pêtli
  zdarzeñ aplikacji u¿ytkownika,
- ogólnie rzecz bior±c - wiêksza interakcja z u¿ytkownikiem ni¿ w
  module readline (modu³ rozwin±³ siê w co¶ pomiêdzy readline a
  mini-bufferem znanym z emacsa),
- obs³uga uniode (je¶li obs³ugiwane przez terminal).

%package utils
Summary:	Utilities for Python pyrepl module
Summary(pl):	Narzêdzia modu³u Pythona pyrepl
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description utils
This package contains pythoni utility - an interactive Python
interpreter with pyrepl module embedded.

%description utils -l pl
Pakiet ten zawiera narzêdzie pythoni - interaktywny interpreter
Pythona z osadzonym weñ modu³em pyrepl.

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
