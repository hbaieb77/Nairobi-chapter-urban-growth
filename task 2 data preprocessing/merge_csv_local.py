import sys
import pandas as pd
from fuzzywuzzy import fuzz, process
from typing import List
import os
from git import Repo

def standardize_column_name(name: str) -> str:
    return name.lower().replace(" ", "_")

def fuzzy_match(value: str, choices: List[str], threshold: int = 80) -> str:
    match, score = process.extractOne(value, choices)
    if score >= threshold:
        return match
    return value

def main(filepaths: List[str], output_path: str):
    dfs = [pd.read_csv(fp) for fp in filepaths]

    # Standardize column names
    for df in dfs:
        df.columns = [standardize_column_name(col) for col in df.columns]

    # Standardize country and city names
    all_countries = []
    all_cities = []
    for df in dfs:
        all_countries.extend(df["country"].unique())
        all_cities.extend(df["city"].unique())

    all_countries = list(set(all_countries))
    all_cities = list(set(all_cities))

    for df in dfs:
        df["country"] = df["country"].apply(lambda x: fuzzy_match(x, all_countries))
        df["city"] = df["city"].apply(lambda x: fuzzy_match(x, all_cities))

    # Perform full join
    merged_df = dfs[0]
    for df in dfs[1:]:
        common_columns = set(merged_df.columns) & set(df.columns)
        common_columns -= {"year", "country", "city"}
        for col in common_columns:
            df = df.rename(columns={col: f"{col}_temp"})
        merged_df = merged_df.merge(df, on=["year", "country", "city"], how="outer")

    # Merge common columns
    for col in merged_df.columns:
        if "_temp" in col:
            original_col = col.replace("_temp", "")
            merged_df[original_col].update(merged_df[col])
            merged_df.drop(col, axis=1, inplace=True)

    # Save the merged file
    merged_df.to_csv(output_path, index=False)

    # Commit the merged file to the local Git repository
    repo = Repo(os.getcwd())
    repo.index.add([output_path])
    repo.index.commit("Add merged CSV file")
    repo.remote("origin").push()

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python merge_csvs.py output.csv input_file1 input_file2 ...")
        sys.exit(1)

    output_path = sys.argv[1]
    input_files = sys.argv[2:]
    main(input_files, output_path)
