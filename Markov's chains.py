import tkinter as tk
from tkinter import ttk
from tkinter import *
import json
import os
import random
from tkinter.scrolledtext import ScrolledText
if(not os.path.exists(os.getcwd()+"\\data_chain.json") ):
    with open("data_chain.json","w") as f:
        json.dump({"first":{},"another":{}},f)
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Articles creartor")
        self.geometry("600x700")
        self.resizable(width = False, height = False)
        with open("data_chain.json","r") as f:
            self.data = json.load(f)
        self.create_elements()

    def create_elements(self):
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('TButton',padding=(30,10,30,10),background = "#4E4E56",focusthickness=3, focuscolor='none',relief="flat",font = "Arial 12 bold",foreground = "#f7f3e9")
        s.map("TButton",background = [("pressed","#4E4E56"),("active","#2a2a2e")])

        self.frame = tk.Frame(self,bg="#4E4E56")
        self.frame.pack(expand = 1,fill = BOTH)


        self.input = tk.Text(self.frame,background = "#f7f3e9",width = 50,height = 10)
        self.input.pack(side = TOP)

        self.makeDataButton = ttk.Button(self.frame,text = "Upload",command = self.make_data_func)
        self.makeDataButton.pack(side = TOP)
        self.cleanInput = ttk.Button(self.frame,text = "Clean",command = self.clean_text_func)
        self.cleanInput.pack(side = TOP)
        
        self.createTextButton = ttk.Button(self.frame,text = "Create text",command = self.create_text_func)
        self.createTextButton.pack(side = BOTTOM)
        self.textLabel = ScrolledText(self.frame,font = "Arial 12 bold")
        self.textLabel.pack(side = BOTTOM)
    def clean_text_func(self):
        self.input.delete("1.0","end")
    def create_text_func(self):
        
        self.firstWords = self.data["first"]
        self.firstWord = list(self.firstWords.keys())[random.randint(0,len(self.firstWords.keys())-1)]
        
        self.secondWord = self.firstWords[self.firstWord][random.randint(0,len(self.firstWords[self.firstWord])-1)]
        self.text = self.firstWord +" "+ self.secondWord
        self.nowWord = self.secondWord
        while self.nowWord in self.data["another"].keys():
            self.nowWord = self.data["another"][self.nowWord]
            self.nowWord = self.nowWord[random.randint(0,len(self.nowWord)-1)]
            self.text+=" "+self.nowWord
            print(self.text)
        self.textLabel.delete("1.0","end")
        self.textLabel.insert("1.0",self.text)



    def make_data_func(self):
        self.text = self.input.get("1.0","end").split(" ")

        for i in range(len(self.text)-1):
            if(i == 0):
                if(not self.text[i] in self.data["first"].keys() or self.text[i] in self.data["first"].keys() and not self.text[i+1] in self.data["first"][self.text[i]]):
                    if(self.text[i] in self.data["first"].keys()):
                        self.data["first"][self.text[i]].append(self.text[i+1])
                    else:
                        self.data["first"][self.text[i]] = [self.text[i+1]]
            else:
                if(not self.text[i] in self.data["another"].keys() or self.text[i] in self.data["another"].keys() and not self.text[i+1] in self.data["another"][self.text[i]] ):
                    if(self.text[i] in self.data["another"].keys()):
                            self.data["another"][self.text[i]].append(self.text[i+1])
                    else:
                        self.data["another"][self.text[i]] = [self.text[i+1]]
        
        with open("data_chain.json","w") as f:
            json.dump(self.data,f)
        print(self.data)
        self.clean_text_func()
app = App()
app.mainloop()