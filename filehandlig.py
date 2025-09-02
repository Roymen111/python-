# Assignment: Data Analysis

# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Make plots look nice
sns.set(style="whitegrid")

# Step 2: Load Dataset with Error Handling
try:
    iris = load_iris(as_frame=True)
    df = iris.frame  # DataFrame version
    df["species"] = df.target.apply(lambda x: iris.target_names[x])  # add species column
    print(" Dataset loaded successfully!")
except FileNotFoundError:
    print(" File not found. Please check the dataset path.")
except Exception as e:
    print(f"Error loading dataset: {e}")

# Step 3: Explore Dataset
print("\n First 5 rows of dataset:")
print(df.head())

print("\n Dataset Info:")
print(df.info())

print("\n Missing Values:")
print(df.isnull().sum())

# Step 4: Clean Data (No missing values in Iris, but demo handling)
df = df.dropna()

# Step 5: Basic Data Analysis
print("\n Summary Statistics:")
print(df.describe())

print("\n Mean Sepal Length by Species:")
print(df.groupby("species")["sepal length (cm)"].mean())

# Step 6: Visualizations

# (a) Line Chart (simulate trend using index vs sepal length)
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length", color="blue")
plt.title("Line Chart: Sepal Length across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# (b) Bar Chart (average petal length by species)
plt.figure(figsize=(8,5))
df.groupby("species")["petal length (cm)"].mean().plot(kind="bar", color=["red","green","blue"])
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# (c) Histogram (distribution of sepal width)
plt.figure(figsize=(8,5))
plt.hist(df["sepal width (cm)"], bins=15, color="purple", alpha=0.7)
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# (d) Scatter Plot (relationship between sepal length & petal length)
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x="sepal length (cm)", y="petal length (cm)", hue="species", style="species", s=80)
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

# Step 7: Findings / Observations
print("\n Observations:")
print("- Iris dataset contains 3 species: Setosa, Versicolor, Virginica.")
print("- Setosa has generally shorter petal lengths, Virginica has the longest.")
print("- Sepal width distribution shows most values between 2.5–3.5 cm.")
print("- Scatter plot shows clear separation of Setosa from other species.")
