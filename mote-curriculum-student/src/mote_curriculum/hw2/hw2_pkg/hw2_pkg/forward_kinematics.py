import rospy

from std_msgs.msg import Header
from sensor_msgs.msg import JointState
from geometry_msgs.msg import TwistStamped

# this is b in your equations
WHEEL_SEPARATION = 0.15  # meters

# you'll need this to convert angular velocity into linear velocity
WHEEL_DIAMETER = 0.066  # meters


class forward_kin:
    def __init__(self):
        # subscribe to messages of type JointState on the /joint_states topic
        self.twist_subscription = rospy.Subscriber(
            "joint_states", JointState, self.joint_state_callback
        )

        # publish TwistStamped messages on the /cmd_vel_ground_truth topic
        # TwistStamped differs Twist because it has a header
        self.twist_publisher = rospy.Publisher(
            "cmd_vel_ground_truth", TwistStamped, queue_size=10
        )

    def joint_state_callback(self, msg: JointState):
        # get the velocity associated with each wheel
        try:
            v_left = msg.velocity[msg.name.index("left_wheel")]
            v_right = msg.velocity[msg.name.index("right_wheel")]
        except Exception as e:
            print(e)

        """
        QUESTION 3.1 BEGINS
        """
        # this time we'll be publishing TwistStamped messages instead of just Twist
        # they're pretty much the same, only with a header this time
        # https://docs.ros.org/en/noetic/api/geometry_msgs/html/msg/TwistStamped.html

        # remember that joint states are in rad/s!
        # your equations may be expecting m/s, you'll need to do that conversion
        v_left_linear = v_left *  WHEEL_DIAMETER / 2 
        v_right_linear = v_right *  WHEEL_DIAMETER / 2 

        # calculate linear and angular velocity, then ...
        linear_v = (v_left_linear + v_right_linear) / 2
        angular_v = (v_right_linear - v_left_linear) / WHEEL_SEPARATION

        # ... create a TwistStamped message, then ...
        twist_msg = TwistStamped()

        # ... update the message values, then ...
        twist_msg.twist.linear.x = linear_v
        twist_msg.twist.angular.z = angular_v

        # ... update the message header, then ...
        twist_msg.header = Header(stamp=rospy.Time.now(), frame_id="base_link")

        # ... publish the message using self.twist_publisher
        self.twist_publisher.publish(twist_msg)

        
        """ 
        QUESTION 3.1 ENDS
        """
        pass


def main(args=None):
    # init the node
    rospy.init_node("forward_kin", anonymous=True)
    _ = forward_kin()

    print("Running forward kinematics node...")

    # let ROS handle ROS things
    rospy.spin()


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
