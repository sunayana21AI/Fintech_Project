# Mutual Fund Analytics Project - Data Dictionary

## 01_fund_master.csv

| Column            | Data Type | Description              |
| ----------------- | --------- | ------------------------ |
| amfi_code         | Integer   | Unique AMFI scheme code  |
| fund_house        | String    | Mutual fund company name |
| scheme_name       | String    | Scheme name              |
| category          | String    | Fund category            |
| sub_category      | String    | Fund sub-category        |
| plan              | String    | Direct/Regular plan      |
| launch_date       | Date      | Scheme launch date       |
| benchmark         | String    | Benchmark index          |
| expense_ratio_pct | Float     | Expense ratio percentage |
| exit_load_pct     | Float     | Exit load percentage     |
| fund_manager      | String    | Fund manager name        |
| risk_category     | String    | Risk classification      |

---

## 02_nav_history.csv

| Column    | Data Type | Description     |
| --------- | --------- | --------------- |
| amfi_code | Integer   | Scheme code     |
| date      | Date      | NAV date        |
| nav       | Float     | Net Asset Value |

---

## 03_aum_by_fund_house.csv

| Column     | Data Type | Description                       |
| ---------- | --------- | --------------------------------- |
| date       | Date      | Reporting date                    |
| fund_house | String    | AMC name                          |
| aum_crore  | Float     | Assets Under Management (Crore ₹) |

---

## 04_monthly_sip_inflows.csv

| Column                    | Data Type | Description         |
| ------------------------- | --------- | ------------------- |
| month                     | Date      | Month               |
| sip_inflow_crore          | Float     | Monthly SIP inflow  |
| active_sip_accounts_crore | Float     | Active SIP accounts |
| sip_aum_lakh_crore        | Float     | SIP AUM             |

---

## 05_category_inflows.csv

| Column           | Data Type | Description       |
| ---------------- | --------- | ----------------- |
| month            | Date      | Month             |
| category         | String    | Fund category     |
| net_inflow_crore | Float     | Net inflow amount |

---

## 06_industry_folio_count.csv

| Column              | Data Type | Description   |
| ------------------- | --------- | ------------- |
| month               | Date      | Month         |
| total_folios_crore  | Float     | Total folios  |
| equity_folios_crore | Float     | Equity folios |
| debt_folios_crore   | Float     | Debt folios   |

---

## 07_scheme_performance.csv

| Column         | Data Type | Description   |
| -------------- | --------- | ------------- |
| amfi_code      | Integer   | Scheme code   |
| scheme_name    | String    | Scheme name   |
| return_1yr_pct | Float     | 1-year return |
| return_3yr_pct | Float     | 3-year return |
| return_5yr_pct | Float     | 5-year return |
| alpha          | Float     | Alpha value   |
| beta           | Float     | Beta value    |
| sharpe_ratio   | Float     | Sharpe Ratio  |

---

## 08_investor_transactions.csv

| Column           | Data Type | Description            |
| ---------------- | --------- | ---------------------- |
| investor_id      | Integer   | Investor identifier    |
| transaction_date | Date      | Transaction date       |
| transaction_type | String    | SIP/Lumpsum/Redemption |
| amount_inr       | Float     | Transaction amount     |

---

## 09_portfolio_holdings.csv

| Column     | Data Type | Description                 |
| ---------- | --------- | --------------------------- |
| amfi_code  | Integer   | Scheme code                 |
| stock_name | String    | Stock name                  |
| sector     | String    | Sector                      |
| weight_pct | Float     | Portfolio weight percentage |

---

## 10_benchmark_indices.csv

| Column      | Data Type | Description     |
| ----------- | --------- | --------------- |
| date        | Date      | Benchmark date  |
| index_name  | String    | Benchmark index |
| index_value | Float     | Index value     |
