#!/usr/bin/env python
"""Gravitational wave generation script."""

import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gravineural.core.waveform import GravitationalWaveGenerator


def main():
    parser = argparse.ArgumentParser(description="Generate waveform")
    parser.add_argument("--mass1", type=float, default=30.0)
    parser.add_argument("--mass2", type=float, default=30.0)

    args = parser.parse_args()

    generator = GravitationalWaveGenerator()
    perturbation = [[0.1, 0, 0, 0], [0, 0.1, 0, 0], [0, 0, 0.1, 0], [0, 0, 0, 0.1]]

    result = generator.generate(perturbation, masses=(args.mass1, args.mass2), spins=(0.5, 0.5))

    print("=" * 50)
    print(f"Waveform Mismatch: {result.mismatch:.4e}")
    print(f"Inference Time: {result.inference_time_ms:.2f} ms")
    print("=" * 50)


if __name__ == "__main__":
    main()
