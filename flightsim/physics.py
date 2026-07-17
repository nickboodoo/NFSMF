"""Forces and motion updates.

This is where lift, drag, thrust, and gravity get combined to move
the aircraft each simulation step. Start simple (gravity only), add
lift/drag/thrust as separate functions once you're ready for them.
"""

from flightsim.constants import GRAVITY


def apply_gravity(aircraft, dt):
    """Update vertical velocity due to gravity over a timestep dt."""
    vx, vy, vz = aircraft.velocity
    aircraft.velocity = (vx, vy - GRAVITY * dt, vz)
    return aircraft


def integrate_position(aircraft, dt):
    """Move the aircraft by its current velocity over a timestep dt."""
    x, y, z = aircraft.position
    vx, vy, vz = aircraft.velocity
    aircraft.position = (x + vx * dt, y + vy * dt, z + vz * dt)
    return aircraft
