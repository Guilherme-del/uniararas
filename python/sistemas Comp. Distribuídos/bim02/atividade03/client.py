import requests as req, json
dados = {
    "nome" : "marcilio oliveira",
    "ra" : "ra1222",
    "email" : "m@fho.edu.br",
    "media" : 5
}
import getpass as gp
#função que vai montar as urls do proxy
def proxies() :
    user = input("User:")
    pwd = gp.getpass("Senha:")
    url = "http://" + user + ":" + pwd + "@127.0.0.1:5000"
    proxies = {
        'http' : url,
        'https': url
    }
    return proxies

response = req.post("http://127.0.0.1:5000/aluno", 
                    data=json.dumps(dados))#, 
                    #proxies=proxies())