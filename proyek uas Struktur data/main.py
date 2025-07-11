from file_handler import cek_file_csv
from tambah import tambah_transaksi
from tampilkan import tampilkan_transaksi, laporan_kategori
from update import update_transaksi
from hapus import hapus_transaksi

def main_menu():
    cek_file_csv()
    while True:
        print("==== MENU MANAJEMEN KEUANGAN ====")
        print("1. Tambah Transaksi")
        print("2. Lihat Riwayat Transaksi")
        print("3. Lihat Laporan per Kategori")
        print("4. Update Transaksi")
        print("5. Hapus Transaksi")
        print("6. Keluar (atau ketik 'q')")

        pilihan = input("Pilih menu (1-6 atau q): ").strip().lower()

        if pilihan == "1":
            tambah_transaksi()
        elif pilihan == "2":
            tampilkan_transaksi()
        elif pilihan == "3":
            laporan_kategori()
        elif pilihan == "4":
            update_transaksi()
        elif pilihan == "5":
            hapus_transaksi()
        elif pilihan == "6" or pilihan == "q" or pilihan == "exit":
            konfirmasi = input("Yakin ingin keluar? (y/n): ").lower()
            if konfirmasi == 'y':
                print("👋 Terima kasih telah menggunakan aplikasi ini!")
                break
            else:
                print("❗ Batal keluar. Kembali ke menu.\n")
        else:
            print("❌ Pilihan tidak valid. Coba lagi.\n")

if __name__ == "__main__":
    main_menu()