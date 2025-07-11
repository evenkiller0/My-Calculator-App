import tkinter as tk
from tkinter import messagebox
import math # Import the math module for square root function

# --- Global variable for calculator logic (current_expression remains global) ---
current_expression = ""

# input_text will now be initialized within create_calculator()

# --- Function to update the display ---
def update_display(value):
    global current_expression
    current_expression += str(value)
    input_text.set(current_expression)

# --- Function to clear the display ---
def clear_display():
    global current_expression
    current_expression = ""
    input_text.set("")

# --- Function to handle button presses (numbers and operators) ---
def button_click(char):
    if char == 'C':
        clear_display()
    elif char == '=':
        calculate_result()
    elif char == '√': # Handle the new square root button
        square_root()
    else:
        update_display(char)

# --- Function to calculate the result ---
def calculate_result():
    global current_expression
    try:
        # Evaluate the expression
        result = eval(current_expression)
        # Check if the result is a whole number and display it as an integer
        if result == int(result):
            result = int(result)
        input_text.set(str(result))
        current_expression = str(result)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")
        clear_display()
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")
        clear_display()

# --- Function to calculate the square root ---
def square_root():
    global current_expression
    try:
        value = float(current_expression) # Convert current expression to a float
        if value < 0:
            messagebox.showerror("Error", "Cannot calculate square root of a negative number!")
            clear_display()
        else:
            result = math.sqrt(value) # Calculate square root
            # Check if the result is a whole number and display it as an integer
            if result == int(result):
                result = int(result)
            input_text.set(str(result))
            current_expression = str(result)
    except ValueError:
        messagebox.showerror("Error", "Invalid input for square root!")
        clear_display()
    except Exception as e:
        messagebox.showerror("Error", "Error during square root calculation.")
        clear_display()


# --- Main application window setup ---
def create_calculator():
    window = tk.Tk()
    window.title("Simple Calculator")
    window.geometry("300x450") # Set initial window size
    window.resizable(False, False) # Prevent resizing for a fixed calculator look

    # --- Initialize input_text AFTER the Tkinter root window is created ---
    global input_text # Declare it global so other functions can access it
    input_text = tk.StringVar()

    # --- Set window icon ---
    # This line uses the iconbitmap() method to set the window's icon.
    # Ensure 'icon.ico' is in the same directory as this script.
    try:
        window.iconbitmap('icon.ico')
    except tk.TclError:
        print("Warning: 'icon.ico' not found or invalid. Default icon will be used.")

    # --- Display Entry Field ---
    # This entry will show the numbers and results.
    display_entry = tk.Entry(
        window,
        font=('Arial', 24, 'bold'),
        textvariable=input_text,
        bd=10,
        insertwidth=4,
        width=14,
        justify='right',
        bg="lightgray",
        relief='groove'
    )
    # Use grid to place the display at the top, spanning all columns
    display_entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")

    # --- Button Layout ---
    # Define the buttons for the calculator
    buttons = [
        ('C', 1, 0), ('/', 1, 1), ('*', 1, 2), ('-', 1, 3),
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('√', 3, 3), # Added Square Root button
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2),
        ('0', 5, 0), ('.', 5, 2),
        ('=', 4, 3) # Equals button will span two rows
    ]

    # Create and place buttons
    for (text, row, col) in buttons:
        # Define button style
        button_style = {
            'font': ('Arial', 18, 'bold'),
            'bd': 5,
            'relief': 'raised',
            'padx': 10,
            'pady': 10,
            'bg': '#f0f0f0' # Light grey background for most buttons
        }

        # Customize colors for operators and special buttons
        if text in ['C', '/', '*', '-', '+', '=', '√']: # Added '√' to operator styling
            button_style['bg'] = '#ff9900' if text not in ['C'] else '#ff6666' # Orange for operators, red for clear
            button_style['fg'] = 'white' # White text for operators

        # Create the button
        button = tk.Button(window, text=text, **button_style, command=lambda char=text: button_click(char))

        # Place the button on the grid
        if text == '0':
            button.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=5, pady=5) # '0' spans 2 columns
        elif text == '=':
            button.grid(row=row, column=col, rowspan=2, sticky="nsew", padx=5, pady=5) # '=' spans 2 rows
        else:
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

    # Configure row and column weights to make buttons expand proportionally
    for i in range(6): # 6 rows (0-5)
        window.grid_rowconfigure(i, weight=1)
    for i in range(4): # 4 columns (0-3)
        window.grid_columnconfigure(i, weight=1)

    window.mainloop()

# --- Run the calculator ---
if __name__ == "__main__":
    create_calculator()
