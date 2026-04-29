#!/usr/bin/env python
"""Quick start example for GRAVI-NEURAL."""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gravineural.core.cno import CovariantNeuralOperator
from gravineural.core.gno import GravitationalNeuralOperator
from gravineural.inference.predictor import GRAVIPredictor


def main():
    print("=" * 60)
    print("GRAVI-NEURAL Quick Start Example")
    print("=" * 60)

    # Create stress-energy tensor for a black hole
    stress_energy = [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
    ]
    coordinates = [0.0, 10.0, 0.0, 0.0]

    # Initialize CNO
    print("\n🔭 Covariant Neural Operator:")
    cno = CovariantNeuralOperator()
    result = cno.compute_metric(stress_energy, coordinates)
    print(f"  EFE Residual: {result.ef_e_residual:.4f} [{result.status}]")
    print(f"  Bianchi Violation: {result.bianchi_violation:.4e}")

    # Initialize GNO
    print("\n🌊 Gravitational Neural Operator:")
    gno = GravitationalNeuralOperator()
    gno_result = gno.forward(stress_energy)
    print(f"  Inference Time: {gno_result.inference_time_ms:.2f} ms")

    # Initialize Predictor
    print("\n📡 GRAVI Predictor:")
    predictor = GRAVIPredictor()
    prediction = predictor.predict(stress_energy, coordinates)
    print(f"  Waveform Mismatch: {prediction.waveform_mismatch:.4e}")
    print(f"  Geodesic Error: {prediction.geodesic_error_m:.3f} m")

    print("\n✅ GRAVI-NEURAL is ready for use!")
    print("📚 Run: python bin/compute_metric.py --spacetime schwarzschild --verbose")
    print("🌐 Dashboard: https://gravineural.netlify.app")


if __name__ == "__main__":
    main()
