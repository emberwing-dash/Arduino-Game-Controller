# Import all of ursina
from ursina import *

# Import the player class
from player import Player
from controller.joystick.analogInput import readAnlog

# Import the sword
from sword import *

# Declare the app
app = Ursina()

def direcVal(val1,val2):
    if val2>=0.7:
        return "right"
    if val2<=0.4:
        return "left"
    if val1>=0.7:
        return "forward"
    if val1<=0.4:
        return "back"

    return "idle"

def update():
    val1, val2 = readAnlog()
    print(val1,val2)
    direcFacing = direcVal(val1, val2)

    speed = 10

    # Arrow keys movement
    if held_keys['up arrow'] or direcFacing == "forward":  # Move forward
        player.position += player.forward * speed * time.dt
    if held_keys['down arrow'] or direcFacing == "back":  # Move backward
        player.position -= player.forward * speed * time.dt
    if held_keys['left arrow'] or direcFacing == "left":  # Strafe left
        player.position -= player.right * speed * time.dt
    if held_keys['right arrow'] or direcFacing == "right":  # Strafe right
        player.position += player.right * speed * time.dt

# Make the player
player = Player("cube", (0, 10, 0), "box")
player.SPEED = 2
player.jump_height = 0.3

# Make the ground
ground = Entity(model = "cube", scale = (100, 1, 100), collider = "box", color = color.light_gray, texture = "white_cube")

# Lighting
PointLight(parent = camera, color = color.white, position = (0, 10, -1.5))
AmbientLight(color = color.rgba(100, 100, 100, 0.1))

# Add skybox
Sky()

# Declare sword
sword = Sword()

# Run the app
app.run()
