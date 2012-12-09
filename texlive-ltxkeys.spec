# revision 24898
# category Package
# catalog-ctan /macros/latex/contrib/ltxkeys
# catalog-date 2011-12-19 23:56:31 +0100
# catalog-license lppl
# catalog-version 0.0.3
Name:		texlive-ltxkeys
Version:	0.3.0
Release:	2
Summary:	A robust key parser for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ltxkeys
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxkeys.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxkeys.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/ltxkeys/pathkeys.sty
%doc %{_texmfdistdir}/doc/latex/ltxkeys/README
%doc %{_texmfdistdir}/doc/latex/ltxkeys/ltxkeys-guide.cfg
%doc %{_texmfdistdir}/doc/latex/ltxkeys/ltxkeys-guide.pdf
%doc %{_texmfdistdir}/doc/latex/ltxkeys/ltxkeys-guide.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3.0-2
+ Revision: 753575
- Rebuild to reduce used resources

* Mon Dec 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.3.0-1
+ Revision: 745302
- Manually increase version as upstream decreased it
- texlive-ltxkeys

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2.7-1
+ Revision: 739824
- texlive-ltxkeys

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1.0-1
+ Revision: 718913
- texlive-ltxkeys
- texlive-ltxkeys
- texlive-ltxkeys
- texlive-ltxkeys

