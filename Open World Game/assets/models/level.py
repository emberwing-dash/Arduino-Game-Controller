from ursina import *
from ursina.shaders import lit_with_shadows_shader
from direct.actor.Actor import Actor

class level1class(Entity):
    def __init__(self,player, **kwargs):
        super().__init__()

        self.normalJump = 0.5
        self.normalSpeed = 3

        self.player = player
        self.player.jump_height = self.normalJump
        self.player.SPEED = self.normalSpeed


        self.block = []
        self.player.position.z = 10
        window.fullscreen = True



    def env(self):
        Sky(texture="sky_default")
        self.ground = Entity(
            model='plane',
            texture='grass',
            collider='mesh',
            scale=Vec3(100, 1, 100)
        )

    def steps(self):
        # Load a few tree models along the x-axis
        self.tree = Entity(
                model='assets/models/objects/tree/models/tree1.fbx',
                texture='assets/models/objects/tree/models/treeOverall.jpg',
                scale=0.5,
                position=(15, 0, 0),
                collider=None,
                shader=lit_with_shadows_shader
            )

