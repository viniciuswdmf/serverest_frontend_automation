from behave import given, when , then
import time

@given(u'que acesse o formulario de cadastro')
def acessar_pagina_cadastro(context):
    context.serverest.login.acessar_site_login(context)
    context.serverest.home.acessar_registro(context)
    time.sleep(5)

@when(u'preencher as informações necessárias')
def preencher_dados_registro(context):
    context.serverest.registro.registrar_com_parametros(context, "Teste QA", "testeqa@email.com", "123456")


@then(u'o usuario deve ser cadastrado')
def validar_registro_usuario(context):
    context.serverest.registro.validar_registro_correto(context)