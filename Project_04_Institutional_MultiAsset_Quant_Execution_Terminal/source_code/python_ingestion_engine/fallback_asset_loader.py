import yfinance as yf
import os
import pandas as pd

target_path = os.path.join(
    os.getcwd(),
    "data",
    "Fact_Market_Prices",
    "TATAMOTORS_Hourly_Log.csv"
)

print("Attempting fallback recovery for Tata Motors...")

ticker_obj = yf.Ticker("TATAMOTORS.NS")

df = ticker_obj.history(
    period="2y",
    interval="1h"
)

# Fallback to M&M if Tata Motors fails
if df.empty:

    print("Fallback triggered -> Switching to M&M")

    df = yf.download(
        "M&M.NS",
        period="2y",
        interval="1h"
    )

    ticker_name = "M&M.NS"

else:
    ticker_name = "TATAMOTORS.NS"

if not df.empty:

    df = df.reset_index()

    if 'Datetime' in df.columns:
        df = df.rename(columns={'Datetime': 'Date'})

    df['Raw_Ticker'] = ticker_name
    df['Asset_Class'] = 'Stock'

    df.to_csv(target_path, index=False)

    print("Fallback asset saved successfully!")