"""Core module for GRAVI-NEURAL constructs."""

from gravineural.core.cno import CovariantNeuralOperator, CovariantResult
from gravineural.core.gno import GravitationalNeuralOperator, GNOResult
from gravineural.core.stcn import SpaceTimeCovariantNetwork, STCNResult
from gravineural.core.mgan import MicroGravityAnomalyNetwork, MGANResult

__all__ = [
    "CovariantNeuralOperator",
    "CovariantResult",
    "GravitationalNeuralOperator",
    "GNOResult",
    "SpaceTimeCovariantNetwork",
    "STCNResult",
    "MicroGravityAnomalyNetwork",
    "MGANResult",
]
