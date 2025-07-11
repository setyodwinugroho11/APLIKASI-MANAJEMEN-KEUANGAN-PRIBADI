import csv
from file_handler import NAMA_FILE
from tampilkan import tampilkan_transaksi

def hapus_transaksi():
    print("\n=== Hapus Transaksi ===")
    tampilkan_transaksi()
    try:
        index = int(input("Masukkan nomor transaksi yang ingin dihapus (1, 2, ...): ")) - 1
        with open(NAMA_FILE, mode='r') as file:
            reader = list(csv.reader(file))
            header, data = reader[0], reader[1:]

        if 0 <= index < len(data):
            konfirmasi = input(f"Yakin ingin menghapus transaksi ke-{index+1}? (y/n): ").lower()
            if konfirmasi == 'y':
                del data[index]
                with open(NAMA_FILE, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(header)
                    writer.writerows(data)
                print("✅ Transaksi berhasil dihapus.\n")
            else:
                print("❌ Penghapusan dibatalkan.\n")
        else:
            print("❌ Nomor transaksi tidak valid.\n")
    except:
        print("❌ Gagal menghapus transaksi.\n")