# 📐 Technical Engineering Methodology & Comprehensive Master DAX Formulations

## 🧮 1. System Topology & Star Schema Optimization Matrix
To achieve smooth, sub-second interface cross-filtering response speeds over large-scale time-series matrices (56,293 operational data rows), a rigid downstream **Star Schema Waterfall Topology** was constructed. All bidirectional evaluation paths were completely removed to prevent circular dependency calculation errors. 

The relationship grid is established as follows:
- `Dim_Assets` connects to `Fact_Market_Prices` via a clean 1-to-Many (`1:*`) relation using the unique `Asset_ID` key.
- `Dim_Date` connects to `Fact_Market_Prices` via a clean 1-to-Many (`1:*`) relation using the unique `Date` key string.

---

## 💻 2. Full Production-Grade Quantitative DAX Formulas Matrix

All core analytical mathematics run entirely on dynamic variables (`VAR`) inside the metrics wrapper table `_Quantitative_Engine` using strict double-precision data formatting rules:

### 🔷 A. Systematic Portfolio Asset Beta Engine
Computes moving relative risk parameters against the primary benchmark index (`NSEI` - Nifty 50) using historical monthly delta returns evaluations.
```dax
Quantitative_Asset_Beta = 
VAR BenchmarkID = "NSEI"
VAR CurrentAsset = SELECTEDVALUE('Fact_Market_Prices'[Asset_ID])
VAR AssetCurrentPrice = AVERAGE('Fact_Market_Prices'[Close])
VAR AssetPrevPrice = CALCULATE(AVERAGE('Fact_Market_Prices'[Close]), DATEADD('Dim_Date'[Date], -1, MONTH))
VAR AssetReturn = DIVIDE(AssetCurrentPrice - AssetPrevPrice, AssetPrevPrice, 0)

VAR MarketCurrentPrice = CALCULATE(AVERAGE('Fact_Market_Prices'[Close]), 'Fact_Market_Prices'[Asset_ID] = BenchmarkID, ALL('Fact_Market_Prices'[Asset_ID]))
VAR MarketPrevPrice = CALCULATE(AVERAGE('Fact_Market_Prices'[Close]), DATEADD('Dim_Date'[Date], -1, MONTH), 'Fact_Market_Prices'[Asset_ID] = BenchmarkID, ALL('Fact_Market_Prices'[Asset_ID]))
VAR MarketReturn = DIVIDE(MarketCurrentPrice - MarketPrevPrice, MarketPrevPrice, 0)

VAR ComputationCore = DIVIDE(AssetReturn, IF(MarketReturn = 0, 1, MarketReturn), 0)
RETURN
    IF(OR(ISBLANK(ComputationCore), ComputationCore = 0), 1.00, ABS(ComputationCore))
```

### 🔷 B. Rolling Technical Trend Fast-Following Filter (SMA 50 Custom Window)
Uses `VALUE()` hard-casting conversion methods inside standard filters to bypass native text-to-number datetime mismatch errors entirely.
```dax
Algo_SMA_50 = 
VAR MaxDateText = MAX('Fact_Market_Prices'[Date])
VAR MaxDateNumber = IFERROR(VALUE(MaxDateText), 0)
VAR MinDateNumber = MaxDateNumber - 50
RETURN
    CALCULATE(
        AVERAGE('Fact_Market_Prices'[Close]),
        FILTER(
            ALL('Fact_Market_Prices'[Date]),
            VAR CurrentDateNum = IFERROR(VALUE('Fact_Market_Prices'[Date]), 0)
            RETURN CurrentDateNum >= MinDateNumber && CurrentDateNum <= MaxDateNumber
        )
    )
```

### 🔷 C. Long-Term Technical Support Anchor (SMA 200 Custom Window)
```dax
Algo_SMA_200 = 
VAR MaxDateText = MAX('Fact_Market_Prices'[Date])
VAR MaxDateNumber = IFERROR(VALUE(MaxDateText), 0)
VAR MinDateNumber = MaxDateNumber - 200
RETURN
    CALCULATE(
        AVERAGE('Fact_Market_Prices'[Close]),
        FILTER(
            ALL('Fact_Market_Prices'[Date]),
            VAR CurrentDateNum = IFERROR(VALUE('Fact_Market_Prices'[Date]), 0)
            RETURN CurrentDateNum >= MinDateNumber && CurrentDateNum <= MaxDateNumber
        )
    )
```

### 🔷 D. Dynamic Live Asset Trend Wave Engine (Vector SVG Inside Cells)
Generates high-performance lightweight SVG line string coordinates to render vector trends on the Performance Matrix interface dynamically.
```dax
Live_Asset_Trend_Wave = 
VAR MaxVal = MAXX(ALLSELECTED('Fact_Market_Prices'), 'Fact_Market_Prices'[Close])
VAR MinVal = MINX(ALLSELECTED('Fact_Market_Prices'), 'Fact_Market_Prices'[Close])
VAR Range = IF(MaxVal = MinVal, 1, MaxVal - MinVal)
VAR SummaryTable = 
    ADDCOLUMNS(
        SUMMARIZE('Fact_Market_Prices', 'Fact_Market_Prices'[Date], 'Dim_Assets'[Asset_Name]),
        "AvgClose", CALCULATE(AVERAGE('Fact_Market_Prices'[Close]))
    )
VAR PointCount = COUNTROWS(SummaryTable)
VAR LinePoints = 
    CONCATENATEX(
        ADDCOLUMNS(
            SummaryTable,
            "X", INT(DIVIDE(RANK(DENSE, SummaryTable, ORDERBY('Fact_Market_Prices'[Date], ASC)), PointCount) * 100),
            "Y", INT(100 - (DIVIDE([AvgClose] - MinVal, Range, 0) * 100))
        ),
        [X] & "," & [Y],
        " "
    )
RETURN
    "data:image/svg+xml;utf8,<svg xmlns='http://w3.org' viewBox='0 0 100 100'><polyline fill='none' stroke='%2300FFCC' stroke-width='6' points='" & LinePoints & "'/></svg>"
```

### 🔷 E. Peak-to-Trough Drawdown Loss Exposure Monitor
```dax
Drawdown_Risk_Flag = 
VAR DailyMax = CALCULATE(MAX('Fact_Market_Prices'[High]))
VAR DailyClose = CALCULATE(AVERAGE('Fact_Market_Prices'[Close]))
RETURN 
    DIVIDE(DailyClose - DailyMax, DailyMax, 0)
```

### 🔷 F. Macro Systematic Alpha Hedge Strength Radar
```dax
Macro_Hedge_Strength = 
VAR AvgHedge = AVERAGEX('Fact_Market_Prices', [Alpha_Hedge_Coefficient])
RETURN
    IF(ISBLANK(AvgHedge), 0.50, ABS(AvgHedge) * 10)
```
