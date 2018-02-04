from kivy.app import App 
from kivy.uix.scatter import Scatter
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ListProperty

from kivy.graphics.vertex_instructions import (Rectangle,
											   Ellipse,
											   Line)

from kivy.graphics.context_instructions import Color

# to import in kivy: #:import keyword module_name
# aka: #:import random random
import random

class ScatterTextWidget(BoxLayout):
	text_colour = ListProperty([1, 0, 0, 1])

	def __init__(self, **kwargs):
		super(ScatterTextWidget, self).__init__(**kwargs)

		with self.canvas.before:
			Color(0, 1, 0, 1)
			Rectangle(pos = (0, 100), size = (300, 100))
			Ellipse(pos = (0, 400), size = (300, 100))
			Line(points=[0, 0, 500, 600, 400, 300],
				close = True,
				width = 3)

	def change_label_colour(self, *args):
		colour = [random.random() for i in range(3)] + [1] # the one makes it opaque
		self.text_colour = colour;

	def change_input_to_upper(self, *args):
		text_input = self.ids['my_textinput']
		label = self.ids['my_label']
		label.text = text_input.text.upper()

	def on_text_colour(self, *args):
		print("We can do things this way too!")

class TutorialApp(App):
	def build(self):
		return ScatterTextWidget()

		

if __name__ == "__main__":
	TutorialApp().run()