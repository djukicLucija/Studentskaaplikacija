import customtkinter as ctk
from tkinter import ttk, messagebox
from db import Database
from datetime import datetime

class StudentGradeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.db=Database("StudentRelational.db")
        self.title("Student Grade Management System")
        self.geometry("1200x800")
        self.configure(fg_color="#2c3e50")

        self.name=ctk.StringVar()
        self.index_number=ctk.StringVar()
        self.course_name=ctk.StringVar()
        self.grade=ctk.StringVar()

        self.selected_student_id=None
        self.selected_course_id=None
        self.create_widgets()
    def create_widgets(self):
        tabview=ctk.CTkTabview(self)

        tabview.pack(expand=True,fill="both",padx=20,pady=20)

        tab_students=tabview.add("Students")
        tab_courses=tabview.add("Courses")
        tab_grades=tabview.add("Grades")
        tab_students.columnconfigure((0,3),weight=1)
        tab_students.columnconfigure((1,2),weight=0)
        tab_courses.columnconfigure((0,3),weight=1)
        tab_courses.columnconfigure((1,2),weight=0)
        tab_grades.columnconfigure((0,3),weight=1)
        tab_grades.columnconfigure((1,2),weight=0)
#student tab
        ctk.CTkLabel(tab_students,text="Name:").grid(row=0,column=1,sticky="e",padx=10,pady=5)
        ctk.CTkEntry(tab_students,textvariable=self.name).grid(row=0,column=2,sticky="w",padx=10,pady=5)

        ctk.CTkLabel(tab_students,text="Index Number:").grid(row=1,column=1,sticky="e",padx=10,pady=5)
        ctk.CTkEntry(tab_students,textvariable=self.index_number).grid(row=1,column=2,sticky="w",padx=10,pady=5)

        ctk.CTkButton(tab_students,text="Add student", command="").grid(row=2,column=1,columnspan=2,pady=10)
#course tab
        ctk.CTkLabel(tab_courses,text="Name:").grid(row=0,column=1,sticky="e",padx=10,pady=5)
        ctk.CTkEntry(tab_courses,textvariable=self.name).grid(row=0,column=2,sticky="w",padx=10,pady=5)

        ctk.CTkButton(tab_courses,text="Add course", command="").grid(row=2,column=1,columnspan=2,pady=10)
#grades tab














if __name__=='__main__':
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app=StudentGradeApp()
    app.mainloop()



