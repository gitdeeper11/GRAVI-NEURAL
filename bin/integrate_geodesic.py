#!/usr/bin/env python
"""Geodesic integration script."""

import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gravineural.core.geodesic import GeodesicSolver


def main():
    parser = argparse.ArgumentParser(description="Integrate geodesic")
    parser.add_argument("--steps", type=int, default=1000)

    args = parser.parse_args()

    solver = GeodesicSolver()
    metric = [[-0.8, 0, 0, 0], [0, 1.2, 0, 0], [0, 0, 100, 0], [0, 0, 0, 100]]
    christoffel = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]]
    initial_pos = [0, 10, 0, 0]
    initial_vel = [1, 0, 0.1, 0]

    result = solver.integrate(metric, christoffel, initial_pos, initial_vel, steps=args.steps)

    print("=" * 50)
    print(f"Position Error: {result.position_error_m:.3f} m")
    print("=" * 50)


if __name__ == "__main__":
    main()
