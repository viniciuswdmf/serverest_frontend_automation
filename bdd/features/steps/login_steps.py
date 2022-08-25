from behave import given, when, then
import time

@when(u'realizar login com CPF e senha válidos')
def realizar_login_teste(context):
    context.serverest.login.acessar_site_login(context)
    context.serverest.login.fazer_login_com_parametros(context, "tarcisio@cy.com", "1")


@then(u'deve validar que o login foi realizado com sucesso')
def verificar_login(context):
    context.serverest.login.validar_login_correto(context)

###################Login sem sucesso

@when(u'realizar login com "{login}" invalido')
def realizar_login_invalido(context, login):
    context.serverest.login.acessar_site_login(context)
    context.serverest.login.fazer_login_invalido(context, login)


@then(u'deve ser exibida a mensagem de erro "{mensagem}"')
def verificar_erro_login(context, mensagem):
    context.serverest.login.validar_login_incorreto(context, mensagem)