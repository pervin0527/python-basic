import random
import pyperclip
import tkinter as tk
import tkinter.messagebox as messagebox

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

    if len(input_website) == 0 or len(input_password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=input_website, 
                                    message=f"These are the details entered: \n \
                                                Email: {input_email} \n Password: {input_password} \n Is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{input_website} | {input_email} | {input_password} \n")
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
website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2) 
website_entry.focus()

email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "pervin0527@gmail.com")

password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1)

## Buttons
password_button = tk.Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()