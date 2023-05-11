# notepad program with tkinter
import tkinter as tk
import tkinter.font as TkFont


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Notepad")
        self.root.resizable(True, True)
        self.root.geometry("400x500")
        #testing color 
        self.root.config(bg='#CBC3E3')

        #upper frame ------------------------------------------------------
        self.upper_frame = tk.Frame(self.root)
        self.upper_frame.grid(column=0, row=0, sticky=tk.W)

        # first button
        self.mb1 = tk.Menubutton(self.upper_frame, text='File', relief='flat', activebackground='#ADD8E6', bd=0)
        #tk.Menu is always inside a tk.Menubutton
        self.mb1.menu = tk.Menu(self.mb1, tearoff=0)
        self.mb1['menu'] = self.mb1.menu

        self.mb1.menu.add_command(label='Save', command=lambda: self.save_file())
        self.mb1.grid(column=0, row=0, sticky=tk.W)

        #second button
        self.mb2 = tk.Menubutton(self.upper_frame, text='Edit', relief='flat', activebackground='#ADD8E6', bd=0)
        #tk.Menu is always inside a tk.Menubutton
        self.mb2.menu = tk.Menu(self.mb2, tearoff=0)
        self.mb2['menu'] = self.mb2.menu

        self.mb2.menu.add_command(label='Undo', command=lambda: self.save_file())
        self.mb2.grid(column=1, row=0, sticky=tk.W)

        #third button
        self.mb3 = tk.Menubutton(self.upper_frame, text='Format', relief='flat', activebackground='#ADD8E6', bd=0)
        #tk.Menu is always inside a tk.Menubutton
        self.mb3.menu = tk.Menu(self.mb3, tearoff=0)
        self.mb3['menu'] = self.mb3.menu

        self.mb3.menu.add_command(label='Word Wrap', command=lambda: self.save_file())
        self.mb3.grid(column=3, row=0, sticky=tk.W)




        # lower frame -------------------------------------------------
        self.lower_frame = tk.Frame(self.root, bg='#FFCCCB')
        self.lower_frame.grid()

        # text widget
        self.text_widget = tk.Text(self.lower_frame, autoseparators=True, undo=True,wrap=tk.WORD, font=TkFont.Font(family='Lucida Console', size=10))
        self.text_widget.grid()
        self.text_widget.columnconfigure(0, weight=1)
        self.text_widget.rowconfigure(0, weight=1)


        self.root.mainloop()


    # save txt file to pc
    def save_file(self):
        
        print('HELLO WORLD')







App()
