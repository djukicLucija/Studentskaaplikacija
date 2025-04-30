
#1 zadatak dugme i check boksovi
'''
import customtkinter
class Aplikacija(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title=("Moja aplikacija")
        self.grid_columnconfigure((0,1),weight=1)

        self.dugme=customtkinter.CTkButton(self,text="Klikni",command=self.dugme_callback)
        self.dugme.grid(row=1,column=0,padx=20,pady=20,sticky="ew",columnspan=2)

        self.checkbox_1=customtkinter.CTkCheckBox(self,text="Opcija1")
        self.checkbox_1.grid(row=0,column=0,padx=20,pady=20,sticky="W")

        self.checkbox_2=customtkinter.CTkCheckBox(self,text="Opcija2")
        self.checkbox_2.grid(row=0,column=1,padx=20,pady=20,sticky="W")
        
    def dugme_callback(self):
        print("dugme je pritisnuto")
    
    
app=Aplikacija()
app.mainloop()
'''

#2 zadatak
'''
import customtkinter
class MyCheckboxFrame(customtkinter.CTkFrame):
    def __init__(self,master,title,values):
        super().__init__(master)
        self.grid_columnconfigure(0,weight=1)
        self.values=values
        self.title=title
        self.checkboxes=[]
        self.title=customtkinter.CTkLabel(self,text=self.title,fg_color="gray",corner_radius=6)
        self.title.grid(row=0,colum=0,padx=10,pady=10,sticky="ew")
        for i, value in enumerate(self.values):
            checkbox=customtkinter.CTkCheckbox(self,text=value)
            checkbox.grid(row=i+1,column=0,padx=10,pady=10,sticky="w")
            self.checkboxes.append(checkbox)
    def get(self):
        checked_box=[]
        for checkbox in self.checkboxes:
            if checkbox in self.checkboxes:
                checked_box.append(checkbox.cget("text"))
        return checked_box
class Aplikacija(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Moja aplikacija")
        self.geometry("400x200")
        self.grid_columnconfigure((0,1),weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.checkbox_frame=MyCheckboxFrame(self,"Values",values=["value 1","value 2","value 3"])
        self.checkbox_frame.grid(row=0,colum=0,padx=10,pady=10,sticky="nsew")
        self.button=customtkinter.CTkButton(self,text="dugme",command=self.button_callback)
        self.button.grid(row1,column=0,padex=10,pady=10,sticky="ew",columnspan=2)
    def button_callback(self):
        print('checkbox_frame:',self.checkbox_frame.get())
app=Aplikacija()
app.mainloop()
'''