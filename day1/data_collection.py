from ros_robot_pkg.srv import moveRobot, moveRobotRelative, setValue
import rospy

from geometry_msgs.msg import Pose

from scipy.spatial.transform import Rotation as R


def get_pose(pos, euler, degrees=False):
    pose = Pose()
    pose.position.x = pos[0]
    pose.position.y = pos[1]
    pose.position.z = pos[2]

    rot = R.from_euler('xyz', euler, degrees=degrees).as_quat()
    pose.orientation.x = rot[0]
    pose.orientation.y = rot[1]
    pose.orientation.z = rot[2]
    pose.orientation.w = rot[3]

    return pose

go_to = lambda pos, rot: move_ur(target_pose=get_pose(pos, rot), frame='davis')

print(moveRobot, moveRobotRelative)

rospy.wait_for_service('/move_ur_relative')
move_ur_r = rospy.ServiceProxy('/move_ur_relative', moveRobotRelative)
move_ur = rospy.ServiceProxy('/move_ur', moveRobot)
vel = rospy.ServiceProxy('/change_ref_vel', setValue)

vel(0.3)

h = .5
corner1 = [-.1, -.8, h]
corner2 = [.1, -.8, h]
corner3 = [.1, -.5, h]
corner4 = [-.1, -.5, h]

mid = [(corner1[0] + corner3[0]) / 2, (corner1[1] + corner3[1]) / 2, (corner1[2] + corner3[2]) / 2]
rot = [0, 3.1415, 0]

go_to(mid, rot)

go_to(corner1, rot)
go_to(corner2, rot)
go_to(corner3, rot)
go_to(corner4, rot)

go_to(mid, rot)



