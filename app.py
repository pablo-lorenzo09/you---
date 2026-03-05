
from flask import Flask, render_template,request,redirect,session
import mysql
import mysql.connector
from model.musica import recuperar_musicas
from model.musica import adicionar_musica
from model.musica import deletar_musica
from model.musica import alterar_musica
from model.musica import recuperar_musicas_filtro
from model.musica import recuperar_musicas_dois
from model.usuario_model import cadastrar_usuarios
from model.usuario_model import autenticar_usuario

from model.genero import recuperar_generos

app = Flask(__name__)
app.secret_key =  "euamoocauakkkmentira"
@app.route("/")
@app.route("/home",methods=["GET"])
def pag_principal():
    musicas = recuperar_musicas()
    genero = recuperar_generos()

    return render_template("principal.html",musicas=musicas,genero=genero)

@app.route("/admin")

def pag_adm():
    musicas = recuperar_musicas_dois()
    genero = recuperar_generos()
    if 'usuario_logado' in session:
        return render_template("administracao.html",musicas=musicas,genero=genero)
    else:
        return redirect("/login")


@app.route("/admin",methods=["POST"])
def pag_adm_post():
    musica = request.form.get("musica")
    cantor = request.form.get("cantor")
    duracao = request.form.get("duracao")
    url_capa = request.form.get("url_capa")
    genero= request.form.get("nome_genero")

    
    adicionar_musica(cantor,duracao,musica,url_capa,genero)
    return redirect("/admin")

@app.route("/admin/delete/<int:id>")
def deletar(id):
    deletar_musica(id)
    return redirect("/admin")
    
@app.route("/admin/alterar/<int:id>")
def alterar(id):
    alterar_musica(id)
    return redirect("/admin")
    
@app.route("/filtrar/<genero_musica>")
def filtro(genero_musica):
    genero = recuperar_generos()
    musicas = recuperar_musicas_filtro(genero_musica)

    return render_template("principal.html",musicas=musicas,genero=genero)

@app.route("/cadastro")
def tela_cadastro():
    return render_template("cadastro.html")

@app.route("/cadastro",methods=["POST"])
def tela_cadastro_post():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    
    cadastrar_usuarios(usuario, senha)
    return render_template("cadastro.html")

@app.route("/login")
def tela_login():
    return render_template("login.html")

@app.route("/login",methods=["POST"])
def tela_login_post():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    
    if autenticar_usuario(usuario, senha):
        session['usuario_logado'] = usuario
        return redirect("/admin")
    else:
        return redirect("/login")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)
