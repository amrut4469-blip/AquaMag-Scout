# 🏗️ Architecture

## System Overview
````mermaid
flowchart TD
    subgraph POD[Sensor Pod]
        M[Magnetometer]
        C[Pulse-Induction Coil]
        S[Sonar Altimeter]
        P[Pressure + IMU]
    end
    M --> EC[Edge Controller<br/>STM32 / ESP32]
    C --> EC
    S --> EC
    P --> EC
    EC --> RP[Raspberry Pi]
    RP --> ML[Signal Processing + TinyML]
    ML --> LINK[Tether / Acoustic Link]
    LINK --> DASH[Surface Dashboard]
    DASH --> MAP[QGIS Seabed Map]
````

## Layers
| Layer | Role |
|---|---|
| Sensing | Magnetometer, coil, sonar altimeter, pressure, IMU |
| Edge | Real-time sampling and timestamping (STM32 / ESP32) |
| Intelligence | Filtering, anomaly detection, classification (Raspberry Pi) |
| Communication | MQTT over tether or acoustic link |
| Surface | React dashboard and QGIS mapping |

## Data Flow
1. Edge controller samples all sensors at a fixed rate with timestamps.
2. Raspberry Pi filters and fuses the data.
3. Anomaly score and class are computed on board.
4. Only compact results (alerts + position + score) are sent to the surface.
5. Raw data stays logged on board for later analysis.

## Interfaces (planned)
| Link | Typical interface |
|---|---|
| Magnetometer, IMU, pressure | I2C / SPI |
| Pulse-induction coil | Driver board + ADC |
| Sonar altimeter | UART |
| Edge controller → Raspberry Pi | UART / USB |
| Pod → surface | Ethernet tether (initial), acoustic link (later) |

## Deployment Modes
| Mode | How the pod is used |
|---|---|
| ROV | Mounted on the vehicle frame |
| Towfish | Towed behind a vessel, away from vessel noise |
| AUV / Lander | Carried as a payload |

## Design Principles
- Low cost, off-the-shelf parts first
- Compute on the edge, send only compact results
- Log raw data on board
- Modular: one pod now, sensor array later