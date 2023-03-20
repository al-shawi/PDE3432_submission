-------------------------------------------------------------------------------------------------------------------------------
							ABOUT ME AND THE ASSESSMENT
-------------------------------------------------------------------------------------------------------------------------------
NAME: HUSSAIN AL-SHAWI
STUDENT ID: M00647271
MODULE: PDE3432- MOBILE ROBOTS AND MANIPULATORS
ASSESSMENT: USING ROS2 TO SPAWN A ROBOT INTO A GAZEBO IGNITION WORLD
-------------------------------------------------------------------------------------------------------------------------------
						HOW TO SPAWN THE ROBOT INTO THE WORLD
-------------------------------------------------------------------------------------------------------------------------------
1. LAUNCH FILE FOR ALL THIS (SPAWN THE ROBOT IN THE ASSES WORLD) (ABLE TO MOVE OUT BALLS FROM THE "PLACE")

 - cd assess_rbot_ws/
 - colcon build
 - source install/setup.bash
 - ros2 launch rbot_pkg ign.launch.py
-------------------------------------------------------------------------------------------------------------------------------
						HOW TO ENABLE TELEOPERATION AND CHANGE SPEED
-------------------------------------------------------------------------------------------------------------------------------
2. WHEN THE WORLD HAVE BEEN LAUNCHED AND THE ROBOT HAVE BEEN SPAWNED 

 - RIGHT CLICK ON THE 3 DOTS IN THE RIGHT CORNER OF THE GAZEBO IGNITION WINDOW
 - IN THE SEARCH BAR, WRITE TELEOP (AND CLICK ON IT) (YOU WILL NOTICE THAT NOTHING HAPPEND)
 - UNDER RBOT WHERE ITS WHITE (THE ENTITY TREE)
 - RIGHT CLICK AND PRESS SHOW TITLE BAR (MAKE SURE NOTHING IS SLECTED)
 - LEFT CLICK ON THE UP ARROW ON THE ENTITY TREE
 - YOU WILL NOW BE ABLE SEE THE TELEOP
 - PRESS ON, SUBSCRIBE TO THE '/cmd_vel' TOPIC
 - MAKE SURE ANGULAR AND LINEAR VELOCITY IS SET TO 1.00 
 - NOW ENABLE THE KEYBOARD BY PRESSING "Input from keyboard (WASD)"
 - IT SHOULD NOW WORK TO MOVE THE ROBOT AROUND THE WORLD WITHOUT ANY PROBLEMS
 - YOU CAN CHANGE THE LINEAR VELOCITY TO 10 (FASTEST) AND ANGULAR VELOCITY TO 2 (FASTEST) AND YOU WILL SEE THAT THE ROBOT RESPOND
   AND INTERACT VERY WELL WITH THE WORLD.
-------------------------------------------------------------------------------------------------------------------------------
						HOW TO READ THE DATA FROM THE SENSOR
-------------------------------------------------------------------------------------------------------------------------------
3. MEASURE LINEAR AND ANGULAR MOTION WITH AN IMU SENSOR BY OPENING A NEW TERMINAL, AND

 - TYPE: ign topic -e -t 'imu'
-------------------------------------------------------------------------------------------------------------------------------
						HOW TO ACCOMPLISH THE TASK
-------------------------------------------------------------------------------------------------------------------------------
4. THE WAY MY ROBOT "RBOT" IS MADE TO ACCOMPLISH THE TASK IS JUST TO PUSH THEM OUT
 
  - TO MOVE OUT THE 2 BALLS ON THE FLOOR FROM "HOME" CAN BE DONE EASLY WITH A VELOCITY OF 1.00
  - THE LAST BALL ON THE STAIRS IS VERY TRICKY!! YOU HAVE TO GO IN THE HOME WITH A LINEAR VELOCITY OF 1.00 (TAKE OUT THE TWO BALLS) 
    THEN GO BEHIND/RIGHT OF THE STAIRS. FACE THE WALL (INFRONT OF THE BALL) HAVE SOME SPACE SO YOU CAN ACCELERATE AND PUT YOUR
    VELOCITY TO 10.00 AND DRIVE AS FAST AS YOU CAN INTO THE WALL AND YOU WILL BOUNCE THE ROBOT ON THE BALL AND IT WILL FALL DOWN
    THE STAIRS AND, THEN YOU CAN TAKE IT OUT FROM "HOME" LIKE YOU DID WITH THE LAST TWO. I WOULD SAY THAT IT IS ABIT OF TRIAL AND ERROR :)
    
    OBS!
    I DOES NOT ALWAYS WORK, AND IT CAN HAPPEN THAT THE ROBOT TURNS UPSIDE DOWN.
    THEN YOU WILL NEED TO CLOSE THE GAZEBO WINDOW AND LAUNCH THE PACKAGE AGAIN
-------------------------------------------------------------------------------------------------------------------------------
					OTHER WAYS TO SPAWN THE ROBOT IN THE WORLD
-------------------------------------------------------------------------------------------------------------------------------
5. ASSES WORLD

 - ign gazebo /home/ros/assess_world/assess2022.sdf -v 4
------------------------------------------------------------------------------------------------------------------------------
6. EMPTY WORLD WITH ROBOT
 
 - ign service -s /world/empty/create --reqtype ignition.msgs.EntityFactory --reptype ignition.msgs.Boolean --timeout 1000 --req
   'sdf_filename: "/home/ros/assess_rbot_ws/src/rbot_pkg/urdf/rbot.urdf", name: "rbot"'
------------------------------------------------------------------------------------------------------------------------------
7. ASSES WORLD WITH ROBOT 

 - ign service -s /world/assess/create --reqtype ignition.msgs.EntityFactory --reptype ignition.msgs.Boolean --timeout 1000 --req
   'sdf_filename: "/home/ros/assess_rbot_ws/src/rbot_pkg/urdf/rbot.urdf", name: "rbot"'
------------------------------------------------------------------------------------------------------------------------------
8. WORKING WITH TELEOP, THEN LATER ON ADDED SENSOR

 - ign service -s /world/assess/create --reqtype ignition.msgs.EntityFactory --reptype ignition.msgs.Boolean --timeout 1000 --req
   'sdf_filename: "/home/ros/assess_rbot_ws/src/rbot_pkg/urdf/rbot.urdf", name: "rbot"'
