import tkinter as tk
import sqlite3
import pandas as pd
from openpyxl.workbook import Workbook
#Criar banco de dados
#conexao = sqlite3.connect("Banco_Clientes.db")

#cursor = conexao.cursor()
#criar tabela
#cursor.execute(''' CREATE TABLE clientes (
#               nome text,
#               sobrenome text,
#               email text, 
#               telefone text
#)
#''')
#conexao.commit()
#conexao.close()

def cadastrar_clientes():
    #Copia da criação do banco
    conexao = sqlite3.connect("Banco_Clientes.db")

    cursor = conexao.cursor()
    #tabela
    cursor.execute("INSERT INTO clientes VALUES (:nome, :sobrenome, :email, :telefone)",
                   {
                       'nome':entry_nome.get(),
                       'sobrenome':entry_sobrenome.get(),
                       'email':entry_email.get(),
                       'telefone':entry_telefone.get()
                   }
                   )
    
    conexao.commit()

    conexao.close()
    entry_nome.delete(0, 'end')
    entry_sobrenome.delete(0, 'end')
    entry_email.delete(0, 'end')
    entry_telefone.delete(0, 'end')
def exportar_clientes():
    #Conectando ao banco
    conexao = sqlite3.connect("Banco_Clientes.db")

    cursor = conexao.cursor()
    #Selecionando tabela
    cursor.execute("SELECT *, oid FROM clientes")
    clientes_cadastrados = cursor.fetchall()
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns=['nome', 'sobrenome', 'email', 'telefone', 'ID_banco'])
    clientes_cadastrados.to_excel('Banco_Clientes.xlsx')
    conexao.commit()
    conexao.close()

#Criar interface grafica
janela = tk.Tk()
janela.title("Ferramenta de cadastro de clientes")
#label
label_nome = tk.Label(janela, text="Nome")
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text="Sobrenome")
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text="E-mail")
label_email.grid(row=2, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela, text="Telefone")
label_telefone.grid(row=3, column=0, padx=10, pady=10)

# Entrys

entry_nome = tk.Entry(janela, text="Nome", width=30)
entry_nome.grid(row=0, column=2, padx=10, pady=10)

entry_sobrenome = tk.Entry(janela, text="Sobrenome", width=30)
entry_sobrenome.grid(row=1, column=2, padx=10, pady=10)

entry_email = tk.Entry(janela, text="E-mail", width=30)
entry_email.grid(row=2, column=2, padx=10, pady=10)

entry_telefone = tk.Entry(janela, text="Telefone", width=30)
entry_telefone.grid(row=3, column=2, padx=10, pady=10)


#botão
botao_cadastrar = tk.Button(janela, text="Cadastrar Cliente", command = cadastrar_clientes)
botao_cadastrar.grid(row=4, column=0, padx=10, pady=10, columnspan=5, ipadx=30)

botao_exportar = tk.Button(janela, text="Exportar", command = exportar_clientes)
botao_exportar.grid(row=5, column=0, padx=10, pady=10, columnspan=5, ipadx=30)

janela.mainloop()
