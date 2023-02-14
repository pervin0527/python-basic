import tkinter as tk

FONT_SIZE = 15


def calculate():
    label_11.config(text=(float(entry.get()) * 1.609))


window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)

entry = tk.Entry()
entry.insert(tk.END, string=0)  # 텍스트의 마지막 문자 위치
entry.grid(row=0, column=1)

label_02 = tk.Label(text="Miles", font=("Arial", FONT_SIZE, "bold"))
label_02.grid(row=0, column=2)

label_10 = tk.Label(text="is equal to", font=("Arial", FONT_SIZE, "bold"))
label_10.grid(row=1, column=0)

label_11 = tk.Label(text="0", font=("Arial", FONT_SIZE, "bold"))
label_11.grid(row=1, column=1)

label_12 = tk.Label(text="Km", font=("Arial", FONT_SIZE, "bold"))
label_12.grid(row=1, column=2)

button = tk.Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()
