DROP TABLE IF EXISTS detail_pemupukan, pemupukan, pertumbuhan, penanaman, pupuk, lahan CASCADE;

CREATE TABLE lahan (
	id_lahan SERIAL PRIMARY KEY,
	nama_lahan VARCHAR(64) NOT NULL,
	lokasi_lahan VARCHAR(255) NOT NULL,
	luas INT NOT NULL
);


CREATE TABLE pupuk (
	id_pupuk SERIAL PRIMARY KEY,
	nama_pupuk VARCHAR(255) NOT NULL,
	jenis_pupuk VARCHAR(64) NOT NULL,
	stok INT NOT NULL,
	satuan VARCHAR(64) NOT NULL,
	deskripsi TEXT
);


CREATE TABLE penanaman (
	id_penanaman SERIAL PRIMARY KEY,
	tanggal_tanam DATE NOT NULL,
	jenis_strawberry VARCHAR(64) NOT NULL,
	jumlah_tanam INT NOT NULL,
	id_lahan INT NOT NULL,
	FOREIGN KEY (id_lahan) REFERENCES lahan(id_lahan)
);


CREATE TABLE pertumbuhan (
	id_pertumbuhan SERIAL PRIMARY KEY,
	tanggal_pengecekan DATE NOT NULL,
	kondisi_tanaman VARCHAR(64) NOT NULL,
	catatan TEXT,
	id_penanaman INT NOT NULL,
	FOREIGN KEY (id_penanaman) REFERENCES penanaman(id_penanaman)
);


CREATE TABLE pemupukan (
	id_pemupukan SERIAL PRIMARY KEY,
	tanggal_pemupukan DATE NOT NULL,
	catatan TEXT,
	id_penanaman INT NOT NULL,
	FOREIGN KEY (id_penanaman) REFERENCES penanaman(id_penanaman)
);


CREATE TABLE detail_pemupukan (
	id_detail_pemupukan SERIAL PRIMARY KEY,
	jumlah_pupuk INT NOT NULL,
	satuan VARCHAR(64) NOT NULL,
	id_pupuk INT NOT NULL,
	id_pemupukan INT NOT NULL,
	FOREIGN KEY (id_pupuk) REFERENCES pupuk(id_pupuk),
	FOREIGN KEY (id_pemupukan) REFERENCES pemupukan(id_pemupukan)
);