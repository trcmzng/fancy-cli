# fancy-cli
This is a library for creating a function selection menu, or line selection in a command interface shell, controlled by the left/right, enter, esc keys


ButtonsRow - row of buttons driven left to right enter (esc - exit)
example of the usage:
```
functions = [
        (print, "\nfirst command"),
        (print, "\nsecond command!")
    ]

    selector = ButtonsRow(["[one]", "[two]", "[three]", "[four]", "[five]", "[six]"], cursor_swap=True,
                          functions_args_list=functions,
                          text_after=f"{Fore.LIGHTBLACK_EX}|{Fore.RED} controls: ←, →, enter, esc")
    selector.run()
```
