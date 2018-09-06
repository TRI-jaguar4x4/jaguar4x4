# ROS2 Jaguar4x4 top-level repository

This is the top-level repository for the ROS2 support on the DrRobot Jaguar4x4.

## Hardware
The hardware that this code was developed against is a Jaguar4x4 Wheel with
Arm (http://jaguar.drrobot.com/specification_4x4wArm.asp).  The code should
work with a Jaguar4x4 without the arm, but the launch files currently won't
work.  In theory a Jaguar4x4 with tracks should also work, but this hasn't
been tested and the base will probably need some tuning.

In addition to the robot itself, a Logitech joystick is needed (which may come
with the robot).  No additional hardware is necessary.

## Connecting to the robot
After connecting the battery and turning on the robot, the Jaguar4x4 will
present a wireless AP to connect to.  The "control" computer that will run
this software should be attached to that AP with a static IP address on
the 192.168.0.0/24 network (ensure that the chosen static IP is not
192.168.0.60 - 192.168.0.69).

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

## Using the robot
Once everything is compiled, the file `install/setup.bash` should be sourced
to get access to all of the necessary parts.  At this point, it should be
possible to run the teleop launch file, which will launch the base node, the
arm node, and the joystick nodes and allow the user to drive the robot around:

```
$ ros2 launch jaguar4x4 jaguar4x4_teleop.py
```

Note that the software comes up in ESTOP mode to ensure safety.  To take the
robot out of ESTOP, click the left analog stick on the joystick.  To put the
robot back into ESTOP, click the right analog stick on the joystick.  Once
out of ESTOP, the dead man switch (top-right RB button) must be held in for
any commands to be sent to the robot.  With RB held down, pressing forwards
or backwards on the left stick should drive the robot linearly, while pressing
left or right on the right stick should turn the robot.  Pressing Y and A will
move the lower (shoulder) joint of the arm up and down, respectively, while
pressing X and B will move the upper (elbow) joint of the arm up and down,
respectively.
