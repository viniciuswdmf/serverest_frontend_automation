from behave import given, when, then
import time

@given(u'que esteja logado')
def estar_logado(context):
    context.serverest.login.acessar_site_login(context)
    context.serverest.login.fazer_login_com_parametros(context, "tarcisio@cy.com", "1")