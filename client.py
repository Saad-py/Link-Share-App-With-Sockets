import kivy
import socket
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.app import App

class mylay(GridLayout):
    def __init__(self, **kwargs):
        super(mylay, self).__init__(**kwargs)

        self.cols = 3

        self.rec = Button(text="recieve")
        self.rec.bind(on_press=lambda x: self.kol())
        self.add_widget(self.rec)

        self.bte = Label(text="Message from admin")
        self.add_widget(self.bte)

    def kol(self):
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socket.gethostname(), 1234))


        while True:
            full_msg = ''
            while True:
                msg = s.recv(8)
                if len(msg) <= 0:
                    break
                full_msg += msg.decode("utf-8")

            if len(full_msg) > 0:
                print(full_msg)

        self.lol = str(full_msg)
        self.bte.text = self.lol



class client(App):
    def build(self):
        a = mylay()
        return a

client().run()