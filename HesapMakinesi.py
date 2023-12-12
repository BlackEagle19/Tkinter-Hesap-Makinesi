import tkinter as tk
from PIL import Image,ImageTk

pencere=tk.Tk()
pencere.geometry("300x300")

sıfır=ImageTk.PhotoImage(Image.open("0_tusu.png"))
bir=ImageTk.PhotoImage(Image.open("1_tusu.png"))
iki=ImageTk.PhotoImage(Image.open("2_tusu.png"))
uc=ImageTk.PhotoImage(Image.open("3_tusu.png"))
dort=ImageTk.PhotoImage(Image.open("4_tusu.png"))
bes=ImageTk.PhotoImage(Image.open("5_tusu.png"))
alti=ImageTk.PhotoImage(Image.open("6_tusu.png"))
yedi=ImageTk.PhotoImage(Image.open("7_tusu.png"))
sekiz=ImageTk.PhotoImage(Image.open("8_tusu.png"))
dokuz=ImageTk.PhotoImage(Image.open("9_tusu.png"))
bolme=ImageTk.PhotoImage(Image.open("bolme_isareti.png"))
cikarma=ImageTk.PhotoImage(Image.open("cikarma_isareti.png"))
çarpma=ImageTk.PhotoImage(Image.open("çarpma_isareti.png"))
toplama=ImageTk.PhotoImage(Image.open("toplama_isareti.png"))
esittir=ImageTk.PhotoImage(Image.open("esittir_isareti.png"))

def basildi(deger):
    mevcut = giris_alani.get()
    giris_alani.delete(0, tk.END)
    giris_alani.insert(0, mevcut + deger)

def hesapla():
    try:
        sonuc = eval(giris_alani.get())
        giris_alani.delete(0, tk.END)
        giris_alani.insert(0, str(sonuc))
    except:
        giris_alani.delete(0, tk.END)
        giris_alani.insert(0, "Hata")

def temizle():
    giris_alani.delete(0, tk.END)


giris_alani = tk.Entry(pencere, width=35, borderwidth=5)
giris_alani.grid(row=0, columnspan=4, padx=10, pady=10)



# Temizle düğmesi
btntemizle = tk.Button(pencere, text='C', command=temizle)
btntemizle.grid(row=6, column=0)





btnsıfır=tk.Button(image=sıfır,command=lambda: basildi("0")) #basıldı fonksiyona taş gönderip çalıştır
btnbir=tk.Button(image=bir,command=lambda: basildi("1")) #basıldı fonksiyona taş gönderip çalıştır
btniki=tk.Button(image=iki,command=lambda: basildi("2")) #basıldı fonksiyona taş gönderip çalıştır
btnüç=tk.Button(image=uc,command=lambda: basildi("3")) #basıldı fonksiyona taş gönderip çalıştır
btndört=tk.Button(image=dort,command=lambda: basildi("4")) #basıldı fonksiyona taş gönderip çalıştır
btnbes=tk.Button(image=bes,command=lambda: basildi("5")) #basıldı fonksiyona taş gönderip çalıştır
btnaltı=tk.Button(image=alti,command=lambda: basildi("6")) #basıldı fonksiyona taş gönderip çalıştır
btnyedi=tk.Button(image=yedi,command=lambda: basildi("7")) #basıldı fonksiyona taş gönderip çalıştır
btnsekiz=tk.Button(image=sekiz,command=lambda: basildi("8")) #basıldı fonksiyona taş gönderip çalıştır
btndokuz=tk.Button(image=dokuz,command=lambda: basildi("9")) #basıldı fonksiyona taş gönderip çalıştır
btnbölme=tk.Button(image=bolme,command=lambda: basildi("/")) #basıldı fonksiyona taş gönderip çalıştır
btnçıkarma=tk.Button(image=cikarma,command=lambda: basildi("-")) #basıldı fonksiyona taş gönderip çalıştır
btnçarpma=tk.Button(image=çarpma,command=lambda: basildi("*")) #basıldı fonksiyona taş gönderip çalıştır
btneşittir=tk.Button(image=esittir,command=hesapla) #basıldı fonksiyona taş gönderip çalıştır
btntoplama=tk.Button(image=toplama,command=lambda: basildi("+")) #basıldı fonksiyona taş gönderip çalıştır



btnsıfır.grid(row=4, column=0, padx=5, pady=5)
btnbir.grid(row=3, column=0, padx=5, pady=5)
btniki.grid(row=3, column=1, padx=5, pady=5)
btnüç.grid(row=3, column=2, padx=5, pady=5)
btndört.grid(row=2, column=0, padx=5, pady=5)
btnbes.grid(row=2, column=1, padx=5, pady=5)
btnaltı.grid(row=2, column=2, padx=5, pady=5)
btnyedi.grid(row=1, column=0, padx=5, pady=5)
btnsekiz.grid(row=1, column=1, padx=5, pady=5)
btndokuz.grid(row=1, column=2, padx=5, pady=5)
btnbölme.grid(row=1, column=3, padx=5, pady=5)
btnçıkarma.grid(row=2, column=3, padx=5, pady=5)
btnçarpma.grid(row=3, column=3, padx=5, pady=5)
btneşittir.grid(row=4, column=3, padx=5, pady=5)
btntoplama.grid(row=4, column=1, columnspan=2, padx=5, pady=5, sticky="ew") # Toplama düğmesi iki sütunu kaplasın
btntemizle.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="ew") # Temizle düğmesi tüm sütunları kaplasın


pencere.mainloop()
