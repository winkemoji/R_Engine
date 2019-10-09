from Builder import EngineBuilder
from Modules.RecommendModule import RecommendBase
from Modules.FilteringModule import FilteringBase
from Modules.FeatureModule import FeatureBase

config = {

}
modules = {
    'FeatureModule': FeatureBase(),
    'RecommendModule': RecommendBase(),
    'FilteringModule': FilteringBase()
}

if __name__ == '__main__':
    EngineBuilder(config=config).build(modules).run()
