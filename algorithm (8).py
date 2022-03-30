import tkinter


def main():
    root = tk()
    gui = Window(root)
    gui.root.mainroot()
    return none


class Window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("650x490")
        self.root.title("Notepad")


        self.textspace=Text(self.root)
        self.textspace.grid(row=0, column=0)
        button(self.root , text="save",command=self.savefile).grid(row=0,column=1)
        button(self.root , text="open",command=self.savefile).grid(row=0,column=2)

    def SaveFile(self):
        savegui=tk()
        savegui.geometry("560x50")
        filecontents=self.textspace.get(0.0,END)





        return none





    pass
while True:
    main()