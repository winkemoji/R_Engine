from R_Engine.Builder import EngineBuilder
from R_Engine.Modules.RecommendModule import RecommendBase
from R_Engine.Modules.FilteringModule import FilteringBase
from R_Engine.Modules.FeatureModule import FeatureBase

config = {

}
modules = {
    'FeatureModule': FeatureBase(),
    'RecommendModule': RecommendBase(),
    'FilteringModule': FilteringBase()
}

if __name__ == '__main__':
    EngineBuilder(config=config).build(modules).run()
