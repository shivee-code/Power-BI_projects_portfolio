import os
import yfinance as yf
import pandas as pd

# Project folders
base_dir = os.path.join(os.getcwd(), "data")
fact_dir = os.path.join(base_dir, "Fact_Market_Prices")

os.makedirs(fact_dir, exist_ok=True)

# Clean old files
for f in os.listdir(fact_dir):
    os.remove(os.path.join(fact_dir, f))

# Assets universe
assets = {
    "TCS.NS": "Stock",
    "INFY.NS": "Stock",
    "RELIANCE.NS": "Stock",
    "HDFCBANK.NS": "Stock",
    "ICICIBANK.NS": "Stock",
    "SBIN.NS": "Stock",
    "ITC.NS": "Stock",
    "TATAMOTORS.NS": "Stock",
    "^NSEI": "Benchmark",
    "^BSESN": "Benchmark",
    "GC=F": "Commodity",
    "INR=X": "Forex"
}

print("Starting Market Data Extraction...")

for ticker, asset_type in assets.items():
    try:
        df = yf.download(
            ticker,
            period="2y",
            interval="1h"
        )

        if not df.empty:

            df.columns = df.columns.get_level_values(0)
            df = df.reset_index()

            # Standard columns
            if 'Datetime' in df.columns:
                df = df.rename(columns={'Datetime': 'Date'})

            df['Raw_Ticker'] = ticker
            df['Asset_Class'] = asset_type

            clean_name = (
                ticker
                .replace(".NS", "")
                .replace("^", "")
                .replace("=F", "")
                .replace("=X", "")
            )

            file_path = os.path.join(
                fact_dir,
                f"{clean_name}_Hourly_Log.csv"
            )

            df.to_csv(file_path, index=False)

            print(f"Saved: {clean_name}")

    except Exception as e:
        print(f"Failed for {ticker}: {e}")

print("All files extracted successfully!")