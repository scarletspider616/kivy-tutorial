from kivy.app import App 
from kivy.uix.scatter import Scatter
from kivy.uix.boxlayout import BoxLayout

# to import in kivy: #:import keyword module_name
# aka: #:import random random
import random

class ScatterTextWidget(BoxLayout):
	def change_label_colour(self, *args):
		colour = [random.random() for i in range(3)] + [1] # the one makes it opaque
		label = self.ids['my_label']
		label.color = colour

	def change_input_to_upper(self, *args):
		text_input = self.ids['my_textinput']
		label = self.ids['my_label']
		label.text = text_input.text.upper()

class TutorialApp(App):
	def build(self):
		return ScatterTextWidget()

		

if __name__ == "__main__":
	TutorialApp().run()