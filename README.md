# Data Analytics Internship – DecodeLabs

**Intern:** Olawoyin Olufunmilayo Esther

## Overview
This repository contains my work for the DecodeLabs Data Analytics Internship, covering data cleaning (Project 1) and exploratory data analysis (Project 2) on a sales dataset.
## Repository Structure
├── main.py                                  # Project 1: Data cleaning script
├── eda.py                                   # Project 2: Exploratory data analysis script
├── cleaned_Dataset_for_Data_Analytics.xlsx  # Cleaned dataset
├── charts/                                  # Visual outputs from eda.py
│   ├── boxplots.png
│   ├── numeric_distributions.png
│   ├── categorical_breakdowns.png
│   ├── monthly_sales_trend.png
│   └── correlation_heatmap.png
└── README.md

## Dataset
1,200 orders across 14 variables, covering product, pricing, payment method, order status, coupon usage, and referral source.
## Project 2: Exploratory Data Analysis
### Problem Statement
The goal was to explore the cleaned sales dataset (1,200 orders, 14 variables) to uncover patterns, trends, and outliers, and turn that into insight the business could act on, before any predictive modeling is attempted.
### Methodology
I ran descriptive statistics on all numeric fields, plotted distributions and category breakdowns, checked revenue over time, tested for outliers using the IQR method, and looked at correlations between variables.
### Key Findings
1. **Order sizes are consistent, not skewed.** Quantity ranges from 1 to 5 per order and is spread fairly evenly, so there's no single "typical" order size dominating the data. This means average-based metrics (like mean quantity) are safe to use without being thrown off by extreme values.

2. **TotalPrice has 8 outliers, all on the high end.** These are orders above roughly $3,330. That's under 1% of all orders, but they're worth a manual look, since they could be bulk purchases, VIP customers, or possibly a pricing error worth flagging to the business.

3. **No single product or channel dominates.** Products (Printer, Tablet, Chair, etc.), payment methods, and referral sources are all fairly evenly distributed. That tells you this isn't a business overly reliant on one product line or one marketing channel, which is generally a sign of a healthy, diversified customer base.
4. **About 1 in 5 orders are cancelled.** `Cancelled` is the most common order status (250 of 1200 orders, ~21%). This is worth flagging as a possible revenue leak. It doesn't tell us why orders are cancelled, but it's a clear area for follow-up (e.g. is it payment failures, stock issues, or customer changes of mind?).

5. **Revenue doesn't show a clear seasonal pattern.** Monthly revenue moves up and down without a repeating cycle, so there's no obvious "high season" or "low season" to plan around based on this data alone.

6. **Order value is driven more by unit price than quantity.** `TotalPrice` correlates more strongly with `UnitPrice` (0.72) than with `Quantity` (0.62). In plain terms: what customers buy matters more to revenue than how many units they buy. Laptop orders bring in the highest average revenue per order; Phones the lowest.

### Recommendations
- Manually review the 8 high-value outlier orders to confirm they're legitimate.
- Investigate the root cause of the 21% cancellation rate, since reducing it even slightly would directly recover revenue.
- Since order value is driven by product mix more than order size, consider strategies that shift customers toward higher-value products (like Laptops) rather than just encouraging larger cart sizes.
