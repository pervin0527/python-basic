import json
import random
import pyperclip
import tkinter as tk
import tkinter.messagebox as messagebox

# ---------------------------- SEARCH DATA ------------------------------- #
def search_data():
    input_website = website_entry.get()
    
    try:
        with open("data.json", "r") as database:
            data = json.load(database)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Doesn't have a database. Please Add the account information.")

    else:
        if input_website in data:
            email = data[input_website]["email"]
            password = data[input_website]["password"]
            messagebox.showinfo(title=input_website, message=f"Email : {email} \n Password : {password} \n")
        else:
            messagebox.showerror(title="Data Not Found", message=f"{input_website} doesn't exist")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    random_letters = [random.choice(letters) for _ in range(nr_letters)]
    random_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    random_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = []
    password_list = random_letters + random_symbols + random_numbers
    random.shuffle(password_list)
    
    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    input_website = website_entry.get()
    input_email = email_entry.get()
    input_password = password_entry.get()
    new_data = {
        input_website:{
            "email" : input_email,
            "password" : input_password
        }
    }

    if len(input_website) == 0 or len(input_password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r", encoding="UTF-8") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w", encoding="UTF-8") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w", encoding="UTF-8") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(height=200, width=200)
img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

## Labels
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)

## Entries
website_entry = tk.Entry(width=21)
website_entry.grid(row=1, column=1) 
website_entry.focus()

email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "pervin0527@gmail.com")

password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1)

## Buttons
search_button = tk.Button(text="Search", width=13, command=search_data)
search_button.grid(row=1, column=2)

password_button = tk.Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()