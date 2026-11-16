import psycopg2

# untuk menghubungkan ke database PostgreSQL
def buat_koneksi():
    try:
        koneksi = psycopg2.connect(
            host="localhost",
            database="kampus",      
            user="postgres",        
            password="passwordku"   
        )
        return koneksi
    except Exception as e:
        print("\n[ERROR] Gagal terhubung ke database:", e)
        return None

def tampilkan_data():
    koneksi = buat_koneksi()
    if not koneksi:
        return
    
    cursor = koneksi.cursor()
    cursor.execute("SELECT nim, nama, prodi FROM mahasiswa ORDER BY nim ASC;")
    daftar_mhs = cursor.fetchall()
    
    print("\n--- DAFTAR DATA MAHASISWA (POSTGRESQL) ---")
    if len(daftar_mhs) == 0:
        print("Belum ada data mahasiswa di database.")
    else:
        print(f"{'No':<4} | {'NIM':<12} | {'Nama Mahasiswa':<25} | {'Program Studi':<18}")
        print("-" * 65)
        for i, mhs in enumerate(daftar_mhs, 1):
            print(f"{i:<4} | {mhs[0]:<12} | {mhs[1]:<25} | {mhs[2]:<18}")
    
    cursor.close()
    koneksi.close()
    print()

def tambah_data():
    print("\n--- TAMBAH DATA MAHASISWA ---")
    nim = input("Masukkan NIM   : ").strip()
    nama = input("Masukkan Nama  : ").strip()
    prodi = input("Masukkan Prodi : ").strip()
    
    if not nim or not nama or not prodi:
        print("Semua data wajib diisi!\n")
        return

    koneksi = buat_koneksi()
    if not koneksi:
        return
        
    cursor = koneksi.cursor()
    try:
        # Perintah SQL untuk memasukkan data2

        query = "INSERT INTO mahasiswa (nim, nama, prodi) VALUES (%s, %s, %s);"
        cursor.execute(query, (nim, nama, prodi))
        koneksi.commit()
        print("Data mahasiswa berhasil ditambahkan ke PostgreSQL!\n")
    except Exception as e:
        print("Gagal menambah data (Kemungkinan NIM sudah terdaftar):", e)
    finally:
        cursor.close()
        koneksi.close()

def ubah_data():
    tampilkan_data()
    print("\n--- UBAH DATA MAHASISWA ---")
    nim_cari = input("Masukkan NIM mahasiswa yang mau diubah: ").strip()
    
    koneksi = buat_koneksi()
    if not koneksi:
        return
        
    cursor = koneksi.cursor()
    
    # Cek apakah datanya ada

    cursor.execute("SELECT nama, prodi FROM mahasiswa WHERE nim = %s;", (nim_cari,))
    mhs = cursor.fetchone()
    
    if not mhs:
        print("Mahasiswa dengan NIM tersebut tidak ditemukan.\n")
        cursor.close()
        koneksi.close()
        return
        
    print(f"Data saat ini -> Nama: {mhs[0]}, Prodi: {mhs[1]}")
    nama_baru = input(f"Nama baru [{mhs[0]}]: ").strip()
    prodi_baru = input(f"Program Studi baru [{mhs[1]}]: ").strip()
    
   
    if not nama_baru:
        nama_baru = mhs[0]
    if not prodi_baru:
        prodi_baru = mhs[1]
        
    try:
        query = "UPDATE mahasiswa SET nama = %s, prodi = %s WHERE nim = %s;"
        cursor.execute(query, (nama_baru, prodi_baru, nim_cari))
        koneksi.commit()
        print("Data berhasil diubah!\n")
    except Exception as e:
        print("Gagal mengubah data:", e)
    finally:
        cursor.close()
        koneksi.close()

def hapus_data():
    tampilkan_data()
    print("\n--- HAPUS DATA MAHASISWA ---")
    nim_cari = input("Masukkan NIM mahasiswa yang mau dihapus: ").strip()
    
    koneksi = buat_koneksi()
    if not koneksi:
        return
        
    cursor = koneksi.cursor()
    try:
        query = "DELETE FROM mahasiswa WHERE nim = %s;"
        cursor.execute(query, (nim_cari,))
        
        if cursor.rowcount > 0:
            koneksi.commit()
            print("Data mahasiswa berhasil dihapus!\n")
        else:
            print("Mahasiswa dengan NIM tersebut tidak ditemukan.\n")
    except Exception as e:
        print("Gagal menghapus data:", e)
    finally:
        cursor.close()
        koneksi.close()

def main():
    while True:
        print("=== APLIKASI PENGELOLAAN DATA MAHASISWA (POSTGRESQL) ===")
        print("1. Tampilkan Seluruh Data Mahasiswa")
        print("2. Menambah Data Mahasiswa")
        print("3. Mengubah Data Mahasiswa")
        print("4. Menghapus Data Mahasiswa")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ").strip()
        
        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            tambah_data()
        elif pilihan == "3":
            ubah_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            print("\nTerima kasih, program selesai.")
            break
        else:
            print("\nPilihan tidak valid, silakan pilih angka 1-5.\n")

if __name__ == "__main__":
    main()