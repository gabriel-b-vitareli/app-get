# Importa a função HTTPServer e BaseHTTPRequestHandler da biblioteca http.server para uso posterior no código:

from http.server import HTTPServer, BaseHTTPRequestHandler


class Servidor(BaseHTTPRequestHandler):
    
    # Método GET (Acessa as informações do servidor)
    def do_GET(self):
       # Envia o código 200 e a mensagem caso a comunicação seja realizada com sucesso:
       self.send_response(200)
       self.end_headers()
       self.wfile.write(b"Servidor funcionando com GET")

    # Método POST (Envia informações do servidor)
    def do_POST(self):
       
       # Pega o tamanho dos dados enviados na requisição, lê e mostra eles:

       tamanho = int(self.headers['Content-Length'])
       dados = self.rfile.read(tamanho)
       print("Dados recebidos:", dados.decode())


       # Envia resposta para o cliente:

       self.send_response(200)
       self.end_headers()
       self.wfile.write(b"POST recebido")


# Habilita o servidor na porta 8000:

HTTPServer(("0.0.0.0", 8000), Servidor).serve_forever()