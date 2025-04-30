#1.Zadatak
import customtkinter
import csv
import os
class EntryFrame(customtkinter.CTkFrame):#fronted
    def __init__(self,master):
        super().__init__(master)
        self.grid_columnconfigure(1,weight=1)

        self.label_naziv=customtkinter.CTkLabel(self,text="Naziv:")
        self.label_naziv.grid(row=0,column=0,padx=10,pady=5,sticky="e")
        self.entry_naziv=customtkinter.CTkEntry(self)
        self.entry_naziv.grid(row=0,column=1,padx=10,pady=5,sticky="ew")

        self.label_reziser=customtkinter.CTkLabel(self,text="Reziser:")
        self.label_reziser.grid(row=1,column=0,padx=10,pady=5,sticky="e")
        self.entry_reziser=customtkinter.CTkEntry(self)
        self.entry_reziser.grid(row=1,column=1,padx=10,pady=5,sticky="ew")

        self.label_zanr=customtkinter.CTkLabel(self,text="Zanr:")
        self.label_zanr.grid(row=2,column=0,padx=10,pady=5,sticky="e")
        self.entry_zanr=customtkinter.CTkEntry(self)
        self.entry_zanr.grid(row=2,column=1,padx=10,pady=5,sticky="ew")

        self.label_ocjena=customtkinter.CTkLabel(self,text="Ocjena:")
        self.label_ocjena.grid(row=3,column=0,padx=10,pady=5,sticky="e")
        self.slider_ocjena=customtkinter.CTkSlider(self,from_=1,to=10,number_of_steps=9)
        self.slider_ocjena.set(5)
        self.slider_ocjena.grid(row=3,column=1,padx=10,pady=5,sticky="ew")

        self.label_ocjena_vrijednost=customtkinter.CTkLabel(self,text="5.0")
        self.label_ocjena_vrijednost.grid(row=4,column=1,padx=10,pady=5,sticky="ew")

        self.slider_ocjena.configure(command=self.promjeni_ocjenu_label)#fja se pozove na promjenu vrijednosti slajdera

    def get(self):
        return{
            "Naziv":self.entry_naziv.get(),
            "Reziser":self.entry_reziser.get(),
            "Zanr":self.entry_zanr.get(),
            "Ocjena":str(round(self.slider_ocjena.get(),1))
        }
    def set(self,data):
        self.entry_naziv.delete(0,"end")
        self.entry_naziv.insert(0,data["Naziv"])
        self.entry_reziser.delete(0,"end")
        self.entry_reziser.insert(0,data["Reziser"])
        self.entry_zanr.delete(0,"end")
        self.entry_zanr.insert(0,data["Zanr"])
        self.slider_ocjena.set(float(data["Ocjena"]))
        self.label_ocjena_vrijednost.configure(text=data["Ocjena"])

    def promjeni_ocjenu_label(self,vrijednost):
        self.label_ocjena_vrijednost.configure(text=f"{round(float(vrijednost),1)}")
class FilmListFrame(customtkinter.CTkScrollableFrame):
    def __init__(self,master,callback):
        super().__init__(master,width=400,height=250)
        self.callback=callback
        self.buttons=[]

    def update_list(self,filmovi):
        for widget in self.winfo_children():
            widget.destroy()
        self.buttons.clear()
        for i, film in enumerate(filmovi):
            tekst=f"{film['Naziv']}|{film['Reziser']} | {film['Zanr']} | {film['Ocjena']}"
            btn=customtkinter.CTkButton(self,text=tekst,anchor="w",width=380,command=lambda i=i:self.callback(i))
            btn.grid(row=i,column=0,padx=5,pady=5,sticky="w")
            self.buttons.append(btn)

class Aplikacija(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Menadzer filmova")
        self.geometry("500x700")

        self.filmovi=self.ucitaj_filmove()
        self.odabrani=None
        
        self.entry_frame=EntryFrame(self)
        self.entry_frame.grid(row=0,column=0,padx=20,pady=10,sticky="ew")

        self.lista_frame=FilmListFrame(self,self.odaberi_film)
        self.lista_frame.grid(row=1,column=0,padx=20,pady=10,sticky="ew")

        self.dugme_dodaj=customtkinter.CTkButton(self,text="Dodaj",command=self.dodaj_film)
        self.dugme_dodaj.grid(row=2,column=0,padx=20,pady=10,sticky="ew")

        self.dugme_izmjeni=customtkinter.CTkButton(self,text="Izmjeni",command=self.izmijeni_film)
        self.dugme_izmjeni.grid(row=3,column=0,padx=20,pady=10,sticky="ew")

        self.dugme_obrisi=customtkinter.CTkButton(self,text="Obrisi",command=self.obrisi_film)
        self.dugme_obrisi.grid(row=4,column=0,padx=20,pady=10,sticky="ew")

        self.dugme_ocisti=customtkinter.CTkButton(self,text="Ocisti",command=self.ocisti_sva_polja)
        self.dugme_ocisti.grid(row=5,column=0,padx=20,pady=10,sticky="ew")

        self.lista_frame.update_list(self.filmovi)
        

    def ucitaj_filmove(self):
        if not os.path.exists("filmovi.csv"):#da je u parent folderu ../
            return[]
        fajl=open("filmovi.csv",encoding="utf-8")
        filmovi=list(csv.DictReader(fajl))
        fajl.close()
        return filmovi
        
    def sacuvaj_filmove(self):
        fajl=open("filmovi.csv","w", newline='',encoding='utf-8')
        polja=["Naziv","Reziser","Zanr","Ocjena"]
        unos=csv.DictWriter(fajl,fieldnames=polja)
        unos.writeheader()
        unos.writerows(self.filmovi)
        fajl.close()
    def dodaj_film(self):
        novi_film=self.entry_frame.get()
        if all(novi_film.values()):
            self.filmovi.append(novi_film)
            self.sacuvaj_filmove()
            self.lista_frame.update_list(self.filmovi)
        else:
            print ("Greska. Sva polja moraju biti popunjena.")
    def izmijeni_film(self):
        if self.odabrani is not None:
            novi_film=self.entry_frame.get()
            if all(novi_film.values()):
                self.filmovi[self.odabrani]=novi_film
                self.sacuvaj_filmove()
                self.lista_frame.update_list(self.filmovi)
            else:
                print("Sva polja moraju biti popunjena")
    def odaberi_film(self,indeks):
        self.odabrani=indeks
        self.entry_frame.set(self.filmovi[indeks])
    def obrisi_film(self):
        if self.odaberi_film is not None:
            del self.filmovi[self.odabrani]
            self.odabrani=None
            self.sacuvaj_filmove()
            self.lista_frame.update_list(self.filmovi)
    def ocisti_sva_polja(self):
        self.entry_frame.entry_naziv.delete(0,"end")
        self.entry_frame.entry_reziser.delete(0,"end")
        self.entry_frame.entry_zanr.delete(0,"end")
        self.entry_frame.slider_ocjena.set(5)
        self.entry_frame.label_ocjena_vrijednost.configure(text="5.00")

app=Aplikacija()
app.mainloop()
