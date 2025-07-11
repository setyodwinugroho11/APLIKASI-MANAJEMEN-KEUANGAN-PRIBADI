import os
import csv

NAMA_FILE = "keuangan.csv"

def cek_file_csv():
    if not os.path.exists(NAMA_FILE):
        with open(NAMA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Tanggal", "Jenis", "Jumlah", "Kategori"])