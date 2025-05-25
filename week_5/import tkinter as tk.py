import tkinter as tk
import pandas as pd


def verify_employee():
    name = name_entry.get()
    dept = dept_entry.get()

    try:
        df = pd.read_csv("GIG-logistics.csv")  # Load the CSV
    except FileNotFoundError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "CSV file not found.")
        return

    employee = df[(df['Name'] == name) & (df['Department'] == dept)]

    if not employee.empty:
        welcome_msg = f"Welcome, {name}!"
        dept_employees = df[df['Department'] == dept]['Name'].tolist()
        if name in dept_employees:
            dept_employees.remove(name)  # Don't include the user
        employee_list = "\n".join(
            dept_employees) if dept_employees else "No other employees in this department."
        result_text.delete(1.0, tk.END)  # Clear previous text
        result_text.insert(
            tk.END, f"{welcome_msg}\n\nOther employees in {dept}:\n{employee_list}")
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Employee not found.")


# --- GUI Setup ---
window = tk.Tk()
window.title("GIG Logistics Employee Verification")

tk.Label(window, text="Name:").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Department:").pack()
dept_entry = tk.Entry(window)
dept_entry.pack()

verify_button = tk.Button(window, text="Verify", command=verify_employee)
verify_button.pack()

result_text = tk.Text(window, height=10, width=40)
result_text.pack()

window.mainloop()
