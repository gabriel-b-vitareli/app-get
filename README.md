# Método POST e GET utilizando Postman e servidor HTTP

A partir do código no arquivo [app-get-post.py](https://github.com/gabriel-b-vitareli/app-get/blob/main/app-get-post.py), criamos um servidor localhost com nosso endereço IP na porta 8000.

A partir desse servidor, usamos o software Postman para requisitar e enviar dados.
O primeiro teste foi usando o método post.

# Requisição com método GET no Postman:

<img width="1919" height="972" alt="image" src="https://github.com/user-attachments/assets/29a40150-89be-4146-9a1b-7f414d02fedf" />

Quando utilizamos esse método, o servidor retornou ao Postman a mensagem "Servidor funcionando com GET", exatamente como havíamos configurado no código. Além disso, ele também retornou o código 200, já que a comunicação foi realizada com sucesso.

# Requisição com método POST:

<img width="1919" height="950" alt="image" src="https://github.com/user-attachments/assets/80679cf3-3f5d-4d73-b94e-52bbd61e7d08" />

Agora utilizando o método post, o Postman envia a requisição (a partir de dados em json) para o servidor, que os recebe e mostra no terminal (nesse caso, o texto "grifado")
