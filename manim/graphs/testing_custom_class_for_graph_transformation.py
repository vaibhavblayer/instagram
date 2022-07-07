# modxy-2.py
# f(x)=||e|^-|x|-1/2|


from manim import *
from sympy.abc import x, y, z, a, b, c, d, f, g
from sympy import *


f1 = Lambda(x, x)
f2 = Lambda(x, x**2)
f3 = Lambda(x, x**3)
f4 = Lambda(x, x**4)
f5 = Lambda(x, x**5)
f6 = Lambda(x, x**6)
f7 = Lambda(x, x**7)
f8 = Lambda(x, x**8)
equations = [f1, f2, f3, f4, f5, f6, f7, f7, f8]



class Testing(Scene):
	
	def construct(self):
		Tex.set_default(color=BLACK)
		Mobject.set_default(color=BLACK)
		Text.set_default(color=BLACK)
		myTemplate = TexTemplate(preamble=r"\usepackage[utopia]{mathdesign}")
		title = Title(latex(equations[0], mode='inline'), tex_template=myTemplate, include_underline=False)

		label=Tex(latex(equations[0]), tex_template=myTemplate).move_to([-3.2, 1.2, 0])
		ax = Axes(
				x_range=[-4, 4, 1],
				y_range=[-4, 4, 1], 
				x_length = 8,
				y_length = 8,
				tips=False,
		).shift(DOWN)

		graph = ax.plot(equations[-1], x_range=(-3, 3, 0.001)).set_color(MAROON_D)
		self.add(ax, title, graph, label)

		for i in range(len(equations)):
			graphi = ax.plot(equations[i], x_range=(-3, 3, 0.001)).set_color(MAROON_D)
			equation = Tex(latex(equations[i], mode='inline'), tex_template=myTemplate)
			self.play(Transform(graph, graphi), Transform(label, equation.move_to([-3.2, 1.2, 0]).scale(0.75)))
			self.wait()




class Modulus(Scene):
	config.frame_width = 10.1
	config.frame_height = 10.1
	config.pixel_width = 400
	config.pixel_height = 400
	config.background_color="#FDEBD0"
	config.movie_file_extension=".mov"
	config.frame_rate=30
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

