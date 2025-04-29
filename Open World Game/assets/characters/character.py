from ursina import *
from ursina.shaders import lit_with_shadows_shader
from panda3d.core import Filename
from direct.actor.Actor import Actor

# app = Ursina()
#
# DirectionalLight()
# Sky()

# Character class as described in previous code
class Character:
    def __init__(self, glb_path):
        self.actor_model = Actor(
            Filename.from_os_specific(glb_path),
        )

        self.character = Entity(
            model=self.actor_model,
            scale=3,
            shader=lit_with_shadows_shader
        )


        self.character.position = (0, 0, 0)
        self.character.rotation_y=180
        #at start play idle animation
        self.animation_play("idle")

    def animations_display(self):
        print("🎬 Actor animations:", self.actor_model.getAnimNames())  # available animations

    def animation_play(self, anim_name):
        # Start with a default animation
        try:
            self.actor_model.loop(anim_name)
        except Exception as e:
            print("❌ Failed to play animation:", e)


# Wrap the Actor in an Ursina Entity


character_1_path='Fran/fbx/export/FranFinal.glb'
character_2_path=''


# ch=Character(character_1_path)
# ch.animation_play('run')
#
# app.run()
