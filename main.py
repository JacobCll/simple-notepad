# notepad program with tkinter
import tkinter as tk
import tkinter.font as TkFont
import tkinter.scrolledtext as scrolledtext


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Notepad")
        self.root.resizable(True, True)
        self.root.geometry("400x500")
        self.root.config(bg='#ffffff')
        #upper frame ------------------------------------------------------
        self.upper_frame = tk.Frame(self.root)
        self.upper_frame.grid(column=0, row=0, sticky=tk.W)

        # first button
        # tk.Menu is always inside tk.Menubutton
        self.mb1 = tk.Menubutton(self.upper_frame, text='File', relief='flat', background='#ffffff',activebackground='#cce8ff', bd=0)
        self.mb1.menu = tk.Menu(self.mb1, tearoff=0)
        self.mb1['menu'] = self.mb1.menu

        self.mb1.menu.add_command(label='Save', command=lambda: self.save_file())
        self.mb1.grid(column=0, row=0, sticky=tk.W)

        #second button
        self.mb2 = tk.Menubutton(self.upper_frame, text='Edit', relief='flat', background='#ffffff',activebackground='#cce8ff', bd=0)
        #tk.Menu is always inside a tk.Menubutton
        self.mb2.menu = tk.Menu(self.mb2, tearoff=0)
        self.mb2['menu'] = self.mb2.menu

        self.mb2.menu.add_command(label='Undo', command=lambda: self.save_file())
        self.mb2.grid(column=1, row=0, sticky=tk.W)

        #third button
        self.mb3 = tk.Menubutton(self.upper_frame, text='Format', relief='flat', background='#ffffff',activebackground='#cce8ff', bd=0)
        #tk.Menu is always inside a tk.Menubutton
        self.mb3.menu = tk.Menu(self.mb3, tearoff=0)
        self.mb3['menu'] = self.mb3.menu

        self.mb3.menu.add_command(label='Word Wrap', command=lambda: self.save_file())
        self.mb3.grid(column=3, row=0, sticky=tk.W)


        # lower frame -------------------------------------------------
        self.lower_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.lower_frame.grid(column=0,row=1,sticky=tk.W+tk.E+tk.S+tk.N)

        # to stretch the widgets 
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        self.lower_frame.columnconfigure(0, weight=1)
        self.lower_frame.rowconfigure(0, weight=1)


        #for horizontal scrollbar   
        self.scrollx = tk.Scrollbar(self.lower_frame, orient='horizontal')
        self.scrollx.grid(column=0, row=1, sticky=tk.W+tk.E+tk.S+tk.N)

        #verticasl scrollbar
        self.scrolly = tk.Scrollbar(self.lower_frame, orient='vertical')
        self.scrolly.grid(column=1, row=0, sticky=tk.W+tk.E+tk.S+tk.N)

        # scrolled text widget
        self.text = tk.Text(self.lower_frame, autoseparators=True, undo=True, bd=1, wrap=tk.NONE, highlightbackground='#f2f2f2',font=TkFont.Font(family='Consolas', size=11), xscrollcommand=self.scrollx.set, yscrollcommand=self.scrolly.set)
        self.text.grid(column=0, row=0, sticky=tk.W+tk.E+tk.S+tk.N)

        # # empty space beside scrollx
        # self.empt = tk.Label(self.lower_frame, text='  ', bg='#f0f0f0')
        # self.empt.grid(column=1, row=1)



        self.root.mainloop()


    # save txt file to pc
    def save_file(self):
        
        print('HELLO WORLD')







App()
