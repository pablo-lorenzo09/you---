from database.conexao import conectar

def cadastrar_usuarios(usuario:str, senha:str):
    conexao,cursor = conectar()

     
    cursor.execute("""insert into `youã`.`usuarios`
                      (`usuario`,
                       `senha`)
                   
                    values
                    (%s,%s)""",(usuario, senha))


    conexao.commit()
    conexao.close()

def autenticar_usuario(usuario:str, senha:str):
    conexao,cursor = conectar()

     
    cursor.execute("""
                    select usuario, senha from usuarios
                   WHERE usuario = %s and senha = %s """,(usuario, senha))
    
    usuarios=cursor.fetchone()
    
    conexao.commit()
    conexao.close()

    if usuarios:
        return True
    else:
        return False
    