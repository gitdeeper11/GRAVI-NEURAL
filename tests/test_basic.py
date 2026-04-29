"""Basic tests for GRAVI-NEURAL."""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gravineural.core.cno import CovariantNeuralOperator
from gravineural.core.gno import GravitationalNeuralOperator
from gravineural.core.stcn import SpaceTimeCovariantNetwork
from gravineural.core.mgan import MicroGravityAnomalyNetwork


def test_cno():
    cno = CovariantNeuralOperator()
    stress_energy = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    coordinates = [0,10,0,0]
    result = cno.compute_metric(stress_energy, coordinates)
    assert 0 <= result.ef_e_residual <= 1
    assert result.status in ["EXCELLENT", "GOOD", "MODERATE", "CRITICAL", "COLLAPSE"]
    print(f"✓ CNO test passed: residual = {result.ef_e_residual:.4f} [{result.status}]")


def test_gno():
    gno = GravitationalNeuralOperator()
    stress_energy = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    result = gno.forward(stress_energy)
    assert len(result.perturbation) == 4
    print(f"✓ GNO test passed: inference time = {result.inference_time_ms:.2f} ms")


def test_stcn():
    stcn = SpaceTimeCovariantNetwork()
    perturbation = [[0.1,0,0,0],[0,0.1,0,0],[0,0,0.1,0],[0,0,0,0.1]]
    coordinates = [0,1,0,0]
    result = stcn.correct(perturbation, coordinates)
    assert result.covariance_error < 0.01
    print(f"✓ S-TCN test passed: covariance error = {result.covariance_error:.4f}")


def test_mgan():
    mgan = MicroGravityAnomalyNetwork()
    gradiometry = [1e-11] * 6
    macro_metric = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    result = mgan.invert(gradiometry, macro_metric)
    assert result.reconstruction_error > 0
    print(f"✓ M-GAN test passed: confidence = {result.confidence:.4f}")


if __name__ == "__main__":
    test_cno()
    test_gno()
    test_stcn()
    test_mgan()
    print("\n✅ All basic tests passed!")
