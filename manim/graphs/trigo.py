        
from manim import *

from myfunctions import config_instagram


class TrigoTable(Scene):
	config_instagram()
	def construct(self):
		cl = "#17202A"
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
            element_to_mobject_config={"unit": "^{\circ}"}
			)
		self.add(t0.set_color(cl).shift(DOWN*2.5).scale(0.8))



		angle = ValueTracker(10)

		a = Circle().scale(1.8).shift(UP*2)
		h = Line(a.get_center(), a.point_at_angle(angle.get_value()))
		c = Dot(point=a.get_center())
		
		bp = Point([1.8*np.cos(angle.get_value()*DEGREES), a.get_center()[1], 0])
		pp = Point(a.point_at_angle(angle.get_value()*DEGREES))

		p = Line([1.8*np.cos(angle.get_value()*DEGREES), a.get_center()[1], 0], a.point_at_angle(angle.get_value()*DEGREES))
		b = Line(a.get_center(), bp)
		arc = Angle(b, h)
		
		g = Group(a, b, c, h, p, bp, pp, arc).set_color(cl)


		self.add(g)

		pp.add_updater(
			lambda x: x.become(Point(a.point_at_angle(angle.get_value()*DEGREES)))
		)

		bp.add_updater(
			lambda x: x.become(Point([1.8*np.cos(angle.get_value()*DEGREES), a.get_center()[1], 0]))
		)

		h.add_updater(
				lambda x: x.become(Line(a.get_center(), pp).set_color(cl))
		)

		p.add_updater(
			lambda x: x.become(Line(bp, pp).set_color(cl))
		)
	

		b.add_updater(
			lambda x: x.become(Line(a.get_center(), bp).set_color(cl))
		)



		arc.add_updater(
			lambda x: x.become(Angle(b, h, stroke_width=4).set_color(cl))
		)


		self.play(angle.animate.set_value(30), run_time=1, rate_function=linear)
		self.wait(0.5)
		self.play(angle.animate.set_value(45), run_time=1, rate_function= FadeOut)
		self.wait(0.5)
		self.play(angle.animate.set_value(60), run_time=1)
		self.wait(0.5)
		self.play(angle.animate.set_value(90), run_time=2)


