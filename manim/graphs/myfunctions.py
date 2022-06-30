# myfunctions.py

from manim import *

def config_instagram(w=800):
	config.frame_width = 10.1
	config.frame_height = 10.1
	config.pixel_width = w
	config.pixel_height = w
	config.background_color="#FDEBD0"

def putAxes():
	name=Axes(
		x_range=[-5, 5, 1],
		y_range=[-1, 5, 1],
		x_length=10,
		y_length=6,
		tips=False,
		).set_color(GRAY_D)
	return name



def setDefaults():
	Text.set_default(color=BLACK)
	Circle.set_default(color=BLACK)
	Line.set_default(color=BLACK)



if __name__ == '__main__':
	config_instagram()
	putAxes()
