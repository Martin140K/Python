# IMPORTANT: Majority of this code was copied, I only edited it and added new features

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
window.fullscreen = True  
editor_camera = EditorCamera(enabled=False, ignore_paused=True)
player = FirstPersonController(position=(0,3,0))       

class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture='white_cube',
            color=color.hsv(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime
        )
class DEATHBLOCK(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            color=color.black,
            highlight_color=color.red,
            texture='white_cube'
        )

class Entity1(Entity):
    def __init__(self, **kwargs):
        super().__init__(model='cube', scale=0.7, origin_y=-.5, color=color.red, collider='box', **kwargs)
deathblock = DEATHBLOCK

class TNT(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            color=color.red,
            highlight_color=color.yellow,
            texture='white_cube'
        )

    def explode(self):
        for entity in scene.entities:
            if distance(entity.position, self.position) <= 3 and isinstance(entity, Voxel):
                destroy(entity)
        destroy(self) 

def input(key):
    global sky
    global sun
    if key == 'left mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=10000)
        if hit_info.hit:
            if isinstance(hit_info.entity, TNT):
                hit_info.entity.explode() 
            else:
                Voxel(position=hit_info.entity.position + hit_info.normal)

    if key == 'right mouse down' and mouse.hovered_entity:
        destroy(mouse.hovered_entity)
    
    if key == 'f' and mouse.hovered_entity:
        mouse.hovered_entity.x += 1
    if key == 'g' and mouse.hovered_entity:
        mouse.hovered_entity.x -= 1
    if key == 'h' and mouse.hovered_entity:
        mouse.hovered_entity.y += 1
    if key == 'j' and mouse.hovered_entity:
        mouse.hovered_entity.y -= 1
    if key == 'k' and mouse.hovered_entity:
        mouse.hovered_entity.z += 1
    if key == 'l' and mouse.hovered_entity:
        mouse.hovered_entity.z -= 1

    if key == 'm' and mouse.hovered_entity:
        position = mouse.hovered_entity.position
        destroy(mouse.hovered_entity)
        TNT(position=position)
    if key == "r":
        player.position=(0,3,0)
    if key == "b":
        player.position=(8,3,8)
    if key == "c":
        player.position=(8,3,8)
        for z in range(1):
            for x in range(1):
                voxel = Voxel(position=(8, 3, 8))
    if key == 'x' and mouse.hovered_entity:
        position = mouse.hovered_entity.position
        destroy(mouse.hovered_entity)
        DEATHBLOCK(position=position)
    if key == "e":
        entity=[Entity1(x=8, y=3, z=8)]
    
    if key == 't' and mouse.hovered_entity:
        position = mouse.hovered_entity.position
        Entity1(position=position)

    if key == '0' and mouse.hovered_entity:
        mouse.hovered_entity.color = color.white
    if key == '1' and mouse.hovered_entity:
        mouse.hovered_entity.color = color.red
    if key == '2' and mouse.hovered_entity:
        mouse.hovered_entity.color = color.orange
    if key == '3' and mouse.hovered_entity:
        mouse.hovered_entity.color = color.yellow
    if key == '4' and mouse.hovered_entity:
        mouse.hovered_entity.color = color.green
    if key == '5' and mouse.hovered_entity:
        mouse.hovered_entity.color = color.blue
    if key == '6' and mouse.hovered_entity:
        mouse.hovered_entity.color = color.violet
    if key == '7' and mouse.hovered_entity:
        mouse.hovered_entity.color = color.pink
    if key == '8' and mouse.hovered_entity:
        mouse.hovered_entity.color = color.gray
    if key == '9' and mouse.hovered_entity:
        mouse.hovered_entity.color = color.black

    if key == '+':
        sun= Light()
    if key == '-':
        sky.color = color.rgb(0,0,0)
        sun = None

def update():
    for entity in scene.entities:
        if isinstance(entity, DEATHBLOCK) and distance(player.position, entity.position) < 0.75:
            end = Text(text = 'You died', scale=14, origin=(0,0), background=True, color=color.red)
            application.pause()

def pause_input(key):
    if key == 'tab':  
        editor_camera.enabled = not editor_camera.enabled
        player.visible_self = editor_camera.enabled
        player.cursor.enabled = not editor_camera.enabled
        mouse.locked = not editor_camera.enabled
        editor_camera.position = player.position
        application.paused = editor_camera.enabled

pause_handler = Entity(ignore_paused=True, input=pause_input)

for z in range(16):
    for x in range(16):
        for y in range(4):
            voxel = Voxel(position=(x, y, z))
entity = Entity1

for z in range(16):
    for x in range(16):
        for y in range(1):
            deathblock = DEATHBLOCK(position=(x, -1000, z))

sky = Sky()
sun = Light()

app.run()
