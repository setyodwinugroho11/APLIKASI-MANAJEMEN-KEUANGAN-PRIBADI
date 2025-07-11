import csv
from file_handler import NAMA_FILE

def tampilkan_transaksi():
    print("\n=== Riwayat Transaksi ===")
    try:
        with open(NAMA_FILE, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            kosong = True
            for i, row in enumerate(reader, start=1):
                print(f"{i}. Tanggal: {row[0]}, Jenis: {row[1]}, Jumlah: Rp{row[2]}, Kategori: {row[3]}")
                kosong = False
            if kosong:
                print("Belum ada transaksi.\n")
    except FileNotFoundError:
        print("❌ File belum ditemukan.\n")

def laporan_kategori():
    print("\n=== Laporan Pengeluaran per Kategori ===")
    kategori_total = {}
    try:
        with open(NAMA_FILE, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[1] == "pengeluaran":
                    jumlah = float(row[2])
                    kategori = row[3]
                    kategori_total[kategori] = kategori_total.get(kategori, 0) + jumlah

        if kategori_total:
            for kategori, total in kategori_total.items():
                print(f"{kategori}: Rp{total}")
        else:
            print("Belum ada data pengeluaran.\n")
    except FileNotFoundError:
        print("❌ File belum ditemukan.\n")