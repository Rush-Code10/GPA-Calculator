import tkinter as tk
from tkinter import ttk

# Define the grading scale
grading_scale = {
    "A+": 4.00,
    "A": 3.75,
    "A-": 3.50,
    "B+": 3.25,
    "B": 3.00,
    "B-": 2.75,
    "C+": 2.50,
    "C": 2.25,
    "C-": 2.00,
    "D": 1.50,
    "F": 0.0
}

# Create the GUI window
root = tk.Tk()
root.title("GPA Calculator")
root.geometry("400x400")

# Create the table
table = ttk.Treeview(root)
table["columns"] = ("course", "grade", "credit_hours")
table.column("#0", width=0, stretch=tk.NO)
table.column("course", anchor=tk.W, width=100)
table.column("grade", anchor=tk.W, width=100)
table.column("credit_hours", anchor=tk.W, width=100)
table.heading("course", text="Course")
table.heading("grade", text="Grade")
table.heading("credit_hours", text="Credit Hours")
table.pack()

# Create the GPA label
gpa_label = tk.Label(root, text="GPA: ")
gpa_label.pack()

# Create the add course button
def add_course():
    # Get the course name, grade, and credit hours from the user
    course_name = course_entry.get()
    course_grade = grade_entry.get()
    credit_hours = int(credit_hours_entry.get())

    # Calculate the grade points for the course
    grade_points = grading_scale[course_grade] * credit_hours

    # Add the course to the table
    course = table.insert("", tk.END, text="", values=(course_name, course_grade, credit_hours))

    # Calculate the total grade points and credit hours
    total_grade_points = sum(grading_scale[table.item(course)["values"][1]] * int(table.item(course)["values"][2]) for course in table.get_children())
    total_credit_hours = sum(int(table.item(course)["values"][2]) for course in table.get_children())

    # Calculate the GPA and update the label
    gpa = total_grade_points / total_credit_hours
    gpa_label.config(text=f"GPA: {gpa:.2f}")

    # Clear the entry fields
    course_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)
    credit_hours_entry.delete(0, tk.END)



# Create the course entry fields
course_label = tk.Label(root, text="Course: ")
course_label.pack()
course_entry = tk.Entry(root)
course_entry.pack()

grade_label = tk.Label(root, text="Grade: ")
grade_label.pack()
grade_entry = ttk.Combobox(root, values=list(grading_scale.keys()))
grade_entry.pack()

credit_hours_label = tk.Label(root, text="Credit Hours: ")
credit_hours_label.pack()
credit_hours_entry = tk.Entry(root)
credit_hours_entry.pack()

add_course_button = tk.Button(root, text="Add Course", command=add_course)
add_course_button.pack()

root.mainloop()