%global tl_name dblfloatfix
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0a
Release:	%{tl_revision}.1
Summary:	Fixes for twocolumn floats
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dblfloatfix
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dblfloatfix.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dblfloatfix.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package solves two problems: floats in a twocolumn document come out
in the right order and allowed float positions are now [tbp]. The
package actually merges facilities from fixltx2e and stfloats.

