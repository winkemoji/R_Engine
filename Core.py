from Mapper import Mapper, Module


class Core(metaclass=Module):
    """
    推荐引擎核心，相关模块注入进核心里。
    """
    def __init__(self, modules):
        self.modules = modules
        for name in modules.keys():
            setattr(self, name, modules[name])


class Engine(object):
    """
    推荐引擎
    """
    def __init__(self, opts=None, inject=dict):
        print('init engine')
        Mapper.register(Core, inject)
        self.core = Core()



    def run(self):
        """
        启动引擎
        :return:
        """
        print('engine is running')

    def shutDown(self):
        """
        关闭引擎
        :return:
        """
        print('engine is shutdown')
