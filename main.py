"""Entry point for NFSMF (Nick's Flight Simulator: Most Flown)."""

import time

from flightsim.simulation import Simulation
from flightsim import render


def main():
    sim = Simulation()

    while sim.aircraft.position[1] > render.FLOOR:
        sim.step()
        render.clear_screen()
        print(f"t={sim.time:.2f}s")
        print(render.ascii_frame(sim.aircraft))
        time.sleep(sim.dt)

    print("landed.")


if __name__ == "__main__":
    main()
