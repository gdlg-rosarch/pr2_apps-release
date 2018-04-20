# Script generated with Bloom
pkgdesc="ROS - pr2_teleop_general"
url='http://ros.org/wiki/pr2_teleop_general'

pkgname='ros-kinetic-pr2-teleop-general'
pkgver='0.6.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-angles'
'ros-kinetic-catkin'
'ros-kinetic-geometry-msgs'
'ros-kinetic-moveit-msgs'
'ros-kinetic-polled-camera'
'ros-kinetic-pr2-common-action-msgs'
'ros-kinetic-pr2-controller-manager'
'ros-kinetic-pr2-controllers-msgs'
'ros-kinetic-pr2-mechanism-msgs'
'ros-kinetic-pr2-msgs'
'ros-kinetic-ps3joy'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
'ros-kinetic-urdf'
)

depends=('ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-angles'
'ros-kinetic-geometry-msgs'
'ros-kinetic-moveit-msgs'
'ros-kinetic-polled-camera'
'ros-kinetic-pr2-arm-kinematics'
'ros-kinetic-pr2-common-action-msgs'
'ros-kinetic-pr2-controller-manager'
'ros-kinetic-pr2-controllers-msgs'
'ros-kinetic-pr2-mannequin-mode'
'ros-kinetic-pr2-mechanism-msgs'
'ros-kinetic-pr2-msgs'
'ros-kinetic-pr2-tuck-arms-action'
'ros-kinetic-ps3joy'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
'ros-kinetic-urdf'
)

conflicts=()
replaces=()

_dir=pr2_teleop_general
source=()
md5sums=()

prepare() {
    cp -R $startdir/pr2_teleop_general $srcdir/pr2_teleop_general
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

