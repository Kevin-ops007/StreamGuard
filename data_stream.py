import numpy as np
import matplotlib.pyplot as plt


def data_stream():
    t = 0
    while True:
        # Simulate a seasonal pattern with noise and occasional anomalies
        seasonal = 10 * np.sin(0.1 * t)  # Seasonal pattern
        noise = np.random.normal(0, 1)  # Random noise
        anomaly = np.random.choice([0, 0, 0, 10])  # Occasional spikes as anomalies
        yield seasonal + noise + anomaly
        t += 1


def detect_anomaly(data_point, ema, alpha, threshold):
    # Calculate new EMA
    ema = alpha * data_point + (1 - alpha) * ema
    deviation = abs(data_point - ema)
    # Set an adaptive threshold
    if deviation > threshold:
        return True, ema
    return False, ema


def plot_data(stream):
    plt.ion()
    fig, ax = plt.subplots()
    data, anomalies = [], []

    for point in stream:
        data.append(point)
        is_anomaly, _ = detect_anomaly(point, ema=0, alpha=0.1, threshold=3)
        anomalies.append(point if is_anomaly else np.nan)

        ax.clear()
        ax.plot(data, label="Data Stream")
        ax.scatter(range(len(anomalies)), anomalies, color="red", label="Anomalies")
        plt.legend()
        plt.draw()
        plt.pause(0.01)


def main():
    stream = data_stream()
    plot_data(stream)


main()
