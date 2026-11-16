# # SOAL 1
# produk = {
#     "Gitar Stratocaster Red": 13000,
#     "Ampli Marshall": 20000,
#     "Kak Zaidan Gaming": 7000,
#     "Paket Umroh Bersama Mas Adya": 25000
# }

# keranjang = {}

# print("TOKO SUKA SLIPKNOT")
# no = 1
# for item, harga in produk.items():
#     print(no, ".", item, "- Rp", harga)
#     no += 1
# print("0. Selesai")

# while True:
#     pilih = input("Pilih barang (nomor): ")
    
#     if pilih == "0":
#         break
        
#     pilih_idx = int(pilih) - 1
#     nama_barang = list(produk.keys())[pilih_idx]
    
#     qty = int(input("Jumlah: "))
    
#     if nama_barang in keranjang:
#         keranjang[nama_barang] += qty
#     else:
#         keranjang[nama_barang] = qty

# subtotal = 0
# print("\n--- STRUK ---")
# for nama, qty in keranjang.items():
#     harga_item = produk[nama] * qty
#     subtotal += harga_item
#     print(nama, "x", qty, "=", harga_item)

# ppn = int(subtotal * 0.11)
# ongkir = 15000
# total = subtotal + ppn + ongkir

# print("Subtotal:", subtotal)
# print("PPN (11%):", ppn)
# print("Ongkir:", ongkir)
# print("Total Bayar:", total)
# print("Terima kasih telah berbelanja di toko Ejak!")
# # SOAL 2
# nums = [5, 11, 7, 15, 21]

# target = 20

# for i in range(len(nums)): # JADI LEN DISINI DIGUNAKAN UNTUK MENGHITUNG JUMLAH DATA PADA LIST DI BAGIAN NUMS
#     for j in range(i + 1, len(nums)): # JIKA range(i + 1) DISINI DIGUNAKAN UNTUK MENCARI PASANGAN YANG COCOK UNTUK MENCAPAI TARGET
#         if nums[i] + nums[j] == target: # JADI DISINI nums[i] + nums[j] berfungsi untuk menjumlahkan data pda indeks ke i dan ke j, untuk menghasilkan target
#             print(f"index yang cocok dengan {target} adalah index ke- {i} dan index ke-{j}") 
#             #jadi output index yang cocok dengan target = 20 adalah index ke 0 dan index 3

# # SOAL 3
# hari = 1
# for hari in range(1, 15):
#     sesi = 1
#     for sesi in range(1, 6):
#         print(f"Hari ke-{hari} Sesi ke-{sesi}")
#         if sesi == 5:
#             break
#         sesi += 1
#     print(f"Hari ke-{hari} telah selesai")
# hari += 1
# if hari == 7:
#             print("Sudah setengah jalan")
# elif hari == 14:
#             print("Selesai")
for i in range (1, 9):
    for j in range(i):
        print ("*", end="")
        print()
