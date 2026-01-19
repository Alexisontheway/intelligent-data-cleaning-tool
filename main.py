import logging
import argparse
from pathlib import Path

from data_cleaner.loader import load_csv
from data_cleaner.cleaner import (
    normalize_columns,
    handle_missing_values,
    remove_duplicates,
)
from data_cleaner.reporter import save_cleaned_data, log_summary


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s",
    force=True,
)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Intelligent Data Cleaning Tool - Phase 1"
    )
    parser.add_argument("input", type=Path, help="Input CSV file")
    parser.add_argument("output", type=Path, help="Output cleaned CSV file")
    return parser.parse_args()


def main():
    args = parse_arguments()

    df = load_csv(args.input)
    df = normalize_columns(df)
    df = handle_missing_values(df)
    df = remove_duplicates(df)

    log_summary(df)
    save_cleaned_data(df, args.output)


if __name__ == "__main__":
    main()
