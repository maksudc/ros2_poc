#!/usr/bin/env python3

from typing import List, Optional
import rclpy
from rclpy.context import Context
from rclpy.node import Node
from rclpy.parameter import Parameter

class MyNode(Node):
    def __init__(self) -> None:
        super().__init__("py_test")
        self.counter_ = 0
        self.get_logger().info("Hello Ros2")
        self.create_timer(0.5, self.timer_callback)
    
    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info("Hello " + str(self.counter_))

def main(args=None):
    rclpy.init(args=args)
    
    # node =  Node("py_test")
    # node.get_logger().info("Hello Ros2")
    # rclpy.spin(node)
    # rclpy.shutdown()

    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

