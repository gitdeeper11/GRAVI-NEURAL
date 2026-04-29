"""Geometry helpers for tensor operations in curved spacetime."""

import math
from typing import List, Tuple


def metric_inverse(metric: List[List[float]]) -> List[List[float]]:
    """Compute inverse metric g^μν."""
    # Simplified for diagonal metric
    inv = [[0.0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        if metric[i][i] != 0:
            inv[i][i] = 1.0 / metric[i][i]
    return inv


def raise_index(
    tensor: List[List[float]],
    metric_inv: List[List[float]],
) -> List[List[float]]:
    """Raise indices of a rank-2 tensor: T^μν = g^μα g^νβ T_αβ."""
    raised = [[0.0 for _ in range(4)] for _ in range(4)]
    for mu in range(4):
        for nu in range(4):
            for alpha in range(4):
                for beta in range(4):
                    raised[mu][nu] += metric_inv[mu][alpha] * metric_inv[nu][beta] * tensor[alpha][beta]
    return raised


def lower_index(
    tensor: List[List[float]],
    metric: List[List[float]],
) -> List[List[float]]:
    """Lower indices of a rank-2 tensor: T_μν = g_μα g_νβ T^αβ."""
    lowered = [[0.0 for _ in range(4)] for _ in range(4)]
    for mu in range(4):
        for nu in range(4):
            for alpha in range(4):
                for beta in range(4):
                    lowered[mu][nu] += metric[mu][alpha] * metric[nu][beta] * tensor[alpha][beta]
    return lowered


def geodesic_distance(
    position1: List[float],
    position2: List[float],
    metric: List[List[float]],
) -> float:
    """Compute proper distance along geodesic."""
    dx = [position2[i] - position1[i] for i in range(4)]
    ds2 = 0.0
    for i in range(4):
        for j in range(4):
            ds2 += metric[i][j] * dx[i] * dx[j]
    return math.sqrt(abs(ds2)) if ds2 > 0 else -math.sqrt(abs(ds2))


def four_velocity(
    velocity_3d: List[float],
    lorentz_factor: float = None,
) -> List[float]:
    """Construct four-velocity from three-velocity."""
    vx, vy, vz = velocity_3d
    v2 = vx ** 2 + vy ** 2 + vz ** 2

    if lorentz_factor is None:
        lorentz_factor = 1.0 / math.sqrt(max(1e-10, 1.0 - v2))

    return [lorentz_factor, lorentz_factor * vx, lorentz_factor * vy, lorentz_factor * vz]
