#language: pt

@login
Funcionalidade: Login no site de teste
    Como um usuário do site de teste
    Quero realizar login 
    Para realizar tarefas no site

Cenário: Fazer login com sucesso
    Quando realizar login com CPF e senha válidos
    Então deve validar que o login foi realizado com sucesso

Esquema do Cenário: Erro ao fazer login
    Quando realizar login com "<login>" invalido
    Então deve ser exibida a mensagem de erro "<mensagem>"
    Exemplos:
        | login     | mensagem                                         |
        | dasjjadsk | Erro: Error: Request failed with status code 400 |