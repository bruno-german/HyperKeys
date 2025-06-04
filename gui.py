import tkinter as tk

class HyperKeysGui(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title("HyperKeys")

if __name__ == "__main__":
    ROOT = tk.Tk()
    ROOT.geometry("300x100")
    APP = HyperKeysGui(parent=ROOT)
    APP.mainloop()