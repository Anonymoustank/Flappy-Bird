import pymunk
import pyglet
from pymunk.pyglet_util import DrawOptions
from pyglet.window import key, mouse
import time

options = DrawOptions()
window = pyglet.window.Window(240, 360, "Game", resizable = False)
window.set_mouse_visible(False)
space = pymunk.Space()
space.gravity = 0, -1000
body = pymunk.Body(1, 100)
player = pymunk.Poly.create_box(body, size=(20, 20))
body.position = 120, 180

space.add(body, player)
last_click_time = time.perf_counter()

@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)

def refresh(time):
    space.step(time)

@window.event
def on_mouse_press(x, y, button, modifiers):
    global last_click_time
    if abs(last_click_time - time.perf_counter()) >= 0.3:
        x, y = body.position
        if y <= 210:
            body.apply_force_at_local_point((0, 50000 - y), (0, 50000 - y))
            last_click_time = time.perf_counter()

if __name__ == "__main__":
    pyglet.clock.schedule_interval(refresh, 1.0/120.0)
    pyglet.app.run()