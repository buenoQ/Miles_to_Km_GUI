from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=300, height=200)
window.config(padx=60, pady=60)

user_Entry = Entry(width=15)
user_Entry.grid(column=1, row=0)

miles = Label(text="Miles", font=('Arial', 15))
miles.grid(column=2, row=0)

is_equal_to = Label(text="is equal to", font=('Arial', 15))
is_equal_to.grid(column=0, row=1, padx=0)

km_number = Label(text="0", font=('Arial', 15))
km_number.grid(column=1, row=1)

km = Label(text="Km", font=('Arial', 15))
km.grid(column=2, row=1)


def miles_to_km():
    kilometers = int(user_Entry.get()) * 1.609
    km_number.config(text=f"{kilometers}")


calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=3)

window.mainloop()
