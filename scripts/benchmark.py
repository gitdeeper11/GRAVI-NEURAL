#!/usr/bin/env python
"""Framework performance benchmarking for GRAVI-NEURAL."""

import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gravineural.core.cno import CovariantNeuralOperator
from gravineural.core.gno import GravitationalNeuralOperator
from gravineural.core.stcn import SpaceTimeCovariantNetwork
from gravineural.core.mgan import MicroGravityAnomalyNetwork


def benchmark_cno(n_iterations: int = 100):
    """Benchmark CNO computation speed."""
    cno = CovariantNeuralOperator()
    stress_energy = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    coordinates = [0,10,0,0]
    
    start = time.time()
    for _ in range(n_iterations):
        result = cno.compute_metric(stress_energy, coordinates)
    elapsed = time.time() - start
    
    print(f"CNO Computation: {n_iterations} iterations in {elapsed:.3f}s")
    print(f"  Average: {elapsed / n_iterations * 1000:.3f} ms per computation")
    return elapsed


def benchmark_gno(n_iterations: int = 100):
    """Benchmark GNO computation speed."""
    gno = GravitationalNeuralOperator()
    stress_energy = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
    start = time.time()
    for _ in range(n_iterations):
        result = gno.forward(stress_energy)
    elapsed = time.time() - start
    
    print(f"GNO Computation: {n_iterations} iterations in {elapsed:.3f}s")
    print(f"  Average: {elapsed / n_iterations * 1000:.3f} ms per computation")
    return elapsed


def benchmark_stcn(n_iterations: int = 100):
    """Benchmark S-TCN computation speed."""
    stcn = SpaceTimeCovariantNetwork()
    perturbation = [[0.1,0,0,0],[0,0.1,0,0],[0,0,0.1,0],[0,0,0,0.1]]
    coordinates = [0,1,0,0]
    
    start = time.time()
    for _ in range(n_iterations):
        result = stcn.correct(perturbation, coordinates)
    elapsed = time.time() - start
    
    print(f"S-TCN Computation: {n_iterations} iterations in {elapsed:.3f}s")
    print(f"  Average: {elapsed / n_iterations * 1000:.3f} ms per computation")
    return elapsed


def benchmark_mgan(n_iterations: int = 100):
    """Benchmark M-GAN computation speed."""
    mgan = MicroGravityAnomalyNetwork()
    gradiometry = [1e-11] * 6
    macro_metric = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    
    start = time.time()
    for _ in range(n_iterations):
        result = mgan.invert(gradiometry, macro_metric)
    elapsed = time.time() - start
    
    print(f"M-GAN Computation: {n_iterations} iterations in {elapsed:.3f}s")
    print(f"  Average: {elapsed / n_iterations * 1000:.3f} ms per computation")
    return elapsed


def main():
    print("=" * 60)
    print("GRAVI-NEURAL Performance Benchmark")
    print("=" * 60)
    
    benchmark_cno(100)
    print()
    benchmark_gno(100)
    print()
    benchmark_stcn(100)
    print()
    benchmark_mgan(100)
    
    print()
    print("=" * 60)
    print("✅ Benchmark complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
