import pandas as pd
from pathlib import Path


DATA_PATH = Path(
    "../data/processed/fund_scorecard.csv"
)


def load_data():

    if not DATA_PATH.exists():

        raise FileNotFoundError(
            "Fund scorecard file not found"
        )


    return pd.read_csv(DATA_PATH)



def recommend_funds(perf, risk):


    risk = risk.strip().lower()


    valid_risks = [
        "low",
        "moderate",
        "high"
    ]


    if risk not in valid_risks:

        raise ValueError(
            "Enter Low, Moderate or High only"
        )



    filtered = perf[
        perf["risk_grade"]
        .fillna("")
        .str.lower()
        .str.contains(risk)
    ]



    if filtered.empty:

        return pd.DataFrame()



    result = (
        filtered
        .sort_values(
            by=[
                "sharpe_ratio",
                "return_3yr_pct"
            ],
            ascending=False
        )
        .head(3)
    )


    result["recommendation_reason"] = (
        "Selected based on "
        "higher Sharpe ratio and returns"
    )


    return result[
        [
            "scheme_name",
            "fund_house",
            "sharpe_ratio",
            "return_3yr_pct",
            "recommendation_reason"
        ]
    ]



if __name__ == "__main__":


    try:


        performance_data = load_data()


        risk_input = input(
            "Risk Appetite (Low/Moderate/High): "
        )


        recommendations = recommend_funds(
            performance_data,
            risk_input
        )


        if recommendations.empty:

            print(
                "No matching funds found"
            )

        else:

            print(
                recommendations
            )


    except Exception as error:

        print(
            f"Error: {error}"
        )