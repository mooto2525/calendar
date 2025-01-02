# SPDX-FileCopyrightText: 2024 Ryusei Fujimura
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    calendar = launch_ros.actions.Node(
        package='mypkg',
        executable='calendar',
        output='screen'
    )

    return launch.LaunchDescription([calendar])
