# 🌦️ India Forecast Confidence System

An interactive weather forecasting and forecast-confidence analysis platform designed to visualize weather predictions for India using NWP/GFS forecast data and machine learning.

##  Project Overview

The India Forecast Confidence System provides an interactive dashboard for analyzing weather forecasts and understanding the reliability of predicted weather conditions.

The system combines numerical weather prediction (NWP) data, GFS forecast data, data analysis, visualization, and machine learning to present forecast results through a user-friendly web dashboard.

## Objectives

- Analyze weather forecast data for India
- Visualize forecast conditions interactively
- Evaluate forecast confidence
- Identify potential forecast errors or "forecast busts"
- Present weather information through an interactive dashboard
- Provide a mobile-friendly interface for easier access

## Key Features

-  India weather forecast visualization
-  Interactive forecast dashboard
-  Forecast trend analysis
-  Forecast confidence analysis
-  Machine-learning-based forecast bust detection
-  Interactive weather visualization
- Mobile-friendly dashboard
-  Multi-day forecast analysis

## Machine Learning

The project uses machine learning techniques to analyze forecast behavior and identify situations where the forecast may significantly deviate from expected conditions.

The trained model is integrated into the dashboard to support forecast-confidence and forecast-bust analysis.

##  Data Sources

The system works with Numerical Weather Prediction (NWP) and Global Forecast System (GFS) forecast data.

The processed forecast data is used for analysis, visualization, and machine-learning-based evaluation.

##  Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Scikit-learn
- Joblib
- NWP / GFS Weather Data
- Machine Learning

##  System Architecture

```text
NWP / GFS Weather Data
          ↓
     Data Processing
          ↓
   Feature Preparation
          ↓
   Machine Learning
          ↓

## Installation
git clone https://github.com/rohitsurya3010/Repository-name-india-weather-forecast.git
cd Repository-name-india-weather-forecast
pip install -r requirements.txt
streamlit run app.py
 Forecast Confidence Analysis
          ↓
   Interactive Dashboard
          ↓
      User Interface
