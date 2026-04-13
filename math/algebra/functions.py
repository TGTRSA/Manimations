from manim import *
import numpy as np

class CompleteLinearFunctionAnimation(Scene):
    def construct(self):
        self.function_intro()
        self.linear_graph()
        
    def function_intro(self):
        """
        the introductory scene of our animation which
        """
        self.f_of_x = MathTex(r"f(x)")
        self.linear_function = MathTex(r"f(x)", r"= y")
        self.y_eq = MathTex(r"y=x")
        
        self.play(Write(self.linear_function))
        
        # Demonstrate function evaluation for different inputs
        for i in range(-8, 9):  # Reduced for speed
            point = MathTex(rf"f({i})={i} ")
            self.play(ReplacementTransform(self.linear_function, point),run_time=0.5)
            self.linear_function = point
        
        # Mapping definition
        self.mapping_definition = MathTex(r"f:", r" x", r"\to", r"y")
        self.play(ReplacementTransform(self.linear_function, self.mapping_definition))
        self.play(self.mapping_definition[1].animate.set_color(RED)) 
        self.play(self.mapping_definition[3].animate.set_color(YELLOW), run_time=1.5)
        self.play(ReplacementTransform(self.mapping_definition, self.y_eq))
        self.wait(1)
        
        # Move equation to corner for next scene
        self.play(self.y_eq.animate.move_to(UP * 3 + RIGHT * 5))
        self.wait(0.5)

    def linear_graph(self):
        """Part 2: Create the linear graph"""
        # Setup axes
        self.axes = Axes(
            x_range=[-8, 8],
            y_range=[-10, 10],
            axis_config={"color": BLUE, "font_size": 20},
            x_length=10,
            y_length=6
        ).shift(DOWN * 0.5)
        
        self.axes_labels = self.axes.get_axis_labels(x_label="x", y_label="f(x)")
        
        # Create and display graph
        def linear_func(x):
            return x
        
        self.graph = self.axes.plot(linear_func, color=RED)
        self.play(Create(self.axes), Write(self.axes_labels), run_time=2)
        self.play(Create(self.graph), run_time=2)
        self.wait(1)
        
        # Add points on the graph
        self.dots = VGroup()
        x = -8
        for y in range(-8, 9, 2):  # Every 2 units for speed
            point = self.axes.coords_to_point(y, x)
            dot = Dot(point, color=YELLOW, radius=0.06)
            self.dots.add(dot)
            
            # Label key points
            if y == -8 or y == 0 or y == 8:
                label = MathTex(rf"({x},{y})", font_size=18).next_to(point, UP * 1.5, buff=0.1)
                self.dots.add(label)
            
            x += 2
        
        self.play(LaggedStart(*[Create(dot) for dot in self.dots], lag_ratio=0.1))
        self.wait(1)

class FirstScene(Scene):
    def construct(self):
        self.function_scene()

    def function_scene(self):
        f_of_x = MathTex(r"f(x)")
        linear_function = MathTex(r"f(x)", r"= y")#font_size=24)
        y = MathTex(r"y=x")
        axes = Axes(
                x_range=[-10,10],
                y_range=[-15,15],
                axis_config={"color":BLUE, "font_size":24},
        )
        
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        linear_function_equation = MathTex(r"f(x)=mx+b", font_size=24).move_to(UP *  3 + RIGHT * 6)

        gradient = MathTex(r"m=\frac{y_2-y_1}{x_2-x_1}")

        linear_function_with_gradient_definition = MathTex(r"f(x)=", gradient, r"x","+b")
        dots = VGroup()
        point_form = MathTex(r"(f(x),x)")

        mapping_definition = MathTex(r"f:", r" x",r"\to", r"y")

        # Creating dashed lines on the axes 
        point_A = axes.coords_to_point(10,10)
        point_B = axes.coords_to_point(10,0)
        point_C = axes.coords_to_point(0,10)
        dashed_line_object_along_y = DashedLine(
                start_point=point_A,
                end_point=point_B,
                dash_length=0.15,
                dashed_ratio =0.5,
                color=RED,
                stroke_width=4
                )
 
        dashed_line_object_along_x = DashedLine(
                start_point=point_C,
                end_point=point_B,
                dash_length=0.15,
                dashed_ratio =0.5,
                color=YELLOW,
                stroke_width=4
                )
        label_for_dashed_along_x = MathTex(r"x_2-x_1")
        label_for_dashed_along_y = MathTex(r"y_2-y_1")
        label_for_dashed_along_y.next_to(dashed_line_object_along_y, buff=0.2)
        label_for_dashed_along_x.next_to(dashed_line_object_along_x, buff=0.2)

        def f_x():
            nonlocal linear_function
            for i in range(10+1):
                point = MathTex(rf"f({i})={i} ")
                self.play(ReplacementTransform(linear_function,point))
       #         self.play(Transform(linear_function,point))
                linear_function = point
        

        def linear_func(x):
            return x
        
        def linear_function_with_gradient(m, x, b):
            return m*x+b

        def quadratic_function(x):
            return x**x
        
        graph = axes.plot(linear_func, color=RED)      

        self.play(Write(linear_function))
        f_x()
        
        self.play(ReplacementTransform(linear_function, mapping_definition))
        self.play(mapping_definition[1].animate.set_color(RED)) 
        self.play(mapping_definition[3].animate.set_color(YELLOW), run_time=2)
        self.play(ReplacementTransform(mapping_definition, y))
        self.wait(1)

        self.play(y.animate.shift(UP * 3 + RIGHT * 6))
        self.play(Create(axes),Write(graph))
        self.add(axes_labels)
        self.wait(1)

        def dot_sequence(axes=axes):
            x = -10 
            for y in range(-10,11,1):

                point =axes.coords_to_point(y,x)
                dots.add(Dot(point, color=YELLOW))

                if y == -10 or y==0 or y==10:
                    label = MathTex(rf"({x},{y})", font_size=24).next_to(point, UP* 2, buff=0.1)
                
                dots.add(label)
                x+=1
                
            self.play(Write(dots))

        dot_sequence()

        def sequence_linear_function():
            pass
        self.wait(1)
        # Giving the full linear equation f(x)=mx+b
        self.play(Transform(y, linear_function_equation))        
        # This is where we explain the gradient
        self.add(dashed_line_object_along_x, dashed_line_object_along_y,label_for_dashed_along_x, label_for_dashed_along_y)
        


