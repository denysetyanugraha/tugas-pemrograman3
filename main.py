import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # konversi ke meter
        
        if height <= 0 or weight <= 0:
            raise ValueError("Oops, ada kesalahan!")
        
        bmi = weight / (height ** 2)
        
        if bmi < 18.5:
            category = "Berat badanmu kurang!"
        elif 18.5 <= bmi < 24.9:
            category = "Berat badanmu pas!"
        elif 25 <= bmi < 29.9:
            category = "Kamu kelebihan berat badan!"
        else:
            category = "..."

        result_label.config(text=f"BMI: {bmi:.2f}\n{category}")
    except ValueError:
        messagebox.showerror("Oops, ada kesalahan!", "Mohon masukkan angka dengan benar.")

# Main windows
root = tk.Tk()
root.title("Kalkulator BMI")
root.resizable(False, False)

# Input
weight_label = tk.Label(root, text="Berat Badan (kg):")
weight_label.grid(row=0, column=0, padx=10, pady=10)

weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

height_label = tk.Label(root, text="Tinggi Badan (cm):")
height_label.grid(row=1, column=0, padx=10, pady=10)

height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=10)

# Tombol
calculate_button = tk.Button(root, text="Hitung", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=20)

# Hasil
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run
root.mainloop()
