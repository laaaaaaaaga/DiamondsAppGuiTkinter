import tkinter as tk

def sel():
    selection = "you chose" +str(var.get())
    label.config(text=selection)

root = tk.Tk()
var = tk.IntVar()
root.geometry("500x500")
root.title("Diamonds value calculating app")


label = tk.Label(root)
label.pack()

textbox0 = tk.Text(root, height=1, font=('Arial',18))
textbox0.pack()
radio0 = tk.Radiobutton(root,text='R0',value = 0, variable=var, padx=10,pady=10, command=sel)
radio0.pack(anchor = tk.W)
radio1 = tk.Radiobutton(root,text='R1',value = 1, variable=var, padx=10,pady=10, command=sel)
radio1.pack(anchor = tk.W)
radio2 = tk.Radiobutton(root,text='R2',value = 2, variable=var, padx=10,pady=10, command=sel)
radio2.pack(anchor = tk.W)
radio3 = tk.Radiobutton(root,text='R3',value = 3, variable=var, padx=10,pady=10, command=sel)
radio3.pack(anchor = tk.W)
radio4 = tk.Radiobutton(root,text='R4',value = 4, variable=var, padx=10,pady=10, command=sel)
radio4.pack(anchor = tk.W)

sendbutton = tk.Button(root,text='wyceń', padx=10)
sendbutton.pack()


root.mainloop()