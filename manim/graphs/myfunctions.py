# myfunctions.py

from manim import *

def config_instagram():
	config.frame_width = 10.1
	config.frame_height = 10.1
	config.pixel_width = 2400
	config.pixel_height = 2400
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



if __name__ == '__main__':
	config_instagram()
	putAxes()
