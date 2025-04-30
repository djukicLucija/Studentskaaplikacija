import customtkinter as ctk
from tkinter import ttk, messagebox
from db import Database  # Klasa za rad sa bazom podataka

# Glavna klasa aplikacije
class StudentApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Povezivanje sa bazom
        self.db = Database("Studenti.db")

        # Osnovne postavke prozora
        self.title("Student")
        self.geometry("1920x1080+0+0")
        self.configure(fg_color="#2c3e50")
        self.state("zoomed")  # Puni ekran

        # Varijable za unos
        self.ime = ctk.StringVar()
        self.indeks = ctk.StringVar()
        self.predmet = ctk.StringVar()
        self.ocjena = ctk.StringVar()

        # Pokretanje kreiranja GUI elemenata
        self.create_widgets()

        # Prikaz svih zaposlenih pri startu
        self.dispaly_all()

    def create_widgets(self):
        # Sekcija za unos podataka
        entries_frame = ctk.CTkFrame(self, fg_color="#535c68")
        entries_frame.pack(side="top", fill="x", padx=20, pady=10)

        # Naslov aplikacije
        title = ctk.CTkLabel(entries_frame, text="Student", font=("Calibri", 24, "bold"),
                             text_color="white")
        title.grid(row=0, columnspan=4, padx=10, pady=20, sticky="w")

        # Polja za unos podataka
        # Ime
        ctk.CTkLabel(entries_frame, text="Ime", font=("Calibri", 16), text_color="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.txtIme = ctk.CTkEntry(entries_frame, textvariable=self.ime, font=("Calibri", 16), width=300)
        self.txtIme.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Indeks
        ctk.CTkLabel(entries_frame, text="Inedks", font=("Calibri", 16), text_color="white").grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.txtIndeks = ctk.CTkEntry(entries_frame, textvariable=self.indeks, font=("Calibri", 16), width=300)
        self.txtIndeks.grid(row=1, column=3, padx=10, pady=10, sticky="w")

        # Predmet
        ctk.CTkLabel(entries_frame, text="Predmet", font=("Calibri", 16), text_color="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.txtPredmet = ctk.CTkEntry(entries_frame, textvariable=self.predmet, font=("Calibri", 16), width=300)
        self.txtPredmet.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Ocjena
        ctk.CTkLabel(entries_frame, text="Ocjena", font=("Calibri", 16), text_color="white").grid(row=2, column=2, padx=10, pady=10, sticky="w")
        self.txtOcjena = ctk.CTkEntry(entries_frame, textvariable=self.ocjena, font=("Calibri", 16), width=300)
        self.txtOcjena.grid(row=2, column=3, padx=10, pady=10, sticky="w")

        # Dugmad za operacije
        btn_frame = ctk.CTkFrame(entries_frame, fg_color="#535c68")
        btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")

        ctk.CTkButton(btn_frame, command=self.add_student, text="Add Details", width=150, font=("Calibri", 16)).grid(row=0, column=0, padx=10)
        ctk.CTkButton(btn_frame, command=self.update_student, text="Update Details", width=150, font=("Calibri", 16)).grid(row=0, column=1, padx=10)
        ctk.CTkButton(btn_frame, command=self.delete_student, text="Delete Details", width=150, font=("Calibri", 16)).grid(row=0, column=2, padx=10)
        ctk.CTkButton(btn_frame, command=self.clear_all, text="Clear Details", width=150, font=("Calibri", 16)).grid(row=0, column=3, padx=10)

        # Sekcija sa tabelom
        tree_frame = ctk.CTkFrame(self, fg_color="#ecf0f1")
        tree_frame.pack(side="top", fill="both", expand=True)

        # Stil tabele
        style = ttk.Style()
        style.configure("mystyle.Treeview", font=('Calibri', 16), rowheight=40)
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))

        # Definisanje kolona u tabeli
        self.tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
        self.tv.heading("1", text="ID")
        self.tv.heading("2", text="Ime")
        self.tv.heading("3", text="Indeks")
        self.tv.heading("4", text="Predmet")
        self.tv.heading("5", text="Ocjena")
        self.tv['show'] = 'headings'

        # Podešavanje širine kolona
        self.tv.column("1", width=30)
        self.tv.column("2", width=60)
        self.tv.column("3", width=100)
        self.tv.column("4", width=80)

        # Kada korisnik klikne na red – poziva se get_data()
        self.tv.bind("<ButtonRelease-1>", self.get_data)
        self.tv.pack(fill="both", expand=True)

    # Učitavanje podataka iz selektovanog reda u polja
    def get_data(self, event):
        selected_row = self.tv.focus()
        data = self.tv.item(selected_row)
        self.row = data["values"]

        if self.row:
            self.ime.set(self.row[1])
            self.indeks.set(self.row[2])
            self.predmet.set(self.row[3])
            self.ocjena.set(self.row[4])

    # Prikaz svih zaposlenih iz baze
    def dispaly_all(self):
        self.tv.delete(*self.tv.get_children())
        for row in self.db.fetch():
            self.tv.insert("", "end", values=row)

    # Dodavanje zaposlenog
    def add_student(self):
        if not all([self.ime.get(), self.indeks.get(), self.predmet.get(), self.ocjena.get()]):
            messagebox.showerror("Error", "Please fill all the fields")
            return
        self.db.insert(self.ime.get(), self.indeks.get(), self.predmet.get(), self.ocjena.get())
        messagebox.showinfo("Success", "Record Inserted")
        self.clear_all()
        self.dispaly_all()

    # Ažuriranje podataka
    def update_student(self):
        if not all([self.ime.get(), self.indeks.get(), self.predmet.get(), self.ocjena.get()]):
            messagebox.showerror("Error", "Please fill all the fields")
            return
        self.db.update(self.row[0], self.ime.get(), self.indeks.get(), self.predmet.get(), self.ocjena.get())
        messagebox.showinfo("Success", "Record Updated")
        self.clear_all()
        self.dispaly_all()

    # Brisanje zaposlenog
    def delete_student(self):
        self.db.remove(self.row[0])
        self.clear_all()
        self.dispaly_all()

    # Reset svih polja
    def clear_all(self):
        for var in [self.ime.get(), self.indeks.get(), self.predmet.get(), self.ocjena.get()]:
            var.set("")
        self.txtAddress.delete("1.0", "end")


# Pokretanje aplikacije
if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # može i "light"
    ctk.set_default_color_theme("blue")
    app = StudentApp()
    app.mainloop()
