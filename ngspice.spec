#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : ngspice
Version  : 44.2
Release  : 20
URL      : https://sourceforge.net/projects/ngspice/files/ng-spice-rework/44.2/ngspice-44.2.tar.gz
Source0  : https://sourceforge.net/projects/ngspice/files/ng-spice-rework/44.2/ngspice-44.2.tar.gz
Summary  : General-purpose circuit simulator
Group    : Development/Tools
License  : GPL-3.0 MPL-2.0
Requires: ngspice-bin = %{version}-%{release}
Requires: ngspice-data = %{version}-%{release}
Requires: ngspice-lib = %{version}-%{release}
Requires: ngspice-license = %{version}-%{release}
Requires: ngspice-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : buildreq-configure
BuildRequires : fftw-dev
BuildRequires : file
BuildRequires : flex
BuildRequires : libXft-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(xaw7)
BuildRequires : readline-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
==================
Ngspice is a mixed-level/mixed-signal circuit simulator. Its code
is based on three open source software packages: Spice3f5, Cider1b1
and Xspice.

%package bin
Summary: bin components for the ngspice package.
Group: Binaries
Requires: ngspice-data = %{version}-%{release}
Requires: ngspice-license = %{version}-%{release}

%description bin
bin components for the ngspice package.


%package data
Summary: data components for the ngspice package.
Group: Data

%description data
data components for the ngspice package.


%package dev
Summary: dev components for the ngspice package.
Group: Development
Requires: ngspice-lib = %{version}-%{release}
Requires: ngspice-bin = %{version}-%{release}
Requires: ngspice-data = %{version}-%{release}
Provides: ngspice-devel = %{version}-%{release}
Requires: ngspice = %{version}-%{release}
Requires: fftw-dev

%description dev
dev components for the ngspice package.


%package lib
Summary: lib components for the ngspice package.
Group: Libraries
Requires: ngspice-data = %{version}-%{release}
Requires: ngspice-license = %{version}-%{release}

%description lib
lib components for the ngspice package.


%package license
Summary: license components for the ngspice package.
Group: Default

%description license
license components for the ngspice package.


%package man
Summary: man components for the ngspice package.
Group: Default

%description man
man components for the ngspice package.


%prep
%setup -q -n ngspice-44.2
cd %{_builddir}/ngspice-44.2
pushd ..
cp -a ngspice-44.2 buildavx2
popd
pushd ..
cp -a ngspice-44.2 buildavx512
popd
pushd ..
cp -a ngspice-44.2 buildapx
popd

%build
## build_prepend_once content
# Make a copy of the source directory for static builds
cp -pr . %{_builddir}/build-static
## build_prepend_once end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1740079861
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --disable-static --with-ngshared --enable-xspice --enable-cider --enable-openmp
## make_prepend content
if [[ -d %{_builddir}/build-static ]] && ! [[ -f %{_builddir}/build-static/config.status ]]; then
pushd %{_builddir}/build-static
./configure --with-x --enable-xspice --enable-cider --with-readline=yes --enable-openmp
make  %{?_smp_mflags}
popd
fi

# Point to the static app to run tests under `make check`
ln -s %{_builddir}/build-static/src/ngspice src/ngspice
## make_prepend end
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --disable-static --with-ngshared --enable-xspice --enable-cider --enable-openmp
## make_prepend content
if [[ -d %{_builddir}/build-static ]] && ! [[ -f %{_builddir}/build-static/config.status ]]; then
pushd %{_builddir}/build-static
./configure --with-x --enable-xspice --enable-cider --with-readline=yes --enable-openmp
make  %{?_smp_mflags}
popd
fi

# Point to the static app to run tests under `make check`
ln -s %{_builddir}/build-static/src/ngspice src/ngspice
## make_prepend end
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
GOAMD64=v4
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v4 -mprefer-vector-width=256 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v4 "
%configure --disable-static --disable-static --with-ngshared --enable-xspice --enable-cider --enable-openmp
## make_prepend content
if [[ -d %{_builddir}/build-static ]] && ! [[ -f %{_builddir}/build-static/config.status ]]; then
pushd %{_builddir}/build-static
./configure --with-x --enable-xspice --enable-cider --with-readline=yes --enable-openmp
make  %{?_smp_mflags}
popd
fi

# Point to the static app to run tests under `make check`
ln -s %{_builddir}/build-static/src/ngspice src/ngspice
## make_prepend end
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildapx/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --host=x86_64-clr-linux-gnu --disable-static --disable-static --with-ngshared --enable-xspice --enable-cider --enable-openmp
## make_prepend content
if [[ -d %{_builddir}/build-static ]] && ! [[ -f %{_builddir}/build-static/config.status ]]; then
pushd %{_builddir}/build-static
./configure --with-x --enable-xspice --enable-cider --with-readline=yes --enable-openmp
make  %{?_smp_mflags}
popd
fi

