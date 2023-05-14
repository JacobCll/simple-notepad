# Python 3
# notepad program with tkinter
import hashlib
import tkinter as tk
import tkinter.font as TkFont
from tkinter import filedialog

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Notepad')
        self.root.resizable(True, True)
        self.root.geometry("400x500")
        self.root.config(bg='#ffffff')

        #upper frame 
        self.upper_frame = tk.Frame(self.root)
        self.upper_frame.grid(column=0, row=0, sticky=tk.W)

        # tk.Menu is always inside tk.Menubutton
        # first button
        self.mb1 = tk.Menubutton(self.upper_frame, text='File', relief='flat', background='#ffffff', activebackground='#cce8ff', bd=0)
        self.mb1.menu = tk.Menu(self.mb1, tearoff=0)
        self.mb1['menu'] = self.mb1.menu

        self.mb1.menu.add_command(label='New', command=lambda: self.new_file())

        self.mb1.menu.add_command(label='Open', command=lambda: self.open_file())
        self.exists = ''
        self.mb1.menu.add_command(label='Save', command=lambda: self.save_file())
        self.mb1.menu.add_command(label='Save As', command=lambda: self.save_as())

        self.mb1.grid(column=0, row=0, sticky=tk.W)

        #second button
        self.mb2 = tk.Menubutton(self.upper_frame, text='Edit', relief='flat', background='#ffffff',activebackground='#cce8ff', bd=0)
        self.mb2.menu = tk.Menu(self.mb2, tearoff=0)
        self.mb2['menu'] = self.mb2.menu

        self.mb2.menu.add_command(label='CHECK', command=lambda: self.file_changed())
        self.mb2.grid(column=1, row=0, sticky=tk.W)

        #third button
        self.mb3 = tk.Menubutton(self.upper_frame, text='Format', relief='flat', background='#ffffff',activebackground='#cce8ff', bd=0)
        self.mb3.menu = tk.Menu(self.mb3, tearoff=0)
        self.mb3['menu'] = self.mb3.menu

        self.wrap_enabled = tk.IntVar()
        self.mb3.menu.add_checkbutton(label='Word Wrap', variable=self.wrap_enabled, command=lambda: self.word_wrap())
        self.mb3.grid(column=3, row=0, sticky=tk.W)

        # lower frame 
        self.lower_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.lower_frame.grid(column=0,row=1,sticky=tk.W+tk.E+tk.S+tk.N)

        # to stretch the widgets 
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.lower_frame.columnconfigure(0, weight=1)
        self.lower_frame.rowconfigure(0, weight=1)

        # Text widget
        self.text = tk.Text(self.lower_frame, autoseparators=True, undo=True, bd=1, wrap=tk.NONE, highlightbackground='#f2f2f2',font=TkFont.Font(family='Consolas', size=11))
        self.text.grid(column=0, row=0, sticky=tk.W+tk.E+tk.S+tk.N)

        #horizontal scrollbar   
        self.scrollx = tk.Scrollbar(self.lower_frame, orient='horizontal', command=self.text.xview)
        self.scrollx.grid(column=0, row=1, sticky=tk.W+tk.E+tk.S+tk.N)
        self.text['xscrollcommand'] = self.scrollx.set

        #vertical scrollbar
        self.scrolly = tk.Scrollbar(self.lower_frame, orient='vertical', command=self.text.yview)
        self.scrolly.grid(column=1, row=0, sticky=tk.W+tk.E+tk.S+tk.N)
        self.text['yscrollcommand'] = self.scrolly.set

        self.root.mainloop()

    ###
    # erases all 
    def new_file(self):
        self.exists = ''
        self.text.delete("1.0","end-1c")
        self.root.title('Notepad')

    # opens an existing file
    def open_file(self):
        try:
            file_path = filedialog.askopenfilename(title="Open note file", filetypes=[("Text File", "*.txt")], defaultextension=".txt")
            if file_path != self.exists:
                with open(file_path, 'r') as txt_file:
                    self.text.delete("1.0","end-1c")
                    data = txt_file.read()
                    self.text.insert('1.0', data)
                
                self.exists = file_path 
                self.tle = self.exists.split('/')[-1]
                self.root.title(f"{self.tle} - Notepad")
        except:
            return
        
    # save existing file
    def save_file(self):
        try:
            if self.file_changed() == True:
                # overwrite the original file    
                with open(self.exists, 'w') as txt_file:
                    txt_file.write(self.retrieve_input())
        except:
            self.save_as()

    def save_as(self):
        try:
            text = self.retrieve_input()
            file_path = filedialog.asksaveasfilename(title="Save note file", initialfile='notefile', filetypes=[("Text File", "*.txt")], defaultextension=".txt", confirmoverwrite=True)
            with open(file_path, 'w') as txt_file:
                txt_file.write(text)
        except:
            return 
    
    ###
    # checks if file is changed or not (True if changed)
    def file_changed(self) -> bool:
        with open(self.exists, "r") as f:
            original = hashlib.md5(f.read().encode('utf-8')).hexdigest()
            copy = hashlib.md5(self.retrieve_input().encode('utf-8')).hexdigest()
        return original != copy
    
    # enable/disable word wrap
    def word_wrap(self):
        if self.wrap_enabled.get() == 0:
            self.text.config(wrap=tk.NONE)
        else:
            self.text.config(wrap=tk.WORD)

    #takes the text in text widget
    def retrieve_input(self):
        content = self.text.get("1.0","end-1c")
        return content

App()