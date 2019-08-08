class FeatureModule:
    def __init__(self):
        print('I am FeatureModule inject into Core')
        pass

    def helloWorld(self):
        print('hello I am FeatureModule')

    pass


class RecommendModule:
    def __init__(self):
        print('I am RecommendModule inject into Core')
        pass

    pass


class FilteringModule:
    def __init__(self):
        print('I am FilteringModule inject into Core')
        pass

    pass