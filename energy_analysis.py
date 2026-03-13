import pandas as pd
import numpy as np

# Sample dataset
data = {
    "Surface_Area": [600,650,700,750,800],
    "Wall_Area": [300,320,340,360,380],
    "Roof_Area": [200,210,220,230,240],
    "Energy_Load": [15,18,21,25,28]
}

# Create DataFrame using Pandas
df = pd.DataFrame(data)

print("Dataset:")
print(df)

# NumPy calculation
average_energy = np.mean(df["Energy_Load"])

print("\nAverage Energy Consumption:", average_energy)

# Maximum and minimum energy usage
print("Maximum Energy Consumption:", np.max(df["Energy_Load"]))
print("Minimum Energy Consumption:", np.min(df["Energy_Load"]))