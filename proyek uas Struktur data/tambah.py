import csv
from file_handler import NAMA_FILE

def tambah_transaksi():
    print("\n=== Tambah Transaksi ===")
    tanggal = input("Tanggal (yyyy-mm-dd): ")
    jenis = input("Jenis [pemasukan/pengeluaran]: ").lower()
    jumlah = float(input("Jumlah (Rp): "))
    kategori = input("Kategori (misal: makan, gaji): ").lower()

    with open(NAMA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([tanggal, jenis, jumlah, kategori])

    print("✅ Transaksi berhasil ditambahkan!\n")