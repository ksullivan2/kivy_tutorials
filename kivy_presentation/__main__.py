from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout



class Marvel(BoxLayout):

    def hulk_smash(self):
        self.ids.loki.text = "SMASH"
        self.ids.loki.font_size = 100
        self.ids.loki.color = (0,1,0,1)
        self.ids.loki.bold = True


class PresentationApp(App):
    def build(self):
        return Marvel()


if __name__ == '__main__':
    PresentationApp().run()