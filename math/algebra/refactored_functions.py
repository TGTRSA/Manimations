
from manim import *
import numpy as np

class CompleteLinearFunctionAnimation(Scene):
    def construct(self):
        # Part 1: Function Introduction
        self.function_introduction()
        
        # Part 2: Linear Graph
        self.linear_graph()
        
        # Part 3: Gradient Explanation
        self.gradient_explanation()
        
        # Part 4: Complete Linear Function
        self.complete_linear_function()
    
    def function_introduction(self):
        """Part 1: Introduce function notation"""
        # Initial function notation
        self.f_of_x = MathTex(r"f(x)")
        self.linear_function = MathTex(r"f(x)", r"= y")
        self.y_eq = MathTex(r"y=x")
        
        self.play(Write(self.linear_function))
        
        # Demonstrate function evaluation for different inputs
        for i in range(5):  # Reduced for speed
            point = MathTex(rf"f({i})={i} ")
            self.play(ReplacementTransform(self.linear_function, point))
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
    
    def gradient_explanation(self):
        """Part 3: Explain gradient/slope"""
        # Show full linear equation
        self.linear_function_equation = MathTex(r"f(x)=mx+b", font_size=24).move_to(UP * 3 + RIGHT * 5)
        self.play(Transform(self.y_eq, self.linear_function_equation))
        self.wait(1)
        
        # Highlight two specific points for gradient calculation
        point1 = self.axes.coords_to_point(-4, -4)
        point2 = self.axes.coords_to_point(4, 4)
        
        dot1 = Dot(point1, color=GREEN, radius=0.1)
        dot2 = Dot(point2, color=GREEN, radius=0.1)
        
        label1 = MathTex(r"(x_1, y_1)", font_size=18).next_to(point1, LEFT + DOWN, buff=0.2)
        label2 = MathTex(r"(x_2, y_2)", font_size=18).next_to(point2, RIGHT + UP, buff=0.2)
        
        self.play(Create(dot1), Create(dot2), Write(label1), Write(label2))
        self.wait(1)
        
        # Create dashed lines for gradient
        point_A = self.axes.coords_to_point(4, 4)
        point_B = self.axes.coords_to_point(4, -4)
        point_C = self.axes.coords_to_point(-4, 4)
        
        self.dashed_line_vertical = DashedLine(
            point_A,
            point_B,
            dash_length=0.15,
            dashed_ratio=0.5,
            color=RED,
            stroke_width=4
        )

        
        self.dashed_line_horizontal = DashedLine(
            point_C,
            point_B,
            dash_length=0.15,
            dashed_ratio=0.5,
            color=YELLOW,
            stroke_width=4
        )

        self.label_vertical = MathTex(r"y_2-y_1", font_size=20, color=RED).next_to(self.dashed_line_vertical, RIGHT, buff=0.2)
        self.label_horizontal = MathTex(r"x_2-x_1", font_size=20, color=YELLOW).next_to(self.dashed_line_horizontal, DOWN, buff=0.2)
        
        self.play(
            Create(self.dashed_line_vertical),
            Create(self.dashed_line_horizontal),
            Write(self.label_vertical),
            Write(self.label_horizontal)
        )
        self.wait(1)
        
        # Show gradient formula
        self.gradient_formula = MathTex(r"m=\frac{y_2-y_1}{x_2-x_1}", font_size=28)
        self.gradient_formula.move_to(UP * 2.5 + LEFT * 4)
        
        # Calculate specific values
        calculation = MathTex(r"=\frac{4 - (-4)}{4 - (-4)} = \frac{8}{8} = 1", font_size=24)
        calculation.next_to(self.gradient_formula, DOWN, buff=0.5)
        
        self.play(Write(self.gradient_formula))
        self.wait(1)
        self.play(Write(calculation))
        self.wait(1)
        
        # Clean up calculation for next part
        self.play(FadeOut(calculation))
    
    def complete_linear_function(self):
        """Part 4: Show complete linear function"""
        # Show combined linear function with gradient
        self.combined_equation = MathTex(r"f(x)=", r"m", r"x", "+b").move_to(UP * 2.5 + LEFT * 4)
        self.play(Transform(self.gradient_formula, self.combined_equation))
        self.wait(1)
        
        # Replace 'm' with the gradient formula
        self.full_linear_equation = MathTex(r"f(x)=", 
                                           r"\frac{y_2-y_1}{x_2-x_1}", 
                                           r"x", 
                                           "+b").move_to(UP * 2.5 + LEFT * 4)
        self.play(ReplacementTransform(self.gradient_formula, self.full_linear_equation))
        self.wait(1)
        
        # Show point-slope form
        point_slope = MathTex(r"y - y_1 = m(x - x_1)", font_size=28)
        point_slope.move_to(DOWN * 3)
        
        self.play(Write(point_slope))
        self.wait(1)
        
        # Connect to general form
        general_form = MathTex(r"y = mx + b", font_size=28, color=GREEN)
        general_form.move_to(DOWN * 3)
        
        self.play(Transform(point_slope, general_form))
        self.wait(1)
        
        # Final summary
        summary = VGroup(
            Text("Linear Function Summary:", font_size=24, color=BLUE),
            MathTex(r"1.\ f:\ x \to y\ (mapping)", font_size=22),
            MathTex(r"2.\ Graph\ is\ a\ straight\ line", font_size=22),
            MathTex(r"3.\ Slope\ m = \frac{\Delta y}{\Delta x}", font_size=22),
            MathTex(r"4.\ Equation:\ f(x) = mx + b", font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        summary.move_to(ORIGIN)
        
        self.play(
            FadeOut(self.dots),
            FadeOut(self.dashed_line_vertical),
            FadeOut(self.dashed_line_horizontal),
            FadeOut(self.label_vertical),
            FadeOut(self.label_horizontal),
            FadeOut(self.full_linear_equation),
            FadeOut(point_slope)
        )
        
        self.play(Write(summary))
        self.wait(3)
        
        # Final zoom out
        self.play(
            summary.animate.scale(0.8).to_edge(UP, buff=1),
            self.axes.animate.scale(0.7).to_edge(DOWN, buff=1),
            self.graph.animate.scale(0.7).to_edge(DOWN, buff=1),
            self.axes_labels.animate.scale(0.7).to_edge(DOWN, buff=1),
            self.linear_function_equation.animate.scale(0.8).to_corner(UR, buff=1)
        )
        
        # Final equation emphasis
        final_eq = MathTex(r"f(x) = mx + b", font_size=36, color=YELLOW)
        final_eq.move_to(DOWN * 2)
        
        self.play(Write(final_eq))
        self.wait(2)


