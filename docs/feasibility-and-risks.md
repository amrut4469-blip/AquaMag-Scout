# ✅ Feasibility & Risks

## Feasibility
| Area | Assessment |
|---|---|
| Technology | ✓ Magnetometers, coils, altimeters and MCUs are proven COTS parts |
| Integration | ✓ Pod is designed to mount on any ROV / AUV / lander |
| Scalability | ✓ Single pod can grow into a sensor array |
| Cost | ✓ Uses off-the-shelf parts instead of specialised survey instruments |
| Benefit | ✓ Faster and cheaper site screening |

**Overall: highly feasible and scalable, subject to the trials above.**

## Risks and Mitigation
| Risk | Mitigation |
|---|---|
| High pressure | Rated housing + potting |
| Corrosion | Titanium / POM + sacrificial anode |
| Sensor drift | Auto-calibration + IMU |
| Vessel noise | Towfish + digital filter |
| Seawater conductivity affects the coil signal | Baseline recording in water, background subtraction |
| Short coil detection range | Operate at low altitude; use sonar altimeter to hold height |
| Weak signal from some deposits | Fuse magnetic + coil data; report detection limits honestly |
| False alarms | Threshold tuning, repeat-pass confirmation |
| Biofouling on long deployments | Smooth housing, periodic cleaning |

## Open Questions
- Which deposit types give a strong enough signal for each sensor
- Best altitude and speed for survey passes
- Whether acoustic links can carry enough data for live alerts