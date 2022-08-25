from features.helper.page_helper import *
from features.page_objects.Serverest.pages.components.el_home import *
from features.page_objects.Serverest.pages.components.el_login import *
from features.page_objects.Serverest.pages.components.el_cadastro import *
from playwright.sync_api import expect
import time

class ServerestCadastro():
    
    def __init__(self, context):
        pass

    def define_email_temporario(self, context):
        try:
            assert isinstance(context.mailosaur_serverid, str) and isinstance(context.mailosaur_domain, str)
            context.mailosaur_email = context.usuario["email"] + context.mailosaur_serverid + context.mailosaur_domain
        except Error:
            print(f'>> Não foi possível definir o e-mail temporário! << \n {Error}')

    # def preencher_cadastro(self, context, nome, email, senha):
    #     context.page.fill(cadastro_elements['INPUT_NOME'], nome)
    #     context.page.fill(cadastro_elements['INPUT_EMAIL'], email)
    #     context.page.fill(cadastro_elements['INPUT_SENHA'], senha)
    #     context.page.click(cadastro_elements['BTN_CADASTRAR']) 

    def preencher_cadastro(self, context):
        context.page.fill(cadastro_elements['INPUT_NOME'], context.usuario["nomeCompleto"])
        context.page.fill(cadastro_elements['INPUT_EMAIL'], context.mailosaur_email)
        context.page.fill(cadastro_elements['INPUT_SENHA'], context.usuario["senha"])
        context.page.click(cadastro_elements['BTN_CADASTRAR'])

    def preencher_cadastro_exception(self, context, tipo_erro):
        if tipo_erro == "nome nao preenchido":
            context.page.fill(cadastro_elements['INPUT_NOME'], " ")
            context.page.fill(cadastro_elements['INPUT_EMAIL'], context.mailosaur_email)
            context.page.fill(cadastro_elements['INPUT_SENHA'], context.usuario["senha"])
            context.page.click(cadastro_elements['BTN_CADASTRAR'])
        else:
            context.page.fill(cadastro_elements['INPUT_NOME'], context.usuario["nomeCompleto"])
            context.page.fill(cadastro_elements['INPUT_EMAIL'], " ")
            context.page.fill(cadastro_elements['INPUT_SENHA'], context.usuario["senha"])
            context.page.click(cadastro_elements['BTN_CADASTRAR'])

    def validar_cadastro_sucesso(self, context):
        locator = context.page.locator(cadastro_elements['ALERTA_CADASTRO'])
        expect(locator).to_have_text("Cadastro realizado com sucesso")

    def validar_cadastro_exception(self, context, mensagem):
        locator = context.page.locator(cadastro_elements['ALERTA_ERRO_CADASTRO'])
        expect(locator).to_have_text(mensagem)