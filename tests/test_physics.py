"""Basic smoke tests for the physics module."""

from flightsim.aircraft import Aircraft
from flightsim.physics import apply_gravity, integrate_position


def test_gravity_reduces_vertical_velocity():
    aircraft = Aircraft()
    apply_gravity(aircraft, dt=1.0)
    assert aircraft.velocity[1] < 0


def test_integrate_position_moves_aircraft():
    aircraft = Aircraft(velocity=(1.0, 0.0, 0.0))
    integrate_position(aircraft, dt=1.0)
    assert aircraft.position[0] == 1.0
