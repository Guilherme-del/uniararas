Construa uma webAPI Rest para o seguinte contexto:

Você deverá fazer a gestão de um carrinho de compras de um site, sendo que cada carrinho pertence a um usuário em específico.
Dessa forma, crie um CRUD para gerenciar esses carrinhos, respeitando os requisitos abaixo. Além disso, você deverá criar um CLIENTE baseado no módulo requests para consumir os endpoints da sua webAPI.

*Você deverá anexar uma documentação sobre sua WEBAPI, ou seja, documentando cada endpoint e a forma de uso, parâmetros necessários para utilizar cada um, método http correto e tipo de retorno.

Fragmento de um JSON que representa a estrutura de usuários/carrinhos:

{
   'usuario' : 'marcilio',
   'nome' : 'Marcilio F Oliveira',
   'id' : 1,
   'carrinho' : {
        'total' : 42,53
        'produtos' : [
             {
                  'codigo' : 1,
                  'nome' : 'película de celular',
                  'valor': 30,00
              },
              {
                  'codigo' : 22,
                  'nome' : 'caneta de quadro branco',
                  'valor' : 12,53
              }
         ]
    }
}

- Endpoint para listar os produtos do carrinho por usuário [Método HTTP GET];
- Endpoint para remover algum produto do carrinho de um determinado usuário através do código [Método HTTP DELETE];
- Endpoint para adicionar algum produto no carrinho de um determinado usuário [Método HTTP POST];
- Endpoint para atualizar o nome do usuário [Método HTTP PUT];
- Endpoint para criar um usuário no servidor [Método HTTP POST];
- Endpoint para exibir o total de usuários existentes [Método HTTP GET];
- Endpoint para exibir a somatória de todos os carrinhos existentes no servidor [Método HTTP GET];