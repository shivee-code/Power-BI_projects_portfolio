import pandas as pd
import os

# Dynamic project path
base_dir = os.path.join(os.getcwd(), "data", "Dim_Lookup")
os.makedirs(base_dir, exist_ok=True)

dim_data = {
    "Asset_ID": [
        "TCS", "INFY", "RELIANCE", "HDFCBANK",
        "ICICIBANK", "SBIN", "TATAMOTORS",
        "ITC", "NSEI", "BSESN", "GC", "INR"
    ],
    
    "Asset_Name": [
        "Tata Consultancy Services",
        "Infosys",
        "Reliance Industries",
        "HDFC Bank",
        "ICICI Bank",
        "State Bank of India",
        "Tata Motors",
        "ITC Limited",
        "Nifty 50 Index",
        "Sensex Index",
        "Gold Commodity",
        "USD/INR Forex"
    ],
    
    "Asset_Type": [
        "Stock", "Stock", "Stock", "Stock",
        "Stock", "Stock", "Stock", "Stock",
        "Benchmark", "Benchmark",
        "Commodity", "Forex"
    ],
    
    "Risk_Category": [
        "Low Beta", "Low Beta", "Medium Beta",
        "Medium Beta", "Medium Beta",
        "High Beta", "High Beta",
        "Low Beta", "Market", "Market",
        "Safe Haven", "Currency Asset"
    ]
}

df_dim = pd.DataFrame(dim_data)

output_path = os.path.join(base_dir, "Dim_Assets.csv")
df_dim.to_csv(output_path, index=False)

print("Metadata Lookup File Created Successfully!")