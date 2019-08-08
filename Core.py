from R_Engine.Mapper import Mapper, Module


class Core(metaclass=Module):
    def __init__(self, modules):
        self.modules = modules
        for name in modules.keys():
            setattr(self, name, modules[name])


class Engine(object):
    def __init__(self, opts=None, inject=dict):
        print('init engine')
        Mapper.register(Core, inject)
        self.core = Core()



    def run(self):
        print('engine is running')

    def shutDown(self):
        print('engine is shutdown')
