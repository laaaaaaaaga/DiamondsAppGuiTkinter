import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.cut = tk.StringVar()
        self.color = tk.StringVar()
        self.clarity = tk.StringVar()
        self.root.geometry("500x500")
        self.root.title("Diamonds value calculating app")
        self.textbox0 = tk.Text(self.root, height=1, font=('Arial', 18))
        self.textbox0.pack()
        self.cutlabel = tk.Label(self.root)
        self.cutlabel.pack()
        self.colorlabel = tk.Label(self.root)
        self.colorlabel.pack()
        self.claritylabel = tk.Label(self.root)
        self.claritylabel.pack()
        self.radioframe = tk.Frame(self.root)
        self.radioframe.columnconfigure(0, weight=1)
        self.radioframe.columnconfigure(1, weight=1)
        self.radioframe.columnconfigure(2, weight=1)
        self.cut_ideal = tk.Radiobutton(self.radioframe, text='Ideal', value='Ideal', variable=self.cut, padx=10, pady=10,command=self.selcut)
        self.cut_ideal.grid(row=0, column=0, sticky=tk.W)
        self.cut_premium = tk.Radiobutton(self.radioframe, text='Premium', value='Premium', variable=self.cut, padx=10, pady=10,command=self.selcut)
        self.cut_premium.grid(row=1, column=0, sticky=tk.W)
        self.cut_very_good = tk.Radiobutton(self.radioframe, text='Very Good', value='Very_good', variable=self.cut, padx=10,pady=10,command=self.selcut)
        self.cut_very_good.grid(row=2, column=0, sticky=tk.W)
        self.cut_good = tk.Radiobutton(self.radioframe, text='Good', value='Good', variable=self.cut, padx=10, pady=10,command=self.selcut)
        self.cut_good.grid(row=3, column=0, sticky=tk.W)
        self.cut_fair = tk.Radiobutton(self.radioframe, text='Fair', value='Fair', variable=self.cut, padx=10, pady=10,command=self.selcut)
        self.cut_fair.grid(row=4, column=0, sticky=tk.W)
        self.color_D = tk.Radiobutton(self.radioframe, text='D', value='D', variable=self.color, padx=10, pady=10,command=self.selcolor)
        self.color_D.grid(row=0, column=1, sticky=tk.W)
        self.color_E = tk.Radiobutton(self.radioframe, text='E', value='E', variable=self.color, padx=10, pady=10,command=self.selcolor)
        self.color_E.grid(row=1, column=1, sticky=tk.W)
        self.color_F = tk.Radiobutton(self.radioframe, text='F', value='F', variable=self.color, padx=10, pady=10,command=self.selcolor)
        self.color_F.grid(row=2, column=1, sticky=tk.W)
        self.color_G = tk.Radiobutton(self.radioframe, text='G', value='G', variable=self.color, padx=10, pady=10,command=self.selcolor)
        self.color_G.grid(row=3, column=1, sticky=tk.W)
        self.color_H = tk.Radiobutton(self.radioframe, text='H', value='H', variable=self.color, padx=10, pady=10,command=self.selcolor)
        self.color_H.grid(row=4, column=1, sticky=tk.W)
        self.color_I = tk.Radiobutton(self.radioframe, text='I', value='I', variable=self.color, padx=10, pady=10,command=self.selcolor)
        self.color_I.grid(row=5, column=1, sticky=tk.W)
        self.clarity_ = tk.Radiobutton(self.radioframe, text='SI1', value='SI1', variable=self.clarity, padx=10, pady=10,command=self.selclarity)
        self.clarity_.grid(row=0, column=2, sticky=tk.W)
        self.clarity_ = tk.Radiobutton(self.radioframe, text='SI2', value='SI2', variable=self.clarity, padx=10, pady=10,command=self.selclarity)
        self.clarity_.grid(row=1, column=2, sticky=tk.W)
        self.clarity_ = tk.Radiobutton(self.radioframe, text='VS1', value='VS1', variable=self.clarity, padx=10, pady=10,command=self.selclarity)
        self.clarity_.grid(row=2, column=2, sticky=tk.W)
        self.clarity_ = tk.Radiobutton(self.radioframe, text='VS2', value='VS2', variable=self.clarity, padx=10, pady=10,command=self.selclarity)
        self.clarity_.grid(row=3, column=2, sticky=tk.W)
        self.clarity_ = tk.Radiobutton(self.radioframe, text='VVS1', value='VVS1', variable=self.clarity, padx=10, pady=10, command=self.selclarity)
        self.clarity_.grid(row=4, column=2, sticky=tk.W)
        self.clarity_ = tk.Radiobutton(self.radioframe, text='VVS2', value='VVS2', variable=self.clarity, padx=10, pady=10,command=self.selclarity)
        self.clarity_.grid(row=5, column=2, sticky=tk.W)
        self.clarity_ = tk.Radiobutton(self.radioframe, text='I1', value='I1', variable=self.clarity, padx=10, pady=10,command=self.selclarity)
        self.clarity_.grid(row=6, column=2, sticky=tk.W)
        self.clarity_ = tk.Radiobutton(self.radioframe, text='IF', value='IF', variable=self.clarity, padx=10, pady=10,command=self.selclarity)
        self.clarity_.grid(row=7, column=2, sticky=tk.W)
        self.radioframe.pack()
        self.sendbutton = tk.Button(self.root, text='wyceń', padx=10)
        self.sendbutton.pack()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()


    def selcut(self):
        cutselection = "you chose " + str(self.cut.get())
        self.cutlabel.config(text=cutselection)

    def selcolor(self):
        colorselection = "you chose " + str(self.color.get())
        self.colorlabel.config(text=colorselection)

    def selclarity(self):
        clarityselection = "you chose " + str(self.clarity.get())
        self.claritylabel.config(text=clarityselection)

    def on_closing(self):
        if messagebox.askyesno(title="Quit?",message="do you want to quit the program?"):
            self.root.destroy()

MyGUI()