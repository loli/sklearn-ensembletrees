"""
The :mod:`sklearn.ensemble` module includes ensemble-based methods for
classification and regression.
"""

from .base import BaseEnsemble
from .forest import RandomForestClassifier
from .forest import RandomForestRegressor
from .forest import RandomTreesEmbedding
from .forest import MixedForestClassifier
from .forest import MixedForestRegressor
from .forest import ExtraTreesClassifier
from .forest import ExtraTreesRegressor
from .bagging import BaggingClassifier
from .bagging import BaggingRegressor
from .weight_boosting import AdaBoostClassifier
from .weight_boosting import AdaBoostRegressor
from .gradient_boosting import GradientBoostingClassifier
from .gradient_boosting import GradientBoostingRegressor

from . import bagging
from . import forest
from . import weight_boosting
from . import gradient_boosting
from . import partial_dependence

__all__ = ["BaseEnsemble", "MixedForestClassifier", "MixedForestRegressor",
           "RandomForestClassifier", "RandomForestRegressor",
           "RandomTreesEmbedding", "ExtraTreesClassifier",
           "ExtraTreesRegressor", "BaggingClassifier",
           "BaggingRegressor", "GradientBoostingClassifier",
           "GradientBoostingRegressor", "AdaBoostClassifier",
           "AdaBoostRegressor", "bagging", "forest", "gradient_boosting",
           "partial_dependence", "weight_boosting"]
