# Bluestock Mutual Fund Analytics Project

## Project Overview

Bluestock Mutual Fund Analytics is an end-to-end financial data analytics project developed to analyze mutual fund performance, risk factors, investor behavior, and market trends.

The project uses data engineering, financial analytics, and business intelligence techniques to convert raw mutual fund data into meaningful insights.

The system includes an automated ETL pipeline, SQLite database storage, exploratory data analysis, performance analytics, advanced risk analysis, recommendation logic, and an interactive Power BI dashboard.

---

# Project Objectives

The main objectives of this project are:

- Automate mutual fund data processing using ETL pipeline
- Clean and transform raw financial datasets
- Store processed data in SQLite database
- Perform Exploratory Data Analysis (EDA)
- Calculate mutual fund performance metrics
- Analyze investment risks
- Understand investor behavior patterns
- Build interactive dashboard visualization
- Develop a fund recommendation system

---

# Project Workflow

```
Raw Mutual Fund Data
          |
          ↓
      ETL Pipeline
          |
          ↓
 Data Cleaning & Transformation
          |
          ↓
    SQLite Database
          |
          ↓
 Exploratory Data Analysis
          |
          ↓
 Performance & Risk Analytics
          |
          ↓
 Advanced Analytics
          |
          ↓
 Power BI Dashboard
```

---

# Folder Structure

```
bluestock_mf_capstone/

│
├── data/
│   ├── raw/                 
│   ├── processed/           
│   └── db/                  
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── scripts/
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   ├── compute_metrics.py
│   └── recommender.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│   └── bluestock_mf_dashboard.pbix
│
├── reports/
│   ├── Final_Report.pdf
│   └── Presentation.pptx
│
└── README.md
```

---

# Technologies Used

## Programming Language

- Python

## Python Libraries

- Pandas
- NumPy
- Matplotlib
- SQLite3

## Database

- SQLite

## Visualization Tool

- Power BI

## Development Environment

- Jupyter Notebook
- VS Code

---

# Dataset Description

The project uses multiple mutual fund datasets.

| Dataset | Description |
|---|---|
| Fund Master | Contains scheme information and fund details |
| NAV History | Historical NAV data for return calculation |
| AUM Data | Asset under management analysis |
| SIP Inflows | Monthly investment trends |
| Scheme Performance | Returns and risk-related metrics |
| Investor Transactions | Investor activity analysis |
| Portfolio Holdings | Portfolio concentration analysis |
| Benchmark Indices | Market comparison data |

---

# ETL Pipeline

The ETL pipeline automates the complete data preparation process.

## Extract

The extraction stage:

- Reads raw CSV files
- Loads financial datasets automatically
- Identifies available data sources


## Transform

The transformation stage performs:

- Duplicate removal
- Missing value handling
- Data cleaning
- Data formatting
- Standardization of columns


## Load

The processed data is stored into:

- Processed CSV files
- SQLite database tables


The pipeline allows the complete data processing workflow to run without manual intervention.

---

# Database Design

SQLite database is used for structured data storage.

Main database tables include:

- fund_master
- nav_history
- aum_by_fund_house
- monthly_sip_inflows
- scheme_performance
- investor_transactions
- portfolio_holdings
- benchmark_indices

The database supports efficient querying and analytics.

---

# Exploratory Data Analysis

EDA was performed to identify patterns and trends.

Analysis includes:

- Fund category distribution
- AUM comparison
- NAV movement trends
- SIP inflow analysis
- Investor transaction analysis

Visualization techniques were used to understand financial patterns.

---

# Performance Analytics

The project evaluates mutual funds using financial metrics.

## Return Metrics

- CAGR
- 3 Year Returns


## Risk Metrics

- Sharpe Ratio
- Alpha
- Beta
- Maximum Drawdown


These metrics help compare funds based on performance and risk.

---

# Advanced Analytics

The project includes advanced financial analysis.

## Value at Risk (VaR)

Measures possible investment loss under normal market conditions.


## Conditional Value at Risk (CVaR)

Measures average loss beyond the VaR limit.


## Rolling Sharpe Ratio

Analyzes performance consistency over time.


## Investor Cohort Analysis

Studies investor groups and investment patterns.


## SIP Continuity Analysis

Classifies investors into:

- Healthy investors
- At-risk investors


## Portfolio Concentration Analysis

Uses HHI (Herfindahl-Hirschman Index) to measure portfolio concentration.

---

# Fund Recommendation System

A recommendation system was developed to suggest suitable funds.

The recommendation logic considers:

- Investor risk category
- Sharpe Ratio
- Fund performance score


The system ranks funds and provides top recommendations.

---

# Power BI Dashboard

An interactive Power BI dashboard was created for visualization.

Dashboard features:

- Fund performance analysis
- Risk analysis
- Investor insights
- Interactive filters
- Slicers
- Dynamic charts


The dashboard helps users understand complex financial information easily.

---

# How to Run the Project

## Step 1: Install Required Libraries

```
pip install pandas numpy matplotlib jupyter
```

---

## Step 2: Run ETL Pipeline

Open terminal:

```
cd scripts
```

Run:

```
python etl_pipeline.py
```

The pipeline will process raw data and generate processed datasets.

---

## Step 3: Execute Notebooks

Run notebooks in the following order:

```
01_data_ingestion.ipynb

02_data_cleaning.ipynb

03_eda_analysis.ipynb

04_performance_analytics.ipynb

05_advanced_analytics.ipynb
```

---

# Important Notes

- Database files are ignored using `.gitignore`
- Raw and processed data are stored separately
- Relative paths are used instead of hard-coded paths
- ETL pipeline supports automated execution
- Data cleaning is performed before analysis

---

# Future Enhancements

The project can be improved by adding:

- Real-time NAV API integration
- Machine learning-based prediction models
- Portfolio optimization techniques
- Streamlit web application
- Automated email reporting system
- Real-time financial monitoring

---

# Conclusion

Bluestock Mutual Fund Analytics provides an end-to-end solution for analyzing mutual fund performance and investment trends.

The project combines data engineering, financial analytics, and visualization to create a complete decision-support system.

It demonstrates how data-driven approaches can improve financial analysis and support better investment decisions.

---

# Author

Bluestock Mutual Fund Analytics Project