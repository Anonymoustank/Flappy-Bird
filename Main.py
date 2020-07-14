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

for i in Moving_Objects.space_list:
    space.add(i)

last_click_time = time.perf_counter()

@window.event
def on_draw():
    window.clear()
    x, y = Moving_Objects.body.position
    Moving_Objects.rocket.position = x - 25, y - 10
    Moving_Objects.rocket.draw()
    x, y = Moving_Objects.lower_body.position
    Moving_Objects.lower_brick.position = x - 14, y - 100
    Moving_Objects.lower_brick.draw()
    x, y = Moving_Objects.upper_body.position
    Moving_Objects.upper_brick.position = x - 14, y - 100
    Moving_Objects.upper_brick.draw()

def refresh(time):
    space.step(time)
    x, y = Moving_Objects.lower_body.position
    Moving_Objects.lower_body.position = x - 2, y
    if x < -15:
        Moving_Objects.lower_body.position = 260, y
    x, y = Moving_Objects.upper_body.position
    Moving_Objects.upper_body.position = x - 2, y
    if x < -15:
        Moving_Objects.upper_body.position = 260, y

@window.event
def on_mouse_press(x, y, button, modifiers):
    global last_click_time
    if abs(last_click_time - time.perf_counter()) >= 0.3:
        x, y = Moving_Objects.body.position
        if y <= 210:
            Moving_Objects.body.apply_force_at_local_point((0, 50000 - y), (0, 50000 - y))
            last_click_time = time.perf_counter()

if __name__ == "__main__":
    pyglet.clock.schedule_interval(refresh, 1.0/120.0)
    pyglet.app.run()