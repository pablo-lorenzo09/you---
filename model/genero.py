from database.conexao import conectar

def recuperar_generos():
    conexao,cursor = conectar()

     
    cursor.execute("SELECT genero,icone,cor FROM genero;")
    
    genero=cursor.fetchall()

    conexao.close()

    return genero