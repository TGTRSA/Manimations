from manim import *


class Transforming(Scene):
    def construct(self):
        two_6th =     MathTex(r"2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2=2^6")
        sixth_power_2 = MathTex(r"\overbrace{2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2}", r"^6" , r"=2", "^6")  
        a_sixth = MathTex(r"\overbrace{a \cdot a \cdot a \cdot a \cdot a \cdot a}^6=a^6")
        last = MathTex(r"a\cdot a")
        self.play(Write(two_6th))
        self.play(Transform(two_6th, a_sixth))
        self.wait(1)
        self.play(FadeTransform(two_6th, last), run_time=0.2)
