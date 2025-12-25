# Methodology — Insurance Risk & Claims Analysis

This section outlines the end-to-end analytical approach followed to build the Insurance Risk & Claims dashboard using Power BI.

## 1. Data Collection
- Imported raw insurance policy and claims data from Excel files.
- Dataset includes customer demographics, vehicle details, coverage zones, claim frequency, and claim amounts.

## 2. Data Cleaning & Preparation
- Removed duplicate policy records.
- Handled missing and null values in claim-related fields.
- Standardized column names and data formats.
- Converted date and numeric fields to appropriate data types.
- Created derived columns for age groups, vehicle age bands, and claim categories.

## 3. Data Transformation (Power Query)
- Grouped and aggregated claim amounts by customer attributes.
- Categorized car usage types (Private vs Commercial).
- Classified coverage zones into Urban, Rural, Suburban, and Highly Urban.
- Built calculated columns for claim frequency and average claim value.

## 4. Data Modeling
- Established relationships between policy, customer, vehicle, and claims tables.
- Optimized data model to improve performance and reduce redundancy.

## 5. DAX Measures
Key DAX measures created include:
- Total Claim Amount
- Average Claim Amount
- Claim Frequency
- Total Policies
- Claims by Demographics and Risk Factors

## 6. Dashboard Design
- KPI cards for high-level performance metrics.
- Bar charts for claim distribution by car make, age group, and education.
- Donut charts for coverage zone and car usage analysis.
- Line chart for claim trends across car manufacturing years.
- Matrix visual to analyze claim behavior by education and marital status.
- Slicers to enable interactive filtering by measures and categories.

## 7. Validation & Optimization
- Cross-checked calculations with source data.
- Optimized visuals for readability and executive-level consumption.
- Ensured dashboard supports interactive and exploratory analysis.

This methodology ensures data accuracy, analytical consistency, and business relevance throughout the project lifecycle.