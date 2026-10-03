# Software & AI

## Pipeline
1. Sample all sensors on the edge controller
2. Filter noise and remove drift using IMU and altimeter data
3. Detect anomalies against the local seabed baseline
4. Classify with a TensorFlow Lite model: Nodule / Sulphide / Crust
5. Send alerts and position-tagged data over MQTT
6. Show on the React dashboard and export to QGIS

## Rules
- AI flags and suggests; humans decide where to sample
- Model accuracy must be measured in tank and sea trials before any claim