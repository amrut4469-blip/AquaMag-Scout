# Architecture

```mermaid
flowchart TD
    S[Sensor Pod] --> EC[Edge Controller STM32 / ESP32]
    EC --> RP[Raspberry Pi]
    RP --> ML[TinyML Classifier]
    ML --> LINK[Tether / Acoustic Link]
    LINK --> DASH[Surface Dashboard]
    DASH --> MAP[QGIS Seabed Map]

### docs/hardware-design.md
```markdown
# Hardware Design

| Component | Purpose |
|---|---|
| Fluxgate / MEMS magnetometer | Magnetic anomaly detection |
| Pulse-induction coil | Conductive metal response |
| Sonar altimeter | Height above seabed |
| Pressure sensor + IMU | Depth and orientation |
| STM32 / ESP32 | Real-time sampling |
| Raspberry Pi | Logging and ML inference |
| Pressure-rated housing | Subsea protection |

## Housing
Pressure-rated housing with potting; titanium or POM with a sacrificial
anode against corrosion.