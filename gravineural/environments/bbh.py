"""Binary Black Hole (BBH) environment configuration (R1)."""

from dataclasses import dataclass


@dataclass
class BBHEnvironment:
    """Binary black hole merger environment."""
    
    mass_ratio: float = 2.0  # q = m1/m2
    spin_magnitude: float = 0.5
    spin_orientation: str = "aligned"
    eccentricity: float = 0.0
    separation_m: float = 20.0  # M_ADM
    
    def get_efe_thresholds(self) -> dict:
        return {"EXCELLENT": 0.005, "GOOD": 0.010, "MODERATE": 0.020, "CRITICAL": 0.050}
    
    def get_baseline_mismatch(self) -> float:
        return 0.0019  # 1.9e-3 from paper
