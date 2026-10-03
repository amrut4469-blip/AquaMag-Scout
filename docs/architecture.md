# Architecture

```mermaid
flowchart TD
    S[Sensor Pod] --> EC[Edge Controller STM32 / ESP32]
    EC --> RP[Raspberry Pi]
    RP --> ML[TinyML Classifier]
    ML --> LINK[Tether / Acoustic Link]
    LINK --> DASH[Surface Dashboard]
    DASH --> MAP[QGIS Seabed Map]