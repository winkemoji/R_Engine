from R_Engine.Builder import EngineBuilder
from R_Engine.Module import FeatureModule, RecommendModule, FilteringModule, HttpContextModule

config = {

}
modules = {
    'FeatureModule': FeatureModule(),
    'RecommendModule': RecommendModule(),
    'FilteringModule': FilteringModule(),
    # 'HttpContextModule': HttpContextModule(),
}



if __name__ == '__main__':
        EngineBuilder(config=config).build(modules).run()