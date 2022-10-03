from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            # the name of the executable is set in CMakeLists.txt, towards the end of
            # the file, in add_executable(...) and the directives following it
            package='proxemic_detector_pkg', executable='turtlebot_proxemic_detector_node', output='screen'),
        launch_ros.actions.Node(
            # the name of the executable is set in CMakeLists.txt, towards the end of
            # the file, in add_executable(...) and the directives following it
            package='proxemic_detector_pkg', executable='rgb_image_publisher_node', output='screen'),
        launch_ros.actions.Node(
            # the name of the executable is set in CMakeLists.txt, towards the end of
            # the file, in add_executable(...) and the directives following it
            package='proxemic_detector_pkg', executable='depth_image_publisher_node', output='screen'),
    ])
