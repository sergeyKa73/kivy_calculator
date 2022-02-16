from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window

Window.size = (250, 200)
Window.clearcolor = (255/255, 186/255, 3/255, 1)
Window.title = 'Converter'

class ConverterApp(App):

    def __init__(self):
        super().__init__()
        self.label = Label(text='Конвертер')
        self.miles = Label(text='Мили')
        self.metres = Label(text='Метры')
        self.santim = Label(text='Сантиметры')
        self.input_data = TextInput(hint_text='Введите значение (км)', multiline=False)
        self.input_data.bind(text=self.on_text)

    def on_text(self, *args):
        data = self.input_data.text
        if data.isnumeric():
            self.miles.text = 'Мили: ' + str(float(data) * 0.62)
            self.metres.text = 'Метры: ' + str(float(data) * 1000)
            self.santim.text = 'Сантиметры: ' + str(float(data) * 100000)
        else:
            self.input_data.text = ''




    def build(self):
        bl = BoxLayout(orientation='vertical')
        bl.add_widget(self.label)
        bl.add_widget(self.input_data)
        bl.add_widget(self.miles)
        bl.add_widget(self.metres)
        bl.add_widget(self.santim)

        return bl

if __name__ == '__main__':
    ConverterApp().run()
