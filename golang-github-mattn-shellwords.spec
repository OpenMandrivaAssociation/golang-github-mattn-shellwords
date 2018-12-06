%global goipath         github.com/mattn/go-shellwords
Version:                1.0.3

%gometa

Name:           %{goname}
Release:        6%{?dist}
Summary:        Parse line as shell words
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package devel
Summary:       %{summary}
BuildArch:     noarch

Provides:       golang-github-mattn-go-shellwords-devel = %{version}-%{release}
Obsoletes:      golang-github-mattn-go-shellwords-devel < 1.0.3-5

%description devel
%{summary}

This package contains library source intended for building other packages
which use import path with %{goipath} prefix.


%prep
%gosetup -q


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%doc README.md
%license LICENSE


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 07 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.3-5
- Re-template against More Go Packaging guidelines

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 22 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.3-3
- Tweak versioning macros.

* Sat Aug 19 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.3-2
- Fix bug in spec unpacking.

* Sat Aug 19 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.3-1
- Switch to released version

* Fri Aug 18 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.git9858af9
- Initial package for Fedora
