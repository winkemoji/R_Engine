from R_Engine.Builder import EngineBuilder
from R_Engine.Modules import RecommendModule, FilteringModule, FeatureModule

config = {

}
modules = {
    'FeatureModule': FeatureModule(),
    'RecommendModule': RecommendModule(),
    'FilteringModule': FilteringModule()
}

if __name__ == '__main__':
    EngineBuilder(config=config).build(modules).run()
