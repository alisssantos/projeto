import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '94156169',
    database = 'bc_projeto',
)
cursor = conexao.cursor()

#CRUD / ENVIO
nome_produto = "barba"
valor = 15
comando = f'INSERT INTO vendas(nome_produto, valor) VALUES ("{nome_produto}", {valor}) '
cursor.execute(comando)
conexao.commit() # edita o banco de dados
resutado = cursor.fetchall() # ler o banco de dados






cursor.close()
conexao.close()