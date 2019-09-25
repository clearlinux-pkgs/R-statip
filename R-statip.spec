#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-statip
Version  : 0.2.0
Release  : 12
URL      : https://cran.r-project.org/src/contrib/statip_0.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/statip_0.2.0.tar.gz
Summary  : Statistical Functions for Probability Distributions and
Group    : Development/Tools
License  : GPL-3.0
Requires: R-statip-lib = %{version}-%{release}
Requires: R-bazar
Requires: R-clue
Requires: R-distrEx
BuildRequires : R-bazar
BuildRequires : R-clue
BuildRequires : R-distrEx
BuildRequires : buildreq-R

%description
# statip: miscellaneous statistical functions
[![Travis-CI Build Status](https://travis-ci.org/paulponcet/statip.svg?branch=master)](https://travis-ci.org/paulponcet/statip)

%package lib
Summary: lib components for the R-statip package.
Group: Libraries

%description lib
lib components for the R-statip package.


%prep
%setup -q -c -n statip

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569385673

%install
export SOURCE_DATE_EPOCH=1569385673
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library statip
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library statip
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library statip
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc statip || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/statip/DESCRIPTION
/usr/lib64/R/library/statip/INDEX
/usr/lib64/R/library/statip/Meta/Rd.rds
/usr/lib64/R/library/statip/Meta/features.rds
/usr/lib64/R/library/statip/Meta/hsearch.rds
/usr/lib64/R/library/statip/Meta/links.rds
/usr/lib64/R/library/statip/Meta/nsInfo.rds
/usr/lib64/R/library/statip/Meta/package.rds
/usr/lib64/R/library/statip/NAMESPACE
/usr/lib64/R/library/statip/NEWS.md
/usr/lib64/R/library/statip/R/statip
/usr/lib64/R/library/statip/R/statip.rdb
/usr/lib64/R/library/statip/R/statip.rdx
/usr/lib64/R/library/statip/help/AnIndex
/usr/lib64/R/library/statip/help/aliases.rds
/usr/lib64/R/library/statip/help/paths.rds
/usr/lib64/R/library/statip/help/statip.rdb
/usr/lib64/R/library/statip/help/statip.rdx
/usr/lib64/R/library/statip/html/00Index.html
/usr/lib64/R/library/statip/html/R.css
/usr/lib64/R/library/statip/tests/testthat.R
/usr/lib64/R/library/statip/tests/testthat/test-mfv.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/statip/libs/statip.so
/usr/lib64/R/library/statip/libs/statip.so.avx2
