from manim import *

ALMOND = "#D6BD98"
greenish = "#44741a"
BG = "#E8EAE7"
MUSTARD_GREEN = "#687D31"
DEEP_SLATE_SPARKLE = "#406768"
MOONSTOLE_BLUE = "#6FA9BB"
PHTHALO_GREEN = "#19350C"

colors = [MUSTARD_GREEN, DEEP_SLATE_SPARKLE, MOONSTOLE_BLUE, PHTHALO_GREEN]

darker_blues = ["#1A4474", "#5b90c4"]

green_gradient = [
    "#013220",  # very dark deep-green / almost forest
    "#2E8B57",  # medium-dark sea-green
    "#57C84D",  # vibrant mid-green
]

exponent_laws = {
    "product_rule": MathTex(r"a^m", r"\cdot", r"a^n", "=", r"a^{m+n}"),
    "quotient_rule": MathTex(r"\frac" r"{a^m}{a^n}", "=", r"a^{m-n}"),
    "power_rule" :MathTex(r"(a", r"^m)", "=", r"a^{m+n}"),
    "power_of_quotient_rule" : MathTex(
            r"\left(",
            r"\frac{a}{b}",
            r"\right)",
            r"^m",
            "=",
            r"\frac{a^m}{b^m}",
        )
}

class Product_Rule_Scene(Scene):
    def construct(self):
        self.product_rule()
    def product_rule(self):
        #Write laws of exponents first
        Laws = Text("Laws of exponents")
        self.camera.background_color = BG

        variable_m = 0
        variable_n = 0

        cdot = MathTex(r"\cdot")

        product_rule = MathTex(r"a^m", r"\cdot", r"a^n", "=", r"a^{m+n}")
        quotient_rule = MathTex(r"\frac{a^m}{a^n}", "=", r"a^{m-n}")
        power_rule = MathTex(r"(a", r"^m)", "=", r"a^{m+n}")
        power_of_quotient_rule = MathTex(
            r"\left(",
            r"\frac{a}{b}",
            r"\right)",
            r"^m",
            "=",
            r"\frac{a^m}{b^m}",
        )

        def set_colors(product, quotient, power, power_quot):
            laws = [product, quotient, power, power_quot]
            colored = []
            for law in laws:
                law.set_color(darker_blues, 50)
                colored.append(law)
            return colored

        laws = set_colors(product_rule, quotient_rule, power_rule, power_of_quotient_rule)
        definitions_group = VGroup(*laws).arrange(DOWN)

        box = SurroundingRectangle(product_rule, buff=0.2).set_color(darker_blues, 20)
        product_rule_text = (
            Text("Product rule", font="Cormorant")
            .next_to(definitions_group[0], UP)
            .set_color(darker_blues)
        )

        def write_all_laws(def_group=definitions_group):
            self.play(Write(def_group))

        def product_rule_explanation(product=product_rule, def_group=definitions_group, pr_text=product_rule_text):
            exponent_m_of_a = MathTex(
                r"a^m = \overbrace{a \cdot a \cdot a \cdots}^{m}"
            ).set_color_by_gradient(*green_gradient)

            a_power = MathTex(
                r"a^2", "=", "a", r"\cdot a"
            ).set_color_by_gradient(*green_gradient)

            basic_exponent_expanded = MathTex(r"2 \cdot 2 = 2^2")

            self.play(Create(box), box.animate.set_stroke(width=2))
            self.wait(1)
            self.play(
                FadeOut(def_group[1]),
                FadeOut(def_group[2]),
                FadeOut(def_group[3]),
            )

            box.add_updater(
                lambda b: b.become(
                    SurroundingRectangle(def_group[0], buff=0.2)
                    .set_color(darker_blues, 50)
                    .set_stroke(width=1)
                )
            )

            self.play(def_group[0].animate.center())
            box.clear_updaters()

            self.play(FadeOut(box))
            self.play(Write(pr_text))
            self.play(FadeOut(product[1], product[2], product[3], product[4]))
            self.wait(1)

            self.play(product[0].animate.center())
            self.wait(1)
            self.play(
                ReplacementTransform(product[0], exponent_m_of_a),
                FadeOut(pr_text),
            )

            self.wait(2)

            def a_power_sequence():
                nonlocal exponent_m_of_a

                two_squared = MathTex(r"2 \cdot 2 = 2^2").set_color_by_gradient(*green_gradient)
                two_cubed = MathTex(r"2 \cdot 2 \cdot 2 = 2^3").set_color_by_gradient(*green_gradient)
                two_4th = MathTex(r"2 \cdot 2 \cdot 2 \cdot 2 = 2^4").set_color_by_gradient(*green_gradient)
                two_5th = MathTex(r"2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 = 2^5").set_color_by_gradient(*green_gradient)
                two_6th = MathTex(r"2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 = 2^6").set_color_by_gradient(*green_gradient)

                seq = VGroup(two_squared, two_cubed, two_4th, two_5th, two_6th)

                for i, obj in enumerate(seq):
                    self.play(ReplacementTransform(exponent_m_of_a, obj), run_time=0.5)
                    self.wait(0.5)
                    if i == len(seq) - 1:
                        break
                    exponent_m_of_a = obj

                return seq

            self.wait(1)
            exponent_seq = a_power_sequence()

            sixth_power_2 = MathTex(
                r"\overbrace{2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2}",
                r"^6",
                r"=2",
                "^6",
            ).set_color_by_gradient(*green_gradient)

            a_sixth = MathTex(
                r"\overbrace{a \cdot a \cdot a \cdot a \cdot a \cdot a}^6 = a^6"
            ).set_color_by_gradient(*darker_blues)

            self.play(ReplacementTransform(exponent_seq, sixth_power_2))
            self.wait(1)
            self.play(ReplacementTransform(sixth_power_2, a_sixth), run_time=1)

            self.wait(2)

            clean_product_rule = MathTex(
                r"a^m \cdot a^n = a^{m+n}"
            ).set_color(darker_blues)

            product_rule_example = MathTex(
                r"a^2 \cdot a^3 = a^5"
            ).set_color_by_gradient(*darker_blues)

            expanded_example = MathTex(
                r"\overbrace{a^2}^{a\cdot a} \cdot "
                r"\underbrace{a^3}_{a\cdot a \cdot a} = "
                r"\overbrace{a^5}^{a\cdot a \cdot a \cdot a \cdot a}"
            ).set_color_by_gradient(*darker_blues)

            self.play(ReplacementTransform(a_sixth, product_rule_example))
            self.wait(1)

            self.play(ReplacementTransform(product_rule_example, expanded_example))
            self.wait(1)

            self.play(ReplacementTransform(expanded_example, clean_product_rule))

        write_all_laws()
        product_rule_explanation()

