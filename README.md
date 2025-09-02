Data Analysis with Pandas & Matplotlib
Objective

The goal of this assignment is to:

Load and explore a dataset using pandas.

Perform basic data analysis and compute statistics.

Create simple plots and charts with matplotlib and seaborn for visualization.

Provide meaningful insights and observations from the data.
 Dataset

Dataset Used: Iris Dataset (from sklearn.datasets.load_iris()).

Description: The Iris dataset contains measurements of 150 samples of iris flowers from three species: Setosa, Versicolor, and Virginica.

Features:

Sepal Length (cm)

Sepal Width (cm)

Petal Length (cm)

Petal Width (cm)

Species (categorical target column)

Tools & Libraries

Python 3

pandas – for data loading, cleaning, and exploration.

matplotlib – for creating visualizations.

seaborn – for enhanced plotting styles.

sklearn – to access the Iris dataset.

Tasks Completed
Task 1: Load & Explore Dataset

Loaded dataset with error handling.

Displayed first rows (.head()), dataset info, and checked missing values.

Cleaned data (handled missing values).

Task 2: Basic Data Analysis

Computed summary statistics (.describe()).

Grouped data by species and computed average measurements.

Task 3: Data Visualizations

Line Chart – Sepal length trend across samples.

Bar Chart – Average petal length per species.

Histogram – Distribution of sepal width.

Scatter Plot – Sepal length vs petal length (with species as color/hue).

All plots include titles, axis labels, and legends.

Key Findings

The dataset is clean with no missing values.

Setosa species has the shortest petal length, while Virginica has the longest.

Sepal width values are mostly between 2.5 – 3.5 cm.

The scatter plot shows clear separation of Setosa from other species, while Versicolor and Virginica overlap slightly.
