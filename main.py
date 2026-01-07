import pandas as pd
import logging
from pathlib import Path


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
