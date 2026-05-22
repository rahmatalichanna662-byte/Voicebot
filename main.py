import os
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.utils import platform

class VoiceBotUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=20, **kwargs)
        
        self.status_label = Label(
            text="Voice Bot Status: Ready (Offline Native Mode)", 
            font_size='18sp',
            size_hint_y=0.2
        )
        self.add_widget(self.status_label)
        
        self.result_label = Label(
            text="Aap jo bolenge woh yahan dikhega...", 
            font_size='20sp', 
            halign='center',
            valign='middle'
        )
        self.result_label.bind(size=self.result_label.setter('text_size'))
        self.add_widget(self.result_label)
        
        self.listen_btn = Button(
            text="Bolna Shuru Karein", 
            font_size='18sp',
            size_hint_y=0.2,
            background_color=(0.1, 0.6, 0.9, 1)
        )
        self.listen_btn.bind(on_press=self.toggle_listening)
        self.add_widget(self.listen_btn)
        
        self.is_listening = False

    def toggle_listening(self, instance):
        if not self.is_listening:
            self.is_listening = True
            self.listen_btn.text = "Sunte hain... (Stop karne ke liye dabayein)"
            self.listen_btn.background_color = (0.9, 0.2, 0.2, 1)
            self.status_label.text = "Status: Listening through Android Native Mic..."
        else:
            self.is_listening = False
            self.listen_btn.text = "Bolna Shuru Karein"
            self.listen_btn.background_color = (0.1, 0.6, 0.9, 1)
            self.status_label.text = "Status: Stopped"

class VoiceBotApp(App):
    def build(self):
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.RECORD_AUDIO, Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
        return VoiceBotUI()

if __name__ == '__main__':
    VoiceBotApp().run()
