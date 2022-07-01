# modulus.py


from manim import *
from myfunctions import *


class Modulus(Scene):
	
	config_instagram()

	def construct(self):
		myTemplate = TexTemplate()
		myTemplate.add_to_preamble(r"\usepackage[utopia]{mathdesign}")

		eq=Tex(r"$f(x)=|x|+1$", tex_template=myTemplate) 
		modx = Tex(r"$|x|$", tex_template=myTemplate).shift(RIGHT*3.6+UP*1).set_color(GRAY_E).scale(0.8)
		modxx = Tex(r"$|x|+1$", tex_template=myTemplate).shift(RIGHT*3.5+UP*2).set_color(GRAY_E).scale(0.8)
		
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
		self.add(modx)
		self.wait(2)

		ll = Line(DOWN*2, RIGHT*3+UP)
		lll = Line(DOWN*2, -RIGHT*3+UP)
		
		ggg = Group()
		for i in range(11):
			p1 = ll.point_from_proportion(i/10)
			p2 = lll.point_from_proportion(i/10)
			ar = Arrow(start=p1+[0, -0.25, 0], end=p1+[0, 0.75, 0]).set_color(GRAY_E)
			ar2 = Arrow(start=p2+[0, -0.25, 0], end=p2+[0, 0.75, 0]).set_color(GRAY_E)
			ggg.add(ar, ar2)


		gg = Group(Dot(point=RIGHT*3+UP), Dot(point=-RIGHT*3+UP), ll, lll)
		self.add(gg.set_color(GRAY_E))
		self.play(ggg.animate.shift(UP*0.25))
		self.play(gg.animate.shift(UP))
		self.add(modxx)
		self.wait()



class Modulus2(Scene):
	
	config_instagram()

	def construct(self):
		myTemplate = TexTemplate()
		myTemplate.add_to_preamble(r"\usepackage[utopia]{mathdesign}")

		eq=Tex(r"$f(x)=|x+1|$", tex_template=myTemplate) 
		modx = Tex(r"$|x|$", tex_template=myTemplate).shift(RIGHT*3.6+UP*1).set_color(GRAY_E).scale(0.8)
		modxx = Tex(r"$|x+1|$", tex_template=myTemplate).shift(RIGHT*3.5+UP*2).set_color(GRAY_E).scale(0.8)
	
		equation = ["$(a+b)^2$", "$a^2+b^2+2ab$", "$a^2+b^2+2ab$"]

		for part in equation:
			self.add(Tex(part))
		

		ll = Line(DOWN*2, RIGHT*3+UP)
		lll = Line(DOWN*2, -RIGHT*3+UP)
		
		ggg = Group()
		for i in range(11):
			p1 = ll.point_from_proportion(i/10)
			p2 = lll.point_from_proportion(i/10)
			ar = Arrow(start=p1+[0, -0.25, 0], end=p1+[0, 0.75, 0]).set_color(GRAY_E)
			ar2 = Arrow(start=p2+[0, -0.25, 0], end=p2+[0, 0.75, 0]).set_color(GRAY_E)
			ggg.add(ar, ar2)


		gg = Group(Dot(point=RIGHT*3+UP), Dot(point=-RIGHT*3+UP), ll, lll)
		self.add(gg.set_color(GRAY_E))
		self.play(ggg.animate.shift(UP*0.25))
		self.play(gg.animate.shift(UP))
		self.add(modxx)
		self.wait()





class Modulus3(Scene):
	config_instagram()
	
	def construct(self):
		name = putAxes()
		
		myTemplate = TexTemplate()
		myTemplate.add_to_preamble(r"\usepackage[utopia]{mathdesign}")
		eq=Tex(r"$f(x)=|x+1|$", tex_template=myTemplate).set_color(BLACK).to_edge(UP)
		
		liner = Line(ORIGIN, [3, 3, 0])
		linel = Line(ORIGIN, [-3, 3, 0])
		og = VGroup(liner, linel).shift(DOWN*2).set_color(BLACK)

		eq1=Tex(r"$|x|$", tex_template=myTemplate).set_color(BLACK).next_to(liner, RIGHT)
		ng = og.copy().set_color(BLACK)
		ag = VGroup().set_color(BLACK)
		for i in range(11):
			p1 = liner.point_from_proportion(i/10)
			p2 = linel.point_from_proportion(i/10)
			ag.add(Arrow(start=p1+[-0.25, 0, 0], end=p1+[-0.8, 0, 0]).set_color(BLACK))
			ag.add(Arrow(start=p2+[0.25, 0, 0], end=p2+[-0.8, 0, 0]).set_color(BLACK))
		self.add(eq)
		self.add(name)
		eq2=Tex(r"$|x+1|$", tex_template=myTemplate).set_color(BLACK).next_to(ng, UR)
		self.play(Create(og))
		self.play(Flash(eq1))
		self.play(ag.animate.shift(LEFT*0.25))
		self.play(ng.animate.shift(LEFT*0.25))
		self.play(Flash(eq2))
		self.wait()
		


class Modulus4(Scene):
	config_instagram(2400)
#	config.background_color=BLACK
#	config.frame_rate=30
#	config.transparent=True
#	config.background_opacity=0.15
	
	def construct(self):
		Tex.set_default(color=BLACK)
		Line.set_default(color=BLACK)
		Mobject.set_default(color=BLACK)
		name = putAxes()
		myTemplate = TexTemplate()
		myTemplate.add_to_preamble(r"\usepackage[utopia]{mathdesign}")
		title=Tex(r"$f(x)=|x+1|$", tex_template=myTemplate).to_edge(UP)
		eq=Tex(r"$|x|$", tex_template=myTemplate)
		eq1=Tex(r"$|x+1|$", tex_template=myTemplate)
		eq2=Tex(r"$|x-1|$", tex_template=myTemplate)
		

		graph = name.plot(
						lambda x: abs(x),
						x_range=(-3, 3, 0.01),
						)

		self.add(title)
		self.play(Create(name))
		self.wait()
		self.add(eq.move_to([3, 1.2, 0]).scale(0.5))
		self.play(Create(graph), Flash(eq, color=BLACK, flash_radius=0.5))
		self.wait()
		self.play(ApplyPointwiseFunction(
				lambda x: x+[-1, 0, 0], graph.copy()
		), graph.animate.set_color(GRAY_C))

		self.add(eq1.move_to([-4, 1.2, 0]).scale(0.5))
		self.play(Flash(eq1, color=BLACK, flash_radius=0.5))
		self.wait()
		self.play(ApplyPointwiseFunction(
				lambda x: x+[1, 0, 0], graph.copy().set_color(BLACK)
		))
		self.add(eq2.move_to([4, 1.2, 0]).scale(0.5))
		self.play(Flash(eq2, color=BLACK, flash_radius=0.5))
		self.wait()
















