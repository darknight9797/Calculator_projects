import tkinter as tk

def calculate_monthly_salary():
    salary = float(salary_entry.get())
    monthly_salary = salary * 100000 // 12
    result_label.config(text=f"Your monthly salary is: {monthly_salary} INR")

root = tk.Tk()
root.title("Salary Calculator")

salary_label = tk.Label(root, text="Enter your salary in LPA:")
salary_label.pack()

salary_entry = tk.Entry(root)
salary_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_monthly_salary)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
