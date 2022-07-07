# final.py
# |x|+|y|=1

from manim import *

f1 = lambda x, y: x + y -1 
f2 = lambda x, y: abs(x) + y -1
f3 = lambda x, y: abs(x) + abs(y) -1
equations = [f1, f2, f3]
tex_equations = ["$x+y=1$", "$|x| + y=1$", "$|x|+|y|=1$"]

class Testing(Scene):
	
	config.frame_width = 10.1
	config.frame_height = 10.1
	config.pixel_width = 1080
	config.pixel_height = 1080
	config.background_color="#FDEBD0"
	config.movie_file_extension=".mov"
	config.frame_rate=60
	
	def construct(self):
		Tex.set_default(color=BLACK)
		Mobject.set_default(color=BLACK)
		Text.set_default(color=BLACK)
		myTemplate = TexTemplate(preamble=r"\usepackage[utopia]{mathdesign}")
		title = Title(tex_equations[-1], tex_template=myTemplate, include_underline=False)

		ax = Axes(
				x_range=[-4, 4, 1],
				y_range=[-4, 4, 1], 
				x_length = 8,
				y_length = 8,
				tips=False,
		).shift(DOWN)


		self.add(ax, title)
		graph = ax.plot_implicit_curve(equations[0]).set_color(MAROON_D)
		tex = Tex(tex_equations[0], tex_template=myTemplate).move_to([-3.2, 1.2, 0])
		for i in range(len(equations)):
			graphi = ax.plot_implicit_curve(equations[i]).set_color(MAROON_D)
			texi = Tex(tex_equations[i], tex_template=myTemplate).scale(0.75).move_to([-3.2, 1.2, 0])
			if i == 0:
				self.play(Create(graph), Write(tex))
				self.wait()
			else:	
				self.play(Transform(graph, graphi), Transform(tex, texi))
				self.wait()

		self.wait()


