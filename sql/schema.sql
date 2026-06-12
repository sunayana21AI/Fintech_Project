CREATE TABLE IF NOT EXISTS fund_master (

    scheme_code INTEGER PRIMARY KEY,

    scheme_name TEXT,

    fund_house TEXT,

    category TEXT,

    expense_ratio_pct REAL

);



CREATE TABLE IF NOT EXISTS nav_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    scheme_code INTEGER,

    date DATE,

    nav REAL,

    FOREIGN KEY (scheme_code)
    REFERENCES fund_master(scheme_code)

);



CREATE TABLE IF NOT EXISTS aum_by_fund_house (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_house TEXT,

    aum_lakh_crore REAL

);



CREATE TABLE IF NOT EXISTS monthly_sip_inflows (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    month TEXT,

    sip_inflow_crore REAL

);



CREATE TABLE IF NOT EXISTS scheme_performance (

    scheme_code INTEGER PRIMARY KEY,

    scheme_name TEXT,

    category TEXT,

    return_3yr_pct REAL,

    sharpe_ratio REAL,

    beta REAL,

    volatility REAL,

    var_95 REAL

);



CREATE TABLE IF NOT EXISTS investor_transactions (

    transaction_id INTEGER PRIMARY KEY,

    investor_id INTEGER,

    state TEXT,

    age_group TEXT,

    transaction_type TEXT,

    amount REAL

);



CREATE TABLE IF NOT EXISTS benchmark_indices (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    index_name TEXT,

    date DATE,

    closing_value REAL,

    return_pct REAL

);