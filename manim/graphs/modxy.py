# modxy.py
# f(x)=||x|^2-2|x|-3|


from manim import *


class Modulus(Scene):
	config.frame_width = 10.1
	config.frame_height = 10.1
	config.pixel_width = 2400
	config.pixel_height = 2400
	config.movie_file_extension=".mov"
	config.background_color="#FDEBD0"

	config.frame_rate=60
#	config.transparent=True
#	config.background_opacity=0.15
	
	def construct(self):
		Tex.set_default(color=BLACK)
		Line.set_default(color=BLACK)
		Mobject.set_default(color=BLACK)
		ax = Axes(
				x_range=[-5, 6, 1],
				y_range=[-5, 6, 1], 
				x_length = 8,
				y_length = 8,
				tips=False,
		).shift(DOWN)
		myTemplate = TexTemplate(preamble=r"\usepackage[utopia]{mathdesign}")
		function = "$f(x)=||x|^2-2|x|-3|$"
		title = Title(function, tex_template=myTemplate, include_underline=False)

		eq=Tex(r"$x^2-2x-3$", tex_template=myTemplate)
		eq1=Tex(r"$|x|^2-2|x|-3$", tex_template=myTemplate)
		eq2=Tex(r"$||x|^2-2|x|-3|$", tex_template=myTemplate)
		

		graph = ax.plot(
						lambda x: x**2-2*x-3,
						x_range=(-4, 4, 0.001),
						)
						

		graph1 = ax.plot(
						lambda x: abs(x)**2-2*abs(x)-3,
						x_range=(-4, 4, 0.001),
						).set_color(MAROON_D)
	
		graph2 = ax.plot(
						lambda x: abs(abs(x)**2-2*abs(x)-3),
						x_range=(-4, 4, 0.001),
						).set_color(MAROON_D)
											
		self.add(title, ax)
		self.wait(1/30)
		self.play(Create(graph.set_color(MAROON_E)), Write(eq.move_to([-3.2, 1.2, 0]).scale(0.75)), Flash(eq, color=BLACK, flash_radius=0.5))
		self.wait()
		self.play(Transform(graph, graph1), Transform(eq, eq1.move_to([-3.2, 1.2, 0]).scale(0.75)))
		self.wait()
		self.play(Transform(graph, graph2), Transform(eq1, eq2.move_to([-3.2, 1.2, 0]).scale(0.75)))
		self.wait(3)

