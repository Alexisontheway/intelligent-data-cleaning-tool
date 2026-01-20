import pandas as pd
import logging
from pathlib import Path

def save_data_quality_report(
    report_path: Path,
    original_rows: int,
    final_rows: int,
    missing_by_column: dict,
) -> None:
    """
    Save a human-readable data quality report to a text file.
    """
    duplicates_removed = original_rows - final_rows

    with open(report_path, "w") as file:
        file.write("DATA QUALITY REPORT\n")
        file.write("===================\n\n")

        file.write(f"Original rows: {original_rows}\n")
        file.write(f"Final rows: {final_rows}\n")
        file.write(f"Duplicates removed: {duplicates_removed}\n\n")

        if missing_by_column:
            file.write("Missing values by column:\n")
            for column, count in missing_by_column.items():
                file.write(f"- {column}: {count}\n")
        else:
            file.write("No missing values detected.\n")
            

def save_cleaned_data(df: pd.DataFrame, output_path: Path) -> None:
    """
    Save cleaned DataFrame to CSV.
    """
    df.to_csv(output_path, index=False)
    logging.info(f"Cleaned data saved to {output_path}")


def log_summary(df: pd.DataFrame) -> None:
    """
    Log basic data quality summary.
    """
    missing_summary = df.isna().sum()
    missing_columns = missing_summary[missing_summary > 0]

    if not missing_columns.empty:
        logging.info("Missing values summary:")
        for col, count in missing_columns.items():
            logging.info(f" - {col}: {count}")
    else:
        logging.info("No missing values remaining.")
