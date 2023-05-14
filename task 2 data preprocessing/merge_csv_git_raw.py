import sys
import pandas as pd
from fuzzywuzzy import fuzz, process
import requests
from typing import List
from io import StringIO

def standardize_column_name(name: str) -> str:
    return name.lower().replace(" ", "_")

def fuzzy_match(value: str, choices: List[str], threshold: int = 80) -> str:
    match, score = process.extractOne(value, choices)
    if score >= threshold:
        return match
    return value

def download_csv(url: str) -> pd.DataFrame:
    response = requests.get(url)
    response.raise_for_status()
    content = response.content.decode('utf-8')
    return pd.read_csv(StringIO(content))

def main(dfs: List[pd.DataFrame], output_path: str):
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

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python merge_csvs_github.py output.csv input_url1 input_url2 ...")
        sys.exit(1)

    output_path = sys.argv[1]
    csv_urls = sys.argv[2:]
    csv_dfs = [download_csv(url) for url in csv_urls]
    main(csv_dfs, output_path)
