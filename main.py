import tkinter as tk
import json
import requests
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.webhook_url = ''
        self.root = tk.Tk()
        self.cut_value = tk.StringVar(value='x')
        self.color_value = tk.StringVar(value='x')
        self.clarity_value = tk.StringVar(value='x')
        self.x_value = tk.DoubleVar()
        self.y_value = tk.DoubleVar()
        self.z_value = tk.DoubleVar()
        self.carat_value = tk.DoubleVar()
        self.depth_value = tk.DoubleVar()
        self.table_value = tk.DoubleVar()
        self.price_value = tk.IntVar()
        self.root.geometry("500x500")
        self.root.title("Diamonds value calculating app")
        self.radio_frame = tk.Frame(self.root)
        self.radio_frame.rowconfigure(0, weight=1)
        self.radio_frame.columnconfigure(0, weight=1)
        self.cut_label = tk.Label(self.radio_frame,text='cut')
        self.cut_label.grid(row =0, column=0, sticky = tk.W)
        self.color_label = tk.Label(self.root,text='color')
        self.color_label.grid(row=1,column=0,sticky=tk.W)
        self.clarity_label = tk.Label(self.root,text='clarity')
        self.clarity_label.grid(row=2,column=0,sticky=tk.W)
        self.cut_ideal = tk.Radiobutton(self.radio_frame, text='Ideal', value='Ideal', variable=self.cut_value, padx=10,
                                        pady=10, command=self.selection_cut)
        self.cut_ideal.grid(row=0, column=1, sticky=tk.W)
        self.cut_premium = tk.Radiobutton(self.radio_frame, text='Premium', value='Premium', variable=self.cut_value, padx=10,
                                          pady=10, command=self.selection_cut)
        self.cut_premium.grid(row=0, column=2, sticky=tk.W)
        self.cut_very_good = tk.Radiobutton(self.radio_frame, text='Very Good', value='Very_good', variable=self.cut_value,
                                            padx=10, pady=10, command=self.selection_cut)
        self.cut_very_good.grid(row=0, column=3, sticky=tk.W)
        self.cut_good = tk.Radiobutton(self.radio_frame, text='Good', value='Good', variable=self.cut_value, padx=10, pady=10,
                                       command=self.selection_cut)
        self.cut_good.grid(row=0, column=4, sticky=tk.W)
        self.cut_fair = tk.Radiobutton(self.radio_frame, text='Fair', value='Fair', variable=self.cut_value, padx=10, pady=10,
                                       command=self.selection_cut)
        self.cut_fair.grid(row=0, column=5, sticky=tk.W)
        self.color_D = tk.Radiobutton(self.radio_frame, text='D', value='D', variable=self.color_value, padx=10, pady=10,
                                      command=self.selection_color)
        self.color_D.grid(row=1, column=1, sticky=tk.W)
        self.color_E = tk.Radiobutton(self.radio_frame, text='E', value='E', variable=self.color_value, padx=10, pady=10,
                                      command=self.selection_color)
        self.color_E.grid(row=1, column=2, sticky=tk.W)
        self.color_F = tk.Radiobutton(self.radio_frame, text='F', value='F', variable=self.color_value, padx=10, pady=10,
                                      command=self.selection_color)
        self.color_F.grid(row=1, column=3, sticky=tk.W)
        self.color_G = tk.Radiobutton(self.radio_frame, text='G', value='G', variable=self.color_value, padx=10, pady=10,
                                      command=self.selection_color)
        self.color_G.grid(row=1, column=4, sticky=tk.W)
        self.color_H = tk.Radiobutton(self.radio_frame, text='H', value='H', variable=self.color_value, padx=10, pady=10,
                                      command=self.selection_color)
        self.color_H.grid(row=1, column=5, sticky=tk.W)
        self.color_I = tk.Radiobutton(self.radio_frame, text='I', value='I', variable=self.color_value, padx=10, pady=10,
                                      command=self.selection_color)
        self.color_I.grid(row=1, column=6, sticky=tk.W)
        self.clarity_SI1 = tk.Radiobutton(self.radio_frame, text='SI1', value='SI1', variable=self.clarity_value, padx=10,
                                          pady=10, command=self.selection_clarity)
        self.clarity_SI1.grid(row=2, column=1, sticky=tk.W)
        self.clarity_SI2 = tk.Radiobutton(self.radio_frame, text='SI2', value='SI2', variable=self.clarity_value, padx=10,
                                          pady=10, command=self.selection_clarity)
        self.clarity_SI2.grid(row=2, column=2, sticky=tk.W)
        self.clarity_VS1 = tk.Radiobutton(self.radio_frame, text='VS1', value='VS1', variable=self.clarity_value, padx=10,
                                          pady=10, command=self.selection_clarity)
        self.clarity_VS1.grid(row=2, column=3, sticky=tk.W)
        self.clarity_VS2 = tk.Radiobutton(self.radio_frame, text='VS2', value='VS2', variable=self.clarity_value, padx=10,
                                          pady=10, command=self.selection_clarity)
        self.clarity_VS2.grid(row=2, column=4, sticky=tk.W)
        self.clarity_VVS1 = tk.Radiobutton(self.radio_frame, text='VVS1', value='VVS1', variable=self.clarity_value, padx=10,
                                           pady=10, command=self.selection_clarity)
        self.clarity_VVS1.grid(row=2, column=5, sticky=tk.W)
        self.clarity_VVS2 = tk.Radiobutton(self.radio_frame, text='VVS2', value='VVS2', variable=self.clarity_value, padx=10,
                                           pady=10, command=self.selection_clarity)
        self.clarity_VVS2.grid(row=2, column=6, sticky=tk.W)
        self.clarity_I1 = tk.Radiobutton(self.radio_frame, text='I1', value='I1', variable=self.clarity_value, padx=10,
                                         pady=10, command=self.selection_clarity)
        self.clarity_I1.grid(row=2, column=7, sticky=tk.W)
        self.clarity_IF = tk.Radiobutton(self.radio_frame, text='IF', value='IF', variable=self.clarity_value, padx=10,
                                         pady=10, command=self.selection_clarity)
        self.clarity_IF.grid(row=2, column=8, sticky=tk.W)
        self.radio_frame.pack()

        self.entry_carat = tk.Entry(self.root, insertwidth=200)
        self.send_button = tk.Button(self.root, text='price', padx=10,command=self.send)
        self.send_button.pack()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def selection_cut(self):
        cut_selection = "you chose " + str(self.cut_value.get())
        self.cut_value=cut_selection

    def selection_color(self):
        color_selection = "you chose " + str(self.color_value.get())
        self.color_value=color_selection

    def selection_clarity(self):
        clarity_selection = "you chose " + str(self.clarity_value.get())
        self.clarity_value=clarity_selection

    def send(self):
        data = {'carat': self.carat_value,
                'cut': self.cut_value,
                'color': self.color_value,
                'clarity': self.clarity_value,
                'depth': self.depth_value,
                'table' : self.table_value,
                'price' : self.price_value,
                'x': self.x_value,
                'y': self.y_value,
                'z':self.z_value}
        r = requests.post(self.webhook_url,data=json.dump(data),headers={'Content-Type': 'application/json'})


    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="do you want to quit the program?"):
            self.root.destroy()


MyGUI()
