from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label



class BugTester(FloatLayout):
    def __init__(self):
        super().__init__()
        for i in range(1,6):
            temp  = GamePiece(5, "Red")
            temp.pos = (i*100,i*200)
            self.add_widget(temp)


class BugTestingApp(App):
    def build(self):
        return BugTester()

class GamePiece(ToggleButton):

    def __init__(self, number, color, **kwargs):
        self.number = number
        self.player_color = color
        #self.background_normal = "5.png"
        super(GamePiece, self).__init__()


if __name__ == '__main__':
    BugTestingApp().run()