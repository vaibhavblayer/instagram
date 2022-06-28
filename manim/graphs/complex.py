from manim import *


class ComplexNumber(Scene):
	config.frame_width = 10
	config.frame_height = 10
	config.pixel_width = 600 
	config.pixel_height = 600


	def construct(self):
		c=Circle().scale(1.5)
		cc=c.copy().set_color(WHITE)
		c.apply_complex_function(
			lambda y: np.exp(y*1j)
		)

		t=ValueTracker(0)
		c.add_updater(
			lambda x: x.become(cc.copy().apply_complex_function(
				lambda x: np.exp(x+t.get_value()*1j)
				)
			)
		)

		self.add(cc)
		self.play(TransformFromCopy(cc, c))
		self.play(t.animate.set_value(PI), run_time=3)






class ComplexNum(Scene):
	def construct(self):
		c=Circle().scale(1.5)
		cc=c.copy()

		t=ValueTracker(0)
		c.add_updater(
				lambda x:x.become(cc.copy().apply_complex_function(
					lambda x:1*np.exp(x*1j)
				))
			)

		self.add(cc)
		self.play(TransformFromCopy(cc, c))
		self.play(t.animate.set_value(3), run_time=3)








class Trace(Scene):
	config.origin=[0, -2, 0]
	config.frame_width = 10.1
	config.frame_height = 10.1
	config.pixel_width = 2400
	config.pixel_height = 2400
	config.background_color="#FDEBD0"
	def construct(self):
		myTemplate = TexTemplate()
		myTemplate.add_to_preamble(r"\usepackage[utopia]{mathdesign}")

		eq=Tex(r"$f(x)=|x|$", tex_template=myTemplate) 
		
		path = VMobject()
		path2=VMobject()
		dot =Dot(point=[0, -2, 0])
		dot2=dot.copy()
		path.set_points_as_corners([dot.get_center(), dot.get_center()])
		path2.set_points_as_corners([dot2.get_center(), dot2.get_center()])
		
		group=Group(path, path2, dot, dot2, eq).set_color(GRAY_E)
		ax=Axes(
			x_range=[-5, 5, 1],
			y_range=[-1, 5, 1],
			x_length=10,
			y_length=6,
			tips=False,
		).set_color(GRAY_D)

		def update_path(path):
			pp = path.copy()
			pp.add_points_as_corners([dot.get_center()])
			path.become(pp)

		def update_path2(path):
			pp = path.copy()
			pp.add_points_as_corners([dot2.get_center()])
			path.become(pp)

		path.add_updater(update_path)
		path2.add_updater(update_path2)

		self.add(group, ax, eq.shift(UP*4))
		self.wait(0.25)
		self.play(dot.animate.shift(3*RIGHT).shift(3*UP))
		self.play(dot2.animate.shift(-3*RIGHT).shift(3*UP))
		self.wait(2)





class Updater(Scene):
	def construct(self):
		d1, d2 = Dot(color=WHITE), Dot(color=WHITE)
		l1 = Line(d1.get_center(), d2.get_center()) 
		x = ValueTracker(0)
		y = ValueTracker(0)
		d1.add_updater(lambda z: z.set_x(x.get_value()))
		d1.add_updater(lambda z: z.set_y(x.get_value()))
		l1.add_updater(lambda z:z.become(Line(d1.get_center(), d2.get_center())))
		self.add(d1, d2, l1)
		self.play(x.animate.set_value(2))
		
		d3=Dot().set_x(2).set_y(2)
		self.add(d3)

		self.wait(2)
		self.play(x.animate.set_value(5))

			




