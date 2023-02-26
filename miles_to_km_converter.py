
from tkinter import *

def miles_to_km():
    miles = miles_input.get()
    km = float(miles) * 1.609
    km_con_label.config(text=f"{km}")
    print(type(miles))

window = Tk()
window.title("Miles to Km converter")
window.config(padx=10, pady=20)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

calculate_button = Button(text= "Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_con_label = Label(text="0")
km_con_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

window.mainloop()
