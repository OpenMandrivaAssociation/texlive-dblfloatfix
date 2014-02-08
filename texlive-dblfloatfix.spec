# revision 17191
# category Package
# catalog-ctan /macros/latex/contrib/dblfloatfix
# catalog-date 2010-03-09 12:54:42 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-dblfloatfix
Version:	1.0
Release:	3
Summary:	Fixes for twocolumn floats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dblfloatfix
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dblfloatfix.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dblfloatfix.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package solves two problems: floats in a twocolumn document
come out in the right order and allowed float positions are now
[tbp]. The packages actually merges facilities from fixltx2e
and stfloats.

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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 750878
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718207
- texlive-dblfloatfix
- texlive-dblfloatfix
- texlive-dblfloatfix
- texlive-dblfloatfix

