# List untuk menyimpan barang dalam keranjang
Keranjang = []

def tampilkan_menu():
    print("=== APLIKASI KASIR SEDERHANA ===")
    print("1. Tambah Barang")
    print("2. Lihat Keranjang")
    print("3. Hitung Total Harga")
    print("4. Keluar")

def tambah_barang():
    nama = input("Masukkan nama barang: ")
    harga = float(input("Masukkan harga barang: "))
    Keranjang.append((nama, harga))
    print(f"{nama} dengan harga Rp{harga} telah ditambahkan ke keranjang.")

def lihat_keranjang():
    if not Keranjang:
        print("Keranjang masih kosong.")
    else:
        print("=== DAFTAR BARANG DALAM KERANJANG ===")
        for i, (nama, harga) in enumerate(Keranjang, 1):
            print(f"{i}. {nama} - Rp{harga}")

def hitung_total():
    total = sum(harga for _, harga in Keranjang)
    if total > 100000:
        diskon = total * 0.10
        total = diskon
        print(f"Anda mendapatkan diskon 10%! Total setelah diskon: Rp{total:.2f}")
    else:
        print(f"Total harga: Rp{total:.2f}")


while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-4): ")
        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            lihat_keranjang()
        elif pilihan == "3":
            hitung_total()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan aplikasi kasir!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")