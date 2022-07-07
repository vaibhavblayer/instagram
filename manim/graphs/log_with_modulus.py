# log_with_modulus.py
# |y|=|log|x||

from manim import *

f1 = lambda x, y: y - np.log(x)
f2 = lambda x, y: y - np.log(abs(x))
f3 = lambda x, y: y - abs(np.log(abs(x)))
f4 = lambda x, y: abs(y) - abs(np.log(abs(x)))
equations = [f1, f2, f3, f4]
tex_equations = ["$y=\log{x}$", "$y=\log{|x|}$", "$y = |\log{|x|}|$", "$|y| = |\log{|x|}|$"]

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
				x_range=[-5, 5, 1],
				y_range=[-5, 5, 1], 
				x_length = 8,
				y_length = 8,
				tips=False,
		).shift(DOWN)


		self.add(ax, title)
		graph = ax.plot_implicit_curve(equations[0], max_quads=2500).set_color(MAROON_D)
		tex = Tex(tex_equations[0], tex_template=myTemplate).move_to([-3.2, 1.2, 0])
		for i in range(len(equations)):
			graphi = ax.plot_implicit_curve(equations[i], max_quads=2500).set_color(MAROON_D)
			texi = Tex(tex_equations[i], tex_template=myTemplate).scale(0.75).move_to([-3.2, 1.2, 0])
			if i == 0:
				self.play(Create(graph), Write(tex))
				self.wait()
			else:	
				self.play(Transform(graph, graphi), Transform(tex, texi))
				self.wait()

		self.wait()


