"""Entry point for NFSMF (Nick's Flight Simulator: Most Flown)."""

from flightsim.simulation import Simulation


def main():
    sim = Simulation()
    sim.run()


if __name__ == "__main__":
    main()