class Quotient_Rule_Scene(Scene):
    def construct(self):
        self.Laws_of_exponents()
        self.zoom_on_quotient()
        self.practical_quotient_expansion()
        self.variable_example()
        self.final_()

    def Laws_of_exponents(self):
        self.title_text = Text("Laws of exponents")
        self.title_text.move_to(UP*3)
        self.laws_group = VGroup()
        for law, text in exponent_laws.items():
            self.laws_group.add(text.set_color_by_gradient(darker_blues))
        self.laws_group.arrange(DOWN)
        self.laws_group.next_to(self.title_text, DOWN, buff=0.5)
        self.play(Write(self.title_text))
        self.play(Write(self.laws_group))
    
    def zoom_on_quotient(self):
        box = SurroundingRectangle(self.laws_group[1], buff=0.2).set_color(darker_blues, 20)
        # boxed = 
        quotient_rule_text = (
            Text("Quotient Rule", font="Cormorant")
            .next_to(self.laws_group[0], UP)
            .set_color(darker_blues)
        )
        box.add_updater(
                lambda b: b.become(
                    SurroundingRectangle(self.laws_group[1], buff=0.2)
                    .set_color(darker_blues, 50)
                    .set_stroke(width=0.5)
                )
            )
        # surrounding the equation with a box to emphasise
        self.play(Create(box))
        # removing the other rules and title
        self.play(FadeOut(self.title_text), FadeOut(self.laws_group[0],self.laws_group[2], self.laws_group[3]))
        # obv
        self.play(Write(quotient_rule_text))
        # moving the quotient rule to the center
        self.play(self.laws_group[1].animate.center())
        # removing updaters for box position 
        # \\*** 
        # *?Is it necessary*\\ 
        box.clear_updaters()
        self.play(FadeOut(box))

    def set_blue(self, thing:Mobject):
        thing.set_color_by_gradient(darker_blues)

    def set_green(self, thing:Mobject):
        thing.set_color_by_gradient(green_gradient)

    def practical_quotient_expansion(self):
        practical_example = MathTex(r"\frac" r"{" r"x" r"^4}" r"{" r"x" r"^2}" r"=\frac{" r"x" r"\cdot x" r"\cdot x " r"\cdot x" r"}" r"{x \cdot x}").set_color_by_gradient(darker_blues)
        expansion = (
            MathTex(r"=\frac{\overbrace{a\cdot a \cdots}^m}{\underbrace{a\cdot a \cdots}_n}")
            .next_to(self.laws_group[1][0], RIGHT)    
        )
        self.set_green(expansion)
        # this a version of practical example
        temp = TexTemplate()
        temp.add_to_preamble(r"\usepackage{cancel}")
        const_ver = MathTex(r"\frac" r"{2^4}" r"{2^2}" r"=\frac{2\cdot 2\cdot 2\cdot 2 }{2 \cdot 2}").set_color_by_gradient(darker_blues)
        canceling = (
            MathTex(r"\frac" r"{2^4}" r"{2^2}" r"=\frac{\cancel{2}\cdot \cancel{2}\cdot 2\cdot 2 }{\cancel{2} \cdot \cancel{2} }", tex_template=temp)
            .set_color_by_gradient(darker_blues)
            
        ) 
        # ? maybe we should explain division

        result = (
            MathTex(r"=", r"\frac{2\cdot2}{1\cdot1}=", r"\frac{2^2}{1}=" r"2^2")
            .next_to(canceling, RIGHT)
        )
        self.set_blue(result)

        # nth_var = MathTex(r"2")
        self.play(self.laws_group[1].animate.center())
        # coloring the definition prt of the equaiton to emphasise it
        self.play(self.laws_group[1][0].animate.set_color(green_gradient))

        # Fade out the non-essential parts of the law definition to focus on the base/ exponent relationship
        # fading out the rest of the equaiton to make room for its expansion
        self.play(FadeOut(self.laws_group[1][1], self.laws_group[1][2]))

        # Display the generic exponential law expansion (a^m / a^n = a^(m-n))
        self.play(Write(expansion))
        self.wait(0.5)

        # Transform the generic expansion into a concrete example with x variables
        # writing the practical example now
        self.play(ReplacementTransform(expansion,practical_example), FadeOut(self.laws_group[1][0]))
        self.wait(1)

        # Substitute x=2 to make it a numerical example instead of algebraic
        # replacing the xs with 2
        self.play(ReplacementTransform(practical_example, const_ver), FadeOut(practical_example))
        self.wait(1)

        # Cancel matching factors in numerator and denominator to simplify
        self.play(ReplacementTransform(const_ver, canceling))        
        self.wait(0.5)

        # Reveal the final simplified result of 2^2 = 4
        self.play(Write(result))
        self.wait(0.5)

        # Remove the cancellation marks and center the result for emphasis
        self.play(FadeOut(canceling), result.animate.center())

        # Remove the first part of the result (the "=" sign and intermediate steps)
        self.play(FadeOut(result[0]), result[0].animate.set_color(BLACK))

        # Finally remove the remaining result (final answer 2^2)
        self.play(FadeOut(result))

    def variable_example(self):
        # preambles
        temp = TexTemplate()
        temp.add_to_preamble(r"\usepackage{cancel}")
        temp.add_to_preamble(r"\usepackage{chemfig}")
        temp.add_to_preamble(r"\usepackage{tikz}")
        
        # variables
        variable_example = MathTex(r"\frac" r"{" r"x" r"^4}" r"{" r"x" r"^2}" r"=\frac{" r"x" r"\cdot x" r"\cdot x " r"\cdot x" r"}" r"{x \cdot x}")
        canceled_out     = MathTex(r"\frac{x^4}{x^2}=\frac{\cancel{x}\cdot \cancel{x} \cdot x\cdot x}{\cancel{x} \cdot \cancel{x} }", tex_template=temp)
        add_brace        = MathTex(r"\frac{x^4}{x^2}=\frac{\overbrace{\cancel{x}\cdot \cancel{x}}^{-2} \cdot x\cdot x}{\underbrace{\cancel{x} \cdot \cancel{x}}_{-2}}", tex_template=temp)
        double_brace     = MathTex(r"\frac{x^4}{x^2}=\frac{\overbrace{\overbrace{\cancel{x}\cdot \cancel{x}}^{-2} \cdot x\cdot x}^{4}}{\underbrace{\cancel{x} \cdot \cancel{x}}_{-2}}", tex_template=temp)
        resulting_expression = MathTex(r"=",r"x^{4-2} ").next_to(double_brace)
        molecule = Tex(r"\chemfig{H-A} \quad \chemfig{B}", tex_template=temp)
        
        # animations
        self.set_blue(variable_example)
        self.play(Write(variable_example))
        self.play(TransformMatchingShapes(variable_example, canceled_out))
        self.wait(1)
        self.play(TransformMatchingShapes(canceled_out, add_brace))
        self.wait(0.5)
        self.play(TransformMatchingShapes(add_brace, double_brace))
        self.play(Write(resulting_expression))
        self.wait(2)
        self.play(FadeOut(resulting_expression, double_brace))

    def final_(self):
        law_ = MathTex(r"\frac{x^m}{x^n}=x^{m-n}")

        self.play(Write(law_))