# Point to the static app to run tests under `make check`
ln -s %{_builddir}/build-static/src/ngspice src/ngspice
## make_prepend end
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :
cd ../buildavx512;
make %{?_smp_mflags} check || : || :
cd ../buildapx;
make %{?_smp_mflags} check || : || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1740079861
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ngspice
cp %{_builddir}/ngspice-%{version}/COPYING %{buildroot}/usr/share/package-licenses/ngspice/a1491cd75848105be6eef7dd4dee78b9bec62718 || :
cp %{_builddir}/ngspice-%{version}/src/spicelib/devices/adms/admst/COPYING %{buildroot}/usr/share/package-licenses/ngspice/c14c8abb8bb45bce3fd27255b2a59b2ba691b2a4 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v4
pushd ../buildavx512/
%make_install_v4
popd
GOAMD64=v3
pushd ../buildapx/
%make_install_va
popd
GOAMD64=v2
%make_install
## install_append content
if [[ -d %{_builddir}/build-static ]]; then
pushd %{_builddir}/build-static
/usr/bin/mkdir -p %{buildroot}/usr/bin
/usr/bin/install -c -m 755 src/ngspice %{buildroot}/usr/bin
/usr/bin/mkdir -p %{buildroot}/usr/share/man/man1
/usr/bin/install -c -m 644 man/man1/ngspice.1 %{buildroot}/usr/share/man/man1
popd
fi
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/ngspice/analog.cm
/V3/usr/lib64/ngspice/digital.cm
/V3/usr/lib64/ngspice/ivlng.vpi
/V3/usr/lib64/ngspice/spice2poly.cm
/V3/usr/lib64/ngspice/table.cm
/V3/usr/lib64/ngspice/xtradev.cm
/V3/usr/lib64/ngspice/xtraevt.cm
/V4/usr/lib64/ngspice/analog.cm
/V4/usr/lib64/ngspice/digital.cm
/V4/usr/lib64/ngspice/ivlng.vpi
/V4/usr/lib64/ngspice/spice2poly.cm
/V4/usr/lib64/ngspice/table.cm
/V4/usr/lib64/ngspice/xtradev.cm
/V4/usr/lib64/ngspice/xtraevt.cm
/VA/usr/lib64/ngspice/analog.cm
/VA/usr/lib64/ngspice/digital.cm
/VA/usr/lib64/ngspice/ivlng.vpi
/VA/usr/lib64/ngspice/spice2poly.cm
/VA/usr/lib64/ngspice/table.cm
/VA/usr/lib64/ngspice/xtradev.cm
/VA/usr/lib64/ngspice/xtraevt.cm
/usr/lib64/ngspice/analog.cm
/usr/lib64/ngspice/digital.cm
/usr/lib64/ngspice/ivlng.vpi
/usr/lib64/ngspice/spice2poly.cm
/usr/lib64/ngspice/table.cm
/usr/lib64/ngspice/xtradev.cm
/usr/lib64/ngspice/xtraevt.cm

%files bin
%defattr(-,root,root,-)
/usr/bin/ngspice

%files data
%defattr(-,root,root,-)
/usr/share/ngspice/scripts/ciderinit
/usr/share/ngspice/scripts/devaxis
/usr/share/ngspice/scripts/devload
/usr/share/ngspice/scripts/setplot
/usr/share/ngspice/scripts/spectrum
/usr/share/ngspice/scripts/spinit
/usr/share/ngspice/scripts/src/ngspice/cmtypes.h
/usr/share/ngspice/scripts/src/ngspice/cosim.h
/usr/share/ngspice/scripts/src/ngspice/miftypes.h
/usr/share/ngspice/scripts/src/verilator_main.cpp
/usr/share/ngspice/scripts/src/verilator_shim.cpp
/usr/share/ngspice/scripts/vlnggen

%files dev
%defattr(-,root,root,-)
/usr/include/ngspice/sharedspice.h
/usr/lib64/libngspice.so
/usr/lib64/pkgconfig/ngspice.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libngspice.so.0.0.12
/V3/usr/lib64/ngspice/ivlng.so
/V4/usr/lib64/libngspice.so.0.0.12
/V4/usr/lib64/ngspice/ivlng.so
/VA/usr/lib64/libngspice.so.0.0.12
/VA/usr/lib64/ngspice/ivlng.so
/usr/lib64/libngspice.so.0
/usr/lib64/libngspice.so.0.0.12
/usr/lib64/ngspice/ivlng.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ngspice/a1491cd75848105be6eef7dd4dee78b9bec62718
/usr/share/package-licenses/ngspice/c14c8abb8bb45bce3fd27255b2a59b2ba691b2a4

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ngspice.1
