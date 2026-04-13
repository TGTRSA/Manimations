from manim import *
import manim

class AllScenes(Scene):
    def construct(self):
        self.the_vector()
        

    def the_vector(self):
        self.vector_a = MathTex(r"\vec{a} = \begin{bmatrix} 1\hat{i}, 2\hat{j} \end{bmatrix}")

        self.axes = Axes(
                x_range=[-5,5],
                y_range=[-5,5],
                axis_config={"color": BLUE, "font_size":10}
                )


        self.play(Write(self.vector_a))
        self.play(self.vector_a.animate.shift(UP * 3 + RIGHT * 6))
