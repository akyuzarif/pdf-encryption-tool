"""
PDF Encryption Application (GUI)
Date: 2025
Author: arifakyuz.com

This application allows you to encrypt selected PDF files with a password and save them to a selected directory.
The GUI is built with Tkinter, and PDF handling is done using the PyPDF2 library.
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
import webbrowser
import os

# Function to select PDF files
def select_pdfs():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    if file_paths:
        pdf_paths_var.set("\n".join(file_paths))

# Function to select output directory
def select_output_folder():
    output_dir = filedialog.askdirectory()
    if output_dir:
        output_path_var.set(output_dir)

# Function to encrypt PDFs
def encrypt_pdfs():
    input_pdf_paths = pdf_paths_var.get().split("\n")
    output_dir = output_path_var.get()
    password = password_entry.get()

    if not input_pdf_paths or not output_dir or not password:
        messagebox.showerror("Error", "Please fill in all the fields!")
        return

    if len(password) < 6:
        messagebox.showerror("Error", "Password must be at least 6 characters!")
        return

    try:
        for input_pdf_path in input_pdf_paths:
            if not os.path.isfile(input_pdf_path):
                continue

            output_pdf_path = os.path.join(output_dir, f"encrypted_{os.path.basename(input_pdf_path)}")

            with open(input_pdf_path, "rb") as input_pdf:
                reader = PyPDF2.PdfReader(input_pdf)
                writer = PyPDF2.PdfWriter()

                for page in reader.pages:
                    writer.add_page(page)

                writer.encrypt(password)

                with open(output_pdf_path, "wb") as output_pdf:
                    writer.write(output_pdf)

        messagebox.showinfo("Success", "All PDF files have been successfully encrypted.")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Tkinter GUI setup
root = tk.Tk()
root.title("PDF Encryption")
root.configure(bg="#f5f5f5")
root.geometry("700x400")
root.resizable(True, True)

pdf_paths_var = tk.StringVar()
output_path_var = tk.StringVar()

title_label = tk.Label(root, text="PDF Encryption", font=("Helvetica", 18, "bold"), bg="#f5f5f5", fg="#333")
title_label.grid(row=0, column=0, columnspan=3, pady=(10, 20))

root.grid_columnconfigure(0, weight=1, minsize=150)
root.grid_columnconfigure(1, weight=2, minsize=250)
root.grid_columnconfigure(2, weight=2, minsize=250)

pdf_select_button = tk.Button(root, text="Select PDF Files", command=select_pdfs, width=20, height=2, bg="#E53935", fg="white", font=("Helvetica", 12), relief="flat", bd=0, padx=10, pady=5)
pdf_select_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

pdf_path_label = tk.Label(root, text="Selected PDF Paths:", bg="#f5f5f5", font=("Helvetica", 10))
pdf_path_label.grid(row=1, column=1, padx=10, pady=10, sticky="w")

pdf_path_frame = tk.Frame(root, bg="#f5f5f5")
pdf_path_frame.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

pdf_path_entry = tk.Entry(pdf_path_frame, textvariable=pdf_paths_var, width=40, font=("Helvetica", 12), relief="solid", bd=1)
pdf_path_entry.pack(padx=10, pady=5)

password_label = tk.Label(root, text="Password:", bg="#f5f5f5", font=("Helvetica", 10))
password_label.grid(row=2, column=1, padx=10, pady=10, sticky="w")

password_frame = tk.Frame(root, bg="#f5f5f5")
password_frame.grid(row=2, column=2, padx=10, pady=10, sticky="ew")

password_entry = tk.Entry(password_frame, show="*", width=40, font=("Helvetica", 12), relief="solid", bd=1)
password_entry.pack(padx=10, pady=5)

save_as_button = tk.Button(root, text="Save To Folder", command=select_output_folder, width=20, height=2, bg="#4CAF50", fg="white", font=("Helvetica", 12), relief="flat", bd=0, padx=10, pady=5)
save_as_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

output_path_label = tk.Label(root, text="Output Folder Path:", bg="#f5f5f5", font=("Helvetica", 10))
output_path_label.grid(row=3, column=1, padx=10, pady=10, sticky="w")

output_path_frame = tk.Frame(root, bg="#f5f5f5")
output_path_frame.grid(row=3, column=2, padx=10, pady=10, sticky="ew")

output_path_entry = tk.Entry(output_path_frame, textvariable=output_path_var, width=40, font=("Helvetica", 12), relief="solid", bd=1)
output_path_entry.pack(padx=10, pady=5)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_pdfs, width=20, height=2, bg="#2196F3", fg="white", font=("Helvetica", 12), relief="flat", bd=0, padx=10, pady=5)
encrypt_button.grid(row=4, column=0, columnspan=3, pady=20, sticky="ew")

footer_label = tk.Label(root, text="www.arifakyuz.com", fg="blue", cursor="hand2", bg="#f5f5f5", font=("Helvetica", 10))
footer_label.grid(row=5, column=0, columnspan=3, pady=10)
footer_label.bind("<Button-1>", lambda e: webbrowser.open("https://www.arifakyuz.com"))

root.mainloop()
