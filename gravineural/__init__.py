"""GRAVI-NEURAL: Covariant Neural Characterization of Metric Tensor Perturbations.

A Physics-Informed AI framework for solving Einstein Field Equations,
learning metric perturbations, and predicting gravitational wave signals
in dynamic gravitational environments.

E-LAB-08 | EntropyLab Research Program
"""

__version__ = "1.0.0"
__doi__ = "10.5281/zenodo.19871822"
__author__ = "Samir Baladi"
__email__ = "gitdeeper@gmail.com"

from gravineural.core.cno import CovariantNeuralOperator
from gravineural.core.gno import GravitationalNeuralOperator
from gravineural.core.stcn import SpaceTimeCovariantNetwork
from gravineural.core.mgan import MicroGravityAnomalyNetwork

__all__ = [
    "CovariantNeuralOperator",
    "GravitationalNeuralOperator",
    "SpaceTimeCovariantNetwork",
    "MicroGravityAnomalyNetwork",
]
