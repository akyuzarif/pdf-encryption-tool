"""
PDF Şifreleme Uygulaması (GUI)
Tarih: 2025
Yazar: arifakyuz.com

Bu uygulama, seçilen PDF dosyalarını belirlenen bir klasöre şifreli olarak kaydeder.
Kullanıcı arayüzü tkinter ile oluşturulmuş, PDF işlemleri için PyPDF2 kütüphanesi kullanılmıştır.
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
import webbrowser
import os

# PDF Dosyalarını Seçme Fonksiyonu
def pdf_seç():
    dosya_yolları = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    if dosya_yolları:
        pdf_yolu_var.set("\n".join(dosya_yolları))

# Çıktı Kaydetme Fonksiyonu
def kaydet_seç():
    çıktı_dizini = filedialog.askdirectory()
    if çıktı_dizini:
        çıktı_yolu_var.set(çıktı_dizini)

# PDF Şifreleme Fonksiyonu
def şifrele():
    girdi_pdf_yolları = pdf_yolu_var.get().split("\n")
    çıktı_dizini = çıktı_yolu_var.get()
    şifre = şifre_entry.get()

    if not girdi_pdf_yolları or not çıktı_dizini or not şifre:
        messagebox.showerror("Hata", "Lütfen tüm alanları doldurduğunuzdan emin olun!")
        return

    if len(şifre) < 6:
        messagebox.showerror("Hata", "Şifre en az 6 karakter olmalıdır!")
        return

    try:
        for girdi_pdf_yolu in girdi_pdf_yolları:
            if not os.path.isfile(girdi_pdf_yolu):
                continue

            çıktı_pdf_yolu = os.path.join(çıktı_dizini, f"şifreli_{os.path.basename(girdi_pdf_yolu)}")

            with open(girdi_pdf_yolu, "rb") as girdi_pdf:
                pdf_okuyucu = PyPDF2.PdfReader(girdi_pdf)
                pdf_yazıcı = PyPDF2.PdfWriter()

                for sayfa in range(len(pdf_okuyucu.pages)):
                    pdf_yazıcı.add_page(pdf_okuyucu.pages[sayfa])

                pdf_yazıcı.encrypt(şifre)

                with open(çıktı_pdf_yolu, "wb") as çıktı_pdf:
                    pdf_yazıcı.write(çıktı_pdf)

        messagebox.showinfo("Başarılı", "Tüm PDF dosyaları başarıyla şifrelendi.")
    
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

# Tkinter Arayüzü
root = tk.Tk()
root.title("PDF Şifreleme")
root.configure(bg="#f5f5f5")
root.geometry("700x400")
root.resizable(True, True)

pdf_yolu_var = tk.StringVar()
çıktı_yolu_var = tk.StringVar()

title_label = tk.Label(root, text="PDF Şifreleme", font=("Helvetica", 18, "bold"), bg="#f5f5f5", fg="#333")
title_label.grid(row=0, column=0, columnspan=3, pady=(10, 20))

root.grid_columnconfigure(0, weight=1, minsize=150)
root.grid_columnconfigure(1, weight=2, minsize=250)
root.grid_columnconfigure(2, weight=2, minsize=250)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)
root.grid_rowconfigure(3, weight=0)
root.grid_rowconfigure(4, weight=0)
root.grid_rowconfigure(5, weight=0)

pdf_seç_button = tk.Button(root, text="PDF Dosyalarını Seç", command=pdf_seç, width=20, height=2, bg="#E53935", fg="white", font=("Helvetica", 12), relief="flat", bd=0, padx=10, pady=5)
pdf_seç_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

pdf_yolu_label = tk.Label(root, text="Seçilen PDF Yolları:", bg="#f5f5f5", font=("Helvetica", 10))
pdf_yolu_label.grid(row=1, column=1, padx=10, pady=10, sticky="w")

pdf_yolu_frame = tk.Frame(root, bg="#f5f5f5")
pdf_yolu_frame.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

pdf_yolu_entry = tk.Entry(pdf_yolu_frame, textvariable=pdf_yolu_var, width=40, font=("Helvetica", 12), relief="solid", bd=1)
pdf_yolu_entry.pack(padx=10, pady=5)

şifre_label = tk.Label(root, text="Şifre:", bg="#f5f5f5", font=("Helvetica", 10))
şifre_label.grid(row=2, column=1, padx=10, pady=10, sticky="w")

şifre_frame = tk.Frame(root, bg="#f5f5f5")
şifre_frame.grid(row=2, column=2, padx=10, pady=10, sticky="ew")

şifre_entry = tk.Entry(şifre_frame, show="*", width=40, font=("Helvetica", 12), relief="solid", bd=1)
şifre_entry.pack(padx=10, pady=5)

kaydet_button = tk.Button(root, text="Farklı Kaydet", command=kaydet_seç, width=20, height=2, bg="#4CAF50", fg="white", font=("Helvetica", 12), relief="flat", bd=0, padx=10, pady=5)
kaydet_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

çıktı_yolu_label = tk.Label(root, text="Kaydedilecek Dosya Yolu:", bg="#f5f5f5", font=("Helvetica", 10))
çıktı_yolu_label.grid(row=3, column=1, padx=10, pady=10, sticky="w")

çıktı_yolu_frame = tk.Frame(root, bg="#f5f5f5")
çıktı_yolu_frame.grid(row=3, column=2, padx=10, pady=10, sticky="ew")

çıktı_yolu_entry = tk.Entry(çıktı_yolu_frame, textvariable=çıktı_yolu_var, width=40, font=("Helvetica", 12), relief="solid", bd=1)
çıktı_yolu_entry.pack(padx=10, pady=5)

şifrele_button = tk.Button(root, text="Şifrele", command=şifrele, width=20, height=2, bg="#2196F3", fg="white", font=("Helvetica", 12), relief="flat", bd=0, padx=10, pady=5)
şifrele_button.grid(row=4, column=0, columnspan=3, pady=20, sticky="ew")

footer_label = tk.Label(root, text="www.arifakyuz.com", fg="blue", cursor="hand2", bg="#f5f5f5", font=("Helvetica", 10))
footer_label.grid(row=5, column=0, columnspan=3, pady=10)
footer_label.bind("<Button-1>", lambda e: webbrowser.open("https://www.arifakyuz.com"))

root.mainloop()
