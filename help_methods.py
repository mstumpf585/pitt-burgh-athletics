import pandas as pd

def flip_columns_and_rows(df):
    """ Take a processed CIR data frame and flip it so the categories are columns"""
    master_pivot = pd.DataFrame()
    for team in ["A", "B", "C", "D"]: 

        team_df = df[["Segment", "Category", "Region", team, "Year"]]
        team_df
        table = pd.pivot_table(team_df, values= team, columns="Category", index = ["Year", "Region", "Segment"])

        if master_pivot.empty:
            master_pivot = table
        else: 
            master_pivot = pd.concat([master_pivot, table])

    return master_pivot