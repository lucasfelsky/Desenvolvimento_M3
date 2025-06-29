-- Primeiro, crie o banco de dados
CREATE DATABASE IF NOT EXISTS banco;

-- Use o banco de dados que acabamos de criar
USE banco;

-- Tabela para Agências
CREATE TABLE IF NOT EXISTS agencia (
    id_agencia INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL
);

-- Tabela para Clientes (relacionada a Agência)
CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL, -- O CPF tem 11 dígitos e não pode se repetir (UNIQUE)
    id_agencia INT NOT NULL,
    -- A linha abaixo cria a ligação (Foreign Key) com a tabela 'agencia'
    FOREIGN KEY (id_agencia) REFERENCES agencia(id_agencia)
);

-- Tabela para Cartões (relacionada a Cliente)
CREATE TABLE IF NOT EXISTS cartao (
    id_cartao INT PRIMARY KEY,
    numero CHAR(16) UNIQUE NOT NULL, -- O número do cartão tem 16 dígitos e é único
    tipo ENUM('débito','crédito') NOT NULL, -- O tipo só pode ser 'débito' ou 'crédito'
    validade DATE NOT NULL,
    id_cliente INT NOT NULL,
    -- A linha abaixo cria a ligação (Foreign Key) com a tabela 'cliente'
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);

-- Tabela para Transferências (relacionada a Cliente de origem e destino)
CREATE TABLE IF NOT EXISTS transferencia (
    id_transferencia INT PRIMARY KEY,
    valor DECIMAL(10,2) NOT NULL,
    data DATETIME NOT NULL,
    id_cliente_origem INT NOT NULL,
    id_cliente_destino INT NOT NULL,
    -- Ligação com o cliente que enviou o dinheiro
    FOREIGN KEY (id_cliente_origem) REFERENCES cliente(id_cliente),
    -- Ligação com o cliente que recebeu o dinheiro
    FOREIGN KEY (id_cliente_destino) REFERENCES cliente(id_cliente)
);