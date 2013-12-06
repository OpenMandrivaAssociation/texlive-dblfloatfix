# revision 28983
# category Package
# catalog-ctan /macros/latex/contrib/dblfloatfix
# catalog-date 2013-01-29 13:50:02 +0100
# catalog-license lppl1.3
# catalog-version 1.0a
Name:		texlive-dblfloatfix
Version:	1.0a
Release:	2
Summary:	Fixes for twocolumn floats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dblfloatfix
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dblfloatfix.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dblfloatfix.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package solves two problems: floats in a twocolumn document
come out in the right order and allowed float positions are now
[tbp]. The package actually merges facilities from fixltx2e and
stfloats.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dblfloatfix/dblfloatfix.sty
%doc %{_texmfdistdir}/doc/latex/dblfloatfix/dblfloatfix.pdf
%doc %{_texmfdistdir}/doc/latex/dblfloatfix/dblfloatfix.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
