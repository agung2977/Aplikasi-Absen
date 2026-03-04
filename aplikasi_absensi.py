import tkinter as tk
from tkinter import messagebox, ttk
import datetime
import csv

# Daftar absensi
absensi = []

def tambah_absen():
    nama = entry_nama.get().strip()
    status = combo_status.get()
    
    if nama == "":
        messagebox.showwarning("Peringatan", "Nama tidak boleh kosong!")
        return
    if status == "":
        messagebox.showwarning("Peringatan", "Pilih keterangan absensi!")
        return
    
    waktu = datetime.datetime.now().strftime("%H:%M:%S")
    data = (nama, status, waktu)
    absensi.append(data)
    
    listbox_absen.insert(tk.END, f"{nama} | {status} | {waktu}")
    entry_nama.delete(0, tk.END)
    combo_status.set("")

def simpan_absensi():
    if not absensi:
        messagebox.showwarning("Peringatan", "Belum ada data absensi!")
        return
    
    tanggal = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"absensi_{tanggal}.csv"
    
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f, delimiter=";")  # pakai ; agar Excel otomatis pecah kolom
        writer.writerow(["No", "Nama", "Keterangan", "Waktu"])
        for i, (nama, status, waktu) in enumerate(absensi, start=1):
            writer.writerow([i, nama, status, waktu])
    
    messagebox.showinfo("Info", f"Absensi berhasil disimpan ke {filename}")

# GUI Utama
root = tk.Tk()
root.title("Aplikasi Absensi Sederhana")
root.geometry("550x450")
root.resizable(False, False)

# Label Judul
judul = tk.Label(root, text="ABSENSI KELAS", font=("Arial", 16, "bold"))
judul.pack(pady=10)

# Frame Input
frame_input = tk.Frame(root)
frame_input.pack(pady=5)

label_nama = tk.Label(frame_input, text="Nama Siswa:")
label_nama.grid(row=0, column=0, padx=5, pady=5, sticky="e")

entry_nama = tk.Entry(frame_input, width=30)
entry_nama.grid(row=0, column=1, padx=5, pady=5)

label_status = tk.Label(frame_input, text="Keterangan:")
label_status.grid(row=1, column=0, padx=5, pady=5, sticky="e")

combo_status = ttk.Combobox(frame_input, values=["Hadir", "Izin", "Sakit", "Alfa"], state="readonly", width=27)
combo_status.grid(row=1, column=1, padx=5, pady=5)

btn_tambah = tk.Button(root, text="Tambah Absen", command=tambah_absen, width=25, bg="lightblue")
btn_tambah.pack(pady=10)

# Listbox untuk daftar hadir
listbox_absen = tk.Listbox(root, width=70, height=12)
listbox_absen.pack(pady=10)

# Tombol Simpan
btn_simpan = tk.Button(root, text="Simpan Absensi", command=simpan_absensi, width=25, bg="lightgreen")
btn_simpan.pack(pady=10)

# Jalankan aplikasi
root.mainloop()
