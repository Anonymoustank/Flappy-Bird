import pymunk
import pyglet
from pymunk.pyglet_util import DrawOptions
from pyglet.window import key, mouse
import time
import Moving_Objects
from pyglet.gl import *
glEnable(GL_TEXTURE_2D)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

options = DrawOptions()
window = pyglet.window.Window(240, 360, "Game", resizable = False)
window.set_mouse_visible(False)
space = pymunk.Space()
space.gravity = 0, -1000

space.add(Moving_Objects.body, Moving_Objects.player, Moving_Objects.lower_body, Moving_Objects.lower_pipe, Moving_Objects.upper_body, Moving_Objects.upper_pipe)
last_click_time = time.perf_counter()

@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)
    x, y = Moving_Objects.body.position
    Moving_Objects.rocket.position = x - 25, y - 25
    Moving_Objects.rocket.draw()

def refresh(time):
    space.step(time)

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