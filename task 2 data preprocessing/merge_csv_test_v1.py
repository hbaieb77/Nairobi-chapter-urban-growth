import sys
import pandas as pd
from typing import List

def standardize_column_name(name: str) -> str:
    return name.lower().replace(" ", "_")

def main(filepaths: List[str], output_path: str):
    dfs = [pd.read_csv(fp) for fp in filepaths]

    # Standardize column names
    for df in dfs:
        df.columns = [standardize_column_name(col) for col in df.columns]

    # Perform full join
    merged_df = dfs[0]
    for df in dfs[1:]:
        common_columns = set(merged_df.columns) & set(df.columns)
        join_columns = {"year", "country"}
        if "city" in merged_df.columns and "city" in df.columns:
            join_columns.add("city")
        common_columns -= join_columns
        for col in common_columns:
            df = df.rename(columns={col: f"{col}_temp"})
        merged_df = merged_df.merge(df, on=list(join_columns), how="outer")

    # Merge common columns with "_temp" and "_x" or "_y" suffixes
    for col in merged_df.columns:
        if "_temp" in col or "_x" in col or "_y" in col:
            original_col = col.replace("_temp", "").replace("_x", "").replace("_y", "")
            if original_col in merged_df.columns:
                merged_df[original_col].update(merged_df[col].dropna())
                merged_df.drop(col, axis=1, inplace=True)
            else:
                merged_df.rename(columns={col: original_col}, inplace=True)

    # Save the merged file
    merged_df.to_csv(output_path, index=False)
    print(f"Merge was successful! Merged file saved as '{output_path}'.")

if __name__ == "__main__":
    output_path = input("Enter the output file name (e.g., merged_output.csv): ")
    input_files = input("Enter the input file names separated by space (e.g., input1.csv input2.csv): ").split()
    main(input_files, output_path)
