import json

def update_json_fields(path):
    with open(path, 'r') as f:
        data = json.load(f)

    target_ip = "192.168.1.50"
    data["MID360"]["host_net_info"]["cmd_data_ip"] = target_ip
    data["MID360"]["host_net_info"]["push_msg_ip"] = target_ip
    data["MID360"]["host_net_info"]["point_data_ip"] = target_ip
    data["MID360"]["host_net_info"]["imu_data_ip"] = target_ip

    data["lidar_configs"][0]["ip"] = "192.168.1.128"

    with open(path, 'w') as f:
        json.dump(data, f, indent=2)


update_json_fields("/root/ros2_ws/install/livox_ros_driver2/share/livox_ros_driver2/config/MID360_config.json")
