import pymunk
import pyglet
from pymunk.pyglet_util import DrawOptions
from pyglet.window import key, mouse
import time
import Moving_Objects

options = DrawOptions()
window = pyglet.window.Window(240, 360, "Game", resizable = False)
window.set_mouse_visible(False)
space = pymunk.Space()
space.gravity = 0, -1000
dead = False
last_click_time = time.perf_counter()
for i in Moving_Objects.space_list:
    space.add(i)
score = 0

@window.event
def on_draw():
    window.clear()
    if dead == False:
        for i in Moving_Objects.sky_list:
            i.draw()
        x, y = Moving_Objects.body.position
        Moving_Objects.rocket.position = x - 25, y - 10
        Moving_Objects.rocket.draw()
        x, y = Moving_Objects.lower_body.position
        Moving_Objects.lower_brick.position = x - 14, y - 100
        Moving_Objects.lower_brick.draw()
        x, y = Moving_Objects.upper_body.position
        Moving_Objects.upper_brick.position = x - 14, y - 100
        Moving_Objects.upper_brick.draw()
        x, y = Moving_Objects.body.velocity
        if y > 0:
            x, y = Moving_Objects.body.position
            Moving_Objects.fire.position = x - 12, y - 30
            Moving_Objects.fire.draw()
        label = pyglet.text.Label('Score: ' + str(score), font_name='Times New Roman', font_size = 16, x = 200, y = 350, anchor_x='center', anchor_y='center', color = (0, 0, 0, 255))
        label.draw()
    else:
        label = pyglet.text.Label('Game Over', font_name='Times New Roman', font_size=24, x=window.width//2, y=window.height//2 + 50, anchor_x='center', anchor_y='center')
        label.draw()
        score_label = pyglet.text.Label('Final Score: ' + str(score), font_name='Times New Roman', font_size=24, x=window.width//2, y=window.height//2 - 50, anchor_x='center', anchor_y='center')
        score_label.draw()

def refresh(time):
    global dead, score
    space.step(time)
    rocket_x, rocket_y = Moving_Objects.rocket.position
    if rocket_y <= -50:
        dead = True
    for i in Moving_Objects.wall_list:
        if len(Moving_Objects.player.shapes_collide(i).points) > 0 or len(Moving_Objects.upper_player.shapes_collide(i).points) > 0:
            dead = True
    x, y = Moving_Objects.lower_body.position
    Moving_Objects.lower_body.position = x - 2, y
    if x < -15:
        Moving_Objects.lower_body.position = 260, y
    x, y = Moving_Objects.upper_body.position
    if rocket_y > 400 and x == rocket_x:
        dead = True
    Moving_Objects.upper_body.position = x - 2, y
    if x < -15:
        Moving_Objects.upper_body.position = 260, y
    for i in Moving_Objects.sky_list:
        x, y = i.position
        i.position = x - 20, y
        if x + i.width/2 <= 0:
            i.position = x + (1.5 * i.width), y
    x, y = Moving_Objects.upper_body.position
    body_x, body_y = Moving_Objects.body.position
    if x == body_x and dead == False:
        score += 1


@window.event
def on_mouse_press(x, y, button, modifiers):
    global last_click_time
    if abs(last_click_time - time.perf_counter()) >= 0.1:
        x, y = Moving_Objects.body.position
        Moving_Objects.body.apply_force_at_local_point((0, 30000), (0, 30000))
        last_click_time = time.perf_counter()

if __name__ == "__main__":
    pyglet.clock.schedule_interval(refresh, 1.0/120.0)
    pyglet.app.run()