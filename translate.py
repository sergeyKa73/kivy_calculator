import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.core.window import Window

Window.size = (350, 300)

import requests

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'MDIwZTQ3MGMtMDZlZi00YTJhLWI0YzMtMjc0N2RlMTYwNDBhOjAxZTRiZmI1NjdhZTQ2MDE4MjE2YTYxZDI3OTZjOTEy'

headers_auth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)


class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call  grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # Set columns
        self.cols = 1

        # Add Input Box
        self.name = TextInput(hint_text='Enter word: ', cursor_color= 'black',  multiline=False)
        self.add_widget((self.name))

        self.translate = Label(text='Перевод')
        self.add_widget((self.translate))

        # Create a Submit Button
        self.sumbit = Button(text='Translate', font_size=14)
        # Bind the button
        self.sumbit.bind(on_press=self.press)
        self.add_widget(self.sumbit)

    def press(self, instanse):
        name = self.name.text
        if auth.status_code == 200:
            token = auth.text

            word = name
            if word:
                headers_translate = {
                    'Authorization': 'Bearer ' + token
                }
                params = {
                    'text': word,
                    'srcLang': 1033,
                    'dstLang': 1049
                }
                r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
                res = r.json()
                try:
                    words = res['Translation']['Translation']
                    self.translate.text = words
                except:
                    self.translate.text = 'no translation found '
            else:
                self.translate.text = 'Error!'


        # Clear the input boxes



class TranslateApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    TranslateApp().run()
