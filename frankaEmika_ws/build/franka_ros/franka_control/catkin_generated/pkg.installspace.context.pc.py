# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include;/opt/ros/melodic/include/libfranka".split(';') if "${prefix}/include;/opt/ros/melodic/include/libfranka" != "" else []
PROJECT_CATKIN_DEPENDS = "controller_interface;franka_hw;franka_msgs;geometry_msgs;pluginlib;realtime_tools;roscpp;sensor_msgs;tf2_msgs;std_srvs".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lfranka_state_controller;/opt/ros/melodic/lib/libfranka.so.0.9.0".split(';') if "-lfranka_state_controller;/opt/ros/melodic/lib/libfranka.so.0.9.0" != "" else []
PROJECT_NAME = "franka_control"
PROJECT_SPACE_DIR = "/home/developer/frankaEmika_ws/install"
PROJECT_VERSION = "0.10.1"
