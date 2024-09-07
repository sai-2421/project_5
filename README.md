# project_5

Singapore Resale Flat Prices Predicting

>**Overview:**

You're working on a project to build a machine learning model that predicts resale flat prices in Singapore using historical data from HDB transactions. The model will be integrated into a Streamlit web app, where users can input flat details and receive a predicted resale price. 

>**Tasks:**

* Data Collection and Preprocessing
* Feature Engineering
* Model Selection and Training
* Model Evaluation
* Streamlit Web Application
* Testing and Validation

>**Detailed Plan:**

* **Data Gathering and Preparation**: Obtain HDB resale flat transaction data from 1990 to the present, clean it by addressing outliers, missing data, and formatting issues, and split it into training and testing datasets.

* **Feature Development**: Identify important factors like location, flat type, floor level, area, model, and lease start date. Generate extra features, such as flat age or proximity to the nearest MRT station, to improve prediction accuracy.

* **Model Training**: Choose and train a suitable regression model (e.g., linear regression, decision trees, random forests), tuning its settings to maximize performance.

* **Model Performance Assessment**: Use metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R² score to evaluate how well the model predicts on unseen data.

* **Streamlit App Development**: Build a user-friendly interface where users can input flat details and get resale price predictions using the trained model.

* **Deployment on Streamlit**: Host your app on Streamlit's cloud platform to make it accessible online.

* **Validation and Testing**: Thoroughly test the deployed app to ensure accuracy by trying out different flat configurations and verifying the results.

>**Conclusion:**

This project offers a great opportunity to gain hands-on experience in data cleaning, exploratory data analysis (EDA), building and deploying machine learning models, and developing web applications. Additionally, you'll gain insights into Singapore's real estate market, enhancing your understanding of the factors that influence property prices.

>**Skills take away From This Project:**

 Data Wrangling, EDA, Model Building, Model Deployment

>**Packages and Libraries**

```python

import pandas as pd

import glob

import os

import seaborn as sns

import matplotlib.pyplot as plt

import numpy as np

import datetime

from scipy.stats import skew

import warnings

warnings.filterwarnings('ignore')

import streamlit as st

from streamlit_option_menu import option_menu

import numpy as np

import pickle

