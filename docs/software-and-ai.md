# 🧠 Software & AI

## Pipeline
```
Acquire → Pre-process → Fuse → Detect anomaly → Classify → Alert + Map
```

| Stage | What happens |
|---|---|
| Acquire | Edge controller samples all sensors with timestamps |
| Pre-process | Noise filter, drift removal, altitude normalisation |
| Fuse | Combines magnetic and coil signals into one anomaly score |
| Detect | Flags readings that differ from the local seabed baseline |
| Classify | Nodule / Sulphide / Crust using a TensorFlow Lite model |
| Alert + Map | MQTT alert, geo-tagged point added to the heatmap |

## Candidate Features
- Magnetic anomaly amplitude and width
- Coil response amplitude and decay shape
- Ratio of magnetic to coil response
- Altitude-corrected values
- Spatial extent of the anomaly along the track

## Model Plan
- Start with a small, simple model so it can run on a Raspberry Pi
- Convert to TensorFlow Lite
- Train first on simulated data, then retrain on tank and sea-trial data
- Measure everything honestly before claiming accuracy

## Evaluation Metrics
| Metric | Why |
|---|---|
| Detection rate | How many real targets were found |
| False alarms per survey | Operator trust |
| Confusion matrix | Which classes get mixed up |
| Latency | Real-time usability |

## Messaging (MQTT)
Topic idea: `aquamag/pod1/alerts`
```json
{
  "time": "2026-01-01T10:15:30Z",
  "lat": 0.0,
  "lon": 0.0,
  "depth_m": 0.0,
  "score": 0.0,
  "class": "sulphide"
}
```
(values above are placeholders)

## Dashboard and Mapping
- React dashboard: live alerts, track, sensor status
- QGIS: geo-tagged heatmap of detections on a seabed map

## Rules
- AI flags and suggests; humans decide where to sample
- Raw data is always logged for later re-analysis
- Model accuracy is reported only from measured trials