import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import cx_Oracle


from tkinter import messagebox

def IntCheck(Value, zina): 
    try:
        intValue = int(Value)
        return True
    except ValueError:
        messagebox.showinfo(title="Kļūda", message=zina)
        return False

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SKLAD")
        self.root.geometry("1280x720")
        self.root.resizable(False, False)
        self.root.configure(bg='#c7c7c7')
        
        self.image = Image.open("Sklad_icon.png").resize((250,188))
        self.image = ImageTk.PhotoImage(self.image)
        
        self.image_label = tk.Label(self.root, image = self.image, bd=0)
        self.image_label.place(x=540, y=100)
        
        self.btnIeietNolik = tk.Button(self.root, text="Ieiet kā noliktavas darbinieks", font=('Arial',16), bg='#819d68', command=self.IeietNolik) 
        self.btnIeietNolik.place(x=100, y=500)

        self.btnIeietRazot = tk.Button(self.root, text="Ieiet kā ražotnes darbinieks", font=('Arial',16), bg='#819d68', command=self.IeietRazot)
        self.btnIeietRazot.place(x=530, y=500)
        
        self.btnIeietAdmin = tk.Button(self.root, text="Ieiet kā administrators", font=('Arial',16), bg='#819d68', command=self.IeietAdmin)
        self.btnIeietAdmin.place(x=950, y=500)
        

        self.root.mainloop()
        
    def TiritGalveno(self):
        self.btnIeietNolik.place_forget()
        self.btnIeietRazot.place_forget()
        self.btnIeietAdmin.place_forget()
        self.image_label.place(x=5, y=5)
        
    def IzdzestLoginSkats(self):
        self.labelLietID.destroy()
        self.labelParole.destroy()
        self.textBoxLietID.destroy()
        self.textBoxParole.destroy()
        self.btnIenakt.destroy()
        self.labelNoraidits.destroy()
        self.btnAtgriezties.destroy()
        
        
    def AtgrieztGalveno(self):
        self.IzdzestLoginSkats()
        self.image_label.place(x=540, y=100)
        self.btnIeietNolik.place(x=100, y=500)
        self.btnIeietRazot.place(x=530, y=500)
        self.btnIeietAdmin.place(x=950, y=500)
        self.userType = None
        
    
    def BuvetLoginSkats(self):     
        self.labelLietID = tk.Label(self.root, text="Lietotāja ID", font=('Arial', 16), bg='#c7c7c7')
        self.labelLietID.place(x=380, y=300)
        
        self.labelParole = tk.Label(self.root, text="Parole", font=('Arial', 16), bg='#c7c7c7')
        self.labelParole.place(x=427, y=340)
        
        self.textBoxLietID = tk.Text(self.root, height=1, width = 25, font=('Arial', 16))
        self.textBoxLietID.place(x=500, y=300)
        
        self.textBoxParole = tk.Text(self.root, height=1, width = 25, font=('Arial', 16))
        self.textBoxParole.place(x=500, y=340)
        
        self.btnIenakt = tk.Button(self.root, text="Ienākt", width = 15, font=('Arial', 16), bg='#819d68', command=self.LoginCheck)
        self.btnIenakt.place(x=555, y=400)
        
        self.labelNoraidits = tk.Label(self.root, font=('Arial', 16), fg='red', bg='#c7c7c7')
        self.labelNoraidits.place(x=535,y=450)
        
        self.btnAtgriezties = tk.Button(self.root, text="Atgriezties", width = 10, font=('Arial', 16), bg='#819d68', command=self.AtgrieztGalveno)
        self.btnAtgriezties.place(x=1100, y=590)        
        
    def IeietNolik(self):
        self.TiritGalveno()
        self.BuvetLoginSkats()     
        self.userType = 'Noliktavas darbinieks'
        
    def IeietRazot(self):
        self.TiritGalveno()
        self.BuvetLoginSkats() 
        self.userType = 'Ražotnes darbinieks'
        
    def IeietAdmin(self):
        self.TiritGalveno()
        self.BuvetLoginSkats() 
        self.userType = 'Admin'
        
    def LoginCheck(self):
        login = self.textBoxLietID.get('1.0', tk.END).strip()
        parole = self.textBoxParole.get('1.0', tk.END).strip()

        zina = "Lietotāja ID var būt tikai skaitlis!"
        if (not IntCheck(login, zina)):                             
            return
        
        login = int(login)
        
        sqlText = 'SELECT ID, PAROLE, TIPS FROM PROFILI WHERE ID = :1 AND PAROLE = :2 AND TIPS = :3'
        cur.execute(sqlText, (login, parole, self.userType))
            
        profils = cur.fetchone()

        if profils:
            print('success')
            self.userID = profils[0]
            if self.userType == 'Noliktavas darbinieks':
                self.IzdzestLoginSkats()
                self.SakumsNolik()
            elif self.userType == 'Ražotnes darbinieks':
                self.IzdzestLoginSkats()
                self.SakumsRazot()
            elif self.userType == 'Admin':
                self.IzdzestLoginSkats()
                self.BuvetSakumsAdminSkats()
        else:
            self.labelNoraidits.config(text='Neizdevās ieiet sistēmā')
                
    def Sveiciens(self):
        sqlText = 'SELECT VARDS, UZVARDS FROM PROFILI WHERE ID = :1'
        cur.execute(sqlText, (self.userID,))
        pilnais_vards = cur.fetchall()
        vards = pilnais_vards[0][0]
        uzvards = pilnais_vards[0][1]
        self.labelSveiciens = tk.Label(self.root, text=f"Sveiks, {vards} {uzvards}!", font=('Arial', 20), bg='#c7c7c7')
        self.labelSveiciens.place(x=500,y=70)
        
    def DzestSveiciens(self):
        self.labelSveiciens.destroy()
                
    def SakumsNolik(self):
        return
    
    def SakumsRazot(self):
        return
    
    def BuvetSakumsAdminSkats(self): 
        self.Sveiciens()
        
        self.btnIzveidotLiet= tk.Button(self.root, text="Izveidot lietotāju", width=15, font=('Arial',16), bg='#819d68', command=self.IeietIzveidotLiet) 
        self.btnIzveidotLiet.place(x=450, y=400)

        self.btnDzestLiet = tk.Button(self.root, text="Dzēst lietotāju", width=15, font=('Arial',16), bg='#819d68', command=self.IeietDzestLiet)
        self.btnDzestLiet.place(x=680, y=400)
        
        self.btnRedigetLiet = tk.Button(self.root, text="Rediģēt lietotāju", width=15, font=('Arial',16), bg='#819d68')
        self.btnRedigetLiet.place(x=450, y=500)
        
        self.btnAudits = tk.Button(self.root, text="Skatīt auditu", width=15, font=('Arial',16), bg='#819d68')
        self.btnAudits.place(x=680, y=500)
        
        self.btnIziet = tk.Button(self.root, text="Iziet", width=10, font=('Arial',16), bg='#819d68', command=self.IzietNoSakumsAdmin)
        self.btnIziet.place(x=1100, y=590)
    
    def IzdzestSakumsAdminSkats(self):
        self.DzestSveiciens()
        self.btnIzveidotLiet.destroy()
        self.btnDzestLiet.destroy()
        self.btnRedigetLiet.destroy()
        self.btnAudits.destroy()
        self.btnIziet.destroy()
        
    def IzietNoSakumsAdmin(self):
        self.IzdzestSakumsAdminSkats()
        self.userID = None
        self.BuvetLoginSkats()

        
    def NakamaisID(self):
        sqlText = 'SELECT ID FROM PROFILI'
        cur.execute(sqlText)
        IDSaraksts = [row[0] for row in cur.fetchall()]       
        indekss = 2
        while True:
            if indekss not in IDSaraksts:
                return indekss
            else:
                indekss+=1
                    
    def PievienotLietCheck(self):
        vards = self.textBoxVards.get('1.0', tk.END).strip()
        uzvards = self.textBoxUzvards.get('1.0', tk.END).strip()
        epasts = self.textBoxEpasts.get('1.0', tk.END).strip()
        parole = self.textBoxParole.get('1.0', tk.END).strip()
        darbavieta = self.textBoxDarbavieta.get('1.0', tk.END).strip()
        loma = self.dropDownLoma.get()
        if not vards:
            self.labelRezultats.config(text="Vārds ir obligāts!", fg='red')
            return
        if not uzvards:
            self.labelRezultats.config(text="Uzvārds ir obligāts!", fg='red')
            return
        if not parole:
            self.labelRezultats.config(text="Parole ir obligāta!", fg='red')
            return
        if not loma:
            self.labelRezultats.config(text="Loma ir obligāta!", fg='red')
            return
        if len(vards) > 50:
            self.labelRezultats.config(text="Vārds ir pārāk garš!", fg='red')
            return
        if len(uzvards) > 50:
            self.labelRezultats.config(text="Uzvārds ir pārāk garš!", fg='red')
            return
        if len(epasts) > 100:
            self.labelRezultats.config(text="E-pasts ir pārāk garš!", fg='red')
            return
        if len(parole) > 30:
            self.labelRezultats.config(text="Parole ir pārāk gara!", fg='red')
            return
        if len(darbavieta) > 100:
            self.labelRezultats.config(text="Darbavieta ir pārāk gara!", fg='red')
            return
        if not darbavieta and loma!= "Admin":
            self.labelRezultats.config(text="Darbavieta nenorādāma tikai administratoriem!", fg='red')
            return
        if darbavieta and loma=="Admin":
            self.labelRezultats.config(text="Administratoriem darbavietu nenorādīt!", fg='red')
            return
        
        ID = int(self.NakamaisID())
        sqlText = 'INSERT INTO PROFILI VALUES (:1, :2, :3, :4, :5, :6, :7)'
        if epasts and loma!="Admin":
            cur.execute(sqlText, (ID, vards, uzvards, epasts, parole, darbavieta, loma))
            conn.commit()
        elif epasts and loma=="Admin":
            cur.execute(sqlText, (ID, vards, uzvards, epasts, parole, None, loma))
            conn.commit()
        elif not epasts and loma!="Admin":
            cur.execute(sqlText, (ID, vards, uzvards, None, parole, darbavieta, loma))
            conn.commit()
        elif not epasts and loma=="Admin":
            cur.execute(sqlText, (ID, vards, uzvards, None, parole, None, loma))
            conn.commit()            
          
        
        self.labelRezultats.config(text=f"Lietotājs ar ID {ID} veiksmīgi pievienots", fg='green')
        self.labelNakamaisID.config(text="Piešķiramais ID: " + str(self.NakamaisID()))
            
        
    def BuvetIzveidotLietSkats(self):   
        self.labelNakamaisID = tk.Label(self.root, text="Piešķiramais ID: " + str(self.NakamaisID()), font=('Arial', 20), bg='#c7c7c7')
        self.labelNakamaisID.place(x=538, y=100)
        
        self.labelVards = tk.Label(self.root, text="Vārds", font=('Arial',16), bg='#c7c7c7')
        self.labelVards.place(x=438, y=160)
        
        self.textBoxVards = tk.Text(self.root, height=1, width = 25, font=('Arial', 16))
        self.textBoxVards.place(x=500, y=160)
        
        self.labelUzvards = tk.Label(self.root, text="Uzvārds", font=('Arial',16), bg='#c7c7c7')
        self.labelUzvards.place(x=417, y=200)
        
        self.textBoxUzvards = tk.Text(self.root, height=1, width = 25, font=('Arial', 16))
        self.textBoxUzvards.place(x=500, y=200)
        
        self.labelEpasts = tk.Label(self.root, text="E-pasts", font=('Arial',16), bg='#c7c7c7')
        self.labelEpasts.place(x=420, y=240)
        
        self.textBoxEpasts = tk.Text(self.root, height=1, width = 25, font=('Arial', 16))
        self.textBoxEpasts.place(x=500, y=240)
        
        self.labelParole = tk.Label(self.root, text="Parole", font=('Arial',16), bg='#c7c7c7')
        self.labelParole.place(x=431, y=280)
        
        self.textBoxParole = tk.Text(self.root, height=1, width = 25, font=('Arial', 16))
        self.textBoxParole.place(x=500, y=280)
        
        self.labelDarbavieta = tk.Label(self.root, text="Darbavieta", font=('Arial',16), bg='#c7c7c7')
        self.labelDarbavieta.place(x=389, y=320)
        
        self.textBoxDarbavieta = tk.Text(self.root, height=1, width = 25, font=('Arial', 16))
        self.textBoxDarbavieta.place(x=500, y=320)
        
        self.labelLoma = tk.Label(self.root, text="Loma", font=('Arial',16), bg='#c7c7c7')
        self.labelLoma.place(x=440, y=360)
        
        lomas = ["Admin", "Noliktavas darbinieks", "Ražotnes darbinieks"]
        self.dropDownLoma = ttk.Combobox(self.root, height=1, width = 25, font=('Arial',16), values=lomas, state="readonly")
        self.dropDownLoma.place(x=500, y=360)
        
        self.btnAtcelt = tk.Button(self.root, text="Atcelt", width=10, font=('Arial',16), bg='#819d68', command=self.IzietNoIzveidotLiet)
        self.btnAtcelt.place(x=1100, y=590)
        
        self.btnPievienotLiet = tk.Button(self.root, text="Pievienot", width=10, font=('Arial',16), bg='#819d68', command=self.PievienotLietCheck)
        self.btnPievienotLiet.place(x=585, y=400)
        
        self.labelRezultats = tk.Label(self.root, font=('Arial', 16), bg='#c7c7c7')
        self.labelRezultats.place(x=500, y=480)
        
    def IeietIzveidotLiet(self):
        self.IzdzestSakumsAdminSkats()
        self.BuvetIzveidotLietSkats()

    def IzdzestIzveidotLietSkats(self):
        self.labelNakamaisID.destroy()
        self.labelVards.destroy()
        self.textBoxVards.destroy()
        self.labelUzvards.destroy()
        self.textBoxUzvards.destroy()
        self.labelEpasts.destroy()
        self.textBoxEpasts.destroy()
        self.labelParole.destroy()
        self.textBoxParole.destroy()
        self.labelDarbavieta.destroy()
        self.textBoxDarbavieta.destroy()
        self.labelLoma.destroy()
        self.dropDownLoma.destroy()
        self.btnAtcelt.destroy()
        self.btnPievienotLiet.destroy()
        self.labelRezultats.destroy()
        
        
    def IzietNoIzveidotLiet(self):
        self.IzdzestIzveidotLietSkats()
        self.BuvetSakumsAdminSkats()
        


    def AtrastPecID(self):
        ID = self.textBoxID.get('1.0', tk.END).strip()
        zina = "Lietotāja ID var būt tikai skaitlis!"
        if (not IntCheck(ID, zina)):                             
            return  
        ID = int(ID)
        sqlText = 'SELECT VARDS, UZVARDS FROM PROFILI WHERE ID = :1'
        cur.execute(sqlText, (ID,))
        profils = cur.fetchone()

        if profils:
            self.labelRezultats.config(text=f"Vārds = {profils[0]}, uzvārds = {profils[1]}", fg='black')
        else:
            self.labelRezultats.config(text='Lietotājs neeksistē!', fg='red')
            
    def DzestLiet(self):
        ID = self.textBoxID.get('1.0', tk.END).strip()
        zina = "Lietotāja ID var būt tikai skaitlis!"
        if (not IntCheck(ID, zina)):                             
            return
        ID = int(ID)
        sqlText = 'SELECT ID, TIPS FROM PROFILI WHERE ID = :1'
        cur.execute(sqlText, (ID,))
        profils = cur.fetchone()

        if not profils:
            self.labelRezultats.config(text='Lietotājs neeksistē!', fg='red')
            return
        if ID == 1:
            self.labelRezultats.config(text='Lietotāju nedrīkst izdzēst!', fg='red')
            return
        if ID == self.userID:
            self.labelRezultats.config(text='Pats savu profilu nevar izdzēst!', fg='red')
            return
        if profils[1] == 'Admin' and self.userID != 1:
            self.labelRezultats.config(text='Administratorus drīkst dzēst tikai galvenais administrators!', fg='red')
            return
        
        sqlText = 'DELETE FROM PROFILI WHERE ID = :1'
        cur.execute(sqlText, (ID,))
        conn.commit()
        self.labelRezultats.config(text=f'Lietotājs ar ID {ID} veiksmīgi idzēsts', fg='green')
        
        
        
    def BuvetDzestLietSkats(self):   
        self.labelID = tk.Label(self.root, text="Lietotāja ID", font=('Arial',16), bg='#c7c7c7')
        self.labelID.place(x=385, y=360)
        
        self.textBoxID = tk.Text(self.root, height=1, width = 25, font=('Arial', 16))
        self.textBoxID.place(x=500, y=360)
        
        self.btnAtcelt = tk.Button(self.root, text="Atcelt", width=10, font=('Arial',16), bg='#819d68', command=self.IzietNoDzestLiet)
        self.btnAtcelt.place(x=1100, y=590)
        
        self.btnAtrast = tk.Button(self.root, text="Atrast", width=10, font=('Arial',16), bg='#819d68', command=self.AtrastPecID)
        self.btnAtrast.place(x=585, y=400)
        
        self.btnDzestLiet = tk.Button(self.root, text="Dzēst", width=10, font=('Arial',16), bg='#819d68', command=self.DzestLiet)
        self.btnDzestLiet.place(x=585, y=460)
        
        self.labelRezultats = tk.Label(self.root, font=('Arial', 16), bg='#c7c7c7')
        self.labelRezultats.place(x=500, y=530)
        
    def IeietDzestLiet(self):
        self.IzdzestSakumsAdminSkats()
        self.BuvetDzestLietSkats()
        
    def IzdzestDzestLietSkats(self):
        self.labelID.destroy()
        self.textBoxID.destroy()
        self.btnAtcelt.destroy()
        self.btnAtrast.destroy()
        self.btnDzestLiet.destroy()
        self.labelRezultats.destroy()
        
    def IzietNoDzestLiet(self):
        self.IzdzestDzestLietSkats()
        self.BuvetSakumsAdminSkats()
        
def main():
    conStr = 'C##SKLADUSER/Sklad_password@localhost:1521/orcl'
    global conn
    conn = cx_Oracle.connect(conStr)
    global cur
    cur = conn.cursor()
    
    MyGUI()
    
    cur.close()
    conn.close()
    
 
if __name__ == "__main__":
    main()
