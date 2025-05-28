import keyboard
import os

class HyperKey:
    def __init__(self):
        self.shortcuts = {
            "ctrl+alt+s": self.turn_off_pc,
            "ctrl+alt+c": self.open_calculator,
            "ctrl+alt+b": self.open_browser
        }
        self.register_shortcuts()

    def register_shortcuts(self):
        for keys, action in self.shortcuts.items():
            keyboard.add_hotkey(keys, action)

    def turn_off_pc(self):
        os.system('shutdown /s /t 1')

    def open_calculator(self):
        os.system("calc")

    def open_browser(self):
        os.system("start chrome")

    def run(self):
        print("⌨️ Escuchando atajos de teclado... (Presiona ESC para salir)")
        keyboard.wait("esc")

if __name__ == "__main__":
    hyperkey = HyperKey()
    hyperkey.run()
