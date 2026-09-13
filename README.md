### 🐍 DecodeLabs Data Analytics Internship

**Analyst:** Olawoyin Olufunmilayo Esther

## 🎯 Problem Statement
Despite having rich historical transaction records, businesses often struggle to uncover hidden trends, pricing outliers, and operational leaks within their sales data. Without a structured exploratory data analysis, teams lack visibility into whether revenue is driven by order volume or product mix, and where potential revenue leakage such as high cancellation rates occurs. 

This project addresses these gaps by cleaning raw sales logs and performing exploratory data analysis on 1,200 orders across 14 variables to extract actionable business intelligence.

## 🛠️ Tools & Skills
* **Python Programming** (Pandas, Data Cleaning, Exploratory Data Analysis, Statistical Summary Metrics)
* **Data Visualization** (Matplotlib, Seaborn, Boxplots, Correlation Heatmaps, Trend Line Analysis)
* **Business Analytics** (Outlier Detection via IQR, Revenue Driver Diagnostics, Cancellation Rate Auditing)

## 📊 Visualizations & Chart References

### 1. Revenue & Pricing Outliers
![Boxplots](charts/boxplots.png)
*Used for identifying high end pricing and revenue outliers via the IQR method.*

### 2. Numeric Distributions
![Numeric Distributions](charts/numeric_distributions.png)
*Illustrates the spread and consistency of order sizes and quantities.*

### 3. Categorical Breakdowns
![Categorical Breakdowns](charts/categorical_breakdowns.png)
*Displays the balanced distribution across products, payment methods, and referral sources.*

### 4. Monthly Sales Trend
![Monthly Sales Trend](charts/monthly_sales_trend.png)
*Tracks monthly revenue movements over time to evaluate seasonality.*

### 5. Correlation Heatmap
![Correlation Heatmap](charts/correlation_heatmap.png)
*Highlights relationships between variables, showing a stronger correlation between total price and unit price than quantity.*

## 💡 Key Findings & Insights
* **Order & Quantity Distribution:** Order sizes are consistent and unskewed, with quantities ranging evenly from 1 to 5 per order, making mean-based metrics reliable.
* **Revenue Outliers:** `TotalPrice` contains 8 high-end outliers (orders above roughly $3,330, representing under 1% of total orders) that warrant manual review for bulk purchases, VIP customers, or pricing errors.
* **Diversified Channels:** Products, payment methods, and referral sources are evenly distributed, reflecting a healthy, diversified customer base not overly reliant on a single product or channel.
* **Revenue Leakage:** Approximately 1 in 5 orders (~21%, or 250 of 1,200 orders) are cancelled, marking a clear operational area to investigate for payment failures, stock issues, or customer friction.
* **Seasonality:** Monthly revenue moves without a repeating cyclical pattern, indicating no obvious high or low season based strictly on this dataset.
* **Revenue Drivers:** Total price correlates more strongly with unit price (0.72) than quantity (0.62), meaning product mix matters more to revenue than cart size. Laptops yield the highest average order revenue, while phones yield the lowest.

## 🚀 Strategic Recommendations
* **Audit Outliers:** Manually review the 8 high-value outlier orders to confirm transaction legitimacy and safeguard revenue tracking.
* **Investigate Cancellations:** Identify root causes behind the 21% cancellation rate to recover potential revenue leakage and improve order completion.
* **Optimize Product Mix:** Shift marketing and sales strategies toward higher-value products like laptops rather than focusing solely on increasing cart size quantities.

## 📁 Repository Files
* `main.py`: The underlying Python script used for data cleaning and preprocessing.
* `eda.py`: The exploratory data analysis script used to generate statistical metrics and visual outputs.
* `cleaned_Dataset_for_Data_Analytics.xlsx`: The final cleaned dataset utilized for analysis.
