from features.page_objects.Serverest.pages.login import *
from features.page_objects.Serverest.pages.commons import *
from features.page_objects.Serverest.pages.home import *

class ServerestIndex():

    def __init__(self, context):
        self.commons = ServerestCommons(context)
        self.home = ServerestHome(context)
        self.login = ServerestLogin(context)
