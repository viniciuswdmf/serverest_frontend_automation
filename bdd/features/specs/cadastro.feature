#language: pt

Funcionalidade: Cadastro no site de teste
    Como futuro usuario do site
    Quero realizar cadastro
    Para poder acessar suas funcionalidades

Contexto: Acessar o site no ambiente selecionado
    Dado que acesse o site
    E que tenha sido gerado um usuario valido
    E que tenha sido gerado um email valido

# @cadastro
# Cenário: Realizar cadastro
#     Dado que acesse o formulario de cadastro
#     Quando preencher as informações necessárias
#     Então o usuario deve ser cadastrado

@cadastro_exception
Esquema do Cenário: Realizar cadastro com erro
    Dado que acesse o formulario de cadastro
    Quando preencher as informações necessárias com "<tipo_erro>"
    Então a "<mensagem>" de erro deve ser exibida
    Exemplos:
    | tipo_erro             |         mensagem                  |
    | nome nao preenchido   | Nome é obrigatório                |
    | email nao preenchido  | Email é obrigatório               |
#     | senha invalida       |          |
#     | nome nao preenchido  |          |
#     | email nao preenchido |          |
#     | senha nao preenchido |          |