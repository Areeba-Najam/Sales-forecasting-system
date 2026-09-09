import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import datetime

st.set_page_config(page_title="Sales Forecasting System", page_icon="📈", layout="centered")

@st.cache_resource
def get_trained_model():
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv"
    df = pd.read_csv(url)
    
    df.columns = [col.strip() for col in df.columns]
    if 'Temp' in df.columns:
        df.rename(columns={'Temp': 'Sales'}, inplace=True)
    elif df.columns[0] != 'Date':
        df.columns = ['Date', 'Sales']
        
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
    df.dropna(inplace=True)
    
    # Feature Engineering
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df['DayOfWeek'] = df['Date'].dt.dayofweek
    df['Sales_Lag1'] = df['Sales'].shift(1)
    df.dropna(inplace=True)
    
    X = df[['Year', 'Month', 'Day', 'DayOfWeek', 'Sales_Lag1']]
    y = df['Sales']
    
    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X, y)
    return model

model = get_trained_model()


st.title("📈 Sales & Trend Forecasting System")
st.markdown("Predict future sales volume and retail trends based on temporal patterns and historical lag data using Machine Learning.")

st.sidebar.header("Forecasting Parameters")
input_date = st.sidebar.date_input("Select Target Date", value=datetime.date(1991, 5, 15))
sales_lag1 = st.sidebar.number_input("Previous Day Sales Value (Lag 1)", min_value=0.0, max_value=50.0, value=12.5, step=0.5)

year = input_date.year
month = input_date.month
day = input_date.day
day_of_week = input_date.weekday()

st.subheader("📊 Prediction Analysis")
if st.button("Generate Sales Forecast", type="primary"):
    input_data = np.array([[year, month, day, day_of_week, sales_lag1]])
    prediction = model.predict(input_data)[0]
    
    st.success(f"Predicted Sales Volume: **{prediction:.2f} units**")
    
    if prediction > 15:
        st.info("Trend Outlook: **High Demand / Peak Sales Period** 🚀")
    else:
        st.warning("Trend Outlook: **Moderate / Standard Sales Period** 📊")

st.markdown("---")
st.caption("Powered by Python, Scikit-Learn, and Streamlit.")