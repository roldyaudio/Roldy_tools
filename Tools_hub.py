from tkinter import *

# App window
root = Tk()
root.geometry("300x300")

# Tittle
root.title("Tools Hub")
# root.resizable(False, False)

# my_button Function
def my_click():
    my_label = Label(root, text=my_entry.get())
    my_label.pack()

# # Label creation
my_label1 = Label(root, text="Hello World")
# my_label2 = Label(root, text="Roldan Robles")

# # Label placement on screen
# my_label1.grid(row=0, column=0)
# my_label2.grid(row=1, column=1)

# Entry creation
my_entry = Entry(root, borderwidth=3,)
my_entry.pack()
my_entry.insert(0, "Enter your path",)

# Button creation
my_button = Button(root, text="Click me", padx=10, pady=10, command=my_click, bg="darkgray", )
# Button placement
my_button.pack()

# Show App
root.mainloop()
