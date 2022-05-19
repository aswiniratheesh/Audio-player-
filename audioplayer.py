from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivymd.uix.picker import MDTimePicker, MDDatePicker
from kivy.utils import platform
from kivy.core.window import Window

if platform not in ["android", "ios"]:
    Window.size = (320, 640)


class Demoproject(ScreenManager):
    pass

    sound = SoundLoader.load('audio.mp3')

    def play_sound(self):
        self.sound.play()

    def play_stop(self):
        self.sound.stop()


class Main(MDApp):
    def build(self):
        Builder.load_file("my.kv")
        return Demoproject()


if __name__ == "__main__":
    Main().run()

