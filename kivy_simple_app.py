from kivy.app import App

#scatter is awesome! you can drag-and-drop and resize and stuff!
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class ScatterTextWidget(BoxLayout):
    pass

#extends kivy's App class to create your app 
class TutorialApp(App):
    #build method creates the ROOT WIDGET and returns it
    #any other interface has to be a sub-widget of this one
    def build(self):
        return ScatterTextWidget()

if __name__ == '__main__':
    #use parens to create an instance of the class!
    TutorialApp().run()
