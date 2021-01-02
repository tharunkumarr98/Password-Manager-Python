from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password_fun():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []
    #
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list = ([random.choice(letters) for _ in range(nr_letters)]) + ([random.choice(numbers) for _ in range(nr_numbers)]) + ([random.choice(symbols) for _ in range(nr_symbols)])

    random.shuffle(password_list)

    password_generated = "".join(password_list)
    password.insert(0, password_generated)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website.get()
    mail = email.get()
    pas = password.get()
    new_data = {
        web: {
            "email": mail,
            "pas": pas,
        }
    }
    old_data = {}
    if web == "" or pas == "":
        messagebox.showinfo(title="Missing Details", message="Don't leave the fields empty")
    else:
        try:
            file = open("data.json", "r")
        except FileNotFoundError as msg:
            file = open("data.json", "w")
                #loading the updated data
            old_data = new_data
            file.close()
        else:
            # read the old data
            old_data = json.load(file)
            # updating the dictionary
            old_data.update(new_data)
            file.close()
        finally:
            with open("data.json", "w") as file:
                json.dump(old_data, file, indent=4)
    website.delete(0, END)
    password.delete(0, END)
def find_password():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError as nam:
        messagebox.showinfo(title="Error", message="login details not found")
    else:
        if website.get() in data:
            mail = data[website.get()]["email"]
            pas = data[website.get()]["pas"]
            messagebox.showinfo(title="Login Details", message=f"Email: {mail}\nPassword: {pas}")
        else:
            messagebox.showinfo(title="Error", message="login details not found")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
MyPass = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=MyPass)
canvas.grid(row=0, column=1)
label_w = Label(text="Website")
label_w.grid(row=1, column=0)
label_eu = Label(text="Email/UserName")
label_eu.grid(row=2, column=0)
label_p = Label(text="Password")
label_p.grid(row=3, column=0)
website = Entry(width=21)
website.grid(row=1, column=1)
website.focus()
email = Entry(width=35)
email.grid(row=2, column=1, columnspan=2)
email.insert(0, "tharunkumarr98@gmail.com")
password = Entry(width=21)
password.grid(row=3, column=1)
generate_password = Button(text="Generate Password", command=generate_password_fun)
generate_password.grid(row=3, column=2)
search_button = Button(text="Search",command=find_password, width=15)
search_button.grid(row=1, column=2)
adds = Button(text="Add", width=36, command=save)
adds.grid(row=4, column=1, columnspan=2)
window.mainloop()
