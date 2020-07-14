import pymunk

body = pymunk.Body(1, 100)
player = pymunk.Poly.create_box(body, size=(20, 20))
body.position = 120, 180

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