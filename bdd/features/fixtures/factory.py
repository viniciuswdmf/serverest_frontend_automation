import json
from os.path import dirname, realpath, isfile
from faker import Faker
from datetime import *


class Factory():

    def __init__(self, context):
        pass

    def retornar_json(self, arquivo):
        with open("features/fixtures/{}".format(arquivo)) as data_teste:
            data = json.load(data_teste)
            return data
    
    def transformar_string_em_Json(self, context, string):
        objetoJson = json.loads(string)

        return objetoJson

    def retornar_usuario_dinamico_valido(self, context):
        usuario = {
            "nomeCompleto": Faker().name(),
            "email": str(datetime.now().strftime("%d_%m_%y-%H_%M_%S@")),
            "senha": Faker('pt_BR').password()
        }
        return usuario


