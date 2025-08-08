# Stock Price Data Downloader

This script allows you to download historical stock price data from Yahoo Finance using the `yfinance` library. The data is saved in CSV format for further analysis.

## Features

- Download stock price data for multiple tickers.
- Specify a date range for the data.
- Automatically creates a `data/` folder to store the downloaded CSV files.
- Handles invalid date formats and missing data gracefully.

## Requirements

The script requires the following Python packages:

- `yfinance`
- `pytest` (for running tests)

Install the dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Usage

Run the script using the command line:

```bash
python downloader.py --tickers TICKER1 TICKER2 ... --start YYYY-MM-DD --end YYYY-MM-DD
```

### Arguments

- `--tickers`: A list of stock tickers (e.g., `AAPL`, `GOOGL`).
- `--start`: The start date in `YYYY-MM-DD` format.
- `--end`: The end date in `YYYY-MM-DD` format.

### Example

To download data for Apple (AAPL) and Oracle(ORCL) from January 1, 2023, to December 31, 2023:

```bash
python downloader.py --tickers AAPL ORCL --start 2023-01-01 --end 2023-12-31
```

The downloaded CSV files will be saved in the `data/` folder.

## Testing

Unit tests are provided to validate the functionality of the script. Run the tests using:

```bash
pytest tests/test_downloader.py
```

## Folder Structure

```
stock_downloader/
├── downloader.py          # Main script
├── tests/
│   └── test_downloader.py # Unit tests
├── requirements.txt       # Dependencies
├── README.MD              # Documentation
└── data/                  # Folder for downloaded CSV files (created automatically)
```

## Author

Mohammed Akram

## License

If you read till here, thanks.. the project is yours and your free to do as you please.

## Note from the author:

This was a pretty simple command line tool that I built to get data about stocks easily.
