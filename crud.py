##### CRUD ######

CREATE DATABASE caduni

CREATE SCHEMA jaelson_matias

CREATE TABLE jaelson_matias.CARTAO
    (
     id_cartao INTEGER IDENTITY,
     credito VARCHAR (50) NOT NULL ,
     tipo VARCHAR (50) NOT NULL ,
     data_emissao DATE NOT NULL ,
     id_proprietario INTEGER NOT NULL
    )
GO

CREATE UNIQUE NONCLUSTERED INDEX
    CARTAO__IDX ON jaelson_matias.CARTAO
    (
     id_proprietario
    )
GO

ALTER TABLE jaelson_matias.CARTAO ADD CONSTRAINT CARTAO_PK PRIMARY KEY CLUSTERED (id_cartao)
     WITH (
     ALLOW_PAGE_LOCKS = ON ,
     ALLOW_ROW_LOCKS = ON )
GO

CREATE TABLE jaelson_matias.MOTORISTA
    (
     id_motorista INTEGER IDENTITY,
     nome VARCHAR (50) NOT NULL ,
     sobrenome VARCHAR (50) NOT NULL ,
     num_cnh BIGINT NOT NULL ,
     data_nascimento DATE NOT NULL
    )
GO

ALTER TABLE jaelson_matias.MOTORISTA ADD CONSTRAINT MOTORISTA_PK PRIMARY KEY CLUSTERED (id_motorista)
     WITH (
     ALLOW_PAGE_LOCKS = ON ,
     ALLOW_ROW_LOCKS = ON )
GO

CREATE TABLE jaelson_matias.ONIBUS
    (
     id_onibus INTEGER IDENTITY,
     placa VARCHAR (50) NOT NULL ,
     linha INTEGER NOT NULL ,
     modelo VARCHAR (50) NOT NULL ,
     ano DATE NOT NULL ,
     id_motorista INTEGER
    )
GO

ALTER TABLE jaelson_matias.ONIBUS ADD CONSTRAINT ONIBUS_PK PRIMARY KEY CLUSTERED (id_onibus)
     WITH (
     ALLOW_PAGE_LOCKS = ON ,
     ALLOW_ROW_LOCKS = ON )
GO

CREATE TABLE jaelson_matias.USUARIO
    (
     id_usuario INTEGER IDENTITY,
     nome VARCHAR (50) NOT NULL ,
     sobrenome VARCHAR (50) NOT NULL ,
     email VARCHAR (50) NOT NULL ,
     bairro VARCHAR (50) NOT NULL ,
     data_nascimento DATE NOT NULL
    )
GO

CREATE UNIQUE NONCLUSTERED INDEX
    USUARIOS__IDX ON jaelson_matias.USUARIO
    (
     id_usuario
    )
GO

ALTER TABLE jaelson_matias.USUARIO ADD CONSTRAINT USUARIO_PK PRIMARY KEY CLUSTERED (id_usuario)
     WITH (
     ALLOW_PAGE_LOCKS = ON ,
     ALLOW_ROW_LOCKS = ON )
GO

ALTER TABLE jaelson_matias.CARTAO
    ADD CONSTRAINT CARTAO_USUARIO_FK FOREIGN KEY
    (
     id_proprietario
    )
    REFERENCES jaelson_matias.USUARIO
    (
     id_usuario
    )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
GO


ALTER TABLE jaelson_matias.ONIBUS
    ADD CONSTRAINT ONIBUS_MOTORISTA_FK FOREIGN KEY
    (
     id_motorista
    )
    REFERENCES jaelson_matias.MOTORISTA
    (
     id_motorista
    )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
GO
