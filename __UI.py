from tkinter import Tk, W, E, BooleanVar,IntVar, Text,Scrollbar,END,messagebox
from tkinter.ttk import Frame,Label, Button,Entry, Checkbutton
import string, random

class UI(Frame):

    def __init__(self):
        self.tk = Tk()
        super().__init__()
        self.initUI()

    def initUI(self):
        self.window=self.master
        self.window.title('Random Password Generator')
        self.window.geometry("325x350")
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)
        self.rowconfigure(5, pad=3)
        self.rowconfigure(6, pad=3)
        self.rowconfigure(7, pad=3)
        self.Label1=Label(self.window, text="Password length").grid(row=0, column=0, pady=5)
        self.Label2=Label(self.window, text="How many password would you like?").grid(row=1, column=0, padx=10,pady=5)
        self.length=Entry(self.window,width=5)
        self.length.grid(row=0,column=1, sticky=W, padx=5)
        self.much=Entry(self.window,width=5)
        self.much.grid(row=1,column=1, sticky=W,padx=5)
        self.numbers=IntVar(self.window)
        self.numbers.set(0)
        self.Label3=Label(self.window, text="Include numbers").grid(row=2, column=0, pady=5)
        self.b1=Checkbutton(self.window, variable=self.numbers,offvalue=0, onvalue=1).grid(row=2,column=1)
        self.spechar=IntVar()
        self.spechar.set(0)
        self.Label4=Label(self.window, text="Include special characters").grid(row=3, column=0, pady=5)
        self.ckb1=Checkbutton(self.window, variable=self.spechar).grid(row=3,column=1)
        self.bt1= Button(
            self.window, text='Generate', command= self.generate).grid(row=4,columnspan=2,padx=10,sticky=W+E)
        self.text=Text(self.window, height=10, width=38)
        self.text.grid(row=5, columnspan=2, padx=10, pady=5)
        self.scroll=Scrollbar(self.window,orient="vertical", width=20,command=self.text.yview)
        self.scroll.grid(row=5, column=1,padx=5,pady=5,sticky='nse')
        self.text['yscrollcommand'] = self.scroll.set


    def generate(self):
        try:
            length=int(self.length.get())
            much=int(self.much.get())
        except:
            messagebox.showerror("ERROR", message="Please, give a number!!!")

            
        if length>36:
            messagebox.showerror("ERROR",message="Please, give a smaller than 36!!!")
            return
        if length<0 or much<0:
            messagebox.showerror("ERROR", message="Please, give a positive number!!!")
            return
        if much>20:
            messagebox.showerror("ERROR", message="Please, give a smaller then 20!!!")
            return

        password=[]
        if self.numbers.get()==0 and self.spechar.get()==0:
            for s in range(0,much):
                password1=""
                for i in range(0,length):  
                    password1 = (password1+ random.choice(string.ascii_letters))
                password.append(password1)
            
        elif self.numbers.get()==1 and self.spechar.get()==0:
            for s in range(0,much):
                password1=""
                for i in range(0,length): 
                    password1 = (password1+ random.choice(string.ascii_letters+string.digits))
                password.append(password1)
        elif self.numbers.get()==1 and self.spechar.get()==1:
            for s in range(0,much):
                password1=""
                for i in range(0,length): 
                    password1 = (password1+ random.choice(string.ascii_letters+string.digits+string.punctuation))
                password.append(password1)
        elif self.numbers.get()==0 and self.spechar.get()==1:
            for s in range(0,much):
                password1=""
                for i in range(0,length): 
                    password1 = (password1+ random.choice(string.ascii_letters+string.punctuation))
                password.append(password1)
        self.text.delete(1.0, END)
        for i in password:
            self.text.insert('2.0', i+'\n')
        return

    def runUI(self):
        self.mainloop()