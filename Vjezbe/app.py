import customtkinter as ctk
from tkinter import ttk, messagebox
from test_db import Database

class ExpenseApp(ctk.CTk):
    def __init__(self):
        super().__init__()


        self.db = Database("troskovi.db")


        self.title("Expense Management System")
        self.geometry("1000x700")
        self.configure(fg_color = "#2c3e50")

        self.category = ctk.StringVar()
        self.amount = ctk.IntVar()
        self.description = ctk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        entry_frame = ctk.CTkFrame(self, fg_color="#34495e")
        entry_frame.pack(side="top", fill="x", padx=20, pady=10)

        #nacin 1 za rasporedjivanje
        title = ctk.CTkLabel(entry_frame, text="Expense Management", font=("Calibri", 24, "bold"), text_color="white")
        title.grid(row=0, columnspan=4, padx=10, pady=10, sticky="w")

        #nacin 2 za rasporedjivanje
        ctk.CTkLabel(entry_frame, text="Category", font=("Calibri", 16, "bold"), text_color="white").grid(row=1, column=0, padx=10, pady=10)

        self.txtCategory = ctk.CTkEntry(entry_frame, textvariable=self.category,  font=("Calibri", 16), width=250)
        self.txtCategory.grid(row=1, column=1, padx=10, pady=10, sticky="w")


        ctk.CTkLabel(entry_frame, text="Amount", font=("Calibri", 16, "bold"), text_color="white").grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.intAmount = ctk.CTkEntry(entry_frame, textvariable=self.amount,  font=("Calibri", 16), width=250)
        self.intAmount.grid(row=1, column=3, padx=10, pady=10, sticky="w")

        ctk.CTkLabel(entry_frame, text="Description", font=("Calibri", 16), text_color="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.textDesc = ctk.CTkEntry(entry_frame, textvariable=self.description,  font=("Calibri", 16), width=600)
        self.textDesc.grid(row=2, column=1, columnspan=3, padx=10, pady=10, sticky="w")

        btn_frame = ctk.CTkFrame(entry_frame, fg_color = "#34495e")
        btn_frame.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="w")

        ctk.CTkButton(btn_frame, command=self.add_expense, text="Add", width=150, font=("Calibri", 16)).grid(row=0, column=0, padx=10)
        ctk.CTkButton(btn_frame, command=self.update_expense, text="Update", width=150, font=("Calibri", 16)).grid(row=0, column=1, padx=10)
        ctk.CTkButton(btn_frame, command=self.delete_expense, text="Delete", width=150, font=("Calibri", 16)).grid(row=0, column=2, padx=10)
        ctk.CTkButton(btn_frame, command=self.clear_expenses, text="Clear", width=150, font=("Calibri", 16)).grid(row=0, column=3, padx=10)

        tree_frame = ctk.CTkFrame(self, fg_color="#ecf0f1")
        tree_frame.pack(side="top", fill="both", expand=True)

        style = ttk.Style()
        style.configure("Treeview", font=("Calibri", 16), rowheight=30)
        style.configure("Treeview.Heading", font=("Calibri", 16))

        self.tv = ttk.Treeview(tree_frame, columns=(1,2,3,4), show="headings")
        self.tv.heading("1", text="ID")
        self.tv.heading("2", text="Category")
        self.tv.heading("3", text="Amount")
        self.tv.heading("4", text="Description")

        self.tv.bind("<ButtonRelease-1>", self.get_data)

        self.tv.pack(fill="both", expand=True)



    #kupi podatke iz polja
    def get_data():
        return   






    #CRUD
    def add_expense():
        return
    def update_expense():
        return
    def delete_expense():
        return
    def clear_expenses():
        return
   






        



if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    app = ExpenseApp()
    app.mainloop()
