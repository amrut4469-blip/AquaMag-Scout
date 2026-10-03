import csv
import numpy as np

WINDOW = 3
THRESHOLD = 3.0  # standard deviations


def moving_average(x, n=WINDOW):
    return np.convolve(x, np.ones(n) / n, mode="same")


def load(path):
    t, mag, coil = [], [], []
    with open(path) as f:
        for r in csv.DictReader(f):
            t.append(int(r["t"]))
            mag.append(float(r["magnetometer_uT"]))
            coil.append(float(r["coil_mV"]))
    return np.array(t), np.array(mag), np.array(coil)


def zscore(x):
    return (x - np.median(x)) / (x.std() + 1e-9)


def main():
    t, mag, coil = load("data/sample_readings.csv")
    score = (zscore(moving_average(mag)) + zscore(moving_average(coil))) / 2
    for ti, s in zip(t, score):
        flag = "METAL ANOMALY" if abs(s) > THRESHOLD / 2 else "normal"
        print(f"t={ti}s  score={s:+.2f}  {flag}")


if __name__ == "__main__":
    main()