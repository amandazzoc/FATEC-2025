/*Ambiente de produção - Real Time*/

-- Criação do Banco de Dados de Produção
CREATE DATABASE IF NOT EXISTS HotelDallasProd;
USE HotelDallasProd;

-- Tabela de Clientes na Produção
CREATE TABLE Clientes (
    ID_Cliente INT PRIMARY KEY,
    Nome VARCHAR(100),
    Idade INT,
    Pais VARCHAR(50)
);

-- Tabela de Reservas na Produção
CREATE TABLE Reservas (
    ID_Reserva INT PRIMARY KEY,
    ID_Cliente INT,
    Data_Entrada DATE,
    Data_Saida DATE,
    Numero_Noites INT,
    FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente)
);

-- Tabela de Quartos na Produção
CREATE TABLE Quartos (
    ID_Quarto INT PRIMARY KEY,
    Tipo_Quarto VARCHAR(50),
    Andar INT,
    Preco_Diaria DECIMAL(10, 2)
);

-- Tabela de Serviços na Produção
CREATE TABLE Servicos (
    ID_Servico INT PRIMARY KEY,
    Nome_Servico VARCHAR(100),
    Categoria VARCHAR(50),
    Preco DECIMAL(10, 2)
);

-- Tabela de Ocupações na Produção (fato transacional)
CREATE TABLE Ocupacoes (
    ID_Ocupacao INT PRIMARY KEY,
    ID_Cliente INT,
    ID_Reserva INT,
    ID_Quarto INT,
    Data DATE,
    ID_Servico INT,
    Quantidade INT,
    Valor_Total DECIMAL(10, 2),
    FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente),
    FOREIGN KEY (ID_Reserva) REFERENCES Reservas(ID_Reserva),
    FOREIGN KEY (ID_Quarto) REFERENCES Quartos(ID_Quarto),
    FOREIGN KEY (ID_Servico) REFERENCES Servicos(ID_Servico)
);


/*Popular as tabelas de Produção*/

-- Inserindo dados em Clientes
INSERT INTO Clientes (ID_Cliente, Nome, Idade, Pais) VALUES
(1, 'Carlos Silva', 45, 'Brasil'),
(2, 'Ana Gomez', 34, 'Argentina'),
(3, 'Lucas Andrade', 29, 'Brasil'),
(4, 'Mariana López', 40, 'México'),
(5, 'Tomás Perez', 35, 'Chile');

-- Inserindo dados em Reservas
INSERT INTO Reservas (ID_Reserva, ID_Cliente, Data_Entrada, Data_Saida, Numero_Noites) VALUES
(1, 1, '2023-01-10', '2023-01-15', 5),
(2, 2, '2023-01-12', '2023-01-14', 2),
(3, 3, '2023-02-05', '2023-02-10', 5);

-- Inserindo dados em Quartos
INSERT INTO Quartos (ID_Quarto, Tipo_Quarto, Andar, Preco_Diaria) VALUES
(1, 'Suíte Luxo', 3, 500.00),
(2, 'Quarto Standard', 2, 300.00),
(3, 'Quarto Deluxe', 4, 450.00);

-- Inserindo dados em Serviços
INSERT INTO Servicos (ID_Servico, Nome_Servico, Categoria, Preco) VALUES
(1, 'Café da Manhã', 'Alimentação', 30.00),
(2, 'Spa', 'Bem-estar', 120.00),
(3, 'Lavanderia', 'Serviço', 50.00);

-- Inserindo dados em Ocupacoes
INSERT INTO Ocupacoes (ID_Ocupacao, ID_Cliente, ID_Reserva, ID_Quarto, Data, ID_Servico, Quantidade, Valor_Total) VALUES
(1, 1, 1, 1, '2023-01-10', 1, 1, 500.00),
(2, 2, 2, 2, '2023-01-12', 2, 1, 300.00),
(3, 3, 3, 3, '2023-02-05', 3, 1, 450.00);

create database if not exists hoteldallasDW;
use hoteldallasDW;

-- Tabela DimCliente
CREATE TABLE DimCliente (
    ID_Cliente INT PRIMARY KEY,
    Nome VARCHAR(100),
    Idade INT,
    Pais_Origem VARCHAR(50)
);
 
-- Tabela DimReserva
CREATE TABLE DimReserva (
    ID_Reserva INT PRIMARY KEY,
    Data_Entrada DATE,
    Data_Saida DATE,
    Numero_Noites INT
);
 
