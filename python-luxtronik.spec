%global srcname luxtronik

Name:           python-%{srcname}
Version:        0.3.14
Release:        1%{?dist}
License:        MIT
Summary:        Library to interact with a Luxtronik heatpump controller
URL:            https://github.com/Bouni/python-luxtronik
Source0:        %{pypi_source}
Source1:        dump-luxtronik.py

BuildRequires:  python3-devel

BuildArch:      noarch

%global _description %{expand:
Python library that allows you to interact with a Luxtronik heatpump controller.
}

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version}
%generate_buildrequires
%pyproject_buildrequires

cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%py3_check_import %{srcname}

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENCE.md
%doc README.md dump-luxtronik.py

%changelog
* Mon Nov 14 2022 Simone Caronni <negativo17@gmail.com> - 0.3.14-1
- First build.
