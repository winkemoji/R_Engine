"""
模块管理包
"""

from .FeatureModule import FeatureModule
from .FilteringModule import FilteringModule
from .RecommendModule import RecommendModule

_all_ = [
    'RecommendModule',
    'FilteringModule',
    'FeatureModule'
]