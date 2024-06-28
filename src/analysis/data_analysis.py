import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("../../data/cleaned/cleaned_healthcare_data.csv")

# Summary statistics
print(data.describe())

# Plot distribution of age
plt.hist(data['age'], bins=30)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()
