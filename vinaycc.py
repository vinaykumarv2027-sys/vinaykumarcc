"""A simple mobile-style app built with Kivy."""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class HomeScreen(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(orientation="vertical", padding=24, spacing=16, **kwargs)
		self.add_widget(Label(text="Welcome", font_size="32sp"))

		self.name_input = TextInput(
			hint_text="Enter your name", multiline=False, font_size="20sp"
		)
		self.add_widget(self.name_input)

		self.message = Label(text="Tap below to say hello.", font_size="20sp")
		self.add_widget(self.message)

		button = Button(text="Say hello", font_size="20sp", size_hint_y=None, height=56)
		button.bind(on_press=self.say_hello)
		self.add_widget(button)

	def say_hello(self, _button):
		name = self.name_input.text.strip() or "there"
		self.message.text = f"Hello, {name}!"


class WelcomeApp(App):
	def build(self):
		self.title = "Welcome App"
		return HomeScreen()


if __name__ == "__main__":
	WelcomeApp().run()
