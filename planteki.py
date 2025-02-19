from kivy.core.text import LabelBase
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivymd.uix.button import MDIconButton

Window.size = (440, 856)


class Planteki(MDApp):

    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("landing.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file("dashboard.kv"))
        return screen_manager

if __name__ == "__main__":


    Planteki().run()
