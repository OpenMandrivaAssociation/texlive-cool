# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/cool
# catalog-date 2007-03-05 15:26:58 +0100
# catalog-license lgpl
# catalog-version 1.35
Name:		texlive-cool
Version:	1.35
Release:	1
Summary:	COntent-Oriented LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cool
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cool.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cool.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cool.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package gives LaTeX the power to retain mathematical
meaning of its expressions in addition to the typsetting
instructions; essentially separating style from the content of
the math. One advantage of keeping mathematical meaning is that
conversion of LaTeX documents to other executable formats (such
as Content MathML or Mathematica code) is greatly simplified.
The package requires the coolstr, coollist and forloop
packages.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cool/cool.sty
%doc %{_texmfdistdir}/doc/latex/cool/Content_LaTeX_Package_Demo.pdf
%doc %{_texmfdistdir}/doc/latex/cool/Content_LaTeX_Package_Demo.tex
%doc %{_texmfdistdir}/doc/latex/cool/README
%doc %{_texmfdistdir}/doc/latex/cool/cool.pdf
#- source
%doc %{_texmfdistdir}/source/latex/cool/cool.dtx
%doc %{_texmfdistdir}/source/latex/cool/cool.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
