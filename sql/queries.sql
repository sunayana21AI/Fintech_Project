-- 1 Top 5 funds by AUM

SELECT *
FROM "03_aum_by_fund_house"
ORDER BY aum_lakh_crore DESC
LIMIT 5;



-- 2 Average NAV

SELECT 
AVG(nav) AS average_nav
FROM "02_nav_history";



-- 3 Monthly SIP inflow

SELECT 
month,
sip_inflow_crore
FROM "04_monthly_sip_inflows"
ORDER BY month;



-- 4 Transactions by state

SELECT
state,
COUNT(*) AS total_transactions
FROM "08_investor_transactions"
GROUP BY state
ORDER BY total_transactions DESC;



-- 5 Funds having expense ratio less than 1%

SELECT
scheme_name,
expense_ratio_pct
FROM "01_fund_master"
WHERE expense_ratio_pct < 1;



-- 6 Fund count by category

SELECT
category,
COUNT(*) AS fund_count
FROM "01_fund_master"
GROUP BY category;



-- 7 Average return by category

SELECT
category,
AVG(return_3yr_pct) AS average_3yr_return
FROM "07_scheme_performance"
GROUP BY category;



-- 8 Top 10 Sharpe ratio funds

SELECT
scheme_name,
sharpe_ratio
FROM "07_scheme_performance"
ORDER BY sharpe_ratio DESC
LIMIT 10;



-- 9 Investor count by age group

SELECT
age_group,
COUNT(*) AS investor_count
FROM "08_investor_transactions"
GROUP BY age_group;



-- 10 Benchmark performance

SELECT *
FROM "10_benchmark_indices";