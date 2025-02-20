from kivy.core.text import LabelBase
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivymd.uix.button import MDIconButton
from kivymd.uix.button import MDButtonText
from kivymd.uix.button import MDFabButton

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup



Window.size = (440, 856)


class Planteki(MDApp):

    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("landing.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file("dashboard.kv"))
        screen_manager.add_widget(Builder.load_file("wiki.kv"))
        screen_manager.add_widget(Builder.load_file("sensor.kv"))
        screen_manager.add_widget(Builder.load_file("plantsmenu.kv"))
        screen_manager.add_widget(Builder.load_file("plantmain.kv"))
        screen_manager.add_widget(Builder.load_file("forgotpass.kv"))
        screen_manager.add_widget(Builder.load_file("verification.kv"))
        screen_manager.add_widget(Builder.load_file("setnewpass.kv"))
        return screen_manager

if __name__ == "__main__":


    Planteki().run()
