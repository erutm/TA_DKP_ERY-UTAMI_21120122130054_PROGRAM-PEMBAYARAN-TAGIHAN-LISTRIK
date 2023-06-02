from tkinter import * 
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


class TagihanListrik():
    def __init__(self, daya, golongan, harga, KWhawal, KWhakhir, totalM, tagihan, uang, admin):
        self.daya = daya
        self.golongan = golongan
        self.harga = harga
        self.KWhawal = KWhawal
        self.KWhakhir = KWhakhir
        self.totalM = totalM
        self.tagihan = tagihan
        self.uang = uang
        self.admin = admin
        
    def getDaya(self):
        return self.daya
    def getGolongan(self):
        return self.golongan
    def getHarga(self):
        return self.harga
    def getKWhawal(self):
        return self.KWhawal
    def getKWhakhir(self):
        return self.KWhakhir
    def getTotalM(self):
        return self.totalM
    def getTagihan(self):
        return self.tagihan
    def getUang(self):
        return self.uang
    def getAdmin(self):
        return self.admin
        

Listrik1 = TagihanListrik("", "", 0, 0, 0, 0, 0, 0, 0)
def masuk():
    napel = inputnapel.get()
    idpel = inputnoid.get()
    if(napel == "Ery Utami" and idpel == "23478890123"):
        messagebox.showinfo("Correct", "ID Pelanggan dan Nama Pelanggan Benar!")
        return
    elif(napel == "" and idpel == ""):
        messagebox.showwarning("Warning", "Masukkan ID Pelanggan dan Nama Pelanggan Dahulu!")
        return
    else:
        messagebox.showwarning("Incorrect","ID Pelanggan dan Nama Pelanggan Salah! Mohon Ulangi Lagi!")
        return
    

def daya_listrik():
    global totaltagihan
    KWh_awal = Listrik1.getKWhawal()
    KWh_akhir = Listrik1.getKWhakhir() 
    KWh_awal = inputawal.get()
    KWh_akhir = inputakhir.get()

    napel = inputnapel.get()
    idpel = inputnoid.get()

    if napel == "" or idpel == "":
        messagebox.showwarning("Warning", "Masukkan ID Pelanggan dan Nama Pelanggan Dahulu!")
    else:
        inputawal.config(state="normal")
        inputakhir.config(state="normal")

    harga = Listrik1.getHarga()
    golongan = Listrik1.getGolongan()
    if strhobi.get() == "450VA":
        harga = "\t\tRp 415"
        golongan = "\t\tR-1/TR"
        biaya_admin = "\t\tRp 3000"
        pengali = 415
        admin = 3000
    elif strhobi.get() == "900VA":
        harga = "\t\tRp 1352"
        golongan = "\t\tR-1/TR"
        biaya_admin = "\t\tRp 5000"
        pengali = 1352
        admin = 5000
    elif strhobi.get() == "1300VA":
        harga = "\t\tRp 1444"
        golongan = "\t\tR-1/TR"
        biaya_admin = "\t\tRp 7000"
        pengali = 1444
        admin = 7000
    elif strhobi.get() == "2200VA":
        harga = "\t\tRp 1444"
        golongan = "\t\tR-1/TR"
        biaya_admin = "\t\tRp 9000"
        pengali = 1444
        admin = 9000
    elif strhobi.get() == "3500VA":
        harga = "\t\tRp 1699"
        golongan = "\t\tR-2/TR"
        biaya_admin = "\t\tRp 11000"
        pengali = 1699
        admin = 11000

    if KWh_awal == "" and KWh_akhir == "":
        messagebox.showwarning("Warning", "KWh Awal dan KWh Akhir Harap Diisi!")
    elif int(KWh_awal) < 0 or int(KWh_akhir) < 0:
        messagebox.showwarning("Warning", "KWh Awal dan KWh Akhir Harus Bernilai Positif!")
    elif int(KWh_awal) >= int(KWh_akhir):
        messagebox.showwarning("Warning", "KWh Akhir Harus Lebih Besar dari KWh Awal")
    elif int(KWh_akhir) > int(KWh_awal):
        totalmeter = (int(KWh_akhir) - int(KWh_awal))
        totaltagihan = (totalmeter * pengali) + admin
    print(totalmeter)
    print(totaltagihan)
    print(harga)
    print(biaya_admin)
    print(golongan)
    labelhkwh = ttk.Label(text = "Harga / KWh\t:" +str(harga), background = "#ffff00")
    labelhkwh.place(x = 10, y = 300)
    labeladmin = ttk.Label(text = "Biaya Admin\t:" +str(biaya_admin), background = "#ffff00")
    labeladmin.place(x = 10, y = 330)
    labelgol = ttk.Label(text = "Golongan\t:" +str(golongan), background = "#ffff00")
    labelgol.place(x = 10, y = 360)
    labelmeter = ttk.Label(text = "Total Meter\t:\t\t" +str(totalmeter), background = "#ffff00")
    labelmeter.place(x = 10, y = 390)
    labeltag = ttk.Label(text = "Total Tagihan\t:\t\tRp " +str(totaltagihan), background = "#ffff00")
    labeltag.place(x = 10, y = 420)
 
