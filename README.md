# Heart Disease Prediction Project

## Overview
This project predicts the presence of heart disease using logistic regression and random forest classifiers. Data preprocessing, exploratory data analysis, model building, and predictions are performed in a step-by-step manner.

## Dataset
The dataset used is `heart.csv`, which contains patient information like age, sex, chest pain type, and more.
**Note**: In the code section labeled "Load libraries & data" you should update the file path (/Users/arpad/Downloads/heart.csv) to match the location where you downloaded or stored the dataset locally.

# Load libraries & data
df = pd.read_csv("/path/to/your/heart.csv")
df.head()

## Key Features
- **EDA**: Visualizations of feature distributions and correlations.
- **Preprocessing**: Handling categorical data and scaling numerical values.
- **Modeling**: Logistic Regression and Random Forest classifiers.
- **Prediction**: Trained models to predict based on user input.

**Notebook Location**: The full notebook can be found at src/heart_disease_prediction.ipynb.

## Dependencies
- Python 3.12
- Libraries: numpy, pandas, scikit-learn, matplotlib, seaborn, plotly, joblib

## References and Resources
- **Dataset**: [Heart Failure Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)
      - This dataset contains patient health metrics and their corresponding heart disease statuses, used for classification modeling.
- **Guide and Inspiration**: [A Guide to Any Classification Problem](https://www.kaggle.com/code/durgancegaur/a-guide-to-any-classification-problem)
      - This project references insights and techniques provided in this guide.
