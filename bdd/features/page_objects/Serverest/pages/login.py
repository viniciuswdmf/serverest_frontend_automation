from features.helper.page_helper import *
from features.page_objects.Serverest.pages.components.el_home import *
from features.page_objects.Serverest.pages.components.el_login import *
from playwright.sync_api import expect
import time

class ServerestLogin():
    
    def __init__(self, context):
        pass

    def acessar_site_login(self, context):
        context.page_helper.acessar(context, "")

    def acessar_cadastro(self, context):
        context.page.click(login_elements['LINK_CADASTRO'])

    def efetuar_login_valido(self, context, cpf, senha):
        context.page.fill(login_elements['INP_LOGIN'], cpf)
        context.page.fill(login_elements['INP_SENHA'], senha)
        context.page.click(login_elements['INP_BTN_LOGIN']) 
        time.sleep(5)

    def fazer_login_invalido(self, context, login):
        context.page.fill(login_elements['INP_LOGIN'], login)   
        context.page.click(login_elements['INP_BTN_LOGIN']) 

    def validar_login_correto(self, context):
        locator = context.page.locator(body_elements['TOAST_SUCESS'])
        expect(locator).to_be_visible()

    def validar_login_incorreto(self, context, mensagem):
        locator = context.page.locator(body_elements['TOAST_ERRO'])
        expect(locator).to_have_text("Cadastro realizado com sucesso")

