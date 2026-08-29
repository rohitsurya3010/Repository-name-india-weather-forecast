# India Forecast Confidence System

An interactive weather forecasting and forecast-confidence analysis dashboard for India using GFS weather forecasts, historical forecast errors, machine learning, and a Forecast Stress Score.

## Project Overview

The India Forecast Confidence System is a Streamlit-based dashboard designed to analyze weather forecast reliability across India.

The system processes forecast results and provides an interactive interface to explore forecast-bust probability, forecast stress, temperature, rainfall, confidence levels, and risk factors for different forecast lead days and Indian states.

## Objectives

- Analyze weather forecast information for India
- Estimate forecast-bust probability
- Evaluate forecast confidence
- Analyze forecast stress across states
- Visualize weather forecast risk
- Compare forecast risk across different lead days
- Provide downloadable forecast results

## Key Features

- India weather forecast analysis
- Forecast-bust probability
- Forecast Stress Score
- Temperature analysis
- Rainfall analysis
- Interactive India Forecast Stress Map
- Forecast Risk Analysis
- 10-Day Bust Probability Trend
- Highest-Risk State identification
- Forecast result CSV download
- Mobile-friendly dashboard

## Methodology

The system combines:

- GFS weather forecast information
- Historical forecast errors
- Machine learning
- Forecast Stress Score
- Forecast confidence analysis

The dashboard uses these results to identify potentially high-risk forecast conditions and present them in an interactive format.

## Dashboard Components

### Forecast Controls

Users can select:

- Forecast Lead Day
- Indian State
- All India

### Key Performance Indicators

The dashboard displays:

- Bust Probability
- Forecast Stress
- Temperature
- Rainfall

### Forecast Stress Map

An interactive map displays forecast stress across India.

The visualization represents:

- State location
- Forecast stress
- Bust probability
- Forecast confidence
- Rainfall
- Temperature
- Wind speed

### Forecast Risk Analysis

An interactive chart compares forecast-bust probability and forecast stress across states.

### 10-Day Bust Probability Trend

The dashboard displays the average predicted bust probability across forecast lead days.

### High-Risk States

The system identifies states with the highest predicted forecast-bust probability.

### Forecast Results Download

Users can download filtered forecast results as a CSV file.

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Scikit-learn
- Joblib
- GFS Weather Forecast Data
- Machine Learning

## Data

The main processed dataset used by the dashboard is:

`FINAL_FORECAST_RESULTS.csv`

The application uses forecast-related fields including:

- Forecast lead day
- State
- Bust probability
- Stress score
- Confidence
- Rainfall
- Temperature
- Wind speed
- Risk reasons

## System Workflow

```text
GFS Weather Forecast Data
            |
            v
Historical Forecast Analysis
            |
            v
Feature Processing
            |
            v
Machine Learning
            |
            v
Forecast-Bust Probability
            |
            v
Forecast Stress and Confidence
            |
            v
Interactive Streamlit Dashboard
