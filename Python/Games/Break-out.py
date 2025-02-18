from ursina import *
import time
app = Ursina()
window.fullscreen = True  

brickCount = 0
wallColor = color.red
brickColor = color.red
lvls = 0
lives = 5

ceiling = Entity(model='quad', x= 0, y = 5, scale = (16,0.2),  collider='box', color = wallColor)
ceiling1 = Entity(model='quad', x= 0, y = 400, scale = (16,0.2),  collider='box', color = wallColor)
left_wall = Entity(model='quad', x= -7.2, y = 0, scale = (0.2,10),  collider='box', color = wallColor)
right_wall = Entity(model='quad', x= 7.2, y = 0, scale = (0.2,10),  collider='box', color = wallColor)
ball = Entity(model='circle', scale=0.2, collider='box', dx = 0.05, dy = -0.05, color = color.white)
paddle = Entity(model='quad', x= 0, y = -3.5, scale = (2, 0.2),  collider='box', color = color.red)
ball.x = paddle.x - 2
ball.y = paddle.y + 2
msg1 = Text(text = f'Level 1', scale=1, origin=(-2,-19), color=color.red)
msg1.fade_out(0,2)

bricks = []
for x_pos in range(-65, 75, 10):
    for y_pos in range(1,6):
        brick = Entity(model='quad', x = x_pos/10 , y = y_pos/3, scale = (0.9, 0.3),  collider='box', color = brickColor)
        brickCount += 1
        bricks.append(brick)

def input(key):
    global bricks
    global lvls
    global lives
    if key == 'o':
        ballReset()
    if key == '+':
        ball.scale *= 2
    if key == '-':
        ball.scale /= 2
    if key == 'p':
        paddle.scale *= 2
    if key == 'l':
        paddle.scale /= 2
    if key == 'm':
        for brick in bricks:
            destroy(brick)
        bricks.clear()  
    if key == 'n':
        lvls -= 1
        for brick in bricks:
            destroy(brick)
        bricks.clear()  
    if key == '7':
        lives = 5

def ballReset():
    ball.x = paddle.x
    ball.y = paddle.y + 1

