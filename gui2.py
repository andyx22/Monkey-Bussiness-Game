import tkinter as tk
from company import Company

company = Company("Monkey Business")

def buy_employee():
    company.buy("employee", 1)
def buy_truck():
    company.buy("truck", 1)
def buy_store():
    company.buy("store", 1)

root = tk.Tk()
root.title("Monkee Business")
root.geometry("500x500")
root.resizable(False, False)

bgfile = tk.PhotoImage(file="E:/Python Projects/tkintergame/bg1.png")
background_label = tk.Label(root, image=bgfile)
background_label.place(x=0, y=0)

label = tk.Label(root, text="Monkee Business", font=("Ms Serif", 30, "bold"))
label.pack(padx=10, pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)

btn1 = tk.Button(buttonframe, text="Banana\n🍌100", font=("Arial", 20), height=3, width=10, command=buy_employee)
btn1.grid(row=1, column=0, sticky=tk.E)

btn2 = tk.Button(buttonframe, text="Banana Tree\n🍌5000", font=("Arial", 20), height=3, width=10, command=buy_truck)
btn2.grid(row=2, column=0, sticky=tk.E)

btn3 = tk.Button(buttonframe, text="Banana Bank\n🍌100000", font=("Arial", 20), height=3, width=10, command=buy_store)
btn3.grid(row=3, column=0, sticky=tk.E)

buttonframe.place(x=325, y=75)

moneyarea = tk.Canvas(root, bg="green", height=358, width=300)
moneyarea.place(x=12, y=75)

worthlabel = tk.Label(moneyarea, font=("Arial", 20))
worthlabel.place(x=1, y=1)

genlabel = tk.Label(moneyarea, font=("Arial", 10))
genlabel.place(x=1, y=39)

barrelfile = tk.PhotoImage(file="E:/Python Projects/tkintergame/box.png")
def barrelupdate():
    if company.worth >= 500:
        barrel1 = tk.Label(moneyarea, image=barrelfile)
        barrel1.place(x=1, y=250)
    if company.worth >= 5000:
        barrel2 = tk.Label(moneyarea, image=barrelfile)
        barrel2.place(x=175, y=250)
    if company.worth >= 50000:
        barrel3 = tk.Label(moneyarea, image=barrelfile)
        barrel3.place(x=1, y=145)
    if company.worth >= 10000:
        barrel4 = tk.Label(moneyarea, image=barrelfile)
        barrel4.place(x=120, y=145)
    if company.worth >= 1000000:
        barrel5 = tk.Label(moneyarea, image=barrelfile)
        barrel5.place(x=175, y=35)

def update():
    worthlabel["text"] = f"🍌{company.worth}"
    genlabel["text"] = f"🍌{company.gen_per_sec} per second"
    company.gen()
    barrelupdate()
    root.after(500, update)
    
update()
root.mainloop()