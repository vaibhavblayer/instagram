from manim import *


class Solution(Scene):
	def construct(self):

		for i in range(-6, 7):
			for j in range(-3, 4):
				self.add(Dot(radius=0.02).shift(LEFT*i + UP*j))




		path= Arc(radius=2, start_angle=-PI/2, angle=PI*1.5)
		self.add(path)

		charge = Dot(radius=0.05, point=[0, -2, 0])
		

		velocity=Arrow(charge.get_center(), path.get_center())

		self.add(charge, velocity)

		label=MathTex(r"\theta")
		self.add(label)
		#label.add_updater(lambda x:x.set_x(charge.get_center()))



		self.play(MoveAlongPath(charge, path), run_time=2)



class PointWithTrace(Scene):
	def construct(self):
		path = VMobject()
		dot = Dot()
		path.set_points_as_corners([dot.get_center(), dot.get_center()])

		def update_path(path):
			previous_path = path.copy()
			previous_path.add_points_as_corners([dot.get_center()])
			path.become(previous_path)

		path.add_updater(update_path)
		self.add(path, dot)
		self.play(
				Rotating(
					dot,
					radians=PI/2,
					about_point=RIGHT,
					run_time=2
				),
				Rotate(
					dot.shift(UP)
				)
			)
		self.wait()
		self.play(dot.animate.shift(RIGHT*2), run_time=5)
		self.play(dot.animate.shift(UP))
		self.play(dot.animate.shift(LEFT))
		self.wait()




class ValueTrackerExample(Scene):
            def construct(self):
                tracker = ValueTracker(0)
                label = Dot(radius=1).add_updater(lambda x : x.set_x(tracker.get_value()))
                self.add(label)
                self.add(tracker)
                tracker.add_updater(lambda mobject, dt: mobject.increment_value(dt))
                self.wait(5)

class ApplyFuncExample(Scene):
            def construct(self):
                circ = Circle().scale(1.5)
                circ_ref = circ.copy()
                circ.apply_complex_function(
                    lambda x: np.exp(x*1j)
                )
                t = ValueTracker(0)
                circ.add_updater(
                    lambda x: x.become(circ_ref.copy().apply_complex_function(
                        lambda x: np.exp(x+t.get_value()*1j)
                    )).set_color(BLUE)
                )
                self.add(circ_ref)
                self.play(TransformFromCopy(circ_ref, circ))
                self.play(t.animate.set_value(TAU*2), run_time=3)
