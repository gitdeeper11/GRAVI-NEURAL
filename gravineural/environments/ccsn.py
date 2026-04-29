"""Core-Collapse Supernova (CCSN) environment configuration (R3)."""

from dataclasses import dataclass


@dataclass
class CCSNEnvironment:
    """Core-collapse supernova environment."""
    
    progenitor_mass: float = 15.0  # M_☉
    metallicity: float = 0.02  # Z/Z_☉
    rotation_rate: float = 0.0
    magnetic_field_g: float = 1e12
    
    def get_efe_thresholds(self) -> dict:
        return {"EXCELLENT": 0.010, "GOOD": 0.020, "MODERATE": 0.040, "CRITICAL": 0.080}
    
    def get_baseline_mismatch(self) -> float:
        return 0.0025  # 2.5e-3 from paper
