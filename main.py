from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window
from kivy.config import Config

Window.rotation = 0
Window.fullscreen = 1
Config.set('graphics', 'resizable', '1')

class calculatorApp(App):
    def build(self):
        self.boxy = RelativeLayout()
        self.laby  = Label(text = "hello", color = (1, 0,0,1),font_size = 40)
        self.boxy.add_widget(self.laby)

        return self.boxy

calculatorApp().run()