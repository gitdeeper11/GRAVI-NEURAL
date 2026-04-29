#!/usr/bin/env python
"""Standalone metric computation script for GRAVI-NEURAL."""

import argparse
import sys
import os
import math

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gravineural.core.cno import CovariantNeuralOperator


def main():
    parser = argparse.ArgumentParser(description="Compute metric from stress-energy tensor")
    parser.add_argument("--spacetime", type=str, default="schwarzschild", help="Spacetime type")
    parser.add_argument("--mass", type=float, default=1.0, help="Mass (solar masses)")
    parser.add_argument("--spin", type=float, default=0.0, help="Spin parameter")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    parser.add_argument("--output", type=str, default=None, help="Output file")

    args = parser.parse_args()

    # Initialize CNO
    cno = CovariantNeuralOperator()

    # Create stress-energy tensor for given spacetime
    stress_energy = [
        [args.mass, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
    ]

    coordinates = [0.0, 10.0, 0.0, 0.0]

    # Compute metric
    result = cno.compute_metric(stress_energy, coordinates)

    print("=" * 60)
    print(f"Spacetime: {args.spacetime}")
    print(f"Mass: {args.mass} M_☉")
    print(f"EFE Residual: {result.ef_e_residual:.4f} [{result.status}]")
    print(f"Bianchi Violation: {result.bianchi_violation:.4e}")
    print(f"Ricci Scalar: {result.ricci_scalar:.4f}")
    print("-" * 60)
    print("Metric Tensor g_μν:")
    for i, row in enumerate(result.metric_tensor):
        print(f"  g_{i}{i}: {row[i]:.6f}")
    print("=" * 60)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(f"Spacetime,{args.spacetime}\n")
            f.write(f"Mass,{args.mass}\n")
            f.write(f"EFE_Residual,{result.ef_e_residual}\n")
            f.write(f"Status,{result.status}\n")
            f.write(f"Bianchi_Violation,{result.bianchi_violation}\n")


if __name__ == "__main__":
    main()
