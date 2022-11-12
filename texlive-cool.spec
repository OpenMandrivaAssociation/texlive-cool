Name:		texlive-cool
Version:	15878
Release:	1
Summary:	COntent-Oriented LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cool
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cool.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cool.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cool.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
