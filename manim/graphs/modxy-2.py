# modxy-2.py
# f(x)=||e|^-|x|-1/2|


from manim import *


class Modulus(Scene):
	config.frame_width = 10.1
	config.frame_height = 10.1
	config.pixel_width = 2400
	config.pixel_height = 2400
	config.background_color="#FDEBD0"

	config.frame_rate=60
#	config.transparent=True
#	config.background_opacity=0.15
	
	def construct(self):
		Tex.set_default(color=BLACK)
		Line.set_default(color=BLACK)
		Mobject.set_default(color=BLACK)
		ax = Axes(
				x_range=[-4, 4, 1],
				y_range=[-4, 4, 1], 
				x_length = 8,
				y_length = 8,
				tips=False,
		).shift(DOWN)
		myTemplate = TexTemplate(preamble=r"\usepackage[utopia]{mathdesign}")
		function = "$f(x)=|e^{-|x|}-0.5|$"
		title = Title(function, tex_template=myTemplate, include_underline=False)

		eq=Tex(r"$e^x$", tex_template=myTemplate)
		eq1=Tex(r"$e^{-x}$", tex_template=myTemplate)
		eq2=Tex(r"$e^{-x} - 0.5$", tex_template=myTemplate)
		eq3=Tex(r"$e^{-|x|} - 0.5$", tex_template=myTemplate)
		eq4=Tex(r"$|e^{-|x|} - 0.5|$", tex_template=myTemplate)
		

		graph = ax.plot(
						lambda x: np.exp(x),
						x_range=(-4, 4, 0.001),
						)
						

		graph1 = ax.plot(
						lambda x: np.exp(-x),
						x_range=(-4, 4, 0.001),
						).set_color(MAROON_D)
	
		graph2 = ax.plot(
						lambda x: np.exp(-x) - 0.5,
						x_range=(-4, 4, 0.001),
						).set_color(MAROON_D)
		
		graph3 = ax.plot(
						lambda x: np.exp(-abs(x)) - 0.5,
						x_range=(-4, 4, 0.001),
						).set_color(MAROON_D)
				
		graph4 = ax.plot(
						lambda x: abs(np.exp(-abs(x)) - 0.5),
						x_range=(-4, 4, 0.001),
						).set_color(MAROON_D)
																							
		self.add(title, ax)
		self.wait(1/30)
		self.play(Create(graph.set_color(MAROON_E)), Write(eq.move_to([-3.2, 1.2, 0]).scale(0.75)), Flash(eq, color=BLACK, flash_radius=0.5))
		self.wait()
		self.play(Transform(graph, graph1), Transform(eq, eq1.move_to([-3.2, 1.2, 0]).scale(0.75)))
		self.wait()
		self.play(Transform(graph, graph2), Transform(eq, eq2.move_to([-3.2, 1.2, 0]).scale(0.75)))
		self.wait()
		self.play(Transform(graph, graph3), Transform(eq, eq3.move_to([-3.2, 1.2, 0]).scale(0.75)))
		self.wait()
		self.play(Transform(graph, graph4), Transform(eq, eq4.move_to([-3.2, 1.2, 0]).scale(0.75)))
		self.wait(3)

