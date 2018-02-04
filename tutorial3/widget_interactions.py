from kivy.app import App 
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class TutorialApp(App):
	def build(self):
		b = BoxLayout(orientation = 'vertical')
		f = FloatLayout()
		s = Scatter()
		l = Label(text="Sensor Hub Setup 0.Alpha",
						font_size = 75)
		t = TextInput(font_size = 75,
					  size_hint_y = None,
					  height = 95)
		t.bind(text=l.setter('text'))
		f.add_widget(s)
		s.add_widget(l)

		# this order determines orientation in box layout
		b.add_widget(t)
		b.add_widget(f)
		return b

		

if __name__ == "__main__":
	TutorialApp().run()