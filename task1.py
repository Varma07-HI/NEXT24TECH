import tkinter as tk
from tkinter import ttk, messagebox

def SubmitRegistrationForm():
    firstname = firstname_entry.get()
    lastname = lastname_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    gender = gender_combobox.get()
    phonenum = phonenum_entry.get()
    address = address_entry.get()

    if not firstname or not lastname or not phonenum or not email or not age or not gender:
        messagebox.showerror("Error", "Ensure that all the fields are filled")
        return
    
    if len(phonenum) != 10:
        messagebox.showerror("Error", "Phone number should be 10 digits")
        return

    try:
        age = int(age)
    except ValueError:
        messagebox.showerror("Error", "Age should be a valid number")
        return
    
    try:
        phonenum = int(phonenum)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid Phone Number")
        return

    messagebox.showinfo("Success", "Registration Completed\nFirst Name: {}\nLast Name: {}\nEmail: {}\nAge: {}\nGender: {}\nPhone Number: {}\nAddress: {}".format(firstname, lastname, email, age, gender, phonenum, address))

window = tk.Tk()
window.title("Simple Registration Form")

window.geometry("500x500")
window.configure(bg="lightblue")

firstname_label = tk.Label(window, text="First Name:", bg="lightblue", font=("Courier", 15, "bold italic"))
firstname_label.place(x=50, y=50)

firstname_entry = tk.Entry(window, font=("Courier", 15, "italic"))
firstname_entry.place(x=200, y=50)

lastname_label = tk.Label(window, text="Last Name:", bg="lightblue", font=("Courier", 15, "bold italic"))
lastname_label.place(x=50, y=100)

lastname_entry = tk.Entry(window, font=("Courier", 15, "italic"))
lastname_entry.place(x=200, y=100)

email_label = tk.Label(window, text="Email:", bg="lightblue", font=("Courier", 15, "bold italic"))
email_label.place(x=50, y=150)

email_entry = tk.Entry(window, font=("Courier", 15, "italic"))
email_entry.place(x=200, y=150)

age_label = tk.Label(window, text="Age:", bg="lightblue", font=("Courier", 15, "bold italic"))
age_label.place(x=50, y=200)

age_entry = tk.Entry(window, font=("Courier", 15, "italic"))
age_entry.place(x=200, y=200)

gender_label = tk.Label(window, text="Gender:", bg="lightblue", font=("Courier", 15, "bold italic"))
gender_label.place(x=50, y=250)

gender_combobox = ttk.Combobox(window, values=["Male", "Female", "Other"], font=("Courier", 15, "italic"))
gender_combobox.place(x=200, y=250)

phonenum_label = tk.Label(window, text="Phone Number:", bg="lightblue", font=("Courier", 14, "bold italic"))
phonenum_label.place(x=50, y=300)

phonenum_entry = tk.Entry(window, font=("Courier", 15, "italic"))
phonenum_entry.place(x=200, y=300)

address_label = tk.Label(window, text="Address:", bg="lightblue", font=("Courier", 15, "bold italic"))
address_label.place(x=50, y=350)

address_entry = tk.Entry(window, font=("Courier", 15, "italic"))
address_entry.place(x=200, y=350)

submit_button = tk.Button(window, text="Submit", command=SubmitRegistrationForm, fg="white", bg="black", font=("Courier", 20, "bold italic"))
submit_button.place(x=200, y=400)

window.mainloop()
