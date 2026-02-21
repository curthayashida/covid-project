import pandas as pd

file_path = r"C:\Personal\Data_Analysis\Covid_Project\state_sales.csv"

df = pd.read_csv(file_path)


states = [
    "California", "Texas", "New York", "Florida",
    "Hawaii", "Nevada", "Nebraska", "South Dakota"
]

years = range(2019, 2025)

filtered_df = df[
    (df["State"].isin(states)) &
    (df["Year"].isin(years))
][[
    "State",
    "Year",
    "Food-at-home sales with taxes and tips (millions of nominal U.S. dollars)",
    "Food-away-from-home sales with taxes and tips (millions of nominal U.S. dollars)"
]]

filtered_df = filtered_df.sort_values(["State", "Year"])

print(filtered_df)
