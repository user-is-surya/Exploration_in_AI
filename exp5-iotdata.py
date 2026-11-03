# IoT Sensor Data Analysis using NumPy
import numpy as np

sensor_data = np.array([24.5, 25.1, 26.3, 27.0, 28.2, 29.1, 27.8, 26.5, 25.7, 30.2])
print("Sensor Data:", sensor_data)

stats = {"Mean": np.mean, "Median": np.median, "Minimum": np.min,
         "Maximum": np.max, "Std. Dev.": np.std}
for label, func in stats.items():
    print(f"{label:<9}:", round(float(func(sensor_data)), 2))

threshold = 28.0
print("Values above", threshold, ":", sensor_data[sensor_data > threshold])