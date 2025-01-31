from conexao import conectar

# Função para criar as tabelas de produtos, vendas e funcionários
def criar_banco():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        tipo TEXT NOT NULL,
                        marca TEXT,
                        preco REAL NOT NULL,
                        quantidade INTEGER NOT NULL
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS vendas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        produto_id INTEGER NOT NULL,
                        quantidade INTEGER NOT NULL,
                        data_venda TEXT NOT NULL,
                        metodo_pagamento TEXT NOT NULL,
                        FOREIGN KEY (produto_id) REFERENCES produtos (id)
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS funcionarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        cargo TEXT NOT NULL,
                        horario TEXT NOT NULL,
                        salario REAL NOT NULL
                    )''')
    conexao.commit()
    conexao.close()