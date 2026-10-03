# 🔧 Hardware Design

## Components
| Component | Purpose | Notes |
|---|---|---|
| Fluxgate / MEMS magnetometer | Magnetic anomaly detection | Fluxgate: more sensitive; MEMS: cheaper. Choice decided in Phase 1 |
| Pulse-induction coil + driver | Conductive metal response | Pulses the coil and reads the decay signal |
| Sonar altimeter | Height above seabed | Needed to normalise coil/magnetic readings |
| Pressure sensor | Depth | Also helps with logging and safety |
| IMU | Orientation, motion | Used for drift and motion compensation |
| STM32 / ESP32 | Real-time sampling | Timestamps all sensor data |
| Raspberry Pi | Logging, ML inference | Runs Python + TensorFlow Lite |
| Pressure-rated housing | Protects electronics | See below |

## Pod Layout