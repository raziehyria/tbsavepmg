
import os
import time
import paramiko

# bc its saved locally, do rosrun
#cd desktop

#os.system('gnome-terminal -- rosrun map_server map_saver -f my_map')
#time.sleep(6)
#rosrun map_server map_saver -f my_map

#apply pgm map filtering from nav onto pgm
os.system('gnome-terminal -- python3 PGMReader.py')
time.sleep(6)

#apply through crop map
os.system('gnome-terminal -- python3 Pathable_Cell_for_Map.py')
time.sleep(6)


#send over 'croppedmap.png' to turtlebot for mc website
os.system('gnome-terminal -- scp ~/modified_map.png ubuntu@192.168.8.209:/home/ubuntu/team2/nodeServer/assets')

time.sleep(4)
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
os.system('gnome-terminal -- roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml')


while True:
	time.sleep(1)
