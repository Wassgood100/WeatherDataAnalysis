import matplotlib.pyplot as plt
import pandas as pd

# Daily temperature data
df = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Temperature": [18, 20, 19, 22, 21, 23, 20],
    "Rainfall":[0, 2, 1, 5, 3, 0, 4],
})

# Plot daily temperatures
plt.figure(figsize=(8, 4))

plt.bar(
    df["Day"],
    df["Temperature"],
    color="deepskyblue",
    edgecolor="navy"
)

plt.title("Daily Temperature Analysis", color="darkblue")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=30)
plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()
plt.show()

# Plot daily rainfall
plt.figure(figsize=(8, 4))

plt.plot(
    df["Day"],
    df["Rainfall"],
    color="darkorange",
    marker="o",
    markersize=8,
    linewidth=2.5,
    markerfacecolor="gold"
)

plt.title("Daily Rainfall Analysis", color="darkred")
plt.xlabel("Day")
plt.ylabel("Rainfall (mm)")
plt.xticks(rotation=30)
plt.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.show()
