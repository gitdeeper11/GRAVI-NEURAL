#!/usr/bin/env python
"""EFE residual validation pipeline."""

import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gravineural.core.cno import CovariantNeuralOperator


def main():
    parser = argparse.ArgumentParser(description="Run EFE residual validation")
    parser.add_argument("--mass", type=float, default=1.0, help="Mass (solar masses)")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")

    args = parser.parse_args()

    cno = CovariantNeuralOperator()
    stress_energy = [[args.mass,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    coordinates = [0, 10 * args.mass, 0, 0]

    result = cno.compute_metric(stress_energy, coordinates)

    print(f"\nEFE Residual Validation")
    print("-" * 40)
    print(f"Mass: {args.mass} M_☉")
    print(f"EFE Residual: {result.ef_e_residual:.4f} [{result.status}]")
    print(f"Bianchi Violation: {result.bianchi_violation:.4e}")
    print(f"Ricci Scalar: {result.ricci_scalar:.4f}")
    
    if args.verbose:
        print("\nMetric Tensor:")
        for i, row in enumerate(result.metric_tensor):
            for j, val in enumerate(row):
                if abs(val) > 1e-6:
                    print(f"  g_{i}{j} = {val:.6f}")
    
    print("\n✅ Validation complete!")


if __name__ == "__main__":
    main()
