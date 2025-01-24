# File: styled_calculator_with_sound.py

import tkinter as tk
from tkinter import messagebox
import os
from playsound import playsound  # Install this package: pip install playsound

def play_click_sound():
    """Play sound for button click."""
    sound_path = "\\python pratice\\click.mp3"  # Path to your click sound file
    if os.path.exists(sound_path):
        try:
            playsound(sound_path, block=False)
        except Exception as e:
            print(f"Error playing sound: {e}")
    else:
        print("Sound file not found.")

def button_click(number):
    """Append clicked number or operator to the entry field."""
    play_click_sound()
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear_entry():
    """Clear the entry field."""
    play_click_sound()
    entry.delete(0, tk.END)

def calculate():
    """Evaluate the expression in the entry field."""
    play_click_sound()
    try:
        result = eval(entry.get())  # Use eval to compute the expression
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        messagebox.showerror("Error", "Invalid Input")
        entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Styled Calculator with Sound")
root.geometry("300x400")
root.configure(bg="#f0f0f0")

# Entry field for the calculator
entry = tk.Entry(root, width=16, font=("Arial", 24), bd=5, insertwidth=4, bg="#fff", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Button styles
button_font = ("Arial", 16)
button_bg = "#d69f0f"
button_active_bg = "#c8c8c8"

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Add buttons to the grid
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(
            root,
            text=text,
            font=button_font,
            bg="#4CAF50",
            fg="#fff",
            activebackground="#45a049",
            command=calculate,
        )
    elif text == "C":
        btn = tk.Button(
            root,
            text=text,
            font=button_font,
            bg="#f44336",
            fg="#fff",
            activebackground="#d32f2f",
            command=clear_entry,
        )
    else:
        btn = tk.Button(
            root,
            text=text,
            font=button_font,
            bg=button_bg,
            activebackground=button_active_bg,
            command=lambda t=text: button_click(t),
        )
    
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Configure grid rows and columns for equal spacing
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the main loop
root.mainloop()