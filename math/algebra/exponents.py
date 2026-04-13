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
    "quotient_rule": MathTex(r"\frac{a^m}{a^n}", "=", r"a^{m-n}"),
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

    def Laws_of_exponents(self):
        title_text = Text("Laws of exponents")
        title_text.move_to(UP*3)
        self.laws_group = VGroup()
        for law, text in exponent_laws.items():
            self.laws_group.add(text)
        self.laws_group.arrange(DOWN)
        self.laws_group.next_to(title_text, DOWN, buff=0.5)
        self.play(Write(title_text))
        self.play(Write(self.laws_group))
    
    def zoom_on_quotient(self):
        box = SurroundingRectangle(self.laws_group[1], buff=0.2).set_color(darker_blues, 20)
        quotient_rule_text = (
            Text("Quotient Rule", font="Cormorant")
            .next_to(self.laws_group[0], UP)
            .set_color(darker_blues)
        )
        self.play(Create(box))
        self.play(Write(quotient_rule_text))




