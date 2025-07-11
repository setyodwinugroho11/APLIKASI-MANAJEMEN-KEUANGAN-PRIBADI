import csv
from file_handler import NAMA_FILE
from tampilkan import tampilkan_transaksi

def update_transaksi():
    print("\n=== Update Transaksi ===")
    tampilkan_transaksi()
    try:
        index = int(input("Masukkan nomor transaksi yang ingin diubah (1, 2, ...): ")) - 1
        with open(NAMA_FILE, mode='r') as file:
            reader = list(csv.reader(file))
            header, data = reader[0], reader[1:]

        if 0 <= index < len(data):
            print("Masukkan data baru (kosongkan untuk tidak mengubah):")
            tanggal = input(f"Tanggal baru [{data[index][0]}]: ") or data[index][0]
            jenis = input(f"Jenis baru [{data[index][1]}]: ") or data[index][1]
            jumlah = input(f"Jumlah baru [{data[index][2]}]: ") or data[index][2]
            kategori = input(f"Kategori baru [{data[index][3]}]: ") or data[index][3]

            data[index] = [tanggal, jenis, jumlah, kategori]

            with open(NAMA_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(data)

            print("✅ Transaksi berhasil diperbarui.\n")
        else:
            print("❌ Nomor transaksi tidak valid.\n")
    except:
        print("❌ Gagal memperbarui transaksi.\n")