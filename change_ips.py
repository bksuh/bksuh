import json
import sys

def update_json_fields(path, t_ip, l_ip):
    with open(path, 'r') as f:
        data = json.load(f)

    target_ip_host = t_ip
    lidar_ip = l_ip
    data["MID360"]["host_net_info"]["cmd_data_ip"] = target_ip_host
    data["MID360"]["host_net_info"]["push_msg_ip"] = target_ip_host
    data["MID360"]["host_net_info"]["point_data_ip"] = target_ip_host
    data["MID360"]["host_net_info"]["imu_data_ip"] = target_ip_host

    data["lidar_configs"][0]["ip"] = lidar_ip

    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    # Check if arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python3 change_ips.py t_ip=<target_ip> l_ip=<lidar_ip>")
        sys.exit(1)

    # Parse arguments
    try:
        t_ip = sys.argv[1].split("=")[1]
        l_ip = sys.argv[2].split("=")[1]
    except IndexError:
        print("Error: Arguments must be in the format t_ip=<target_ip> l_ip=<lidar_ip>")
        sys.exit(1)

    # Path to the JSON file
    json_path = "/root/ros2_ws/install/livox_ros_driver2/share/livox_ros_driver2/config/MID360_config.json"

    # Update JSON fields
    update_json_fields(json_path, t_ip, l_ip)
    print(f"Updated JSON file at {json_path} with t_ip={t_ip} and l_ip={l_ip}")
