"""Rendering/display output.

Bare-bones ASCII renderer: draws the aircraft's altitude as a marker
on a vertical scale, one frame per simulation step. Good enough to
watch gravity work until a real renderer exists.
"""

import os

FLOOR = -25.0    # y position treated as ground level (meters)
CEILING = 5.0    # y position treated as top of the display (meters)
ROWS = 20        # number of rows in the vertical scale


def ascii_frame(aircraft, floor=FLOOR, ceiling=CEILING, rows=ROWS):
    """Return a multi-line string plotting the aircraft's altitude
    as '->' on a vertical scale between floor and ceiling."""
    y = aircraft.position[1]

    frac = (y - floor) / (ceiling - floor)
    frac = min(max(frac, 0.0), 1.0)  # clamp so off-scale altitudes still show at an edge
    marker_row = round((1 - frac) * (rows - 1))

    lines = []
    for row in range(rows):
        if row == marker_row:
            lines.append(f"->  altitude: {y:6.1f} m")
        else:
            lines.append("|")
    lines.append("=" * 12 + " ground")
    return "\n".join(lines)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
