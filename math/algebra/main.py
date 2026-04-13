from manim import *
import time

X_VAR = MathTex("x")

class Expression(Scene):

    def construct(self):
        #self.variables()
        #self.the_variable_scene())
        #self.the_algbraic_expression()
        self.algebraic_operations()

    def variables(self):
        variables_text = "Variables"
        variable_obj = Text(variables_text)
        x_var = MathTex("x")
        x_var.set(color=RED)
        y_var = MathTex("y")
        y_var.set(color=BLUE)
        y_var.set().next_to(x_var, RIGHT)
        
        variable_obj.set().next_to(x_var, UP)
        # self.play() renders while Write() writes the equation like a chalkboard and pen
        self.add(variable_obj)
        self.play(Write(x_var), Write(y_var))
        self.wait(1)


    

    def the_variable_scene(self):

        x_container =self.createMathObj("x", BLUE)
        x_equal_sign = self.createMathObj("=",position_var=x_container, position=RIGHT)
        two = self.createMathObj("2", 
                                 BLUE, 
                                 position_var=x_equal_sign, position=RIGHT)

        y_container =self.createMathObj("y", RED)
        y_equal_sign = self.createMathObj("=",
                                          position_var=y_container, 
                                          position=RIGHT)
        one = self.createMathObj("1", RED, 
                                 position_var=y_equal_sign, 
                                 position=RIGHT)

        
        mu_container=self.createMathObj("\mu", YELLOW)
        mu_equal_sign = self.createMathObj("=",position_var=mu_container, position=RIGHT)
        five = self.createMathObj("5", YELLOW, position_var=mu_equal_sign, position=RIGHT)
        x_group = VGroup(x_container, x_equal_sign, two)
        y_group = VGroup(y_container, y_equal_sign, one)
        mu_group = VGroup(mu_container, mu_equal_sign, five)
        
        animations = [x_group, y_group, mu_group]

        
        #containersText = Text("The container").shift(ORIGIN + UP * 2).set_x_index(5).align_to(y_group, ORIGIN)
        THE_TEXT = Text("The")#.shift(ORIGIN + UP * 2).set_z_index(5).to_edge(UP)
        CONTAINER_TEXT = Text(" variable").next_to(THE_TEXT, RIGHT)
        TEXT_GROUP = VGroup(THE_TEXT, CONTAINER_TEXT).shift(ORIGIN + UP * 2).set_z_index(5).to_edge(UP)
        def animation_sequence(animations:list, text=TEXT_GROUP):
            self.play(Write(text, run_time=2))
            container_x =self.createMathObj("\hspace{0.5cm} x{2}^{variable}", RED, position_var=THE_TEXT, position=RIGHT, buff=0.5)
            container_x.match_height(text)

            self.add(animations[0])
            self.play(animations[0].animate())
            self.wait(1)
            
            self.play(animations[1].animate.shift(UP))
            self.wait(1)
            
            self.play(animations[2].animate.shift(DOWN))
            self.play(ReplacementTransform(CONTAINER_TEXT,container_x))

        animation_sequence(animations)

    def the_algbraic_expression(self):
        expression1 = MathTex("3-2=1")
        expression2 = self.createMathObj("5-4=1", position_var=expression1, position=UP)
        expression3 = self.createMathObj("10-9=1", position_var=expression1,position=DOWN)
        expressions_list = [expression1,expression2,expression3] 
        expressions_group = VGroup(expression1, expression2, expression3)
        
        equiavalence_expression = Tex(r"{$1=\begin{cases} 3-2\\5-4\\10-9\end{cases}$}")
        
        def animation_sequence(expressions=expressions_list):
          
            self.add(expressions_group)
            
            self.wait(1)
            self.play(ReplacementTransform(expressions_group, equiavalence_expression))
        
        animation_sequence()

    def algebraic_operations(self):
        number_expression = self.createMathObj("1+1 = 2")

        multiplication = self.createMathObj(r"2\times1=2")
        multiplication_variation1 = self.createMathObj("2\cdot1=2")
        multiplication_variation2 = self.createMathObj("2(1) = 2")

        two_x = self.createMathObj("x+x=2x")

        coefficient_label = Label("coeffiecient", color="#6d8fa3")

        multiplication_definition = MathTex(r"2\times1=1+1")
        multiplication_definition2 = MathTex(r"3\times1=1+1+1")
        multiplication_definition3 = self.createMathObj(r"3\times1=1+1+1")
        
        nice_color="#0D2966"
        multiplication_math_definition = self.createMathObj(r"n \times 1 = \overbrace{1+1\cdots}^n", col=nice_color)
        multiplication_elaborating_sequence_1 = self.createMathObj(r"3\times2=2+2+2", position_var=multiplication_definition, position=DOWN, buff=1) 
        multiplication_elaborating_sequence_2 = self.createMathObj(r"6\times3=6+6+6", 
                                                                   position_var=multiplication_elaborating_sequence_1, 
                                                                   position=DOWN) 
    
        multiplication_elaborating_sequence_3 = self.createMathObj(r"4\times1=1+1+1+1", 
                                                                   position_var=multiplication_elaborating_sequence_2, 
                                                                   position=DOWN)

        elaborating_sequence_group = VGroup(multiplication_elaborating_sequence_1, 
                                            multiplication_elaborating_sequence_2,
                                            multiplication_elaborating_sequence_3)
        
        cdot = self.createMathObj(r"\cdot")

        definition_addition_of_variables = MathTex(r"n", r"\times", r"x=\overbrace{x+x}^n")
        
        before_sequence_group = VGroup(multiplication_math_definition, elaborating_sequence_group)
        final_two_x = MathTex(r"2x =",
                              r"2 \cdot x =",r" 2(x)")
        
        two_times_one = MathTex(r"2\times 1 = 2\cdot 1=", r"2(1)").next_to(final_two_x, DOWN)
        elab_two_times_1 = MathTex("=1+1").next_to(two_times_one, DOWN, buff=1)
        elab_two_times_x = MathTex("=x+x").next_to(final_two_x, DOWN)
        final_animations = VGroup(final_two_x, two_times_one, elab_two_times_x, elab_two_times_1)
        x_plus_x = self.createMathObj("x+x=2x")
        def addition_scene(two_x=two_x):
            # Starting with but why does x+x = 2x? => addtion then multiplication definition
            nonlocal before_sequence_group
            self.add(two_x)
            self.wait(1)
            self.play(ReplacementTransform(two_x, number_expression), run_time=2)
            self.wait(1)
            self.play(ReplacementTransform(number_expression, multiplication))
            self.wait(1)
            self.play(ReplacementTransform(multiplication, multiplication_definition)) 
            self.wait(1)
            self.play(ReplacementTransform(multiplication_definition, multiplication_definition2))
            self.play(ReplacementTransform(multiplication_definition2, multiplication_definition3))
            
            self.play(ReplacementTransform(multiplication_definition3, multiplication_math_definition))
            
            self.play(Write(elaborating_sequence_group))
            #self.remove(multiplication_math_definition)
            self.wait(1)
            for i in range(1, 10):
                output = f"{i}"
                sequence = MathTex(str(output), r"\times ",r"1", r"=", rf"{output}",r"(1)")
                self.play(ReplacementTransform(before_sequence_group, sequence))
                
                before_sequence_group = sequence
        addition_scene()

        self.play(ReplacementTransform(before_sequence_group, final_two_x))
        self.play(Write(two_times_one), run_time=1)
        self.play(two_times_one.animate.next_to(elab_two_times_x, DOWN))

        self.play(Write(elab_two_times_x))
        self.play(Write(elab_two_times_1))
        self.wait(1)
        self.play(ReplacementTransform(final_animations, x_plus_x),run_time=2)   

    def createMathObj(self,expression, col=None,position_var=None, position=None, buff=None):
        math_obj = MathTex(expression)
        
        if col is not None:    
            math_obj.set(color=col)
        if position_var is not None: 
            if buff is not None:
                math_obj.set().next_to(position_var, position, buff)
            else: 
                math_obj.set().next_to(position_var, position)

        
        return math_obj
