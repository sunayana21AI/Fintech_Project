import pandas as pd

perf = pd.read_csv(
    "../data/processed/fund_scorecard.csv"
)

risk = input(
    "Risk Appetite (Low/Moderate/High): "
)

result = (
    perf[
        perf["risk_grade"]
        .str.contains(risk, case=False)
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print(result[
    [
        "scheme_name",
        "fund_house",
        "sharpe_ratio"
    ]
])