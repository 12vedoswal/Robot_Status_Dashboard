import rclpy
from rclpy.node import Node
from robot_status_interfaces.msg import RobotStatus
import random

class RobotPublisher(Node):
    def __init__(self, robot_name):
        super().__init__(robot_name + "_publisher")
        self.robot_name = robot_name
        self.publishers_ = self.create_publisher(RobotStatus, '/robot_status',10)
        self.timer_ = self.create_timer(1.0,self.publish_status_callback)

        self.battery = 100.0

        self.current_task =["patroling", "Charging", "Idle", "Inspection"]

        self.status = ["Idle" , "Active" , "Warning"]


    def publish_status_callback(self):
        msg = RobotStatus()
        msg.robot_name = self.robot_name
        msg.battery = self.battery
        msg.temperature = random.uniform(15.0,55.0)
        msg.speed = random.uniform(100.0,500.0)
        msg.current_task = random.choice(self.current_task)
        msg.status = random.choice(self.status)
        self.publishers_.publish(msg)
        
        self.get_logger().info(f"{self.robot_name} | with {self.battery}% battery is in {msg.status} state and cuurent performing {msg.current_task} task!")

        

def main(args=None):
    rclpy.init(args=args)
    import sys

    if len(sys.argv) > 1:
        robot_name = sys.argv[1]
    else:
        robot_name = 'robot_1'
    node = RobotPublisher(robot_name)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__" :
    main()