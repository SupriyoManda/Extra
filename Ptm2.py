import tkinter as tk
from tkinter import messagebox

# Sample data
TEACHER_SEATING = {
    "Math": "Table 1",
    "Science": "Table 2",
    "English": "Table 3",
    "History": "Table 4",
}

USERS = {
    "parent": {"username": "parent", "password": "parent123"},
    "teacher": {"username": "teacher", "password": "teacher123"},
}

# Sample slots for booking
AVAILABLE_SLOTS = {
    "Math": ["10:00 AM - 10:15 AM", "10:30 AM - 10:45 AM"],
    "Science": ["11:00 AM - 11:15 AM", "11:30 AM - 11:45 AM"],
    "English": ["12:00 PM - 12:15 PM", "12:30 PM - 12:45 PM"],
    "History": ["1:00 PM - 1:15 PM", "1:30 PM - 1:45 PM"],
}

# Track booked slots
BOOKED_SLOTS = {}
PARENT_BOOKINGS = {}

# Parent Dashboard
def parent_dashboard():
    def book_slot(subject):
        def confirm_booking():
            student_name = student_entry.get()
            selected_slot = slot_var.get()
            if student_name and selected_slot in AVAILABLE_SLOTS[subject]:
                AVAILABLE_SLOTS[subject].remove(selected_slot)
                BOOKED_SLOTS.setdefault(subject, []).append((selected_slot, student_name))
                PARENT_BOOKINGS.setdefault(subject, []).append((selected_slot, student_name))
                messagebox.showinfo("Success", f"Slot '{selected_slot}' for '{subject}' booked successfully for {student_name}!")
                slot_window.destroy()
            else:
                messagebox.showerror("Error", "Please enter a student name and select a valid slot.")

        slot_window = tk.Toplevel(dashboard)
        slot_window.title(f"Book Slot for {subject}")
        slot_window.geometry("300x250")

        tk.Label(slot_window, text=f"Available Slots for {subject}", font=("Arial", 14)).pack(pady=10)

        tk.Label(slot_window, text="Student Name:").pack()
        student_entry = tk.Entry(slot_window)
        student_entry.pack()

        slot_var = tk.StringVar(value=None)
        for slot in AVAILABLE_SLOTS[subject]:
            tk.Radiobutton(slot_window, text=slot, variable=slot_var, value=slot).pack(anchor="w")

        tk.Button(slot_window, text="Confirm Booking", command=confirm_booking).pack(pady=10)

    def delete_slot():
        selected_subject = subject_var.get()
        if selected_subject in PARENT_BOOKINGS and PARENT_BOOKINGS[selected_subject]:
            selected_slot, student = PARENT_BOOKINGS[selected_subject].pop()
            BOOKED_SLOTS[selected_subject].remove((selected_slot, student))
            AVAILABLE_SLOTS[selected_subject].append(selected_slot)
            messagebox.showinfo("Success", f"Slot '{selected_slot}' for '{selected_subject}' deleted successfully!")
        else:
            messagebox.showerror("Error", "No booked slots available to delete.")

    dashboard = tk.Toplevel(root)
    dashboard.title("Parent Dashboard")
    dashboard.geometry("400x400")

    tk.Label(dashboard, text="Teacher Seating Arrangements", font=("Arial", 14)).pack(pady=10)
    
    subject_var = tk.StringVar()
    tk.Label(dashboard, text="Select Subject:").pack()
    tk.OptionMenu(dashboard, subject_var, *TEACHER_SEATING.keys()).pack()
    
    tk.Button(dashboard, text="Book Slot", command=lambda: book_slot(subject_var.get())).pack(pady=5)
    tk.Button(dashboard, text="Delete Slot", command=delete_slot).pack(pady=5)

    tk.Button(dashboard, text="Logout", command=dashboard.destroy).pack(pady=20)

# Teacher Dashboard
def teacher_dashboard():
    def view_booked_slots():
        booked_window = tk.Toplevel(dashboard)
        booked_window.title("Booked Slots")
        booked_window.geometry("350x400")
        tk.Label(booked_window, text="Booked Slots", font=("Arial", 14)).pack(pady=10)

        for subject, slots in BOOKED_SLOTS.items():
            tk.Label(booked_window, text=f"{subject}:", font=("Arial", 12, "bold")).pack()
            for slot, student in slots:
                tk.Label(booked_window, text=f"- Time: {slot}, Student: {student}").pack()
    
    dashboard = tk.Toplevel(root)
    dashboard.title("Teacher Dashboard")
    dashboard.geometry("400x400")
    
    tk.Button(dashboard, text="View Booked Slots", command=view_booked_slots).pack(pady=10)
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
