from ursina import *
import math

sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)


# ThirdPersonController with Character integration
class ThirdPersonController(Entity):
    def __init__(self, character, position=(0, 10, 0), SPEED=2, jump_height=0.3, velocity=(0, 0, 0), MAXJUMP=1, gravity=1,
                 controls="wasd", **kwargs):
        super().__init__(
            model="cube",
            position=position,
            scale=(1.3, 1, 1.3),
            texture="assets/models/texture/trans.png",
            tag="player",
            collider="box"
        )

        self.character = character  # Integrate Character object into controller
        self.character.character.parent = self  # Parent the character model to the controller entity
        self.character.character.position = (0, 0, 0)  # Position the character correctly

        self.collider = BoxCollider(self, center=Vec3(0, 1, 0), size=Vec3(1, 1, 1))
        mouse.locked = True
        camera.parent = self
        camera.position = (0, 8, -10)
        camera.rotation = (30, 0, 0)
        camera.fov = 100

        self.velocity_x, self.velocity_y, self.velocity_z = velocity
        self.SPEED = SPEED
        self.MAXJUMP = MAXJUMP
        self.jump_count = 0
        self.gravity = gravity
        self.jump_height = jump_height
        self.slope =0
        self.controls = controls
        self.sensitivity = 80

        # Additional attributes based on kwargs
        for key, value in kwargs.items():
            try:
                setattr(self, key, value)
            except:
                print(key, value)

    def jump(self):
        self.velocity_y = self.jump_height * 40
        self.jump_count += 1

    def update(self):
        y_movement = self.velocity_y * time.dt

        # Gravity & Jump Logic
        direction = (0, sign(y_movement), 0)
        yRay = boxcast(origin=self.world_position, direction=direction,
                       distance=self.scale_y / 2 + abs(y_movement), ignore=[self, ] )
        if yRay.hit:
            self.jump_count = 0
            self.velocity_y = 0
        else:
            self.y += y_movement
            self.velocity_y -= self.gravity * time.dt * 25

        # Horizontal Movement Logic using held_keys
        x_movement = (self.forward[0] * held_keys[self.controls[0]] +
                      self.left[0] * held_keys[self.controls[1]] +
                      self.back[0] * held_keys[self.controls[2]] +
                      self.right[0] * held_keys[self.controls[3]]) * time.dt * 6 * self.SPEED

        z_movement = (self.forward[2] * held_keys[self.controls[0]] +
                      self.left[2] * held_keys[self.controls[1]] +
                      self.back[2] * held_keys[self.controls[2]] +
                      self.right[2] * held_keys[self.controls[3]]) * time.dt * 6 * self.SPEED

        # Apply movement
        if x_movement != 0:
            direction = (sign(x_movement), 0, 0)
            xRay = boxcast(origin=self.world_position, direction=direction,
                           distance=self.scale_x / 2 + abs(x_movement), ignore=[self, ], thickness=(1, 1))

            if not xRay.hit:
                self.x += x_movement

        if z_movement != 0:
            direction = (0, 0, sign(z_movement))
            zRay = boxcast(origin=self.world_position, direction=direction,
                           distance=self.scale_z / 2 + abs(z_movement), ignore=[self, ], thickness=(1, 1))

            if not zRay.hit:
                self.z += z_movement

        # Rotate the player
        self.rotation_x -= mouse.velocity[1] * self.sensitivity * 30 * time.dt
        self.rotation_y += mouse.velocity[0] * self.sensitivity * 30 * time.dt
        camera.rotation_x = min(max(-80, camera.rotation_x), 80)
        self.rotation_x = min(max(-20, self.rotation_x), 20)

        # Call the animation update (can trigger based on movement)
        if (held_keys["w"] or held_keys["a"] or held_keys["s"] or held_keys["d"]):
            self.character.animation_play("walk2")
        elif held_keys["space"]:
            if self.jump_count < self.MAXJUMP:
                self.character.animation_play("jump")
                self.jump()
        else:
            self.character.animation_play("idle")

    def input(self, key):
        pass
        if key == "space":
            if self.jump_count < self.MAXJUMP:
                self.character.animation_play("jump")
                self.jump()
        #
        if key=="w" or key=="a" or key=="s" or key=="d":
            self.character.animation_play("walk")
        #
        # else:
        #     self.character.animation_play("idle")

if __name__ == "__main__":
    app = Ursina()

    player = ThirdPersonController(character=Entity(model="cube", color=color.red, scale=(1, 2, 1)))  # Example character

    ground = Entity(model="cube", color=color.light_gray, collider="box", texture="grass", scale=(100, 1, 100))

    Sky()

    PointLight(parent=camera, color=color.white, position=(0, 10, -1.5))
    AmbientLight(color=color.rgba(100, 100, 100, 0.1))

    app.run()
