# SPDX-FileCopyrightText: 2024 Ryusei Fujimura
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import subprocess

class CalendarTalker(Node):
    def __init__(self):
        super().__init__('calendar')
        self.pub = self.create_publisher(String, 'calendar', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.month = 1
        self.year = 2025

    def timer_callback(self):
        command = ['cal', str(self.month), str(self.year)]
        result = subprocess.run(command, capture_output=True, text=True)
        calendar_data = result.stdout
        msg = String()
        msg.data = calendar_data
        self.pub.publish(msg)
        self.month += 1
        if self.month > 12:
            self.month = 1
            self.year += 1

def main():
    rclpy.init()
    calendar = CalendarTalker()
    rclpy.spin(calendar)
