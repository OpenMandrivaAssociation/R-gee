%global packname  gee
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          4.13.18
Release:          2
Summary:          Generalized Estimation Equation solver
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/gee_4.13-18.tar.gz
Requires:         R-stats 
Requires:         R-MASS 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-stats
BuildRequires:    R-MASS 
BuildRequires:    blas-devel
BuildRequires:    lapack-devel

%description
Generalized Estimation Equation solver

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
