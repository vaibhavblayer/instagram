# modxy-test.py
# f(x)=||e|^-|x|-1/2|


from manim import *
from sympy.abc import x, y, z
from sympy import *

f1 = Lambda(x, exp(x))
f2 = Lambda(x, exp(-x))
f3 = Lambda(x, exp(abs(x)))
f4 = Lambda(x, exp(-abs(x)) -0.5)
f5 = Lambda(x, abs(exp(-abs(x))-0.5))
equations = [f1, f2, f3, f4, f5]



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

