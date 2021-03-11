#!/usr/bin/env python3

from __future__ import print_function

import sys
import rospy
from beginner_tutorials.srv import *

def add_two_ints_client(x,y):
    # client code for calling a service
        # don't need rospy.init_node
        # waits until service called "add_two_ints" is available
    rospy.wait_for_service('add_two_ints')
    try:
        # create handle for calling service
        add_two_ints = rospy.ServiceProxy('add_two_ints',AddTwoInts)
        # call service
            # You have declared service as AddTwoInts type of service
            # Therfore it does the work of generating an AddTwoIntsRequest object for you
        resp1 = add_two_ints(x,y)
        return resp1.sum
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x,y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s+%s"%(x,y))
    print("%s + %s = %s"%(x,y,add_two_ints_client(x,y)))
