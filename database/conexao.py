import mysql.connector

def conectar():
    tipo_conexao = "NUVEM"
    if tipo_conexao == "LOCAL":
        conexao=mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="root",
                database="youã"
            )
    else:
        conexao=mysql.connector.connect(
                host="servidor-pablo-servidor-pablo.a.aivencloud.com",
                port=12176,
                user="avnadmin",
                password="AVNS_VFMgYg6Tyz27bFOtd4N",
                database="youã"
            )
    cursor=conexao.cursor(dictionary=True)

    return conexao, cursor

