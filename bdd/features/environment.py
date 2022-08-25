from playwright.sync_api import sync_playwright
from features.page_objects.Serverest.serverest_page_index import *
from features.helper.page_helper import *
from features.fixtures.factory import *
from behave import use_fixture
from behave.model import Status
import time


def before_all(context):
    print("-----------------Iniciando teste--------------")
    # instancia do navegador:
    playwright = sync_playwright().start()
    headless = context.config.userdata.getbool('headless', False)
    context.browser = playwright.chromium.launch(headless=headless)

    # Instância dos page objects:
    context.serverest = ServerestIndex(context)
    # Instância do page_helpers:
    context.page_helper = PageHelper(context)
    # Instância do factory:
    context.factory = Factory(context)

    #mailosaur
    context.mailosaur_serverid = "zlp5m1hh"
    context.mailosaur_domain = ".mailosaur.net"
    context.mailosaur_api_key = "HLPud1BuDOUeTAoA"
    
def before_scenario(context, scenario):
    use_fixture(browser_context_fixture, context)

def after_step(context, step):
    pass

def after_all(context):
    print("----------------Encerrando teste---------------")
    context.browser.close()

def browser_context_fixture(context):
    # Cria novo contexto
    context.browser_options = context.browser.new_context()
    context.browser_options.clear_cookies()
    context.browser_options.clear_permissions()

    # Cria nova página
    context.page = context.browser_options.new_page()
    context.page.set_default_timeout(10000)

    yield context.browser_options

    # Limpa o contexto
    context.browser_options.close()