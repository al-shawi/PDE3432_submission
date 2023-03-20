from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():

    # Define the command to spawn the robot in the world
    # Uses the ign service command to spawn the robot model in the Gazebo world
    spawn_robot_cmd = ['ign', 'service', '-s', '/world/assess/create', '--reqtype', 'ignition.msgs.EntityFactory', '--reptype', 'ignition.msgs.Boolean', '--timeout', '1000', '--req', 'sdf_filename: "/home/ros/assess_rbot_ws/src/rbot_pkg/urdf/rbot.urdf", name: "rbot"']

    # Define the command to start gazebo
    # uses the ign gazebo command to start Gazebo with the path to the simulation world file
    start_gazebo_cmd = ['ign', 'gazebo', '/home/ros/assess_rbot_ws/src/rbot_pkg/world/assess_world/assess2022.sdf', '-v', '4']

    # Run the command lines
    # ExecuteProcess nodes using the ExecuteProcess action from the launch.actions
    spawn_robot_node = ExecuteProcess(
        cmd=spawn_robot_cmd,
        output='screen'
    )

    start_gazebo_node = ExecuteProcess(
        cmd=start_gazebo_cmd,
        output='screen'
    )

    # Return the launch description with the command lines
    return LaunchDescription([
        spawn_robot_node,
        start_gazebo_node
    ])
