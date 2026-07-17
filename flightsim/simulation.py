"""Main simulation loop.

Simulation owns the aircraft state and advances it forward in time in
fixed-size steps (dt). Rendering and input handling will hook in here
once they exist.
"""

from flightsim.aircraft import Aircraft
from flightsim import physics


class Simulation:
    def __init__(self):
        self.aircraft = Aircraft()
        self.time = 0.0
        self.dt = 1 / 60  # seconds per simulation step (60Hz)

    def step(self):
        physics.apply_gravity(self.aircraft, self.dt)
        physics.integrate_position(self.aircraft, self.dt)
        self.time += self.dt

    def run(self, steps=60):
        for _ in range(steps):
            self.step()
        print(f"t={self.time:.3f}s  aircraft={self.aircraft}")
