import time

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from controller.joystick.analogInput import readAnlog

app = Ursina()
player = FirstPersonController()
Sky()

boxes = []
for i in range(20):
    for j in range(20):
        box = Button(color=color.white, model='cube',position=(j,0,i),
                     texture='textures/grass.jpg',parent=scene,origin_y=0.5)
        boxes.append(box)

#custom movements (with arduino)
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

    direcFacing = direcVal(val1,val2)
    #time.sleep(2)

    speed = 5

    # Arrow keys movement
    if held_keys['up arrow'] or direcFacing=="forward":  # Move forward
        player.position += player.forward * speed * time.dt
    if held_keys['down arrow'] or direcFacing=="back":  # Move backward
        player.position -= player.forward * speed * time.dt
    if held_keys['left arrow'] or direcFacing=="left":  # Strafe left
        player.position -= player.right * speed * time.dt
    if held_keys['right arrow'] or direcFacing=="right":  # Strafe right
        player.position += player.right * speed * time.dt

    # You can also add vertical movement (jump) or any other modifications if necessary
    if held_keys['space']:  # Jump (optional, if you want space to still make the player jump)
        player.y += speed * time.dt
app.run()