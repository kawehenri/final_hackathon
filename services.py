# Importação da conexão
from conexao import *

# Função de adicionar a despesa
def adicionar_despesa(categoria, valor):
    conn = conn()
    if conn.is_connected():
        cursor = conn.cursor()
        sql = 'INSERT INTO despesas (categoria, valor, data) VALUES (%s, %s, NOW())'
        cursor.execute(sql, (categoria, valor))
        conn.commit()
        cursor.close()
        conn.close()
        print("Despesa adicionada com sucesso!")
    else:
        print("Erro ao conectar ao banco de dados")

# Função de listar as despesas
def listar_despesas():
    conn = conn()
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute('SELECT id, categoria, valor, data FROM despesas')
        despesas = cursor.fetchall()
        cursor.close()
        conn.close()
        return despesas
    else:
        print("Erro ao conectar ao banco de dados")
        return []

# Calculando categoria por categoria
def calcular_total_por_categoria():
    conn = conn()
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute('SELECT categoria, SUM(valor) FROM despesas GROUP BY categoria')
        totais = cursor.fetchall()
        cursor.close()
        conn.close()
        return totais
    else:
        print("Erro ao conectar ao banco de dados")
        return []

# Função de calcular o gasto total
def calcular_gasto_mensal():
    conn = conn()
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute('SELECT SUM(valor) FROM despesas WHERE MONTH(data) = MONTH(NOW())')
        total_mensal = cursor.fetchone()[0] or 0
        cursor.close()
        conn.close()
        return total_mensal
    else:
        print("Erro ao conectar ao banco de dados")
        return 0

# Função para calcular a media
def calcular_media_diaria():
    total_mensal = calcular_gasto_mensal()
    from datetime import datetime
    dia_atual = datetime.now().day
    media_diaria = total_mensal / dia_atual if dia_atual else 0
    return media_diaria
