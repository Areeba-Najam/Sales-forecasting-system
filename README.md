# 📈 Sales & Trend Forecasting System

An end-to-end data science and machine learning web application that predicts future sales and retail trends based on historical time-series data and temporal features.

## 🚀 Problem Statement
Businesses need accurate insight into future sales trends to optimize inventory management, forecast revenue streams, and streamline operational planning. This project implements an automated machine learning system that ingests historical sales/temperature time-series data, extracts robust seasonal features, and forecasts future metric volumes.

## 🛠️ Tech Stack & Tools
- Python (Core programming language)
- Pandas & NumPy (Data manipulation and feature engineering)
- Scikit-Learn (Random Forest Regressor & evaluation metrics)
- Streamlit (Interactive web application framework)
- Matplotlib & Seaborn (Data visualization)

## 📊 Project Workflow
1. Data Collection: Automatically loads real-world historical time-series datasets via public repositories.
2. Data Cleaning & Preprocessing: Handles missing values, parses date fields into standard datetime formats, and ensures chronological sorting.
3. Feature Engineering: Extracts granular temporal variables (`Year`, `Month`, `Day`, `DayOfWeek`) and constructs **lag features** (`Sales_Lag1`) to capture prior period sales momentum.
4. Model Training: Trains a robust **Random Forest Regressor** to capture non-linear trends and seasonal fluctuations.
5. Evaluation: Evaluates model performance using industry-standard metrics:
   - MAE (Mean Absolute Error)**
   - RMSE (Root Mean Square Error)**
6. Interactive Web App: Deployed via Streamlit, allowing users to select target dates and input previous sales values to generate instant predictions.

## ⚙️ Project File Structure

sales-forecasting-system/
│
├── app.py              # Streamlit interactive web application frontend
├── requirements.txt    # Python package dependencies
└── README.md           # Project documentation

💻 How to Run Locally
Clone the repository:
Bash
git clone [https://github.com/Areeba-Najam/sales-forecasting-system.git](https://github.com/Areeba-Najam/sales-forecasting-system.git)
cd sales-forecasting-system

Install dependencies:
Bash
pip install -r requirements.txt
Run the Streamlit application:

Bash
streamlit run app.py
🌐 Live Web App Deployment
Hosted seamlessly via Streamlit Community Cloud directly connected to this GitHub repository.

👤 Author
Areeba Najam

Computer Science Student | Software & Machine Learning Enthusiast
