import tkinter as tk
from tkinter import messagebox

def workflow_calculator(num_clients, num_employees):
    # Define time spent by each specialist in minutes
    time_intake = 10
    time_preparer = 60
    time_quality_review = 15

    # Total time required for each client
    total_time_per_client = time_intake + time_preparer + time_quality_review
    
    # Calculate the proportion of tasks for each role
    proportion_intake = time_intake / total_time_per_client
    proportion_preparer = time_preparer / total_time_per_client
    proportion_quality_review = time_quality_review / total_time_per_client

    # Calculate the number of employees needed for each role
    employees_intake = int(num_employees * proportion_intake)
    employees_preparer = int(num_employees * proportion_preparer)
    employees_quality_review = int(num_employees * proportion_quality_review)

    # Adjust if the sum doesn't equal the total number of employees due to rounding
    remaining_employees = num_employees - (employees_intake + employees_preparer + employees_quality_review)
    
    if remaining_employees > 0:
        employees_preparer += remaining_employees  # Add remaining employees to preparers

    # Output the result
    return {
        "clients": num_clients,
        "employees": num_employees,
        "intake_specialists": employees_intake,
        "preparers": employees_preparer,
        "quality_review_specialists": employees_quality_review
    }

def calculate():
    try:
        num_clients = int(client_entry.get())
        num_employees = int(employee_entry.get())
        result = workflow_calculator(num_clients, num_employees)
        
        result_text.set(f"Intake Specialists: {result['intake_specialists']}\n"
                        f"Preparers: {result['preparers']}\n"
                        f"Quality Review Specialists: {result['quality_review_specialists']}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for clients and employees.")

# Setup GUI
root = tk.Tk()
root.title("Workflow Calculator")

tk.Label(root, text="Number of Clients:").grid(row=0)
tk.Label(root, text="Number of Employees:").grid(row=1)

client_entry = tk.Entry(root)
employee_entry = tk.Entry(root)
client_entry.grid(row=0, column=1)
employee_entry.grid(row=1, column=1)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.grid(row=3, columnspan=2)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=2, columnspan=2)

root.mainloop()
