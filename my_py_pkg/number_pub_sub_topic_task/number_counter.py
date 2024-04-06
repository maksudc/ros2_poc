#!/user/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64

from my_py_pkg.number_pub_sub_topic_task.settings import NUMBER_TOPIC, NUMBER_COUNTER_TOPIC

class NumberCounter(Node):
    def __init__(self) -> None:
        super().__init__("number_counter")

        self.counter_ = 0

        self.publisher_ = self.create_publisher(Int64, NUMBER_COUNTER_TOPIC, 10)
        self.subsriber = self.create_subscription(Int64, NUMBER_TOPIC, self.callback_on_number_received, 10)

    def callback_on_number_received(self, msg: Int64) -> None:
        self.counter_+= 1

        msg = Int64()
        msg.data = self.counter_

        self.publisher_.publish(msg)

def main(args=None) -> None:
  rclpy.init(args = args)
  node = NumberCounter()
  rclpy.spin(node)
  rclpy.shutdown()

if __name__ ==  '__main__':
   main()