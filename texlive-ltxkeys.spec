Name:		texlive-ltxkeys
Epoch:		1
Version:	28332
Release:	1
Summary:	A robust key parser for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ltxkeys
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxkeys.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxkeys.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides facilities for creating and managing keys
in the sense of the keyval and xkeyval packages, but it is
intended to be more robust and faster. Its robustness comes
from its ability to preserve braces in key values throughout
parsing. The need to preserve braces in key values arises often
in parsing keys (for example, in the xwatermark package). The
package is faster than xkeyval package because (among other
things) it avoids character-wise parsing of key values (called
"selective sanitization" by the xkeyval package). The package
also provides functions for defining and managing keys.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ltxkeys/ltxkeys.sty
%doc %{_texmfdistdir}/doc/latex/ltxkeys/README
%doc %{_texmfdistdir}/doc/latex/ltxkeys/ltxkeys-guide-table1.tex
%doc %{_texmfdistdir}/doc/latex/ltxkeys/ltxkeys-guide.cfg
%doc %{_texmfdistdir}/doc/latex/ltxkeys/ltxkeys-guide.pdf
%doc %{_texmfdistdir}/doc/latex/ltxkeys/ltxkeys-guide.tex
%doc %{_texmfdistdir}/doc/latex/ltxkeys/ltxkeys-test-20121122.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
