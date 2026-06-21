

🏡 California Housing Price Predictor

This project is a complete end-to-end Machine Learning pipeline that analyzes the California Housing dataset to predict house prices (Regression) and classify property affordability (Classification). The project is deployed as an interactive web application using Streamlit.
 🚀 Live Demo

A live version of this application can be accessed here:
https://california-housing-project.streamlit.app/

## 📋 Project Overview

The objective of this project is to perform a full Data Science workflow, including data preprocessing, Exploratory Data Analysis (EDA), model training, evaluation, and finally, deployment.

### Key Features:

Data Cleaning & EDA: Handling missing values and analyzing feature correlations.
Regression Model:Using `Linear Regression` to predict continuous house prices.
Classification Model: Using `Logistic Regression` to categorize houses as "Affordable" or "Expensive."
Interactive Dashboard: A `Streamlit` web application allowing users to input property details for real-time predictions.

🛠 Technologies Used

Python:Programming language.
Scikit-Learn: Machine learning library for model training and scaling.
Streamlit: Framework for building the interactive web interface.
Pandas: for data manipluate
Matplotlib & Seaborn: For visualizing model performance and data trends.

## 📂 Project Structure

```text
├── models/                   # Contains trained .pkl files (Model & Scaler)
├── notebook/                 # Jupyter notebook with training code
├── app.py                    # Main script for the Streamlit web app
├── housing.csv               # The original dataset
├── requirements.txt          # Python library dependencies
└── README.md                 # Project documentation



  How to Run

1. Clone the repository:
bash
git clone <git remote add origin https://github.com/Shushila-Rai/ML-WEEK3--TASK.git>
cd <ML WEEK3-TASK>



2. Install dependencies:
bash
pip install -r requirements.txt




3. Run the application:
bash
streamlit run app.py





## 📈 Model Performance

We evaluated the models using industry-standard metrics:

1 Regression:** Mean Absolute Error (MAE) and Mean Squared Error (MSE).
2 Classification:** Accuracy Score, Precision, Recall, and Confusion Matrix.

Visualizations for these metrics are integrated directly into the **"Model Performance"** tab within the application.

📝 Documentation

Training: The `model_training.ipynb` notebook documents the step-by-step process of cleaning the data and training the models.
Deployment:** The application is hosted on Streamlit Cloud, ensuring accessibility and ease of use for end-users.

