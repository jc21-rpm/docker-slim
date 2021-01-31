%define debug_package %{nil}

%global gh_user docker-slim

Name:           docker-slim
Version:        1.34.0
Release:        1
Summary:        Minify and Secure Docker containers
Group:          Applications/System
License:        APACHEv2.0
URL:            https://github.com/docker-slim/docker-slim
Source:         https://github.com/%{gh_user}/%{name}/archive/%{version}.tar.gz
BuildRequires:  golang >= 1.13, make, which

%description
Don't change anything in your Docker container image and minify
it by up to 30x making it secure too! Keep doing what you are
doing. No need to change anything. Use the base image you want.
Use the package manager you want. Don't worry about hand
optimizing your Dockerfile. You shouldn't have to throw away
your tools and your workflow to have small container images.
Don't worry about manually creating Seccomp and AppArmor
security profiles. You shouldn't have to become an expert in
Linux syscalls, Seccomp and AppArmor to have secure containers.
Even if you do know enough about it wasting time reverse
engineering your application behavior can be time consuming.
docker-slim will optimize and secure your containers by
understanding your application and what it needs using various
analysis techniques. It will throw away what you don't need
reducing the attack surface for your container.

%prep
%setup -q -n %{name}-%{version}

%build
go build -o bin/docker-slim cmd/docker-slim/main.go
go build -o bin/docker-slim-sensor cmd/docker-slim-sensor/main.go

%install
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 0755 bin/%{name} $RPM_BUILD_ROOT%{_bindir}
install -m 0755 bin/%{name}-sensor $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf %{buildroot}

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-sensor

%changelog
* Mon Feb 1 2021 Jamie Curnow <jc@jc21.com> 1.34.0-1
- v1.34.0

* Thu Dec 17 2020 Jamie Curnow <jc@jc21.com> 1.33.0-1
- v1.33.0

* Tue Aug 25 2020 Jamie Curnow <jc@jc21.com> 1.32.0-1
- v1.32.0

* Tue Jul 28 2020 Jamie Curnow <jc@jc21.com> 1.30.0-1
- v1.30.0

* Fri Mar 20 2020 Jamie Curnow <jc@jc21.com> 1.29.0-1
- v1.29.0

* Tue Mar 17 2020 Jamie Curnow <jc@jc21.com> 1.28.1-1
- v1.28.1

* Mon Mar 2 2020 Jamie Curnow <jc@jc21.com> 1.27.0-1
- v1.27.0

* Fri Nov 29 2019 Jamie Curnow <jc@jc21.com> 1.26.1-1
- v1.26.1

* Sun Nov 17 2019 Jamie Curnow <jc@jc21.com> 1.26.0-1
- v1.26.0

* Mon Aug 5 2019 Jamie Curnow <jc@jc21.com> 1.25.3-1
- v1.25.3

* Tue Jul 23 2019 Jamie Curnow <jc@jc21.com> 1.25.2-1
- Initial spec
