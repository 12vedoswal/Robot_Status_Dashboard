import rclpy
from rclpy.node import Node
from robot_status_interfaces.msg import RobotStatus
import time

class Dashboard(Node):
    def __init__(self):
        super().__init__("dashboard")
        self.subscriptions_ = self.create_subscription(RobotStatus, "/robot_status", self.dashboard_callback,10)

        self.robot_data = {}
        self.display_timer = self.create_timer(1.0, self.display_timer_callback)

    def dashboard_callback(self, msg):
        
        self.robot_data[msg.robot_name] = { 
            'battery' : msg.battery ,
            'temperature' : msg.temperature ,
            'speed' : msg.speed ,
            'task' : msg.current_task,
            'status' : msg.status,
            'time' : time.time()
        }

    def display_timer_callback(self):
        
        print('\n' + '=' * 80)
        print('     Robot Status Dashboard')
        print('=' * 80)

        print(
            f'{'Robot':<12}'
            f'{'Battery':<12}'
            f'{'Temperature':<10}'
            f'{'Speed':<10}'
            f'{'Task':<15}'
            f'{'Status':<12}'
            f'{'Alert'}'
        )

        print(f'-' * 80)
        current_time = time.time()

        for robot,data in self.robot_data.items():
            alert ='Ok'

            if data['battery'] <20:
                alert="Low battery"
            
            elif data['temperature'] >70:
                alert="Overheating"

            elif current_time - data['time'] >5:
                alert="Offline"

            print(
                f'{'Robot':<12}'
                f'{data['battery']:<12.1f}'
                f'{data['temperature']:<12.1f}'
                f'{data['speed']:<10.1f}'
                f'{data['task']:<15}'
                f'{data['status']:<12}'
                f'{alert}'
            )

def main(args=None):
    rclpy.init(args=args)
    node = Dashboard()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__" :
    main()