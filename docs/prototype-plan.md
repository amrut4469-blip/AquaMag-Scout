# 🧪 Prototype Plan

| Phase | Objective | Key Activities | Exit Criteria |
|---|---|---|---|
| 1 | Sensor selection + bench test | Compare magnetometer and coil options; measure noise and range in air | Chosen sensor set with measured baselines |
| 2 | Pressure housing + data logger | Build housing, integrate edge controller and Pi, log data | Pod logs all sensors reliably in a bucket test |
| 3 | ML anomaly classifier | Build simulation and training data, train and convert TFLite model | Model runs on Pi in real time |
| 4 | Water-tank trial | Bury or place known metal targets, run repeated passes | Detection and false-alarm results recorded |
| 5 | Sea trial + optimisation | Test on ROV / towfish, tune thresholds | Real survey data and a trial report |

## Tank Trial Test Matrix (Phase 4)
| Variable | Values to test |
|---|---|
| Target type | Ferrous, non-ferrous, no target |
| Target size | Small, medium, large |
| Altitude | Low, medium, high |
| Speed | Slow, medium |

## Deliverables
- Working pod prototype
- Dataset from bench and tank trials
- Trained TFLite model with measured results
- Dashboard and QGIS output
- Trial report with honest limitations

## Dependencies
- Access to a tank or pool for Phase 4
- Access to a vessel or ROV for Phase 5