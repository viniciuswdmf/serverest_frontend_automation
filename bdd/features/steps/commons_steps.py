from behave import given, when, then
import time

@given(u'que acesse o site')
def acesso_site(context):
    context.serverest.login.acessar_site_login(context)

@given(u'que tenha sido gerado um usuario valido')
def gerar_usuario_valido(context):
    context.usuario = context.factory.retornar_usuario_dinamico_valido(context)


@given(u'que tenha sido gerado um email valido')
def gerar_email_valido(context):
    context.serverest.cadastro.define_email_temporario(context)

# @given(u'que esteja logado')
# def estar_logado(context):
#     context.serverest.login.acessar_site_login(context)
#     context.serverest.login.fazer_login_com_parametros(context, "tarcisio@cy.com", "1")