import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CalenderListener(Node):
    def __init__(self):
        super().__init__('calender_listener')
        self.subscription = self.create_subscription(String, 'calender', self.listener_callback, 10)
    def listener_callback(self, msg):
        self.get_logger().info(f'Received calendar data:\n{msg.data}')

def main():
    rclpy.init()
    calender_listener = CalenderListener()
    rclpy.spin(calender_listener)
