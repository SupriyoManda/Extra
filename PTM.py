import tkinter as tk
from tkinter import messagebox

# Sample data
teachers = {
    'Mr. Smith': ['10:00 AM', '11:00 AM', '12:00 PM'],
    'Ms. Davis': ['09:30 AM', '10:30 AM', '11:30 AM'],
}

scheduled_meetings = {}

# Parent window for booking a slot
def parent_login():
    parent_window = tk.Toplevel()
    parent_window.title("Parent Dashboard")

    # Enter Student's Name
    tk.Label(parent_window, text="Enter Student's Name:").pack(pady=5)
    student_name_var = tk.StringVar()
    student_name_entry = tk.Entry(parent_window, textvariable=student_name_var)
    student_name_entry.pack(pady=5)

    # Search bar
    tk.Label(parent_window, text="Search Teacher:").pack(pady=5)
    search_var = tk.StringVar()
    search_entry = tk.Entry(parent_window, textvariable=search_var)
    search_entry.pack(pady=5)

    def search_teacher():
        teacher_name = search_var.get()
        if teacher_name in teachers:
            schedule_label.config(text=f"Available slots for {teacher_name}: {teachers[teacher_name]}")
            update_roster(teachers[teacher_name])
        else:
            schedule_label.config(text="Teacher not found")

    search_button = tk.Button(parent_window, text="Search", command=search_teacher)
    search_button.pack(pady=5)

    schedule_label = tk.Label(parent_window, text="")
    schedule_label.pack(pady=5)

    # Booking function
    def book_slot():
        teacher_name = search_var.get()
        selected_slot = slot_var.get()
        student_name = student_name_var.get()

        if not student_name:
            messagebox.showwarning("Error", "Please enter the student's name.")
            return

        if teacher_name in teachers and selected_slot in teachers[teacher_name]:
            scheduled_meetings.setdefault(teacher_name, []).append((selected_slot, student_name))
            teachers[teacher_name].remove(selected_slot)
            messagebox.showinfo("Success", f"Meeting booked with {teacher_name} at {selected_slot} for {student_name}")
            notify_teacher(teacher_name, selected_slot, student_name)
            update_roster(teachers[teacher_name])
        else:
            messagebox.showwarning("Error", "Slot not available")

    # Dropdown for slots
    slot_var = tk.StringVar(parent_window)
    slot_dropdown = tk.OptionMenu(parent_window, slot_var, *["Select teacher first"])
    slot_dropdown.pack(pady=5)

    def update_slots(*args):
        teacher_name = search_var.get()
        if teacher_name in teachers:
            slot_dropdown['menu'].delete(0, 'end')
            for slot in teachers[teacher_name]:
                slot_dropdown['menu'].add_command(label=slot, command=tk._setit(slot_var, slot))

    search_var.trace("w", update_slots)

    # Book button
    book_button = tk.Button(parent_window, text="Book Slot", command=book_slot)
    book_button.pack(pady=10)

    # Roster (Listbox) to show available slots
    roster_label = tk.Label(parent_window, text="Available Slots:")
    roster_label.pack(pady=5)
    
    roster = tk.Listbox(parent_window)
    roster.pack(pady=5)

    def update_roster(slots):
        roster.delete(0, tk.END)  # Clear previous entries
        for slot in slots:
            roster.insert(tk.END, slot)  # Add new slots

def notify_teacher(teacher_name, slot, student_name):
    messagebox.showinfo("Notification", f"{teacher_name}, you have a meeting with {student_name} at {slot}.")

# Teacher window for browsing schedule
def teacher_login():
    teacher_window = tk.Toplevel()
    teacher_window.title("Teacher Dashboard")

    def display_schedule():
        teacher_name = search_var.get()
        if teacher_name in scheduled_meetings:
            meeting_info = scheduled_meetings.get(teacher_name, [])
            if meeting_info:
                meeting_list = [f"{slot} with {student}" for slot, student in meeting_info]
                update_teacher_roster(meeting_list)
            else:
                schedule_label.config(text="No meetings scheduled")
        else:
            schedule_label.config(text="No meetings scheduled")

    tk.Label(teacher_window, text="Enter Your Name:").pack(pady=5)
    search_var = tk.StringVar()
    search_entry = tk.Entry(teacher_window, textvariable=search_var)
    search_entry.pack(pady=5)

    search_button = tk.Button(teacher_window, text="View Schedule", command=display_schedule)
    search_button.pack(pady=5)

    schedule_label = tk.Label(teacher_window, text="")
    schedule_label.pack(pady=5)

    # Roster for Teacher to see their meetings
    roster_label = tk.Label(teacher_window, text="Scheduled Meetings:")
    roster_label.pack(pady=5)

    teacher_roster = tk.Listbox(teacher_window)
    teacher_roster.pack(pady=5)

    def update_teacher_roster(meetings):
        teacher_roster.delete(0, tk.END)  # Clear previous entries
        for meeting in meetings:
            teacher_roster.insert(tk.END, meeting)

# Login window
def login_window():
    window = tk.Tk()
    window.title("PTM Login")

    tk.Label(window, text="Login as:").pack(pady=10)

    parent_button = tk.Button(window, text="Parent", command=parent_login)
    parent_button.pack(pady=5)

    teacher_button = tk.Button(window, text="Teacher", command=teacher_login)
    teacher_button.pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    login_window()