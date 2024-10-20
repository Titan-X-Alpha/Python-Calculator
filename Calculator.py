# Make a proper calculator with UI
import tkinter as tk

def on_button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def erase_last_char():
    current_text = entry.get()
    entry.delete(len(current_text) - 1, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget to display the calculation
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
entry.grid(row=0, column=0, columnspan=4)

# Define buttons for numbers and operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', 'x',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create the buttons and place them on the grid
row = 1
col = 0
for button in buttons:
    if button == "=":
        btn = tk.Button(root, text=button, width=4, height=2, font=('Arial', 18),
                        command=calculate)
    else:
        btn = tk.Button(root, text=button, width=4, height=2, font=('Arial', 18),
                        command=lambda value=button: on_button_click(value))
    btn.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Add a Clear button
clear_button = tk.Button(root, text='C', width=4, height=2, font=('Arial', 18),
                         command=clear_entry)
clear_button.grid(row=row, column=col)

# Add an Erase button
erase_button = tk.Button(root, text='⌫', width=4, height=2, font=('Arial', 18),
                         command=erase_last_char)
erase_button.grid(row=row, column=col+1)

# Run the application
root.mainloop()