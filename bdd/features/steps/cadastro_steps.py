from behave import given, when , then
import time

@given(u'que acesse o formulario de cadastro')
def acessar_pagina_cadastro(context):
    context.serverest.login.acessar_cadastro(context)

@when(u'preencher as informações necessárias')
def preencher_dados_cadastro(context):
    context.serverest.cadastro.preencher_cadastro(context)


@then(u'o usuario deve ser cadastrado')
def validar_cadastro_usuario(context):
    context.serverest.cadastro.validar_cadastro_sucesso(context)


@when(u'preencher as informações necessárias com "{tipo_erro}"')
def preencher_dados_cadastro_erro(context, tipo_erro):
    context.serverest.cadastro.preencher_cadastro_exception(context, tipo_erro)

@then(u'a "{mensagem}" de erro deve ser exibida')
def validar_cadastro_usuario_erro(context, mensagem):
    context.serverest.cadastro.validar_cadastro_exception(context, mensagem)