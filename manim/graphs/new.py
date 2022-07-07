# new.py
# |f(x)|=x^2 -2x -3

from manim import *

f1 = lambda x: x**2 -1 
f2 = lambda x: -x**2 + 1
f3 = lambda x, y: abs(y) -x**2 + 1 
equations = [f1, f2, f3]
tex_equations = ["$x^2 -1$", "$-(x^2-1)$", "$|f(x)|=x^2-1$"]

class Testing(Scene):
	
	config.frame_width = 10.1
	config.frame_height = 10.1
	config.pixel_width = 400
	config.pixel_height = 400
	config.background_color="#FDEBD0"
	config.movie_file_extension=".mov"
	config.frame_rate=30
	
	def construct(self):
		Tex.set_default(color=BLACK)
		Mobject.set_default(color=BLACK)
		Text.set_default(color=BLACK)
		myTemplate = TexTemplate(preamble=r"\usepackage[utopia]{mathdesign}")
		title = Title(tex_equations[-1], tex_template=myTemplate, include_underline=False)

		label=Tex(tex_equations[-1], tex_template=myTemplate).move_to([-3.2, 1.2, 0])
		ax = Axes(
				x_range=[-4, 4, 1],
				y_range=[-4, 4, 1], 
				x_length = 8,
				y_length = 8,
				tips=False,
		).shift(DOWN)

		graph = ax.plot_implicit_curve(equations[-1], ).set_color(MAROON_D)
		self.add(ax, title, graph, label)

		for i in range(len(equations)-1):
			graphi = ax.plot(equations[i], x_range=(-3, 3, 0.001)).set_color(MAROON_D)
			equation = Tex(tex_equations[i], tex_template=myTemplate)
			self.play(Transform(graph, graphi), Transform(label, equation.move_to([-3.2, 1.2, 0]).scale(0.75)))
			self.wait()




