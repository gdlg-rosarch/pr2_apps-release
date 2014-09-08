Name:           ros-hydro-pr2-mannequin-mode
Version:        0.5.6
Release:        1%{?dist}
Summary:        ROS pr2_mannequin_mode package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/pr2_mannequin_mode
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-pr2-controller-manager
Requires:       ros-hydro-pr2-controllers-msgs
Requires:       ros-hydro-trajectory-msgs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-pr2-controller-manager
BuildRequires:  ros-hydro-pr2-controllers-msgs
BuildRequires:  ros-hydro-trajectory-msgs

%description
The pr2_mannequin_mode package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Sep 08 2014 Laura Lindzey <lindzey@gmail.com> - 0.5.6-1
- Autogenerated by Bloom

* Sun Sep 07 2014 Laura Lindzey <lindzey@gmail.com> - 0.5.6-0
- Autogenerated by Bloom

