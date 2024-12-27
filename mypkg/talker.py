import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import subprocess

class CalenderTalker(Node):
    def __init__(self):
        super().__init__('calender_talker')
        self.pub = self.create_publisher(String, 'calender', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.month = 1
        self.year = 2025

    def timer_callback(self):
        command = ['cal', str(self.month), str(self.year)]
        result = subprocess.run(command, capture_output=True, text=True)
        calender = result.stdout
        msg = String()
        msg.data = calender
        self.pub.publish(msg)
        self.month += 1
        if self.month > 12:
            self.month = 1
            self.year += 1

def main():
    rclpy.init()
    calender_talker = CalenderTalker()
    rclpy.spin(calender_talker)
