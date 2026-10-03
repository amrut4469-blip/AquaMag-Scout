# AquaMag Scout

Concept prototype for SIH 2026 (SIH26064): a low-cost seafloor metal
anomaly detector for ROV/AUV use. Team: Bug Busters.

## Status
Early-stage concept. The code here is a small simulation of the
signal-processing idea, not a tested underwater system.

## Idea
Fuse magnetometer + pulse-induction coil readings, filter noise,
and flag readings that deviate from the seabed baseline.

## Run
pip install -r requirements.txt
python src/detect.py

## Planned
- Hardware bench test (STM32/ESP32 + magnetometer)
- TinyML classifier
- Water-tank trial