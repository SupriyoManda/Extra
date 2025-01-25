import tkinter as tk
from tkinter import messagebox

# Sample data
TEACHER_SEATING = {
    "Math": "Table 1",
    "Science": "Table 2",
    "English": "Table 3",
    "History": "Table 4",
}

STUDENT_DETAILS = [
    {"Name": "John Doe", "Class": "10", "Roll No": "1"},
    {"Name": "Jane Smith", "Class": "10", "Roll No": "2"},
    {"Name": "Emily Davis", "Class": "10", "Roll No": "3"},
]

USERS = {
    "parent": {"username": "parent", "password": "parent123"},
    "teacher": {"username": "teacher", "password": "teacher123"},
}


# Parent Dashboard
def parent_dashboard():
    def search_teacher():
        query = search_var.get().lower()
        result_frame.pack_forget()
        result_frame.pack(pady=10)

        for widget in result_frame.winfo_children():
            widget.destroy()

        for subject, seating in TEACHER_SEATING.items():
            if query in subject.lower() or query in seating.lower():
                tk.Label(result_frame, text=f"{subject}: {seating}", font=("Arial", 12)).pack()

    dashboard = tk.Toplevel(root)
    dashboard.title("Parent Dashboard")
    dashboard.geometry("400x400")

    tk.Label(dashboard, text="Teacher Seating Arrangements", font=("Arial", 14)).pack(pady=10)

    # Search bar
    search_var = tk.StringVar()
    search_frame = tk.Frame(dashboard)
    search_frame.pack(pady=10)

    tk.Entry(search_frame, textvariable=search_var, width=25).pack(side="left", padx=5)
    tk.Button(search_frame, text="Search", command=search_teacher).pack(side="left")

    # Result frame
    result_frame = tk.Frame(dashboard)
    result_frame.pack(pady=10)

    for subject, seating in TEACHER_SEATING.items():
        tk.Label(result_frame, text=f"{subject}: {seating}", font=("Arial", 12)).pack()

    tk.Button(dashboard, text="Logout", command=dashboard.destroy).pack(pady=20)


# Teacher Dashboard
def teacher_dashboard():
    def search_student():
        query = search_var.get().lower()
        result_frame.pack_forget()
        result_frame.pack(pady=10)

        for widget in result_frame.winfo_children():
            widget.destroy()

        for student in STUDENT_DETAILS:
            if query in student["Name"].lower() or query in student["Class"].lower() or query in student["Roll No"]:
                details = f"Name: {student['Name']}, Class: {student['Class']}, Roll No: {student['Roll No']}"
                tk.Label(result_frame, text=details, font=("Arial", 12)).pack()

    dashboard = tk.Toplevel(root)
    dashboard.title("Teacher Dashboard")
    dashboard.geometry("400x400")

    tk.Label(dashboard, text="Student Details", font=("Arial", 14)).pack(pady=10)

    # Search bar
    search_var = tk.StringVar()
    search_frame = tk.Frame(dashboard)
    search_frame.pack(pady=10)

    tk.Entry(search_frame, textvariable=search_var, width=25).pack(side="left", padx=5)
    tk.Button(search_frame, text="Search", command=search_student).pack(side="left")

    # Result frame
    result_frame = tk.Frame(dashboard)
    result_frame.pack(pady=10)

    for student in STUDENT_DETAILS:
        details = f"Name: {student['Name']}, Class: {student['Class']}, Roll No: {student['Roll No']}"
        tk.Label(result_frame, text=details, font=("Arial", 12)).pack()

    tk.Button(dashboard, text="Logout", command=dashboard.destroy).pack(pady=20)


# Login Validation
def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == USERS["parent"]["username"] and password == USERS["parent"]["password"]:
        messagebox.showinfo("Login Successful", "Welcome, Parent!")
        parent_dashboard()
    elif username == USERS["teacher"]["username"] and password == USERS["teacher"]["password"]:
        messagebox.showinfo("Login Successful", "Welcome, Teacher!")
        teacher_dashboard()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")


# Main Window
root = tk.Tk()
root.title("PTM Login")
root.geometry("300x200")

tk.Label(root, text="PTM Login", font=("Arial", 16)).pack(pady=10)

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Username:").grid(row=0, column=0, pady=5, sticky="e")
username_entry = tk.Entry(frame)
username_entry.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Password:").grid(row=1, column=0, pady=5, sticky="e")
password_entry = tk.Entry(frame, show="*")
password_entry.grid(row=1, column=1, pady=5)

tk.Button(frame, text="Login", command=validate_login).grid(row=2, column=0, columnspan=2, pady=10)
tk.Button(frame, text="Quit", command=root.quit).grid(row=3, column=0, columnspan=2)

root.mainloop()
