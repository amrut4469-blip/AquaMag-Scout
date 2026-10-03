"""Sensor fusion + anomaly detection + a simple rule-based classifier
(placeholder for the planned TinyML model)."""
import numpy as np
from scipy.ndimage import uniform_filter, label, center_of_mass


def robust_z(x):
    med = np.median(x)
    mad = np.median(np.abs(x - med)) + 1e-9
    return (x - med) / (1.4826 * mad)


def fuse(mag, coil, bg=25):
    m = robust_z(mag - uniform_filter(mag, bg))    # remove slow drift
    c = robust_z(coil - uniform_filter(coil, bg))
    return (m + c) / 2


def find_anomalies(score, mag, coil, thr=5.0):
    labels, n = label(score > thr)
    found = []
    for i in range(1, n + 1):
        mask = labels == i
        area = int(mask.sum())
        if area < 4:
            continue
        cy, cx = center_of_mass(mask)
        found.append({"x": cx, "y": cy, "area": area,
                      "kind": classify(area, coil[mask].max() - np.median(coil))})
    return found


def classify(area, coil_peak):
    if coil_peak > 5:
        return "sulphide"
    return "crust" if area > 60 else "nodule"