def update():
    global lvls
    global paddle
    paddle.x = clamp(paddle.x, -6, 6)
    paddle.y = clamp(paddle.y, -4, -2)
    ball.x += ball.dx
    ball.y += ball.dy
    paddle.x += (held_keys['right arrow'] - held_keys['left arrow']) * time.dt *5
    paddle.x += (held_keys['d'] - held_keys['a']) * time.dt *5
    paddle.y += (held_keys['up arrow'] - held_keys['down arrow']) * time.dt *5
    paddle.y += (held_keys['w'] - held_keys['s']) * time.dt *5
    
    hit_info = ball.intersects()
    if hit_info.hit:        
        if hit_info.entity == left_wall or hit_info.entity == right_wall:
            ball.dx = -ball.dx
        if hit_info.entity == ceiling:
            from ursina.prefabs.ursfx import ursfx
            ursfx([(0.0, 0.0), (0.1, 0.9), (0.15, 0.75), (0.3, 0.14), (0.6, 0.0)], volume=0.20, wave='square', pitch=random.uniform(-5,1), pitch_change=-20, speed=0.5)
            lvls + 1
            for brick in bricks:
                destroy(brick)
            bricks.clear()
            ball.dy = -ball.dy
        if hit_info.entity == ceiling1:
            ball.dy = -ball.dy
        if hit_info.entity in bricks:
            destroy(hit_info.entity)
            bricks.remove(hit_info.entity)
            from ursina.prefabs.ursfx import ursfx
            ursfx([(0.0, 0.0), (0.1, 0.9), (0.15, 0.75), (0.3, 0.14), (0.6, 0.0)], volume=0.1, wave='noise', pitch=random.uniform(-25,-20), pitch_change=-20, speed=2.0)
            ball.dy = -ball.dy
        if hit_info.entity == paddle:
            ball.dy = -ball.dy
            ball.dx = 0.025*(ball.x - paddle.x)
        
    if ball.y < -5:
        global lives
        from ursina.prefabs.ursfx import ursfx
        ursfx([(0.0, 0.0), (0.1, 0.9), (0.15, 0.75), (0.3, 0.14), (0.6, 0.0)], volume=10, wave='triangle', pitch=random.uniform(-25,-22), pitch_change=-2, speed=1.0)
        ballReset()
        lives -= 1
        msg1 = Text(text = f'You lost a life, {lives} remaining', scale=1, origin=(-2,-19), color=color.red)
        msg1.fade_out(0,2)
    
    if lives <= 0:
        message = Text(text = 'You lost!', scale=2, origin=(0,0), background=True, color=color.red)
        application.pause()

    if len(bricks) == 0 and lvls == 0:
        ballReset()
        lvls += 1
        for x_pos in range(-65, 75, 10):
            for y_pos in range(1,8):
                brick = Entity(model='quad', x = x_pos/10 , y = y_pos/3, scale = (0.9, 0.3),  collider='box', color = brickColor)
                bricks.append(brick)
        msg1 = Text(text = f'Level 2', scale=1, origin=(-2,-19), color=color.red)
        msg1.fade_out(0,2)
    elif len(bricks) == 0 and lvls == 1:
        ballReset()
        lvls += 1
        for x_pos in range(-65, 75, 10):
            for y_pos in range(1,11):
                brick = Entity(model='quad', x = x_pos/10 , y = y_pos/3, scale = (0.9, 0.3),  collider='box', color = brickColor)
                bricks.append(brick)
        msg1 = Text(text = f'Level 3', scale=1, origin=(-2,-19), color=color.red)
        msg1.fade_out(0,2)
    elif len(bricks) == 0 and lvls == 2:
        ballReset()
        lvls += 1
        for x_pos in range(-65, 75, 10):
            for y_pos in range(-4,10):
                brick = Entity(model='quad', x = x_pos/10 , y = y_pos/3, scale = (0.9, 0.3),  collider='box', color = brickColor)
                bricks.append(brick)
        msg1 = Text(text = f'Level 4', scale=1, origin=(-2,-19), color=color.red)
        msg1.fade_out(0,2)
    elif len(bricks) == 0 and lvls == 3:
        ballReset()
        lvls += 1
        for x_pos in range(-102, 105, 6):
            for y_pos in range(1,6):
                brick = Entity(model='quad', x = x_pos/15 , y = y_pos/4, scale = (0.35, 0.22),  collider='box', color = brickColor)
                bricks.append(brick)
        msg1 = Text(text = f'Level 5', scale=1, origin=(-2,-19), color=color.red)
        msg1.fade_out(0,2)
    elif len(bricks) == 0 and lvls == 4:
        ballReset()
        lvls += 1
        for x_pos in range(-102, 105, 6):
            for y_pos in range(1,11):
                brick = Entity(model='quad', x = x_pos/15 , y = y_pos/4, scale = (0.35, 0.22),  collider='box', color = brickColor)
                bricks.append(brick)
        msg1 = Text(text = f'Level 6', scale=1, origin=(-2,-19), color=color.red)
        msg1.fade_out(0,2)
    elif len(bricks) == 0 and lvls == 5:
        ballReset()
        lvls += 1
        for x_pos in range(-102, 105, 6):
            for y_pos in range(1,15):
                brick = Entity(model='quad', x = x_pos/15 , y = y_pos/4, scale = (0.35, 0.22),  collider='box', color = brickColor)
                bricks.append(brick)
        msg1 = Text(text = f'Level 7', scale=1, origin=(-2,-19), color=color.red)
        msg1.fade_out(0,2)
    elif len(bricks) == 0 and lvls == 6:
        ballReset()
        lvls += 1
        for x_pos in range(-210, 215, 6):
            for y_pos in range(1,11):
                brick = Entity(model='quad', x = x_pos/30 , y = y_pos/7, scale = (0.15, 0.08),  collider='box', color = brickColor)
                bricks.append(brick)
        msg1 = Text(text = f'Level 8', scale=1, origin=(-2,-19), color=color.red)
        msg1.fade_out(0,2)
        ceiling.x = 10000
    elif len(bricks) == 0 and lvls == -1:
        ballReset()
        ceiling1.y = 4
        for brick in bricks:
            destroy(brick)
        bricks.clear()  
        lvls -= 1
        for x_pos in range(1, 2, 1):
            for y_pos in range(1,2):
                brick = Entity(model='quad', x = x_pos/1 , y = y_pos/4, scale = (2, 1),  collider='box', color = brickColor)
                bricks.append(brick)
    elif len(bricks) == 0 and lvls == -2:
        ceiling.y += 10000
        ceiling1.y += 10000
        right_wall.y += 10000
        left_wall.y += 10000
        for brick in bricks:
            destroy(brick)
        bricks.clear()  
    elif len(bricks) == 0 and lvls == -3:
        for brick in bricks:
            destroy(brick)
        bricks.clear()  
        ballReset()
        ceiling.y += 10000
        ceiling1.y += 10000
        right_wall.y = 0
        left_wall.y = 0
        for x_pos in range(-210, 215, 6):
            for y_pos in range(-10,30):
                brick = Entity(model='quad', x = x_pos/30 , y = y_pos/7, scale = (0.15, 0.08),  collider='box', color = brickColor)
                bricks.append(brick)
    if ball.y == 5:
        if lvls == -2:
            lvls -= 1
            ballReset()
            for brick in bricks:
                destroy(brick)
            bricks.clear()
        from ursina.prefabs.ursfx import ursfx
        ursfx([(0.0, 0.0), (0.1, 0.9), (0.15, 0.75), (0.3, 0.14), (0.6, 0.0)], volume=0.20, wave='square', pitch=5, pitch_change=-20, speed=1)
    if ball.y >= 9:
        message = Text(text = 'CONGRATULATIONS! You have finished the game', scale=2, origin=(0,0), background=True, color=color.blue)
        application.pause()
        ball.y = -1000

window.color = color.black  
    
app.run()