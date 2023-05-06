# fancy-cli
This is a library for creating a function selection menu, or line selection in a command interface shell, controlled by the left/right, enter, esc keys


ButtonsRow - row of buttons driven left to right enter (esc - exit)
        example of the usage:
        ![alt text](https://i.ibb.co/Pgp61gs/2023-05-06-20-57-29.gif "usage1")

        an even simpler example:
        ``` python
        functions = [
                (print, "\nfirst command"),
                (print, "\nsecond command!")
            ]

        selector = ButtonsRow(["[one]", "[two]", "[three]", "[four]", "[five]", "[six]"], cursor_swap=True,
                                  functions_args_list=functions,
                                  text_after=f"{Fore.LIGHTBLACK_EX}|{Fore.RED} controls: ←, →, enter, esc")
        selector.run()
        ```

SelectValue - select a line from the proposed
        ``` python 
        selectvalue = SelectValue("Какую функцию выполнить? ", ["Первая функция", "Действие 2", "Действие 3"], cursor_swap=True)
        selectvalue.run()
        value = selectvalue.get_value()
        print(f"Вы выбрали: {value}")
        time.sleep(1)
        ```
