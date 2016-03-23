Name:           ros-indigo-pr2-teleop-general
Version:        0.5.21
Release:        1%{?dist}
Summary:        ROS pr2_teleop_general package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_teleop_general
Source0:        %{name}-%{version}.tar.gz

Requires:       bullet-devel
Requires:       ros-indigo-actionlib
Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-angles
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-moveit-msgs
Requires:       ros-indigo-polled-camera
Requires:       ros-indigo-pr2-common-action-msgs
Requires:       ros-indigo-pr2-controller-manager
Requires:       ros-indigo-pr2-controllers-msgs
Requires:       ros-indigo-pr2-mechanism-msgs
Requires:       ros-indigo-pr2-msgs
Requires:       ros-indigo-ps3joy
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-tf
Requires:       ros-indigo-urdf
BuildRequires:  bullet-devel
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-angles
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-moveit-msgs
BuildRequires:  ros-indigo-polled-camera
BuildRequires:  ros-indigo-pr2-common-action-msgs
BuildRequires:  ros-indigo-pr2-controller-manager
BuildRequires:  ros-indigo-pr2-controllers-msgs
BuildRequires:  ros-indigo-pr2-mechanism-msgs
BuildRequires:  ros-indigo-pr2-msgs
BuildRequires:  ros-indigo-ps3joy
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-urdf

%description
pr2_teleop_general

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Mar 23 2016 Devon Ash <dash@clearpathrobotics.com> - 0.5.21-1
- Autogenerated by Bloom

* Tue Mar 22 2016 Devon Ash <dash@clearpathrobotics.com> - 0.5.21-0
- Autogenerated by Bloom

* Tue Feb 10 2015 Devon Ash <dash@clearpathrobotics.com> - 0.5.18-0
- Autogenerated by Bloom

* Fri Feb 06 2015 Devon Ash <dash@clearpathrobotics.com> - 0.5.17-0
- Autogenerated by Bloom

