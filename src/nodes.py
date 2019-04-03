#!/usr/bin/env python

import roslib
import rospy
import rosnode

from std_msgs.msg import String

def pubNodeInfos():
  # Get the ~private namespace parameters from command line or launch file.
  topic = rospy.get_param('~topic', 'running_nodes')
  rospy.loginfo('topic = %s', topic)
  pub = rospy.Publisher(topic, String, queue_size=1)
  
  while not rospy.is_shutdown():
    nodeString = ""
    nodes = rosnode.get_node_names()

    for node in nodes:
      nodeString += node + " "
    rospy.loginfo(nodeString)

    pub.publish(nodeString)
    rospy.sleep(10)


if __name__ == '__main__':
  try:
    rospy.init_node('node_info_publisher', anonymous=False)
    pubNodeInfos()
  except rospy.ROSInterruptException:
    print "node interrupted"
