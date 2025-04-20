import pickle
import os
import tkinter as tk
from tkinter import ttk, messagebox


class EmployeeManager:
    FILE_NAME = "employee.dat"

    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("500x500")
        self.root.configure(bg="#ffffff")

        ttk.Label(root, text="Employee ID:").grid(row=0, column=0, padx=10, pady=5)
        self.emp_id = ttk.Entry(root)
        self.emp_id.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(root, text="Name:").grid(row=1, column=0, padx=10, pady=5)
        self.emp_name = ttk.Entry(root)
        self.emp_name.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(root, text="Department:").grid(row=2, column=0, padx=10, pady=5)
        self.emp_dep = ttk.Entry(root)
        self.emp_dep.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(root, text="Salary:").grid(row=3, column=0, padx=10, pady=5)
        self.emp_sal = ttk.Entry(root)
        self.emp_sal.grid(row=3, column=1, padx=10, pady=5)

        btn_frame = ttk.Frame(root)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=10)

        self.create_btn = ttk.Button(btn_frame, text="Create", command=self.create_entry)
        self.create_btn.grid(row=0, column=0, padx=5)

        self.fetch_btn = ttk.Button(btn_frame, text="Fetch All", command=self.fetch_entries)
        self.fetch_btn.grid(row=0, column=1, padx=5)

        self.search_btn = ttk.Button(btn_frame, text="Search", command=self.search_entry)
        self.search_btn.grid(row=1, column=0, padx=5, pady=5)

        self.delete_btn = ttk.Button(btn_frame, text="Delete", command=self.delete_entry)
        self.delete_btn.grid(row=1, column=1, padx=5, pady=5)

        self.exit_btn = ttk.Button(btn_frame,text="Exit", command=self.exit_entry)
        self.exit_btn.grid(row=2, column=1, padx=5, pady=5)


        # Data display area
        self.data_area = tk.Text(root, height=10, width=55)
        self.data_area.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        self.data_area.insert(tk.END, "Employee Records will appear here...\n")

    def display_message(self, message):
        self.data_area.delete("1.0", tk.END)
        self.data_area.insert(tk.END, message)

    def create_entry(self):
        emp = {
            "Emp.ID": int(self.emp_id.get()),
            "Emp.Name": self.emp_name.get(),
            "Emp.Dep": self.emp_dep.get(),
            "Salary": int(self.emp_sal.get())
        }
        with open(self.FILE_NAME, "ab") as f:
            pickle.dump(emp, f)
        self.display_message("Employee Added!")

    def fetch_entries(self):
        try:
            with open(self.FILE_NAME, "rb") as f:
                records = []
                while True:
                    try:
                        emp = pickle.load(f)
                        records.append(f"ID: {emp['Emp.ID']}, Name: {emp['Emp.Name']}, Dept: {emp['Emp.Dep']}, Salary: {emp['Salary']}")
                    except EOFError:
                        break
                if records:
                    self.display_message("\n".join(records))
                else:
                    self.display_message("No employee records found.")
        except FileNotFoundError:
            self.display_message("No employee records exist.")

    def search_entry(self):
        emp_no = int(self.emp_id.get())
        try:
            with open(self.FILE_NAME, "rb") as f:
                while True:
                    try:
                        emp = pickle.load(f)
                        if emp["Emp.ID"] == emp_no:
                            self.display_message(f"ID: {emp['Emp.ID']}, Name: {emp['Emp.Name']}, Dept: {emp['Emp.Dep']}, Salary: {emp['Salary']}")
                            return
                    except EOFError:
                        break
        except FileNotFoundError:
            pass
        self.display_message("Employee not found!")

    def delete_entry(self):
        emp_no = int(self.emp_id.get())
        temp_file = "temp.dat"
        found = False

        try:
            with open(self.FILE_NAME, "rb") as f, open(temp_file, "wb") as temp:
                while True:
                    try:
                        emp = pickle.load(f)
                        if emp["Emp.ID"] != emp_no:
                            pickle.dump(emp, temp)
                        else:
                            found = True
                    except EOFError:
                        break

            if found:
                os.remove(self.FILE_NAME)
                os.rename(temp_file, self.FILE_NAME)
                self.display_message("Employee Deleted!")
            else:
                self.display_message("Employee not found!")
        except FileNotFoundError:
            self.display_message("No employee records exist.")
    
    def exit_entry(self):
        exit()

root = tk.Tk()
app = EmployeeManager(root)
root.mainloop()
