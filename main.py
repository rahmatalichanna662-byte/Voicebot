import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import speech_recognition as sr
import threading

kivy.require('2.1.0')

class VoiceBotLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(VoiceBotLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15

        # Title Label
        self.title_label = Label(
            text="Rahmat's Voice Bot", 
            font_size='24sp', 
            bold=True,
            size_hint_y=None,
            height=50
        )
        self.add_widget(self.title_label)

        # Status Label
        self.status_label = Label(
            text="Status: Ready", 
            font_size='16sp',
            size_hint_y=None,
            height=40
        )
        self.add_widget(self.status_label)

        # Output Text Area
        self.output_text = TextInput(
            hint_text="Aap jo bolenge, woh yahan text ban kar aayega...", 
            readonly=True, 
            font_size='18sp',
            multiline=True
        )
        self.add_widget(self.output_text)

        # Mic Button
        self.mic_button = Button(
            text="🎙️ Bolne Ke Liye Click Karein", 
            font_size='20sp',
            background_color=(0.2, 0.6, 1, 1),
            size_hint_y=None,
            height=60
        )
        self.mic_button.bind(on_press=self.start_listening_thread)
        self.add_widget(self.mic_button)

    def start_listening_thread(self, instance):
        # UI ko freeze hone se bachane ke liye background thread
        threading.Thread(target=self.listen_voice).start()

    def listen_voice(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.status_label.text = "Status: Aap ki aawaz sun raha hoon..."
            r.adjust_for_ambient_noise(source, duration=1)
            try:
                audio = r.listen(source, timeout=5)
                self.status_label.text = "Status: Aawaz ko samajh raha hoon..."
                
                # Urdu aur English dono support ke liye
                text = r.recognize_google(audio, language='ur-PK')
                self.output_text.text = f"Aapne kaha: {text}"
                self.status_label.text = "Status: Kaam mukammal!"
            except sr.WaitTimeoutError:
                self.status_label.text = "Status: Koi aawaz nahi aayi."
            except sr.UnknownValueError:
                self.output_text.text = "Sorry, aawaz saaf nahi thi. Dobara koshish karein."
                self.status_label.text = "Status: Error"
            except Exception as e:
                self.output_text.text = f"Error: {str(e)}"
                self.status_label.text = "Status: Error"

class VoiceBotApp(App):
    def build(self):
        return VoiceBotLayout()

if __name__ == '__main__':
    VoiceBotApp().run()
