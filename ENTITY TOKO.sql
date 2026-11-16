CREATE TABLE menu (
	menu_id SERIAL PRIMARY KEY,
	nama_menu VARCHAR (100) NOT NULL,
	harga_menu NUMERIC (10,2)
);

CREATE TABLE PELANGGAN (
	pelanggan_id SERIAL PRIMARY KEY,
	nama_pelanggan VARCHAR (100) NOT NULL,
	no_hp VARCHAR (13) NOT NULL UNIQUE
);

CREATE TABLE MEJA (
	meja_id SERIAL PRIMARY KEY,
	no_meja INT NOT NULL,
	kapasitas INT NOT NULL
);

CREATE TABLE DETAIL_PESANAN (
	detail_pesanan_id SERIAL PRIMARY KEY,
	jumlah_pesanan INT NOT NULL,
	sub_total NUMERIC (10,2) NOT NULL,
	menu_id INT NOT NULL,
	pesanan_id INT NOT NULL,

	FOREIGN KEY (menu_id)
	REFERENCES MENU (menu_id),

	FOREIGN KEY (pesanan_id)
	REFERENCES PESANAN (pesanan_id)
);

CREATE TABLE PESANAN (
	pesanan_id SERIAL PRIMARY KEY,
	tanggal_pesanan DATE NOT NULL,
	total_harga NUMERIC (10,2) NOT NULL,
	pelanggan_id INT NOT NULL,
	meja_id INT NOT NULL,
	kasir_id INT NOT NULL,

	FOREIGN KEY (pelanggan_id)
	REFERENCES PELANGGAN(id_pelanggan),

	FOREIGN KEY (meja_id)
	REFERENCES MEJA (meja_id),

	FOREIGN KEY (kasir_id)
	REFERENCES KASIR(kasir_id)
);

CREATE TABLE KASIR (
	kasir_id SERIAL PRIMARY KEY,
	nama_kasir VARCHAR (100) NOT NULL,
	email VARCHAR (100) UNIQUE NOT NULL,
	no_hp INT,
	pesanan_id INT NOT NULL UNIQUE,

	FOREIGN KEY (pesanan_id)
	REFERENCES PESANAN(pesanan_id)
);

-- UNIQUE = UNIQUE IDENTIFIER (TIDAK BOLEH DUPLIKAT)
-- NOT NULL = WAJIB DIISI (MANDATORY)

CREATE TABLE mahasiswa (
	nama varchar (100) PRIMARY KEY,
	email varchar (100) UNIQUE,
	umur int (umur >= 50 and <= 50),
	status varchar (50) DEFAULT "AKTIF"
	nama_prodi varchar (50),

	FOREIGN KEY (nama_prodi)
	REFERENCES prodi (nama_prodi)
);

INSERT INTO prodi (nama_prodi) VALUES ('TEKNOLOGI INFORMASI');
INSERT INTO prodi (nama_prodi) VALUES ('SISTEM INFORMASI');
INSERT INTO prodi (nama_prodi) VALUES ('INFORMATIKA');

ALTER TABLE mahasiswa
ADD COLUMN alamat Text;

ALTER TABLE mahasiswa
ADD COLUMN alamat TYPE varchar (255);

ALTER TABLE mahasiswa
RENAME COLUMN alamat TO alamat_mahasiswa;

select * from mahasiswa;
select * from prodi;

CREATE TABLE prodi (
	nama_prodi varchar (50) PRIMARY KEY
);

DROP TABLE mahasiswa;
DROP TABLE prodi;

--- CONTOH DESIMAL
DECIMAL (10,2)

--- CONTOH ANOMALI
CREATE TABLE produk (
	kode_produk SERIAL PRIMARY KEY
	nama_produk VARCHAR (100) NOT NULL,
	deskripsi_produk VARCHAR NOT NULL,
	harga DECIMAL(10,2) CHECK (harga > 0),
	stok INT DEFAULT '0' CHECK (stok >= 0),
	berat REAL,
	id_kategori INT,
	FOREIGN KEY (id_kategori)
	REFERENCES kategori_produk(id_kategori)
	ON DELETE SET NULL
	ON UPDATE CASCADE
);

--- ANOMALI
Smallint = tahun, bulan 
Int = Harga_baran g INT
DATE  = tanggal_lah ir DATE, tanggal_mer deka DATE  
TIME = jam_buka TIME, waktu_mulai _ujian TIME