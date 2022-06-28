from manim import *






class SinCurve(Scene):
	
	config.frame_width = 10
	config.frame_height = 10
	config.pixel_width = 2400 
	config.pixel_height = 2400

	def construct(self):
		axes = Axes(
				x_range=[0, 8, PI/2],
				y_range=[-1.5, 1.5, 1],
				x_length=8,
				y_length=3,
				tips=False,
				)
		labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
		sin_curve=axes.plot(lambda x:np.sin(x), x_range=[0, 2*PI])
#		sin_label=axes.get_graph_label(sin_curve, "\\sin(x)", x_val=PI/2, direction=UP)
		self.add(sin_curve, axes, labels)





class ComplexNumber(Scene):
	def construct(self):
		c=Circle().set_color(RED)
		cc=c.copy().set_color(BLUE)
		c.apply_complex_function(
			lambda x: np.exp(x*1j)
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
		self.play(t.animate.set_value(TAU), run_time=3)

