"""Binary Neutron Star (BNS) environment configuration (R2)."""

from dataclasses import dataclass


@dataclass
class BNSEnvironment:
    """Binary neutron star inspiral environment."""
    
    mass_ratio: float = 1.0
    tidal_deformability_lambda1: float = 500.0
    tidal_deformability_lambda2: float = 500.0
    equation_of_state: str = "SLy"
    eccentricity: float = 0.0
    
    def get_efe_thresholds(self) -> dict:
        return {"EXCELLENT": 0.008, "GOOD": 0.015, "MODERATE": 0.030, "CRITICAL": 0.060}
    
    def get_baseline_mismatch(self) -> float:
        return 0.0023  # 2.3e-3 from paper
