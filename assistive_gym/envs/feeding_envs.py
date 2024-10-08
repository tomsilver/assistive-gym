from .feeding import FeedingEnv
from .feeding_mesh import FeedingMeshEnv
from .agents import pr2, baxter, sawyer, jaco, stretch, panda, human, human_mesh
from .agents.pr2 import PR2
from .agents.baxter import Baxter
from .agents.sawyer import Sawyer
from .agents.jaco import Jaco
from .agents.stretch import Stretch
from .agents.panda import Panda
from .agents.human import Human
from .agents.human_mesh import HumanMesh

robot_arm = 'right'
human_controllable_joint_indices = human.head_joints
class FeedingPR2Env(FeedingEnv):
    def __init__(self):
        super(FeedingPR2Env, self).__init__(robot=PR2(robot_arm), human=Human(human_controllable_joint_indices, controllable=False))

class FeedingBaxterEnv(FeedingEnv):
    def __init__(self):
        super(FeedingBaxterEnv, self).__init__(robot=Baxter(robot_arm), human=Human(human_controllable_joint_indices, controllable=False))

class FeedingSawyerEnv(FeedingEnv):
    def __init__(self):
        super(FeedingSawyerEnv, self).__init__(robot=Sawyer(robot_arm), human=Human(human_controllable_joint_indices, controllable=False))

class FeedingJacoEnv(FeedingEnv):
    def __init__(self):
        super(FeedingJacoEnv, self).__init__(robot=Jaco(robot_arm), human=Human(human_controllable_joint_indices, controllable=False))

class FeedingStretchEnv(FeedingEnv):
    def __init__(self):
        super(FeedingStretchEnv, self).__init__(robot=Stretch('wheel_'+robot_arm), human=Human(human_controllable_joint_indices, controllable=False))

class FeedingPandaEnv(FeedingEnv):
    def __init__(self):
        super(FeedingPandaEnv, self).__init__(robot=Panda(robot_arm), human=Human(human_controllable_joint_indices, controllable=False))

class FeedingPR2MeshEnv(FeedingMeshEnv):
    def __init__(self):
        super(FeedingPR2MeshEnv, self).__init__(robot=PR2(robot_arm), human=HumanMesh())

class FeedingBaxterMeshEnv(FeedingMeshEnv):
    def __init__(self):
        super(FeedingBaxterMeshEnv, self).__init__(robot=Baxter(robot_arm), human=HumanMesh())

class FeedingSawyerMeshEnv(FeedingMeshEnv):
    def __init__(self):
        super(FeedingSawyerMeshEnv, self).__init__(robot=Sawyer(robot_arm), human=HumanMesh())

class FeedingJacoMeshEnv(FeedingMeshEnv):
    def __init__(self):
        super(FeedingJacoMeshEnv, self).__init__(robot=Jaco(robot_arm), human=HumanMesh())

class FeedingStretchMeshEnv(FeedingMeshEnv):
    def __init__(self):
        super(FeedingStretchMeshEnv, self).__init__(robot=Stretch('wheel_'+robot_arm), human=HumanMesh())

class FeedingPandaMeshEnv(FeedingMeshEnv):
    def __init__(self):
        super(FeedingPandaMeshEnv, self).__init__(robot=Panda(robot_arm), human=HumanMesh())

