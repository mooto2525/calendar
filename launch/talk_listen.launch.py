import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    calendar = launch_ros.actions.Node(
        package='calendar_data',
        executable='calendar',
        )
    listener = launch_ros.actions.Node(
        package='calendar_data',
        executable='listener',
        output='screen'
        )

    return launch.LaunchDescription([calendar, listener])
