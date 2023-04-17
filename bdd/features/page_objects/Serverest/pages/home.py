from features.helper.page_helper import *
from features.page_objects.Serverest.pages.components.el_home import *
from features.page_objects.Serverest.pages.components.el_login import *
from playwright.sync_api import expect
import time

class ServerestHome():
    
    def __init__(self, context):
        pass

    def acessar_movimentacao(self, context):
        context.page.click(body_elements['MENU_MOVIMENTACAO']) 
        time.sleep(5)
    
    def acessar_extrato(self, context):
        context.page.click(body_elements['MENU_EXTRATO'])
        time.sleep(5)

    def acessar_conta(self, context):
        context.page.click(body_elements['DROPDOWN_MENU'])
        time.sleep(3)
        context.page.click(body_elements['MENU_CONTA'])
        time.sleep(5)

    def resetar_infos(self, context):
        context.page.click(body_elements['DROPDOWN_MENU'])
        time.sleep(3)
        context.page.click(body_elements['MENU_RESET'])

    def validar_reset(self, context):
        locator = context.page.locator(body_elements['TOAST_SUCESS'])
        expect(locator).to_be_visible()