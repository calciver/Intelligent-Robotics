#!/usr/bin/python

import math
import time
import rospy
from geometry_msgs.msg import Twist

def goForward(cmd):
    _linear = 0.2
    _angular = 0

    twist = Twist()
    twist.linear.x = _linear
    twist.angular.z = _angular

    cmd.publish(twist)


def stopMoving(cmd):
    cmd.publish(Twist())

if __name__ == '__main__':
    rospy.init_node('move_forward')
    cmd = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=10)
    t_end = time.time() + 10
    while time.time() < t_end:
        goForward(cmd)
    stopMoving(cmd)
