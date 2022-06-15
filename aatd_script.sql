CREATE DATABASE IF NOT EXISTS aatd_citas;
use aatd_citas; 

create table usuario (
	id int not null auto_increment,
	nombre varchar(50),
	apellidos varchar(50),
	email varchar(255),
	password varchar(255),
	fecha date not null,
	CONSTRAINT pk_usuario PRIMARY KEY(id),
	CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

create table consultorio (
	id int not null auto_increment,
	nombre varchar(200),
	fecha date not null,
	CONSTRAINT pk_consultorio PRIMARY KEY(id)
)ENGINE=InnoDb;

create table doctor (
	id int not null auto_increment,
	nombre varchar(50),
	apellidos varchar(50),
	email varchar(255),
	direccion varchar(255),
	telefono varchar(255),
	fecha date not null,
	consultorio_id int,
	CONSTRAINT pk_doctor PRIMARY KEY(id),
    CONSTRAINT fk_doctor_consultorio FOREIGN KEY(consultorio_id) REFERENCES consultorio(id)
)ENGINE=InnoDb;

create table citas(
	id int not null auto_increment,
	titulo varchar(100),
	nota text,
	paciente varchar(255),
	sintomas text,
	usuario_id int,
	doctor_id int,
	fecha date not null,
	fecha_cita date not null,
	CONSTRAINT pk_cita PRIMARY KEY(id),
    CONSTRAINT fk_cita_usuario FOREIGN KEY(usuario_id) REFERENCES usuario(id),
    CONSTRAINT fk_cita_doctor FOREIGN KEY(doctor_id) REFERENCES doctor(id)
)ENGINE=InnoDb;