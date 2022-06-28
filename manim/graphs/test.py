from manim import *

from myfunctions import *

topics=["calculus", "probability", "integral-calculus", "7765974537", "Vaibhav Blayer", "mechanics", "electrodynamics", "fluid-mechanics"]


class Test(Scene):
	config_instagram()
	def construct(self):
		a = Circle()
		ax = putAxes()
		group=Group(a, ax)

		for topic in topics:
			t = Text(topic).set_color(BLACK)
			self.add(t)


		self.add(group)




class Line(Scene):
    def construct(self):
        curve = ParametricFunction(lambda t: [t, np.sin(t), 0], t_range=[-PI, PI, 0.01], stroke_width=10)
        new_curve = CurvesAsSubmobjects(curve)
        new_curve.set_color_by_gradient(BLUE, RED)
        self.add(new_curve.shift(UP), curve)



class TrigoTable(Scene):
    def construct(self):
#		b = Line(a.get_center(), a.get_right())
#		c = Dot()
#		h = Line(a.get_center(), a.point_at_angle(PI/4))
        t0 = IntegerTable(
            [[0,30,45,60,90],
            [90,60,45,30,0]],
            col_labels=[
                MathTex("\\frac{\sqrt{0}}{2}"),
                MathTex("\\frac{\sqrt{1}}{2}"),
                MathTex("\\frac{\sqrt{2}}{2}"),
                MathTex("\\frac{\sqrt{3}}{2}"),
                MathTex("\\frac{\sqrt{4}}{2}")],
            row_labels=[MathTex("\sin"), MathTex("\cos")],
            h_buff=1,
            element_to_mobject_config={"unit": "^{\circ}"})
        self.add(t0.set_color(BLUE_E).shift(DOWN*2.5).scale(0.8))

class Rectangle(Scene):
    def construct(self):
        decimal = DecimalNumber().to_edge(UP).set_color(BLUE_C)
        a = Circle()
        b = a.copy().set_stroke(GRAY_E)

        decimal.add_updater(lambda d: d.set_value(a.get_radius()))

        self.add(a, b, decimal)
        self.play(a.animate.set(radius=3))
        self.wait()
