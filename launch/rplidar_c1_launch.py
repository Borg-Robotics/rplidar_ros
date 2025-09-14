#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    # Get the path to the parameter files
    config_file = os.path.join(
        get_package_share_directory('rplidar_ros'),
        'config',
        'rplidar_c1_params.yaml'
    )
    
    laser_filter_config = os.path.join(
        get_package_share_directory('rplidar_ros'),
        'config',
        'laser_filter_config.yaml'
    )

    return LaunchDescription([
        Node(
            package='rplidar_ros',
            executable='rplidar_node',
            name='rplidar_node',
            parameters=[config_file],
            output='screen',
            remappings=[('scan', 'scan_raw')]),

        Node(
            package='laser_filters',
            executable='scan_to_scan_filter_chain',
            name='scan_to_scan_filter_chain',
            parameters=[laser_filter_config],
            remappings=[
                ('scan', 'scan_raw'),      # Input from lidar
                ('scan_filtered', 'scan')  # Output filtered scan
            ],
            output='screen'),
    ])