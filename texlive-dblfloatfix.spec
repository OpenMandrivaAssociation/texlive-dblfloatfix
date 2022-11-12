Name:		texlive-dblfloatfix
Version:	28983
Release:	1
Summary:	Fixes for twocolumn floats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dblfloatfix
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dblfloatfix.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dblfloatfix.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
