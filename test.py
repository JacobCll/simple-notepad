import tkinter as tk
class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Notepad")
        self.root.resizable(True, True)
        self.root.geometry("400x500")
        self.root.config(bg='#CBC3E3')

        self.l1 = tk.Label(self.root, bg='#FFCCCB', text='HELLO')
        self.l1.grid(column=0, row=0)

        self.l2 = tk.Label(self.root, bg='#FFCCCB', text='HI')
        self.l2.grid(column=1, row=1)

        self.l3 = tk.Label(self.root, bg='#FFCCCB', text='TEST')
        self.l3.grid(column=2, row=2)

        self.l4 = tk.Label(self.root, bg='#FFCCCB', text='GRID')
        self.l4.grid(column=3, row=3)

        self.l5 = tk.Label(self.root, bg='#FFCCCB', text='YES')
        self.l5.grid(column=3, row=0)

        self.mb = tk.Menubutton(self.root, text='File', relief='flat', activebackground='#ADD8E6', bd=0)
        self.mb.menu = tk.Menu(self.mb, tearoff=0)
        self.mb['menu'] = self.mb.menu

        self.mb.menu.add_command(label='save', command=lambda: self.save_file())
        self.mb.grid(column=10, row=0,sticky=tk.NW)

        self.root.mainloop()





App()