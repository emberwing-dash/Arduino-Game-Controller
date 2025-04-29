from ursina import *
from controller.ThirdPersonControl.TPC import ThirdPersonController
from assets.models.level import level1class
from assets.characters.character import Character
from controller.joystick.analogInput import readAnlog

game = Ursina()



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

    #Arrow keys movement
    if held_keys['up arrow'] or direcFacing == "forward":  # Move forward
        player.position += player.forward * speed * time.dt
        player.character.animation_play("walk")
    if held_keys['down arrow'] or direcFacing == "back":  # Move backward
        player.position -= player.forward * speed * time.dt
        player.character.animation_play("walk")
    if held_keys['left arrow'] or direcFacing == "left":  # Strafe left
        player.position -= player.right * speed * time.dt
        player.character.animation_play("walk")
    if held_keys['right arrow'] or direcFacing == "right":  # Strafe right
        player.position += player.right * speed * time.dt
        player.character.animation_play("walk")
def windowChoice(choice,player):
    if choice=="1":
        lvl1=level1class(player)
        lvl1.env()
        #lvl1.steps()

fran=Character("assets/characters/Fran/fbx/export/FranFinal.glb")
fran.animations_display()
player=ThirdPersonController(fran)


windowChoice("1",player)
game.run()