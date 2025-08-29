from launch import LaunchDescription
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    return LaunchDescription([
        # 🔹 base_link → laser 고정 변환 추가
        launch_ros.actions.Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            # translation (x y z) + rotation (roll pitch yaw) + parent child
            arguments=['0.27', '0.0', '0.0', '0', '0', '0', 'base_link', 'laser'],
            name='static_tf_pub'
        ),

        # 🔹 slam_toolbox 실행
        launch_ros.actions.Node(
          parameters=[
            {'use_sim_time': True},
            get_package_share_directory("slam_toolbox") + '/config/mapper_params_offline.yaml'
          ],
          package='slam_toolbox',
          executable='sync_slam_toolbox_node',
          name='slam_toolbox',
          output='screen'
        )
    ])

