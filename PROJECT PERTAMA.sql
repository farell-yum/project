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