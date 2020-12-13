import socket
import kivy
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput



class MyLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.cols = 2

        self.start = Button(text="Start Server", font_size=40)
        self.start.bind(on_press=lambda x: self.socket_start())
        self.add_widget(self.start)

        self.msg = TextInput(multiline=True)
        self.add_widget(self.msg)

        

        self.add_widget(Label(text="What the others see."))

    def socket_start(self):
        idk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        idk.bind((socket.gethostname(), 1234))
        idk.listen(5)
        print('litenin')
        textofinput = str(self.msg.text)
        while True:
            # now our endpoint knows about the OTHER endpoint.
            clientsocket, address = idk.accept()
            print(f"Connection from {address} has been established.")
            clientsocket.send(bytes('Testing', 'utf8'))
            clientsocket.send(bytes(textofinput, 'utf8'))


class Work_Messenger(App):
    def build(self):
        a = MyLayout()

        return a


if __name__ == '__main__':
    Work_Messenger().run()