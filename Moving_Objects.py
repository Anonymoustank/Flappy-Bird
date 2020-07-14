import pymunk
import pyglet

space_list = []

body = pymunk.Body(1, 100)
player = pymunk.Poly.create_box(body, size = (25, 20))
body.position = 120, 180

upper_player = pymunk.Segment(body, (0, 20), (0, 30), radius = 10)
upper_player.position = 120, 210

damp_level = 1
def zero_gravity(body, gravity, damping, dt):
    pymunk.Body.update_velocity(body, (0, -1000), damp_level, dt)
body.velocity_func = zero_gravity


lower_body = pymunk.Body(1, 100, pymunk.Body.KINEMATIC)
lower_body.position = 240, 0
lower_pipe = pymunk.Poly.create_box(lower_body, size=(30, 200))

upper_body = pymunk.Body(1, 100, pymunk.Body.KINEMATIC)
upper_body.position = 240, 360
upper_pipe = pymunk.Poly.create_box(upper_body, size=(30, 200))

rocket = pyglet.resource.image("Rocket.png")
rocket.width, rocket.height = 50, 50
rocket = pyglet.sprite.Sprite(rocket)

lower_brick = pyglet.resource.image("Brick.PNG")
lower_brick.width, lower_brick.height = 30, 200
lower_brick = pyglet.sprite.Sprite(lower_brick)

upper_brick = pyglet.resource.image("Brick.PNG")
upper_brick.width, upper_brick.height = 30, 200
upper_brick = pyglet.sprite.Sprite(upper_brick)

space_list = [body, player, upper_player, lower_body, lower_pipe, upper_body, upper_pipe]