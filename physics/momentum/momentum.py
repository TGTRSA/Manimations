from manim import *

ELECTRIC_BLUE = "#4DB5FF"
VIVID_SKY_BLUE = "#00CCFF"
AZURE = "#007FFF"

class LinearMomentum(Scene):
    def construct(self):
        self.linear_momentum()


    def linear_momentum(self):
        linear_momentum_definition = MathTex(r"p=m \cdot v")
        dot = Dot(color=AZURE)
        tracer = TracedPath(dot.get_center, stroke_color=YELLOW, stroke_width=3)
        self.add(dot,tracer)
        self.play(dot.animate.shift(RIGHT * 4), run_time=3)
    
        pass
    
