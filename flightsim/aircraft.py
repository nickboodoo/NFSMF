"""Aircraft state and configuration."""

from dataclasses import dataclass


@dataclass
class Aircraft:
    """Minimal aircraft state. Expand with wing area, drag coefficient,
    engine thrust curve, etc. as the physics model grows.
    """

    mass: float = 1000.0                  # kg
    position: tuple = (0.0, 0.0, 0.0)     # x, y, z in meters
    velocity: tuple = (0.0, 0.0, 0.0)     # m/s
    orientation: tuple = (0.0, 0.0, 0.0)  # pitch, roll, yaw in radians
