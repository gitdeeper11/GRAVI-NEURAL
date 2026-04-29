"""Real-time EFE residual monitoring engine."""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class EFERecord:
    """Single EFE measurement record."""
    timestamp: float
    efe_residual: float
    status: str
    bianchi_violation: float
    ricci_scalar: float


class EFEMonitor:
    """Real-time EFM monitor for gravitational systems."""
    
    def __init__(self, alert_threshold: float = 0.02):
        self.alert_threshold = alert_threshold
        self.history: List[EFERecord] = []
    
    def update(self, efe_residual: float, status: str, bianchi_violation: float, ricci_scalar: float) -> EFERecord:
        """Update monitor with new measurement."""
        import time
        
        record = EFERecord(
            timestamp=time.time(),
            efe_residual=efe_residual,
            status=status,
            bianchi_violation=bianchi_violation,
            ricci_scalar=ricci_scalar
        )
        self.history.append(record)
        
        if len(self.history) > 1000:
            self.history.pop(0)
        
        return record
    
    def get_mean_residual(self) -> float:
        """Get mean EFE residual over recent history."""
        if not self.history:
            return 0.0
        return sum(r.efe_residual for r in self.history) / len(self.history)
    
    def get_trend(self) -> str:
        """Get EFE residual trend."""
        if len(self.history) < 5:
            return "stable"
        
        recent = [r.efe_residual for r in self.history[-5:]]
        if recent[-1] > recent[0] * 1.05:
            return "increasing"
        elif recent[-1] < recent[0] * 0.95:
            return "decreasing"
        return "stable"
