# notepad program with tkinter
import tkinter as tk


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Notepad")
        self.root.resizable(True, True)
        self.root.geometry("400x500")

        self.upper_frame = tk.Frame(self.root)
        self.upper_frame.pack(anchor='nw')

        # menu bar 
        self.mb = tk.Menubutton(self.upper_frame, text='File', relief='raised', activebackground='#ADD8E6', bd=0)
        self.mb.menu = tk.Menu(self.mb, tearoff=0)
        self.mb['menu'] = self.mb.menu

        self.mb.menu.add_command(label='save', command=lambda: self.save_file())
        self.mb.pack()
        
        # lower frame
        self.lower_frame = tk.Frame(self.root)
        self.lower_frame.pack()

        # text input



        self.root.mainloop()


    # save txt file to pc
    def save_file(self):
        print('HELLO WORLD')







App()
