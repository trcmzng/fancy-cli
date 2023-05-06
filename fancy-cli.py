import time
import keyboard
from colorama import Fore, Back, init, Style
init(autoreset=True)
import os

class ButtonsRow:
    def __init__(self, button_names=["Test button"], cursor_swap=False, colors_active=Back.CYAN + Fore.LIGHTWHITE_EX,
                 colors_activated=Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX, colors_inactive=Back.BLACK + Fore.CYAN,
                 functions_args_list=[], text_after='', pre_text=[]):
        self.version = 2

        self.min = 1                # minimal id of selected button
        self.now = self.min         # default selected button
        self.buttons = button_names # button names from init to list

        self.pre_text = pre_text    # опционально - текст выбранной функции (если есть - текст меню обновляется после os.system(cls), что может выглядеть как пропуск кадров в меню)
                                    # если нет, то всё работает быстро, обновляя меню через \r

        self.max = len(self.buttons)
        self.text_after = text_after             # optional - text after buttons (for example: tooltip)
        self.CURSOR_SWAP = cursor_swap           # опционально - будет ли курсор переходить на другую сторону
        self.colors_active = colors_active       # опционально - цвет выбранной кнопки
        self.colors_inactive = colors_inactive   # опционально - цвет обычной кнопки
        self.colors_activated = colors_activated # опционально - цвет активированной кнопки
        self.functions_args_list = functions_args_list    # список функций для кнопок
                                                          # сюда передавать список из кортежей в котором первое значение это функция а второй это аргументы
                                                          # пример:

                                                          # functions = [
                                                          #         (print, "\nfirst command"),
                                                          #         (print, "\nsecond command!"),
                                                          #     ]

        self.safe_clear = 1  # dont change
        self.safe_stop = 1   # dont change
        self.render_board(self.min, color=self.colors_active)



    def run(self):
        self.on = True
        keyboard.on_press(self.on_press_lambda)
        keyboard.wait('esc')
        self.safe_stop = 0

    def on_press_lambda(self, event):
        return self.on_press(event)

    def on_press(self, event):
        if self.on:
            button = event.name
            if button == "left":
                if not self.safe_clear:
                    os.system('cls')
                self.safe_clear = 1
                self.change(-1)
            elif button == "right":
                if not self.safe_clear:
                    os.system('cls')
                self.safe_clear = 1
                self.change(1)
            elif button == "esc":
                self.on = False
                self.delete()
            elif button == "enter":
                if not self.safe_clear:
                    os.system('cls')
                self.safe_clear = 1
                result = self.get_now()
                self.run_function(self.get_now())

    def get_now(self):
        return self.now

    def change(self, value):
        self.now = self.now + value
        if not self.CURSOR_SWAP:
            if self.now < self.min:
                self.now = self.min
            if self.now > self.max:
                self.now = self.max
        else:
            if self.now < self.min:
                self.now = self.max
            if self.now > self.max:
                self.now = self.min

        self.render_board(self.get_now(), color=self.colors_active)

    def render_board(self, id, color):
        if self.safe_stop:
            if len(self.pre_text) > 0:
                os.system("cls")
            board = f"{self.colors_inactive}{' '.join(self.buttons).replace(self.buttons[id - 1], color + self.buttons[id - 1] + self.colors_inactive)}"
            print(board + " " + self.text_after, end="\r")
            try:
                print(f"{self.pre_text[id - 1]}")

            except: pass
        else:

            keyboard.unhook_all()
            del self

    def run_function(self, id):
        os.system('cls')
        self.render_board(id, self.colors_activated)
        try:
            function_args = self.functions_args_list[id - 1]
            function = function_args[0]
            args = function_args[1:]
            function(*args)
        except IndexError: print("\nДля этой кнопки не назначена функция")
        self.safe_clear = 0

    def delete(self):
        del self

class SelectValue():
    def __init__(self, prompt, button_names=["Test button"], cursor_swap=False, colors_active=Back.CYAN + Fore.LIGHTWHITE_EX,
                 colors_activated=Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX, colors_inactive=Back.BLACK + Fore.CYAN):

        self.min = 1  #dont change
        self.now = self.min
        self.buttons = button_names
        self.max = len(self.buttons)
        self.safe_stop = 1
        self.prompt = prompt

        self.CURSOR_SWAP = cursor_swap
        self.colors_active = colors_active
        self.colors_inactive = colors_inactive
        self.colors_activated = colors_activated
        self.result = None

        self.render_board(self.min, color=self.colors_active)

    def run(self):
        self.on = True
        keyboard.on_press(self.on_press_lambda)
        keyboard.wait('enter')

        self.safe_stop = 0

    def on_press_lambda(self, event):
        return self.on_press(event)

    def on_press(self, event):
        button = event.name
        if button == "left":
            self.safe_clear = 1
            self.change(-1)
        elif button == "right":
            self.safe_clear = 1
            self.change(1)
        elif button == "enter":
            self.safe_clear = 1
            self.on = False
            self.run_function(self.get_now())

    def get_now(self):
        return self.now

    def change(self, value):
        self.now = self.now + value
        if not self.CURSOR_SWAP:
            if self.now < self.min:
                self.now = self.min
            if self.now > self.max:
                self.now = self.max
        else:
            if self.now < self.min:
                self.now = self.max
            if self.now > self.max:
                self.now = self.min

        self.render_board(self.get_now(), color=self.colors_active)

    def render_board(self, id, color):
        if self.safe_stop:
            board = f"{self.prompt}{self.colors_inactive}{' '.join(self.buttons).replace(self.buttons[id - 1], color + self.buttons[id - 1] + self.colors_inactive)}"
            print(board, end="\r")
        else:
            del self
    def get_value(self):

        return self.result

    def run_function(self, id):
        selected = self.buttons[id - 1]
        self.result = selected
        self.safe_clear = 0
        print("\n")
