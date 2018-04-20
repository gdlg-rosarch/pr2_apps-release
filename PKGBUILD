# Script generated with Bloom
pkgdesc="ROS - Basic applications for the PR2 robot"
url='http://ros.org/wiki/pr2_apps'

pkgname='ros-kinetic-pr2-apps'
pkgver='0.6.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-pr2-app-manager'
'ros-kinetic-pr2-kinematics'
'ros-kinetic-pr2-mannequin-mode'
'ros-kinetic-pr2-position-scripts'
'ros-kinetic-pr2-teleop-general'
'ros-kinetic-pr2-tuckarm'
)

conflicts=()
replaces=()

_dir=pr2_apps
source=()
md5sums=()

prepare() {
    cp -R $startdir/pr2_apps $srcdir/pr2_apps
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

