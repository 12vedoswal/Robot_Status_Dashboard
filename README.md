# Robot_Status_publisher
A ROS 2 project that simulates multiple autonomous robots publishing their operational status to a central dashboard. The dashboard continuously monitors each robot's health, detects abnormal conditions, and provides a live terminal-based monitoring interface.

✨ Features
Simulates multiple robots using independent publisher nodes
Publishes robot telemetry over a common ROS 2 topic
Displays a real-time monitoring dashboard

Tracks:
🔋 Battery Level
🌡️ Temperature
🚀 Speed
📋 Current Task
⚙️ Robot Status

Automatic health alerts:
Low Battery
Overheating
Robot Offline
Supports adding any number of robots

🛠️ Technologies Used
ROS 2
Python
rclpy
Custom ROS 2 Messages
Publisher–Subscriber Architecture

📂 Project Structure
multi_robot_dashboard/
│
├── robot_publisher.py      # Publishes robot status
├── dashboard.py            # Displays live dashboard
└── robot_status_interfaces/
    └── RobotStatus.msg     # Custom message definition
    
🚀 How it Works
Each robot runs its own publisher node.
Every second, a robot publishes:
Battery percentage
Temperature
Speed
Current task
Robot status
The dashboard subscribes to /robot_status.
Incoming data is stored and refreshed every second.
Health conditions are evaluated and alerts are displayed whenever necessary.

Example Dashboard
================================================================================
                     Robot Status Dashboard
================================================================================

Robot        Battery    Temperature  Speed     Task          Status      Alert
--------------------------------------------------------------------------------
robot_1      92.0       31.5         254.3     Patroling     Active      OK
robot_2      18.0       28.7         180.5     Charging      Warning     Low Battery
robot_3      74.0       75.4         320.8     Inspection    Active      Overheating

Future Improvements
RViz visualization
Web-based dashboard
Battery drain simulation
Data logging
Graphical plots
Robot diagnostics service
Integration with Nav2 and SLAM
MQTT/IoT monitoring

Learning Outcomes
ROS 2 Publisher/Subscriber communication
Custom message creation
Managing multiple ROS 2 nodes
Real-time monitoring systems
Python-based ROS 2 application development
