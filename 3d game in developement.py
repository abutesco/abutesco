from ursina import *
from ursina.prefabs.first_person_controller \
    import FirstPersonController

app = Ursina()
ground = Entity(model= 'plane',
                texture= 'grass',
                collider= 'mesh',
                scale= (1000,10, 1000))

player = FirstPersonController()
Sky()

myBox = Entity(model= 'cube',
                color= color.black,
                collider= 'box',
                posistion= (5, 0.5, 5))
myball = Entity(model= 'sphere',
                 color= color.blue, 
                 collider= 'sphere',
                 position= (5, 0.5, 10))

blocks = []
directions = []
window.fullscreen = True
from random import uniform

for i in range(8):
    r = uniform(-2,2)
    block = Entity(
        model= 'cube',
        color= color.brown,
        texture= 'white_cube',
        position=(r, -1+i , 3+i*5),
        scale=(3,0.5,3),
        collider='box'
    )
    if r < 0:
        directions.append(1)
    else:
        directions.append(-1)
        

    goal = Entity(
        color= color.gold,
        model='cube',
        textur= 'white_cube',
        position=(0,11,55),
        scale=(10,1,10),
        collider='box'
    )
    blocks.append(block)

def update():
   # if player.y > 1:
       # destroy(ground)
    i = 0
    for block in blocks:
        block.x -= directions[i]*time.dt
        if abs(block.x) > 5:
            directions[i] *= -1
        i = i + 1

def input(key):
    if key == 'q':
        quit()
app.run()
