# Logistic Regression
This repository contains a series of Python scripts for data analysis and building a logistic regression model based on data from Hogwarts students. The goal is to explore the data, visualize it, and use a logistic regression classifier to predict which Hogwarts house each student belongs to.

## Data Analysis
In this first phase, basic exploratory data analysis is performed. The describe.py program takes a dataset as input and displays descriptive statistics for all numerical features. The results include:

- Count: Number of values.
- Mean: Average of the values.
- Std: Standard deviation.
- Min: Minimum value.
- 25%: First quartile.
- 50% (Median): Median.
- 75%: Third quartile.
- Max: Maximum value.
- Range: Difference between highest and lowest values.
- Nan values: Number of null values.

This analysis helps you better understand the format and characteristics of the data.<br>
Usage: `python3 ./describe.py dataset_name`

## Data Visualization
Data visualization is essential for gaining insights and detecting potential anomalies. This section includes several scripts to create plots that answer specific questions.

Histogram (histogram.py): Displays a histogram to identify which Hogwarts course has a homogeneous score distribution across all four houses.<br>
Usage: `python3 histogram.py`

Scatter Plot (scatter_plot.py): Displays a scatter plot to identify the two most similar features.<br>
Usage: `python3 scatter_plot.py`

Pair Plot (pair_plot.py): Displays a pair plot (or scatter plot matrix) to help select the features to be used in the logistic regression.<br>
Usage: `python pair_plot.py`

## Logistic regression
The final part of the project is to create a logistic regression model to classify students into one of the Hogwarts houses.

Training (logreg_train.py): This script trains a logistic regression model using the gradient descent algorithm. The result is a file containing the weights to be used for making predictions.<br>
Usage: `python3 ./logreg_train.py dataset_name [flag]`

**Flag options:**  
_Batch Gradient Descent_ (default):  
`python3 logreg_train.py dataset.csv`  
`python3 logreg_train.py dataset.csv -b`  
_Stochastic Gradient Descent_:  
`python3 logreg_train.py dataset.csv -s`  
_Mini-batch Gradient Descent_:  
`python3 logreg_train.py dataset.csv -m`  

Prediction (logreg_predict.py): Using the weights trained in the previous step, this script predicts the house for each student in a test dataset and generates a houses.csv file with the results.<br>
Usage: `python3 ./logreg_predict.py dataset_name weights.json`

### Requirements
Python 3.x<br>
Libraries: numpy, pandas, matplotlib, json, sys, pyrsistent.

### Usage Instructions
- Clone this repository to your local machine.
- Run the data analysis and visualization scripts to explore the data.
- Use logreg_train to train the logistic regression model.
- Use logreg_predict to generate the predictions.
