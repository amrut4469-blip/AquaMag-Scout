import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from seabed_sim import make_survey
from detector import fuse, find_anomalies

mag, coil, truth = make_survey()
score = fuse(mag, coil)
found = find_anomalies(score, mag, coil)

print(f"True targets : {len(truth)}")
print(f"Detected     : {len(found)}")
for f in found:
    print(f"  ({f['x']:.0f}, {f['y']:.0f})  area={f['area']}  -> {f['kind']}")

fig, ax = plt.subplots(1, 2, figsize=(11, 4.8), facecolor="#06141f")
for a in ax:
    a.set_facecolor("#06141f"); a.tick_params(colors="white")
ax[0].imshow(mag, cmap="viridis"); ax[0].set_title("Raw magnetometer", color="white")
ax[1].imshow(score, cmap="inferno"); ax[1].set_title("Fused anomaly score", color="white")
for f in found:
    ax[1].plot(f["x"], f["y"], "c+", ms=14, mew=2)
    ax[1].text(f["x"] + 2, f["y"] - 2, f["kind"], color="cyan", fontsize=8)
fig.suptitle("AquaMag Scout - simulated seabed survey", color="white")
plt.tight_layout()
plt.savefig("heatmap.png", dpi=140, facecolor=fig.get_facecolor())