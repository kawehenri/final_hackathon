# Conexão com o banco
import mysql.connector

conn = mysql.connector.connect(
    user='root',
    host='localhost',
    database='sistema_despesas'
)

# Verificação da conexão
if conn.is_connected:
    print('Banco conectado com sucesso! ')

else:
    print('Falha ao conectar com o banco! ')