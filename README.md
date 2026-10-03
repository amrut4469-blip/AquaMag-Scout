# AquaMag Scout

Low-cost, deployable seafloor metal detection sensor pod for ocean resource exploration.

**Smart India Hackathon 2026** | Problem Statement SIH26064 | Ministry of Earth Sciences (MoES)
Theme: Robotics and Drones | Category: Hardware | Team: Bug Busters (Team ID 139910)

## Problem
Seabed surveys happen in dark, deep and remote water. Conventional survey sensors are costly and heavy, so exploration stays slow and sparse.

## Solution
A compact sensor pod that fuses two sensing physics and classifies targets on the device (edge AI):

| Sensor | Purpose | Signal falloff |
|---|---|---|
| Magnetometer (fluxgate / MEMS) | Detects magnetic anomalies | ~ 1/r^3 |
| Pulse-induction (PI) coil | Detects conductive metal | ~ 1/r^6 |
| Sonar altimeter | Height above seabed | - |
| Pressure sensor + IMU | Depth, roll, pitch | - |

## Pipeline
```
Sensors -> Edge controller (STM32 / ESP32 + Raspberry Pi)
        -> Signal processing + classifier (background / nodule / sulphide / crust)
        -> Metal anomaly alert + geo-tagged heatmap
        -> Surface dashboard (tether / acoustic link, MQTT)
```

## Repository structure
| Path | What it contains |
|---|---|
| `edge/` | Python edge software: simulator, signal processing, classifier, MQTT, main pipeline |
| `firmware/` | ESP32 sensor-pod firmware (starter template) |
| `dashboard/` | React surface dashboard (single HTML file) |
| `docs/` | Physics model behind the feasibility chart |
| `hardware/` | Bill of materials |

## Quick start (simulation, no hardware needed)
```
pip install -r requirements.txt
python edge/train_classifier.py
python edge/main.py
```
`edge/main.py` writes `data/survey.csv`, `data/survey.json` and `data/survey.geojson`.
- Open `dashboard/index.html` in a browser and load `data/survey.json`.
- Load `data/survey.geojson` in QGIS to see the seabed map.
- Optional: `python docs/physics_model.py` regenerates the signal-vs-height chart.

## Limitations (honest notes)
- The software pipeline currently runs on synthetic, physics-based data. Real results need water-tank and sea trials.
- Hobby-grade magnetometers are too noisy for small targets; the prototype needs a fluxgate or better MEMS sensor.
- The cost figure (Rs 0.7 lakh vs Rs 12 lakh) is an indicative target, not a measured price.
- The firmware is a starter template and must be tuned on real hardware.

## Roadmap
- [x] Software pipeline on simulated data
- [ ] Phase 1: Sensor selection + bench test
- [ ] Phase 2: Pressure housing + data logger
- [ ] Phase 3: ML anomaly classifier on real data
- [ ] Phase 4: Water-tank trial with metal targets
- [ ] Phase 5: Sea trial + optimisation

## References
- https://www.sih.gov.in/
- https://moes.gov.in/
- https://www.niot.res.in/
- https://www.isa.org.jm/
- https://www.tensorflow.org/lite