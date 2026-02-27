CREATE DATABASE IF NOT EXISTS youã;

USE youã;

CREATE TABLE IF NOT EXISTS genero (
 genero VARCHAR(30) NOT NULL PRIMARY KEY,
 icone VARCHAR(100),
 cor VARCHAR(10)
);



CREATE TABLE IF NOT EXISTS musica (
 id_musica INT NOT NULL primary KEY auto_increment,
 cantor VARCHAR(50),
 duracao TIME,
 nome VARCHAR(50),
 url_capa VARCHAR(255),
 nome_genero VARCHAR(30) NOT NULL,
 stats VARCHAR(30) NOT NULL,
 constraint fk_musica_genero foreign key (nome_genero) references genero (genero)
);
