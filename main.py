import tkinter as tk


def selcut():
    cutselection = "you chose " + str(cut.get())
    cutlabel.config(text=cutselection)


def selcolor():
    colorselection = "you chose " + str(color.get())
    colorlabel.config(text=colorselection)


def selclarity():
    clarityselection = "you chose " + str(clarity.get())
    claritylabel.config(text=clarityselection)


root = tk.Tk()
cut = tk.StringVar()
color = tk.StringVar()
clarity = tk.StringVar()

root.geometry("500x500")
root.title("Diamonds value calculating app")

textbox0 = tk.Text(root, height=1, font=('Arial', 18))
textbox0.pack()

cutlabel = tk.Label(root)
cutlabel.pack()
colorlabel = tk.Label(root)
colorlabel.pack()
claritylabel = tk.Label(root)
claritylabel.pack()

radioframe = tk.Frame(root)
radioframe.columnconfigure(0, weight=1)
radioframe.columnconfigure(1, weight=1)
radioframe.columnconfigure(2, weight=1)

cut_ideal = tk.Radiobutton(radioframe, text='Ideal', value='Ideal', variable=cut, padx=10, pady=10, command=selcut)
cut_ideal.grid(row=0, column=0, sticky=tk.W)
cut_premium = tk.Radiobutton(radioframe, text='Premium', value='Premium', variable=cut, padx=10, pady=10,
                             command=selcut)
cut_premium.grid(row=1, column=0, sticky=tk.W)
cut_very_good = tk.Radiobutton(radioframe, text='Very Good', value='Very_good', variable=cut, padx=10, pady=10,
                               command=selcut)
cut_very_good.grid(row=2, column=0, sticky=tk.W)
cut_good = tk.Radiobutton(radioframe, text='Good', value='Good', variable=cut, padx=10, pady=10, command=selcut)
cut_good.grid(row=3, column=0, sticky=tk.W)
cut_fair = tk.Radiobutton(radioframe, text='Fair', value='Fair', variable=cut, padx=10, pady=10, command=selcut)
cut_fair.grid(row=4, column=0, sticky=tk.W)

color_D = tk.Radiobutton(radioframe, text='D', value='D', variable=color, padx=10, pady=10, command=selcolor)
color_D.grid(row=0, column=1, sticky=tk.W)
color_E = tk.Radiobutton(radioframe, text='E', value='E', variable=color, padx=10, pady=10, command=selcolor)
color_E.grid(row=1, column=1, sticky=tk.W)
color_F = tk.Radiobutton(radioframe, text='F', value='F', variable=color, padx=10, pady=10, command=selcolor)
color_F.grid(row=2, column=1, sticky=tk.W)
color_G = tk.Radiobutton(radioframe, text='G', value='G', variable=color, padx=10, pady=10, command=selcolor)
color_G.grid(row=3, column=1, sticky=tk.W)
color_H = tk.Radiobutton(radioframe, text='H', value='H', variable=color, padx=10, pady=10, command=selcolor)
color_H.grid(row=4, column=1, sticky=tk.W)
color_I = tk.Radiobutton(radioframe, text='I', value='I', variable=color, padx=10, pady=10, command=selcolor)
color_I.grid(row=5, column=1, sticky=tk.W)

clarity_ = tk.Radiobutton(radioframe, text='SI1', value='SI1', variable=clarity, padx=10, pady=10, command=selclarity)
clarity_.grid(row=0, column=2, sticky=tk.W)
clarity_ = tk.Radiobutton(radioframe, text='SI2', value='SI2', variable=clarity, padx=10, pady=10, command=selclarity)
clarity_.grid(row=1, column=2, sticky=tk.W)
clarity_ = tk.Radiobutton(radioframe, text='VS1', value='VS1', variable=clarity, padx=10, pady=10, command=selclarity)
clarity_.grid(row=2, column=2, sticky=tk.W)
clarity_ = tk.Radiobutton(radioframe, text='VS2', value='VS2', variable=clarity, padx=10, pady=10, command=selclarity)
clarity_.grid(row=3, column=2, sticky=tk.W)
clarity_ = tk.Radiobutton(radioframe, text='VVS1', value='VVS1', variable=clarity, padx=10, pady=10,
                          command=selclarity)
clarity_.grid(row=4, column=2, sticky=tk.W)
clarity_ = tk.Radiobutton(radioframe, text='VVS2', value='VVS2', variable=clarity, padx=10, pady=10,
                          command=selclarity)
clarity_.grid(row=5, column=2, sticky=tk.W)
clarity_ = tk.Radiobutton(radioframe, text='I1', value='I1', variable=clarity, padx=10, pady=10, command=selclarity)
clarity_.grid(row=6, column=2, sticky=tk.W)
clarity_ = tk.Radiobutton(radioframe, text='IF', value='IF', variable=clarity, padx=10, pady=10, command=selclarity)
clarity_.grid(row=7, column=2, sticky=tk.W)

radioframe.pack()

sendbutton = tk.Button(root, text='wyceń', padx=10)
sendbutton.pack()

root.mainloop()
