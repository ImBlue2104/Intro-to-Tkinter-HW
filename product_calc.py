from tkinter import Tk, Label, Entry, END, Button

# create window
root = Tk()
root.title("Getting Started with Widgets!")
root.geometry("400x300")

# Add the labels and entries
Label(root, text="This GUI application returns the product of the two numbers given by the user!", 
      fg='white', bg='black').pack()

Label(root, text="Enter First Number:", fg='black', bg='#d0efff').pack()
Num_1 = Entry(root, fg="black", bg='grey', width=50)
Num_1.pack()

Label(root, text="Enter Second Number:", fg='black', bg='#d0efff').pack()
Num_2 = Entry(root, fg="black", bg='grey', width=50)
Num_2.pack()

#function to multiply and display
def calc():
    n1 = int(Num_1.get())
    n2 = int(Num_2.get())
    product = n1*n2
    Label(root, text=f"Product: {product}", 
      fg='white', bg='black').pack()


Button(text="Submit",fg='white',bg="black", command = calc).pack()

root.mainloop()
