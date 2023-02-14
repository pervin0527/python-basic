import tkinter as tk

window = tk.Tk()
window.title("Challenge")
window.minsize(width=640, height=480)
window.config(padx=20, pady=20)  # padding

label = tk.Label(text="Label", font=("Arial", 24, "bold"))
label["text"] = "This is Label"
label.config(padx=30, pady=30)
label.grid(row=0, column=0)

button1 = tk.Button(text="Button1")
button1.grid(row=1, column=1)

button2 = tk.Button(text="Button2")
button2.grid(row=0, column=2)

entry = tk.Entry(width=50)
entry.grid(row=2, column=3)

window.mainloop()
