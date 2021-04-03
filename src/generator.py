#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import Int8

def talker():
    pub = rospy.Publisher('random_numbers', Int8, queue_size=10)
    rospy.init_node('generator', anonymous=True)
    rate = rospy.Rate(1) # 10hz

    while not rospy.is_shutdown():
        num = random.randrange(10)
        rospy.loginfo(num)
        pub.publish(num)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
