import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CalendarListener(Node):
    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(String, 'calendar', self.listener_callback, 10)
    def listener_callback(self, msg):
        self.get_logger().info(f'Received calendar data:\n{msg.data}')

def main():
    rclpy.init()
    listener = CalendarListener()
    rclpy.spin(listener)
