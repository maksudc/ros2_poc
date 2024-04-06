#!/user/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

from my_py_pkg.number_pub_sub_topic_task.settings import NUMBER_TOPIC


class NumberPublisher(Node):
    def __init__(self):
        super().__init__("number_publisher")
        self.publisher_ = self.create_publisher(Int64, NUMBER_TOPIC, 10)
        self.timer_ = self.create_timer(0.5, self.publish_number)
    
    def publish_number(self):
        msg = Int64()
        msg.data = 100
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args = args)
    node = NumberPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
