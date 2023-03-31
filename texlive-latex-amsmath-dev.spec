Name:		texlive-latex-amsmath-dev
Version:	64899
Release:	2
Summary:	Development pre-release of the LaTeX amsmath bundle
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/latex-amsmath-dev
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-amsmath-dev.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-amsmath-dev.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-amsmath-dev.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a pre-release version of the standard LaTeX amsmath
bundle. It accompanies the pre-testing kernel code
(latex-base-dev), and is intended for testing by knowledgeable
users.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/source
%doc %{_texmfdistdir}/source/latex-dev
%doc %{_texmfdistdir}/source/latex-dev/amsmath
%doc %{_texmfdistdir}/source/latex-dev/amsmath/amsxtra.ins
%doc %{_texmfdistdir}/source/latex-dev/amsmath/amsxtra.dtx
%doc %{_texmfdistdir}/source/latex-dev/amsmath/amstext.ins
%doc %{_texmfdistdir}/source/latex-dev/amsmath/amstext.dtx
%doc %{_texmfdistdir}/source/latex-dev/amsmath/amsopn.ins
%doc %{_texmfdistdir}/source/latex-dev/amsmath/amsopn.dtx
%doc %{_texmfdistdir}/source/latex-dev/amsmath/amsmath.ins
%doc %{_texmfdistdir}/source/latex-dev/amsmath/amsmath.dtx
%doc %{_texmfdistdir}/source/latex-dev/amsmath/amsgen.ins
%doc %{_texmfdistdir}/source/latex-dev/amsmath/amsgen.dtx
%doc %{_texmfdistdir}/source/latex-dev/amsmath/amscd.ins
%doc %{_texmfdistdir}/source/latex-dev/amsmath/amscd.dtx
%doc %{_texmfdistdir}/source/latex-dev/amsmath/amsbsy.ins
%doc %{_texmfdistdir}/source/latex-dev/amsmath/amsbsy.dtx
%{_texmfdistdir}/tex
%{_texmfdistdir}/tex/latex-dev
%{_texmfdistdir}/tex/latex-dev/amsmath
%{_texmfdistdir}/tex/latex-dev/amsmath/amsxtra.sty
%{_texmfdistdir}/tex/latex-dev/amsmath/amstext.sty
%{_texmfdistdir}/tex/latex-dev/amsmath/amstex.sty
%{_texmfdistdir}/tex/latex-dev/amsmath/amsopn.sty
%{_texmfdistdir}/tex/latex-dev/amsmath/amsmath.sty
%{_texmfdistdir}/tex/latex-dev/amsmath/amsmath-2018-12-01.sty
%{_texmfdistdir}/tex/latex-dev/amsmath/amsgen.sty
%{_texmfdistdir}/tex/latex-dev/amsmath/amscd.sty
%{_texmfdistdir}/tex/latex-dev/amsmath/amsbsy.sty
%{_texmfdistdir}/doc
%doc %{_texmfdistdir}/doc/latex-dev
%doc %{_texmfdistdir}/doc/latex-dev/amsmath
%doc %{_texmfdistdir}/doc/latex-dev/amsmath/testmath.tex
%doc %{_texmfdistdir}/doc/latex-dev/amsmath/testmath.pdf
%doc %{_texmfdistdir}/doc/latex-dev/amsmath/technote.tex
%doc %{_texmfdistdir}/doc/latex-dev/amsmath/technote.pdf
%doc %{_texmfdistdir}/doc/latex-dev/amsmath/subeqn.tex
%doc %{_texmfdistdir}/doc/latex-dev/amsmath/subeqn.pdf
%doc %{_texmfdistdir}/doc/latex-dev/amsmath/manifest.txt
%doc %{_texmfdistdir}/doc/latex-dev/amsmath/diffs-m.txt
%doc %{_texmfdistdir}/doc/latex-dev/amsmath/changes.txt
%doc %{_texmfdistdir}/doc/latex-dev/amsmath/amsxtra.pdf
%doc %{_texmfdistdir}/doc/latex-dev/amsmath/amstext.pdf
%doc %{_texmfdistdir}/doc/latex-dev/amsmath/amsopn.pdf
%doc %{_texmfdistdir}/doc/latex-dev/amsmath/amsmath.pdf
%doc %{_texmfdistdir}/doc/latex-dev/amsmath/amsldoc.tex
%doc %{_texmfdistdir}/doc/latex-dev/amsmath/amsldoc.pdf
%doc %{_texmfdistdir}/doc/latex-dev/amsmath/amsgen.pdf
%doc %{_texmfdistdir}/doc/latex-dev/amsmath/amscd.pdf
%doc %{_texmfdistdir}/doc/latex-dev/amsmath/amsbsy.pdf
%doc %{_texmfdistdir}/doc/latex-dev/amsmath/ams-internal.txt
%doc %{_texmfdistdir}/doc/latex-dev/amsmath/ams-external.txt
%doc %{_texmfdistdir}/doc/latex-dev/amsmath/README.md

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
