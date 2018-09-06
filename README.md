# ROS2 Jaguar4x4 top-level repository

This is the top-level repository for the ROS2 support on the DrRobot Jaguar4x4.

## Getting started
This code is known to work on Ubuntu 18.04 running ROS2 Bouncy.
Other Ubuntu or ROS2 distributions may work, but your mileage may
vary.

Start by installing ROS2 Bouncy from packages, starting with the
instructions at https://github.com/ros2/ros2/wiki/Linux-Install-Debians

Now do the following:

1.  wget https://raw.githubusercontent.com/TRI-jaguar4x4/jaguar4x4/master/jaguar4x4.repos
1.  mkdir -p ~/jaguar_ws/src
1.  cd ~/jaguar_ws
1.  vcs import src < ~/jaguar4x4.repos

At this point, all of the code necessary will be installed, we can now build:

1.  source /opt/ros/bouncy/setup.bash
1.  colcon build --event-handlers console_direct+

This will take a bit of time to compile, especially on slower machines.
