import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Lab3/Lenna_(test_image).png', cv2.IMREAD_COLOR_BGR)
if img is None:
    raise FileNotFoundError("image.jpg not found")

colors = ("b", "g", "r")
hist_size = 256
ranges = [0, 256]

histograms = []
for i, col in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [hist_size], ranges)
    histograms.append(hist)


# Plot
plt.figure(figsize=(8,4))
for hist, col in zip(histograms, colors):
    plt.plot(hist, color=col)
plt.title("Histogram kolorów BGR")
plt.xlabel("Wartość koloru")
plt.ylabel("Częstotliwość wystąpień")
plt.xlim([0, hist_size-1])
plt.show()