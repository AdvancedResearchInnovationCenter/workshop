from ros_robot_pkg.srv import moveRobot, moveRobotRelative
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

print(moveRobot, moveRobotRelative)

rospy.wait_for_service('/move_ur_relative')
move_ur_r = rospy.ServiceProxy('/move_ur_relative', moveRobotRelative)
move_ur = rospy.ServiceProxy('/move_ur', moveRobot)

init_pos = [0, -.8, .33]
init_rot = [0, 3.1415, 0]

final_pos = [0, -.3, .33]
final_rot = init_rot

init_pose = get_pose(init_pos, init_rot)
final_pose = get_pose(final_pos, final_rot)
print(final_pose)

move_ur(target_pose=init_pose, frame='davis')

move_ur(target_pose=final_pose, frame='davis')

move_ur(target_pose=init_pose, frame='davis')