-- Tabela DimQuarto
CREATE TABLE DimQuarto (
    ID_Quarto INT PRIMARY KEY,
    Tipo_Quarto VARCHAR(50),
    Andar INT,
    Preco_Diaria DECIMAL(10, 2)
);
 
 
-- Tabela DimTempo
CREATE TABLE DimTempo (
    ID_Tempo INT PRIMARY KEY,
    Data DATE,
    Ano INT,
    Mes INT,
    Trimestre INT,
    Dia_Semana VARCHAR(10)
);
 
-- Tabela DimServico
CREATE TABLE DimServico (
    ID_Servico INT PRIMARY KEY,
    Nome_Servico VARCHAR(100),
    Categoria VARCHAR(50),
    Preco DECIMAL(10, 2)
);

/* Script SQL para Tabela Fato */
-- Tabela FatoOcupacao
CREATE TABLE FatoOcupacao(
	ID_Ocupacao INT PRIMARY KEY,
	ID_Cliente INT,
	ID_Reserva INT,
	ID_Quarto INT,
	ID_Tempo INT,
	ID_Servico INT,
	Quantidade INT,
	Valor_Total DECIMAL(10, 2),
	FOREIGN KEY (ID_Cliente) REFERENCES DimCliente(ID_Cliente),
	FOREIGN KEY (ID_Reserva) REFERENCES DimReserva(ID_Reserva),
	FOREIGN KEY (ID_Quarto) REFERENCES DimQuarto(ID_Quarto),
	FOREIGN KEY (ID_Tempo) REFERENCES DimTempo(ID_Tempo),
	FOREIGN KEY (ID_Servico) REFERENCES DimServico(ID_Servico)
);

/*Processo de ETL Transferindo os dados da Produção para o DW*/
-- Extrair e inserir dados na DimCliente
SELECT * FROM dimcliente

INSERT INTO DimCliente (ID_Cliente, Nome, Idade, Pais_Origem)
SELECT ID_Cliente, Nome, Idade, Pais FROM hotelDallasProd.Clientes

SELECT * FROM dimreserva

INSERT INTO DimReserva (ID_Reserva, Data_Entrada, Data_Saida, Numero_Noites)
SELECT ID_Cliente, Data_Entrada, Data_Saida, Numero_Noites FROM hotelDallasProd.Reservas

SELECT * FROM dimquarto

INSERT INTO DimQuarto (ID_Quarto, Tipo_Quarto, Andar, Preco_Diaria)
SELECT ID_Quarto, Tipo_Quarto, Andar, Preco_Diaria FROM hotelDallasProd.quartos

SELECT * FROM dimservico

INSERT INTO dimservico (ID_Servico, Nome_Servico, Categoria, Preco)
SELECT ID_Servico, Nome_Servico, Categoria, Preco FROM hotelDallasProd.servicos

SELECT * FROM dimtempo

INSERT INTO dimtempo (ID_Tempo, Data, Ano, Mes, Trimestre, Dia_Semana)
SELECT 
	ROW_NUMBER() OVER(ORDER BY Data) AS ID_Tempo,
	Data,
	YEAR(Data) AS ano,
	MONTH(Data) AS mes,
	QUARTER(Data) AS trimestre,
	DAYNAME(Data) AS Dia_Semana
FROM(
	SELECT DISTINCT DATA FROM hoteldallasprod.ocupacoes
) AS t;

SELECT * FROM hotelDallasProd.ocupacoes

SELECT * FROM fatoocupacao



CREATE TABLE Ocupacoes (
    ID_Ocupacao INT PRIMARY KEY,
    ID_Cliente INT,
    ID_Reserva INT,
    ID_Quarto INT,
    Data DATE,
    ID_Servico INT,
    Quantidade INT,
    Valor_Total DECIMAL(10, 2),
    FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente),
    FOREIGN KEY (ID_Reserva) REFERENCES Reservas(ID_Reserva),
    FOREIGN KEY (ID_Quarto) REFERENCES Quartos(ID_Quarto),
    FOREIGN KEY (ID_Servico) REFERENCES Servicos(ID_Servico)
);

INSERT INTO fatoocupacao(ID_Ocupacao, ID_Cliente, ID_Reserva, ID_Quarto, ID_Servico, Quantidade, Valor_Total)
SELECT ID_Ocupacao, ID_Cliente, ID_Reserva, ID_Quarto, ID_Servico, Quantidade, Valor_Total FROM hotelDallasProd.ocupacoes