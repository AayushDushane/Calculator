import tkinter as tk


def add_to_display(character):
    current_text = display.get()
    display.set(current_text + character)


def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.set(result)
    except Exception:
        display.set("Error")


def clear():
    display.set("")


window = tk.Tk()
window.title("Calculator")
window.geometry("400x500")

display = tk.StringVar()
display.set("")

display_label = tk.Label(window, textvariable=display, font=(
    "Helvetica", 20), anchor="e", padx=10, pady=10, bg="lightgray")
display_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

button_frame = tk.Frame(window)
button_frame.grid(row=1, column=0, columnspan=4, sticky="nsew")

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '.', '0', '+', '='
]

row, col = 0, 0
for button in buttons:
    if button == '=':
        tk.Button(button_frame, text=button, padx=20, pady=20, command=calculate,
                  bg="lightblue").grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    else:
        tk.Button(button_frame, text=button, padx=20, pady=20, command=lambda b=button: add_to_display(
            b), bg="lightblue").grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(window, text="Clear", padx=20, pady=20, command=clear, bg="red", fg="white").grid(
    row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

developer_label = tk.Label(
    window, text="Developed by Aayush Dushane", font=("Helvetica", 10))
developer_label.grid(row=3, column=0, columnspan=4, pady=10, sticky="nsew")

for i in range(4):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

window.mainloop()
