# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/cool
# catalog-date 2007-03-05 15:26:58 +0100
# catalog-license lgpl
# catalog-version 1.35
Name:		texlive-cool
Version:	1.35
Release:	4
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

%description
The package gives LaTeX the power to retain mathematical
meaning of its expressions in addition to the typsetting
instructions; essentially separating style from the content of
the math. One advantage of keeping mathematical meaning is that
conversion of LaTeX documents to other executable formats (such
as Content MathML or Mathematica code) is greatly simplified.
The package requires the coolstr, coollist and forloop
packages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.35-2
+ Revision: 750548
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.35-1
+ Revision: 718150
- texlive-cool
- texlive-cool
- texlive-cool
- texlive-cool

