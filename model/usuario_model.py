from database.conexao import conectar

def cadastrar_usuarios(usuario, senha):
    conexao,cursor = conectar()

     
    cursor.execute("""insert into `youã`.`usuarios`
                      (`usuario`,
                       `senha`)
                   
                    values
                    (%s,%s)""",(usuario, senha))


    conexao.commit()
    conexao.close()

    print(senha)

def autenticar_usuario(login, senha):
    pass