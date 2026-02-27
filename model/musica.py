from database.conexao import conectar



def recuperar_musicas():
    conexao,cursor = conectar()

     
    cursor.execute("""SELECT musica.id_musica,musica.cantor,musica.duracao,musica.nome,musica.url_capa,musica.nome_genero,musica.stats,genero.cor FROM musica
                        inner join genero on musica.nome_genero = genero.genero 
                        ORDER BY musica.id_musica ASC;""")

    musicas=cursor.fetchall()


    conexao.close()

    return musicas

def adicionar_musica(cantor:str,duracao:str,musica:str,url_capa:str,genero:str) -> bool:
    """
    Adicona músicas com as informações passadas através dos parâmetros.
    """

    conexao,cursor = conectar()

     
    cursor.execute("""INSERT INTO musica (cantor, duracao, nome, stats, url_capa, nome_genero)
                   VALUES(%s,%s,%s,%s,%s,%s)""",(cantor,duracao,musica,"ATIVO",url_capa,genero) )

    conexao.commit()
    conexao.close()

def deletar_musica(id:int) -> bool:

    conexao,cursor = conectar()

     
    cursor.execute("""DELETE FROM musica WHERE id_musica = %s""",(id,))



    conexao.commit()
    conexao.close()

def alterar_musica(id:int) -> bool:
    conexao, cursor = conectar()

    cursor.execute("""SELECT stats FROM musica WHERE id_musica = %s""",(id,))

    status=cursor.fetchone()

    if status["stats"] == "ATIVO":
        cursor.execute("""UPDATE musica
                        SET stats = %s
                        WHERE id_musica = %s;""",("INATIVO",id))
        
    if status["stats"] == "INATIVO":
        cursor.execute("""UPDATE musica
                        SET stats = %s
                        WHERE id_musica = %s;""",("ATIVO",id))

    conexao.commit()
    conexao.close()

def recuperar_musicas_filtro(genero):

    conexao, cursor = conectar()

    cursor.execute("""SELECT musica.id_musica,musica.cantor,musica.duracao,musica.nome,musica.url_capa,musica.nome_genero,musica.stats,genero.cor FROM musica
                        INNER JOIN genero ON musica.nome_genero = genero.genero
                        WHERE musica.nome_genero = %s
                        ORDER BY musica.id_musica ASC;""",(genero,))

    musicas=cursor.fetchall()

    conexao.close()

    return musicas