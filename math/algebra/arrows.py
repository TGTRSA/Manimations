from manim import *


class ArrowPlay(Scene):
    def construct(self):
        self.general()

    def general(self):
        arrow_text = Text("Arrow(DOWN , RIGHT)")#=> i assume its from x => to y
        arrow_right = arrow_text.get_right()
        arrow_left = arrow_text.get_left()
        left_right = Arrow(arrow_left+DOWN, arrow_left+ RIGHT)
        
        self.play(Write(arrow_text))
        self.play(Write(left_right))
