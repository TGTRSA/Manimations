from manim import *
import numpy as np

class SpinningParticle(ThreeDScene):
    def construct(self):
        self.sphere_movement()

    def sphere_movement(self):
        self.set_camera_orientation(
            phi=90 * DEGREES,
            theta=-45 * DEGREES,
            gamma=0
        )
        path = ParametricFunction(
                lambda t: [np.sin(t), np.cos(t), 0],
                t_range=[0,2 *PI],
                color=BLUE
                )
        #self.add(path)
        dot = Dot(color=RED)
        self.add(dot)

        self.play(MoveAlongPath(dot, path), run_time=3)
        self.wait(1)
