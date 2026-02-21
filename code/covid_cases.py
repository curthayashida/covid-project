import pandas as pd

def total_cases_end_of_year_multi(df, states, years):
    
    df = df.copy()
    df.columns = df.columns.str.strip()

    results = []

    for state in states:
        state_df = df[df['State'] == state]

        if state_df.empty:
            continue

        for year in years:
            # find columns containing the year
            cols_year = [col for col in state_df.columns if str(year) in col]

            if not cols_year:
                continue

            # sort columns to guarantee last date
            cols_year_sorted = sorted(cols_year)
            last_date = cols_year_sorted[-1]

            total_cases = state_df[last_date].sum()

            results.append({
                'State': state,
                'Year': year,
                'Total_Cases': total_cases
            })

    return pd.DataFrame(results)
	
states = ['CA', 'TX', 'NY', 'FL', 'IL', 'GA', 'WA', 'SD']
years = [2020, 2021, 2022, 2023]

cases_df = total_cases_end_of_year_multi(df, states, years)
print(cases_df)