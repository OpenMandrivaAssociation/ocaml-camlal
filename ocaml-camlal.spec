Name:           ocaml-camlal
Version:        1.0.0
Release:        2
Summary:        CamlAL is an OCaml bindings for OpenAL
License:        LGPL
Group:          Development/Other
URL:            http://sourceforge.net/projects/camlal/
Source0:        http://camlal.svn.sourceforge.net/viewvc/camlal/trunk/camlal.tar.gz
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml
BuildRequires:  libopenal-devel
BuildRequires:  libfreealut-devel

%description
CamlAL is an OCaml wrapper for the OpenAL and ALUT libraries.
(http://www.openal.org)

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n camlal

cat > META <<EOF
description     = "%{summary}"
version         = "%{version}"
archive(byte)   = "camlal.cma"
archive(native) = "camlal.cmxa"
EOF

%build
make
test -d doc || mkdir doc
ocamldoc -d doc -html -v -I camlal/_build/ camlal/*.ml

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/camlal
mkdir -p $OCAMLFIND_DESTDIR/stublibs
ocamlfind install camlal \
    camlal/*.ml camlal/_build/*.{cmi,cma,a,cmxa,cmx,so} META

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS.txt COPYING.txt README.txt TODO.txt VERSION.txt
%dir %{_libdir}/ocaml/camlal
%{_libdir}/ocaml/camlal/META
%{_libdir}/ocaml/camlal/*.cma
%{_libdir}/ocaml/camlal/*.cmi
%{_libdir}/ocaml/stublibs/*.so*

%files devel
%defattr(-,root,root)
%doc doc
%{_libdir}/ocaml/camlal/*.a
%{_libdir}/ocaml/camlal/*.cmxa
%{_libdir}/ocaml/camlal/*.cmx
%{_libdir}/ocaml/camlal/*.ml



%changelog
* Sat Aug 22 2009 Florent Monnier <blue_prawn@mandriva.org> 1.0.0-1mdv2010.0
+ Revision: 419703
- BuildRequires:  ocaml-findlib
- import ocaml-camlal

