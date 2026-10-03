"""Synthetic seabed survey: magnetometer + pulse-induction coil grids
with a few buried metal targets. All numbers are ASSUMED, for demo only."""
import numpy as np

KINDS = {  # kind: (magnetometer uT, coil mV, spread in cells)
    "nodule":   (4.0, 3.0, 2.0),
    "sulphide": (9.0, 8.0, 2.5),
    "crust":    (3.0, 1.5, 4.0),
}


def make_survey(size=60, n_targets=4, seed=7):
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:size, 0:size]
    mag = 48 + 0.02 * xx + 0.5 * np.sin(yy / 9) + rng.normal(0, 0.25, (size, size))
    coil = 10 + rng.normal(0, 0.2, (size, size))
    names = list(KINDS)
    targets = []
    for _ in range(n_targets):
        cx, cy = (int(v) for v in rng.integers(8, size - 8, 2))
        kind = names[rng.integers(0, len(names))]
        am, ac, w = KINDS[kind]
        g = np.exp(-((xx - cx) ** 2 + (yy - cy) ** 2) / (2 * w ** 2))
        mag += am * g
        coil += ac * g
        targets.append((cx, cy, kind))
    return mag, coil, targets