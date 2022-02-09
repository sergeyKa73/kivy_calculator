from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button
from kivy.config import Config

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "300")
Config.set("graphics", "height", "300")

choice = ['X', '0']
switch = 0


class TTTApp(App):

    def tic_tac_toe(self, instance):
        global switch

        instance.disabled = True
        instance.text = choice[switch]
        if not switch:
            switch = 1
        else:
            switch = 0

        coordinate = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # X
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Y
            (0, 4, 8), (2, 4, 6),
        )

        vector = (
            [self.button[x].text for x in (0, 1, 2)],
            [self.button[x].text for x in (3, 4, 5)],
            [self.button[x].text for x in (6, 7, 8)],

            [self.button[y].text for y in (0, 3, 6)],
            [self.button[y].text for y in (1, 4, 7)],
            [self.button[y].text for y in (2, 5, 8)],

            [self.button[d].text for d in (0, 4, 8)],
            [self.button[d].text for d in (2, 4, 6)],

        )

        win = False
        color = [0, 1, 0, 1]

        for index in range(8):
            if vector[index].count('X') == 3 or vector[index].count('0') == 3:
                win = True
                for i in coordinate[index]:
                    self.button[i].color = color
                break

        if win:
            for index in range(9):
                self.button[index].disabled = True

    def restart(self, instance):
        global switch;
        switch = 0
        for index in range(9):
            self.button[index].color = [0, 0, 0, 1]
            self.button[index].text = ''
            self.button[index].disabled = False

    def build(self):
        self.title = 'Крестики-нолики'

        root = BoxLayout(orientation="vertical", padding=5)

        gl = GridLayout(cols=3)
        self.button = [0 for _ in range(9)]
        for index in range(9):
            self.button[index] = Button(
                color=[0, 0, 0, 1],
                font_size=24,
                disabled=False,
                on_press=self.tic_tac_toe
            )
            gl.add_widget(self.button[index])
        root.add_widget(gl)

        root.add_widget(Button(
            text='Restart',
            size_hint=[1, .1],
            on_press=self.restart
        ))

        return root


if __name__ == '__main__':
    TTTApp().run()