def pembayaran():
    uang = Listrik1.getUang()
    uang = inputuang.get()
    if(uang == ""):
        messagebox.showwarning("Warning","Isi Uang Terlebih Dahulu!")
    elif(int(uang) < int(totaltagihan)):
        messagebox.showwarning("Warning","Uang Anda Kurang!")
    elif(int(uang) >= int(totaltagihan)):
        kembali = (int(uang) - int(totaltagihan))
    print(kembali)
    labelkembali = ttk.Label(text = "Uang Kembali\t:\t\tRp " +str(kembali), background = "#ffff00")
    labelkembali.place(x = 10, y = 530) 
    
def tutup_program():
    utama.destroy()
    messagebox.showinfo("Info", "Terima Kasih Telah Membayar Tepat Waktu!")

#tampilan utama
utama = tk.Tk()  
utama.geometry("700x650")
utama.resizable(False, False)
utama.title("Program Pembayaran Tagihan Listrik")
utama.config(background="#338A94")

#mengganti logo icon di windows tkinter
logo = PhotoImage(file = "Logo pln.png")
utama.iconphoto(False, logo)       

#label  
label = ttk.Label(text = "Pembayaran Tagihan Listrik", font = "impact 15", background = "red")
label.grid (row = 0, column = 0)
label.pack()
labelnapel = ttk.Label(text = "Nama Pelanggan\t:")
labelnapel.place(x = 10, y = 60) 

labelidpel = ttk.Label(text = "ID Pelanggan\t:")
labelidpel.place(x = 10, y = 90)

labeldaya = ttk.Label(text = "Pilih Daya Listrik\t:")
labeldaya.place(x = 10, y = 170)

labelawal = ttk.Label(text = "KWh Awal\t:")
labelawal.place(x = 10, y = 200)

labelakhir = ttk.Label(text = "KWh Akhir\t:")
labelakhir.place(x = 10, y = 230)

labelhkwh = ttk.Label(text = "Harga / KWh\t:")
labelhkwh.place(x = 10, y = 300)

labeladmin = ttk.Label(text = "Biaya Admin\t:")
labeladmin.place(x = 10, y = 330)

labelgol = ttk.Label(text = "Golongan\t:")
labelgol.place(x = 10, y = 360)

labelmeter = ttk.Label(text = "Total Meter\t:")
labelmeter.place(x = 10, y = 390)

labeltag = ttk.Label(text = "Total Tagihan\t:")
labeltag.place(x = 10, y = 420)

labeluang = ttk.Label(text = "Uang Anda\t:")
labeluang.place(x = 10, y = 460)

labelkembali = ttk.Label(text = "Uang Kembali\t:")
labelkembali.place(x = 10, y = 530)

#input  
napel = StringVar(utama)
inputnapel = ttk.Entry(utama, width = 55)
inputnapel.place(x = 200, y = 59) 

noid = IntVar(utama)
inputnoid = ttk.Entry(utama, width = 55)
inputnoid.place(x = 200, y = 89)  

KWh_awal=IntVar(utama)
inputawal = ttk.Entry(utama, width = 55, state="disabled")
inputawal.place(x = 200, y = 200)

KWh_akhir =IntVar(utama)
inputakhir = ttk.Entry(utama, width = 55, state="disabled")
inputakhir.place(x = 200, y = 230)

uang = DoubleVar(utama)
inputuang = ttk.Entry(utama, width = 55)
inputuang.place(x = 200, y = 460)

#combobox
strhobi = StringVar(value = "450VA") 
Cb1 = ttk.Combobox(utama, width = 7, textvariable = strhobi, state = "readonly")
Cb1.place(x = 200, y = 170)

#menambahkan daftar dropdown pada combobox
Cb1["value"] = ("450VA", "900VA", "1300VA", "2200VA", "3500VA") 

#button
button = ttk.Button(utama, command = masuk, text = "Check")
button.place(x = 460, y = 120)
button1 = ttk.Button(utama, command = daya_listrik, text = "Hitung")
button1.place(x = 460, y = 260)
button2 = ttk.Button(utama, command = pembayaran, text = "Bayar")
button2.place(x = 459, y = 490)
button3 = ttk.Button(utama, command = tutup_program, text = "Close", width = 20)
button3.place(x = 540, y = 600)

#untuk menampilkan tampilan dari GUI
utama.mainloop()
