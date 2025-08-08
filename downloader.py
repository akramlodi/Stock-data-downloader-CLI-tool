"""
Stock price data downloader
Author: Mohammed Akram
Description: This can be used to download the stock price data
using yfinance API in CSV file.
"""

import argparse
import yfinance as yf
from datetime import datetime
from pathlib import Path


def download_data(ticker, start, end):
    """Download data from Yahoo Finance."""
    try:
        data = yf.download(ticker, start=start, end=end, auto_adjust=True)
        if data.empty:
            print(f"[WARNING] No data found for {ticker}")
            return None
        return data
    except Exception as e:
        print(f"[ERROR]: Failed to download {ticker}: {e}")
        return None


def validate_date(start, end):
    """Validate provided date format as Year, Month, and Day."""
    try:
        datetime.strptime(start, "%Y-%m-%d")
        datetime.strptime(end, "%Y-%m-%d")
        return True
    except ValueError:
        print("[ERROR] Dates must be in format YYYY-MM-DD")
        return False


def save_to_csv(ticker, data):
    """Save the data to file."""
    file_path = Path("data") / f"{ticker}.csv"
    data.to_csv(file_path)
    print(f"[INFO] Saved {ticker}.csv in data/")


def create_data_folder():
    """Create 'data' folder if it doesn't exist."""
    Path("data").mkdir(exist_ok=True)
    print("[INFO] 'data/' folder ready.")


def main():
    parser = argparse.ArgumentParser(
        description="Download stock price data from Yahoo Finance."
    )
    parser.add_argument(
        "--tickers", nargs="+", required=True,
        help="List of stock tickers (ex: AAPL)"
    )
    parser.add_argument(
        "--start", required=True, help="Start date in YYYY-MM-DD format"
    )
    parser.add_argument(
        "--end", required=True, help="End date in YYYY-MM-DD format"
    )
    args = parser.parse_args()

    if not validate_date(args.start, args.end):
        return None

    create_data_folder()

    print("[INFO] Downloading data for tickers.")
    for ticker in args.tickers:
        df = download_data(ticker, args.start, args.end)
        if df is not None:
            save_to_csv(ticker, df)

    print("[INFO] Files have been downloaded.")

    return


if __name__ == "__main__":
    main()
