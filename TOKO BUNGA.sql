DROP TABLE IF EXISTS Pengiriman, Pembayaran, Detail_pesanan, Pesanan, Pelanggan, Bunga CASCADE;

CREATE TABLE Bunga (
	id_bunga SERIAL PRIMARY KEY,
	nama_bunga VARCHAR(64) NOT NULL,
	harga_bunga DECIMAL(10,2) NOT NULL,
	stok INT NOT NULL,
	deskripsi TEXT
);


CREATE TABLE Pelanggan (
	id_pelanggan SERIAL PRIMARY KEY,
	nama_pelanggan VARCHAR(100) NOT NULL,
	no_telepon VARCHAR(13) NOT NULL UNIQUE,
	alamat TEXT NOT NULL
);


CREATE TABLE Pesanan (
	id_pesanan SERIAL PRIMARY KEY,
	tanggal_pesanan DATE NOT NULL,
	total_harga NUMERIC(10,2) NOT NULL,
	catatan TEXT,
	id_pelanggan INT NOT NULL,
	FOREIGN KEY (id_pelanggan) REFERENCES Pelanggan(id_pelanggan)
);


CREATE TABLE Detail_pesanan (
	id_detail_pesanan SERIAL PRIMARY KEY,
	jumlah INT NOT NULL,
	diskon DECIMAL(10,2) NOT NULL,
	sub_total NUMERIC(10,2) NOT NULL,
	id_bunga INT NOT NULL,
	id_pesanan INT NOT NULL,
	FOREIGN KEY (id_bunga) REFERENCES Bunga(id_bunga),
	FOREIGN KEY (id_pesanan) REFERENCES Pesanan(id_pesanan)
);


CREATE TABLE Pembayaran (
	id_pembayaran SERIAL PRIMARY KEY,
	tanggal_pembayaran DATE NOT NULL,
	metode_pembayaran VARCHAR(64) NOT NULL,
	harga_bayar NUMERIC(10,2) NOT NULL,
	harga_kembali NUMERIC(10,2),
	id_pesanan INT NOT NULL UNIQUE,
	FOREIGN KEY (id_pesanan) REFERENCES Pesanan(id_pesanan)
);


CREATE TABLE Pengiriman (
	id_pengiriman SERIAL PRIMARY KEY,
	tanggal_pengiriman DATE NOT NULL,
	status_pengiriman VARCHAR(64) NOT NULL,
	catatan TEXT,
	id_pesanan INT NOT NULL UNIQUE,
	FOREIGN KEY (id_pesanan) REFERENCES Pesanan(id_pesanan)
);