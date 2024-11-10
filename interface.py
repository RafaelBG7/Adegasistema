import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from helpers import adicionar_produto, listar_produtos, registrar_venda, listar_vendas, adicionar_funcionario, listar_funcionarios
from datetime import datetime

# Função para iniciar a interface gráfica
def iniciar_interface():
    def atualizar_estoque():
        produtos = listar_produtos()
        listbox_produtos.delete(0, tk.END)
        for produto in produtos:
            listbox_produtos.insert(tk.END, f"{produto[1]} - {produto[2]} - {produto[3]} - R${produto[4]} - Qtd: {produto[5]}")

    def atualizar_vendas():
        vendas = listar_vendas()
        listbox_vendas.delete(0, tk.END)
        for venda in vendas:
            listbox_vendas.insert(tk.END, f"{venda[1]} - Qtd: {venda[2]} - Data: {venda[3]} - Pagamento: {venda[4]}")

    def atualizar_funcionarios():
        funcionarios = listar_funcionarios()
        listbox_funcionarios.delete(0, tk.END)
        for funcionario in funcionarios:
            listbox_funcionarios.insert(tk.END, f"{funcionario[1]} - Cargo: {funcionario[2]} - Horário: {funcionario[3]} - Salário: R${funcionario[4]}")

    def adicionar():
        nome = entry_nome.get()
        tipo = entry_tipo.get()
        marca = entry_marca.get()
        preco = float(entry_preco.get())
        quantidade = int(entry_quantidade.get())
        adicionar_produto(nome, tipo, marca, preco, quantidade)
        messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
        atualizar_estoque()

    def vender():
        produto_nome = combobox_produto_nome.get()
        produto_id = next((produto[0] for produto in listar_produtos() if produto[1] == produto_nome), None)
        if produto_id is None:
            messagebox.showerror("Erro", "Produto não encontrado!")
            return
        quantidade = int(entry_quantidade_venda.get())
        data_venda = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        observacao = entry_observacao.get()
        valor_venda = float(entry_valor_venda.get())
        funcionario_nome = combobox_funcionario.get()
        metodo_pagamento = combobox_metodo_pagamento.get()
        registrar_venda(produto_id, quantidade, data_venda, metodo_pagamento)
        messagebox.showinfo("Sucesso", "Venda registrada com sucesso!")
        atualizar_estoque()
        atualizar_vendas()

    def adicionar_func():
        nome = entry_nome_func.get()
        cargo = entry_cargo_func.get()
        horario = combobox_horario_func.get()
        salario = float(entry_salario_func.get())
        adicionar_funcionario(nome, cargo, horario, salario)
        messagebox.showinfo("Sucesso", "Funcionário adicionado com sucesso!")
        atualizar_funcionarios()

    janela = tk.Tk()
    janela.title("Sistema de Controle de Estoque - Adega")
    janela.geometry("1920x1080")
    janela.state('zoomed')  # Para abrir em tela cheia

    notebook = ttk.Notebook(janela)
    notebook.pack(expand=True, fill='both')

    # Aba de Adição de Produtos
    aba_produtos = ttk.Frame(notebook)
    notebook.add(aba_produtos, text='Registrar Estoque')

    frame_produtos = tk.LabelFrame(aba_produtos, text="Adicionar Produto", padx=10, pady=10)
    frame_produtos.pack(fill="both", expand=True, padx=10, pady=10)

    tk.Label(frame_produtos, text="Nome do Produto").grid(row=0, column=0, sticky="w")
    entry_nome = tk.Entry(frame_produtos)
    entry_nome.grid(row=0, column=1, sticky="ew")

    tk.Label(frame_produtos, text="Tipo").grid(row=1, column=0, sticky="w")
    entry_tipo = tk.Entry(frame_produtos)
    entry_tipo.grid(row=1, column=1, sticky="ew")

    tk.Label(frame_produtos, text="Marca").grid(row=2, column=0, sticky="w")
    entry_marca = tk.Entry(frame_produtos)
    entry_marca.grid(row=2, column=1, sticky="ew")

    tk.Label(frame_produtos, text="Preço").grid(row=3, column=0, sticky="w")
    entry_preco = tk.Entry(frame_produtos)
    entry_preco.grid(row=3, column=1, sticky="ew")

    tk.Label(frame_produtos, text="Quantidade").grid(row=4, column=0, sticky="w")
    entry_quantidade = tk.Entry(frame_produtos)
    entry_quantidade.grid(row=4, column=1, sticky="ew")

    botao_adicionar = tk.Button(frame_produtos, text="Adicionar Produto", command=adicionar)
    botao_adicionar.grid(row=5, column=1, pady=10, sticky="ew")

    listbox_produtos = tk.Listbox(frame_produtos, width=80)
    listbox_produtos.grid(row=6, column=0, columnspan=2, pady=10, sticky="ew")

    # Aba de Registro de Vendas
    aba_vendas = ttk.Frame(notebook)
    notebook.add(aba_vendas, text='Registrar Venda')

    frame_vendas = tk.LabelFrame(aba_vendas, text="Registrar Venda", padx=10, pady=10)
    frame_vendas.pack(fill="both", expand=True, padx=10, pady=10)

    tk.Label(frame_vendas, text="Nome do Produto").grid(row=0, column=0, sticky="w")
    combobox_produto_nome = ttk.Combobox(frame_vendas)
    combobox_produto_nome.grid(row=0, column=1, sticky="ew")
    combobox_produto_nome['values'] = [produto[1] for produto in listar_produtos()]
    combobox_produto_nome['state'] = 'readonly'

    tk.Label(frame_vendas, text="Quantidade Vendida").grid(row=1, column=0, sticky="w")
    entry_quantidade_venda = tk.Entry(frame_vendas)
    entry_quantidade_venda.grid(row=1, column=1, sticky="ew")

    tk.Label(frame_vendas, text="Observação").grid(row=2, column=0, sticky="w")
    entry_observacao = tk.Entry(frame_vendas)
    entry_observacao.grid(row=2, column=1, sticky="ew")

    tk.Label(frame_vendas, text="Valor da Venda").grid(row=3, column=0, sticky="w")
    entry_valor_venda = tk.Entry(frame_vendas)
    entry_valor_venda.grid(row=3, column=1, sticky="ew")

    tk.Label(frame_vendas, text="Funcionário").grid(row=4, column=0, sticky="w")
    combobox_funcionario = ttk.Combobox(frame_vendas)
    combobox_funcionario.grid(row=4, column=1, sticky="ew")
    combobox_funcionario['values'] = [funcionario[1] for funcionario in listar_funcionarios()]
    combobox_funcionario['state'] = 'readonly'

    tk.Label(frame_vendas, text="Método de Pagamento").grid(row=5, column=0, sticky="w")
    combobox_metodo_pagamento = ttk.Combobox(frame_vendas, values=["Dinheiro", "Pix", "Crédito", "Débito"])
    combobox_metodo_pagamento.grid(row=5, column=1, sticky="ew")
    combobox_metodo_pagamento['state'] = 'readonly'

    botao_vender = tk.Button(frame_vendas, text="Registrar Venda", command=vender)
    botao_vender.grid(row=6, column=1, pady=10, sticky="ew")

    listbox_vendas = tk.Listbox(frame_vendas, width=80)
    listbox_vendas.grid(row=7, column=0, columnspan=2, pady=10, sticky="ew")

    # Aba de Cadastro de Funcionários
    aba_funcionarios = ttk.Frame(notebook)
    notebook.add(aba_funcionarios, text='Cadastrar Funcionário')

    frame_funcionarios = tk.LabelFrame(aba_funcionarios, text="Adicionar Funcionário", padx=10, pady=10)
    frame_funcionarios.pack(fill="both", expand=True, padx=10, pady=10)

    tk.Label(frame_funcionarios, text="Nome do Funcionário").grid(row=0, column=0, sticky="w")
    entry_nome_func = tk.Entry(frame_funcionarios)
    entry_nome_func.grid(row=0, column=1, sticky="ew")

    tk.Label(frame_funcionarios, text="Cargo").grid(row=1, column=0, sticky="w")
    entry_cargo_func = tk.Entry(frame_funcionarios)
    entry_cargo_func.grid(row=1, column=1, sticky="ew")

    tk.Label(frame_funcionarios, text="Horário").grid(row=2, column=0, sticky="w")
    combobox_horario_func = ttk.Combobox(frame_funcionarios, values=["9h às 17h", "17h às 01h"])
    combobox_horario_func.grid(row=2, column=1, sticky="ew")
    combobox_horario_func['state'] = 'readonly'

    tk.Label(frame_funcionarios, text="Salário").grid(row=3, column=0, sticky="w")
    entry_salario_func = tk.Entry(frame_funcionarios)
    entry_salario_func.grid(row=3, column=1, sticky="ew")

    botao_adicionar_func = tk.Button(frame_funcionarios, text="Adicionar Funcionário", command=adicionar_func)
    botao_adicionar_func.grid(row=4, column=1, pady=10, sticky="ew")

    listbox_funcionarios = tk.Listbox(frame_funcionarios, width=80)
    listbox_funcionarios.grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")

    # Aba de Listagem de Produtos e Vendas
    aba_listagem = ttk.Frame(notebook)
    notebook.add(aba_listagem, text='Listagem')

    frame_listagem_produtos = tk.LabelFrame(aba_listagem, text="Produtos", padx=10, pady=10)
    frame_listagem_produtos.pack(fill="both", expand=True, padx=10, pady=10)

    listbox_produtos_listagem = tk.Listbox(frame_listagem_produtos, width=80)
    listbox_produtos_listagem.pack(fill="both", expand=True, padx=10, pady=10)

    frame_listagem_vendas = tk.LabelFrame(aba_listagem, text="Vendas", padx=10, pady=10)
    frame_listagem_vendas.pack(fill="both", expand=True, padx=10, pady=10)

    listbox_vendas_listagem = tk.Listbox(frame_listagem_vendas, width=80)
    listbox_vendas_listagem.pack(fill="both", expand=True, padx=10, pady=10)

    atualizar_estoque()
    atualizar_vendas()
    atualizar_funcionarios()
    janela.mainloop()