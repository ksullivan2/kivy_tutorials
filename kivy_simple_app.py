from kivy.app import App

#scatter is awesome! you can drag-and-drop and resize and stuff!
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout



#extends kivy's App class to create your app 
class TutorialApp(App):
    #build method creates the ROOT WIDGET and returns it
    #any other interface has to be a sub-widget of this one
    def build(self):
        b = BoxLayout(orientation="vertical")
        t = TextInput(font_size=150,
                      #size hint is a number that tells it how big to be proportionally
                      size_hint_y=None,
                      height = 200,
                      text = "default")
        
        f = FloatLayout()
        s = Scatter()
        l = Label(text="Hello!",
                      font_size=150)

        t.bind(text=l.setter("text"))

        
        #order matters: text needs to be first to be at top
        b.add_widget(t)
        b.add_widget(f)
        
        f.add_widget(s)
        #because label is child of scatter widget, it has the scatter behavior
        s.add_widget(l)

       
        return b

def some_function(*args):
    print("text changed")

if __name__ == '__main__':
    #use parens to create an instance of the class!
    TutorialApp().run()
