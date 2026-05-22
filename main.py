import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import threading
import os

from vosk import Model, KaldiRecognizer
import pyaudio

kivy.require('2.1.0')

class VoiceBotLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(VoiceBotLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15

        self.add_widget(Label(text="Rahmat's Offline Voice Bot", font_size='24sp', bold=True, size_hint_y=None, height=50))
        
        self.status_label = Label(text="Status: Model Load Ho Raha Hai...", font_size='16sp', size_hint_y=None, height=40)
        self.add_widget(self.status_label)

        self.output_text = TextInput(hint_text="Aap jo bolenge, woh bina internet yahan text banega...", readonly=True, font_size='18sp', multiline=True)
        self.add_widget(self.output_text)

        self.mic_button = Button(text="🎙️ Bolne Ke Liye Click Karein", font_size='20sp', background_color=(0.2, 0.6, 1, 1), size_hint_y=None, height=60)
        self.mic_button.bind(on_press=self.start_listening_thread)
        self.add_widget(self.mic_button)

        threading.Thread(target=self.load_offline_model).start()

    def load_offline_model(self):
        try:
            self.model = Model(lang="en-us")
            self.rec = KaldiRecognizer(self.model, 16000)
            self.status_label.text = "Status: Offline Mode Ready!"
        except Exception as e:
            self.status_label.text = f"Model Load Error: {str(e)}"

    def start_listening_thread(self, instance):
        self.status_label.text = "Status: Sun raha hoon (No Internet)..."
        threading.Thread(target=self.listen_offline).start()

    def listen_offline(self):
        try:
            p = pyaudio.PyAudio()
            stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
            stream.start_stream()

            for _ in range(0, int(16000 / 8000 * 5)):
                data = stream.read(8000, exception_on_overflow=False)
                if self.rec.AcceptWaveform(data):
                    break
            
            import json
            result = json.loads(self.rec.Result())
            text = result.get("text", "")
            
            if text:
                self.output_text.text = f"Aapne kaha: {text}"
                self.status_label.text = "Status: Kaam mukammal!"
            else:
                self.output_text.text = "Aawaz samajh nahi aayi, dobara koshish karein."
                self.status_label.text = "Status: Ready"

            stream.stop_stream()
            stream.close()
            p.terminate()
        except Exception as e:
            self.output_text.text = f"Mic Error: {str(e)}"
            self.status_label.text = "Status: Error"

class VoiceBotApp(App):
    def build(self):
        return VoiceBotLayout()

if __name__ == '__main__':
    VoiceBotApp().run()
  
