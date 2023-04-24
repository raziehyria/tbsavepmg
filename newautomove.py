import os
import time
import paramiko

# Launch roscore in a new terminal
os.system('gnome-terminal -- roscore')

# Wait for roscore to start up
time.sleep(5)

# Launch turtlebot3_robot.launch in a new terminal
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('192.168.8.209', username='ubuntu', password='turtlebot')

shell = ssh.invoke_shell()
shell.send('roslaunch turtlebot3_bringup turtlebot3_robot.launch\n')

# Wait for turtlebot3_robot.launch to start up
time.sleep(8)

# Launch turtlebot3_slam.launch in a new terminal
os.system('gnome-terminal -- roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping')

# Wait for turtlebot3_slam.launch to start up
time.sleep(10)

# Launch move_base.launch in a new terminal
os.system('gnome-terminal -- roslaunch turtlebot3_navigation move_base.launch')

# Wait for move_base.launch to start up
time.sleep(5)

# Launch explore.launch in a new terminal
os.system('gnome-terminal -- roslaunch explore_lite explore.launch')

completion_threshold = 0.8  # set the completion threshold here
while True:
    time.sleep(1)
    # Check the map's status
    status = os.system('rosrun map_server map_saver -f /tmp/my_map')
    if status == 0:  # if the map has been successfully saved
        print("Map saved successfully")
        break
    elif status == 256:  # if the map is still being built
        print("Map is still being built")
        # Check the completion percentage of the map
        with open('/tmp/my_map.yaml', 'r') as f:
            yaml_str = f.read()
        completion_percent = yaml_str.count('occ') / yaml_str.count(' ')
        if completion_percent >= completion_threshold:
            # If the completion percentage is greater than or equal to the threshold, save the map
            print(f"Map completion threshold ({completion_threshold * 100}%) reached. Saving map...")
            os.system('rosrun map_server map_saver -f /tmp/my_map')
