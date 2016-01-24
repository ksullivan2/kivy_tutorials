from kivy.app import App

from kivy.uix.label import Label
#scatter is awesome! you can drag-and-drop and resize and stuff!
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout



#extends kivy's App class to create your app 
class TutorialApp(App):
    #build method creates the ROOT WIDGET
    #any other interface has to be a sub-widget of this one
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text="Hello!",
                      font_size=150)
        #makes children widgets
        f.add_widget(s)
        s.add_widget(l)
        return f

if __name__ == '__main__':
    #use parens to create an instance of the class!
    TutorialApp().run()
