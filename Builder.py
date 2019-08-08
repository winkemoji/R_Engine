from R_Engine.Core import Engine


def EngineBuilder(config):
    return Builder(config)


class Builder:
    def __init__(self, opts):
        self.opts = opts

    def build(self, modules):
        return Engine(opts=self.opts, inject=modules)
