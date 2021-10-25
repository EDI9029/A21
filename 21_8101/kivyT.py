from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
  
class Kivy_UI(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.rows = 2
        self.add_widget(Label(text="UserName"))
        self.username = TextInput(multiline=False, font_name="C://Users/ROCAF/Desktop/DroidSansFallbackFull.ttf")
        self.add_widget(self.username)

class TestApp(App):
    def build(self):
        return Kivy_UI()
  
TestApp().run()