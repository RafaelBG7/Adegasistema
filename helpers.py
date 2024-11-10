from conexao import conectar

def adicionar_produto(nome, tipo, marca, preco, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO produtos (nome, tipo, marca, preco, quantidade) VALUES (?, ?, ?, ?, ?)", 
                   (nome, tipo, marca, preco, quantidade))
    conexao.commit()
    conexao.close()

def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conexao.close()
    return produtos

def registrar_venda(produto_id, quantidade, data_venda, metodo_pagamento):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO vendas (produto_id, quantidade, data_venda, metodo_pagamento) VALUES (?, ?, ?, ?)", 
                   (produto_id, quantidade, data_venda, metodo_pagamento))
    cursor.execute("UPDATE produtos SET quantidade = quantidade - ? WHERE id = ?", 
                   (quantidade, produto_id))
    conexao.commit()
    conexao.close()

def listar_vendas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT v.id, p.nome, v.quantidade, v.data_venda, v.metodo_pagamento FROM vendas v JOIN produtos p ON v.produto_id = p.id")
    vendas = cursor.fetchall()
    conexao.close()
    return vendas

def adicionar_funcionario(nome, cargo, horario, salario):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO funcionarios (nome, cargo, horario, salario) VALUES (?, ?, ?, ?)", 
                   (nome, cargo, horario, salario))
    conexao.commit()
    conexao.close()

def listar_funcionarios():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()
    conexao.close()
    return funcionarios