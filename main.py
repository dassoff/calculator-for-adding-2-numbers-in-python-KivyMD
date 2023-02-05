from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class MainScreen(Screen):
    def calculate(self, value):
        try:
            self.ids.output.text = str(float(self.ids.input_1.text) + float(self.ids.input_2.text))
        except ValueError:
            self.ids.output.text = "Invalid input"

class SumApp(MDApp):
    def build(self):
        self.screen_manager = Builder.load_file("ui.kv")
        return self.screen_manager

if __name__ == "__main__":
    SumApp().run()
