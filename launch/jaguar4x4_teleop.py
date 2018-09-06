# Copyright 2018 Toyota Research Institute.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import ament_index_python.packages
import launch
import launch_ros.actions

def generate_launch_description():
    jaguar_base = launch_ros.actions.Node(package='jaguar4x4_base',
                                          node_executable='jaguar4x4_base_node',
                                          output='screen')

    jaguar_arm = launch_ros.actions.Node(package='jaguar4x4_arm',
                                          node_executable='jaguar4x4_arm_node',
                                          output='screen')

    teleop_twist_joy_params_file = os.path.join(ament_index_python.packages.get_package_share_directory('jaguar4x4'), 'teleop_twist_joy_params.yaml')
    teleop_twist_joy = launch_ros.actions.Node(package='teleop_twist_joy',
                                               node_executable='teleop_node',
                                               output='screen',
                                               arguments=['__params:=' + teleop_twist_joy_params_file])

    joy = launch_ros.actions.Node(package='joy',
                                  node_executable='joy_node',
                                  output='screen')

    return launch.LaunchDescription([jaguar_base, teleop_twist_joy, joy, jaguar_arm,
                                     launch.actions.RegisterEventHandler(event_handler=launch.event_handlers.OnProcessExit(
                                         target_action=jaguar_base,
                                         on_exit=[launch.actions.EmitEvent(event=launch.events.Shutdown())],
                                         )),
    ])
