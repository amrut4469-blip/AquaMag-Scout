# 💡 Solution Overview

**AquaMag Scout** is a compact sensor pod that fuses four sensing sources and
runs detection on the sensor itself.

## Concept
1. A **pulse-induction coil** responds to conductive metal.
2. A **magnetometer** responds to magnetic anomalies.
3. A **sonar altimeter** gives height above the seabed.
4. A **pressure sensor + IMU** give depth and orientation.
5. An **edge controller** filters the data, detects anomalies and classifies them.
6. Results go to a **surface dashboard** as alerts and a geo-tagged heatmap.

## Why Two Sensing Physics?
| Sensor | Good at | Weak at |
|---|---|---|
| Magnetometer | Magnetic / ferrous material, larger range | Non-magnetic metals |
| Pulse-induction coil | Conductive metals | Short range, needs low altitude |

Using both lets each cover the other's blind spots and reduces false alarms.

## Innovation and Uniqueness
- ✔ Low-cost off-the-shelf parts
- ✔ Two sensing physics fused
- ✔ Edge AI on the sensor
- ✔ Plug-and-play on ROV / AUV

## Output
Metal anomaly alert → Nodule / Sulphide / Crust → geo-tagged heatmap →
surface dashboard.

## Expected Impact
Survey cost ↓ | Coverage ↑ | Site screening speed ↑ | Deployability ↑

## Assumptions to Validate
- COTS sensors give usable signals through a pressure housing
- Fused scoring beats either sensor alone
- Classification is feasible from the available signal features