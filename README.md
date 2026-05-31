# customer_behaviour_analysis
Customer Shopping Behavior Analysis using Python, PostgreSQL, SQL, and Power BI. An end-to-end analytics project that explores customer purchasing patterns, product performance, customer satisfaction, discount impact, and shopping behavior through interactive dashboards and data-driven insights.
# Customer Shopping Behavior Analysis

## Overview

This project is an end-to-end Data Analytics solution that analyzes customer shopping behavior and purchasing patterns. The objective is to transform raw transactional data into meaningful business insights through data cleaning, exploratory analysis, SQL querying, and interactive dashboard visualization.

The project demonstrates the complete analytics workflow, including data preparation in Python, business analysis using SQL, dashboard development in Power BI, report creation, and presentation development using Gamma.

---

## Dataset

The dataset contains customer shopping transactions and behavioral information.

### Dataset Summary

| Metric         | Value |
| -------------- | ----- |
| Total Records  | 3,900 |
| Total Features | 18    |

### Key Data Categories

* Customer Information

  * Customer ID
  * Age
  * Gender
  * Location

* Product Information

  * Item Purchased
  * Category
  * Size
  * Color
  * Season

* Transaction Information

  * Purchase Amount
  * Previous Purchases
  * Frequency of Purchases
  * Payment Method
  * Shipping Type

* Customer Experience

  * Review Rating
  * Subscription Status
  * Discount Applied

* Derived Features

  * Age Group
  * Purchase Frequency Days

---

## Tools & Technologies

| Tool                            | Purpose                            |
| ------------------------------- | ---------------------------------- |
| Python (Pandas, NumPy)          | Data Cleaning & Analysis           |
| Jupyter Notebook                | Exploratory Data Analysis          |
| PostgreSQL / MySQL / SQL Server | Database Management & SQL Analysis |
| SQL                             | Business Queries & Insights        |
| Power BI                        | Interactive Dashboard Development  |
| Gamma                           | Project Presentation               |
| Microsoft Word                  | Project Documentation              |

---

## Project Workflow

### 1. Data Loading

* Imported dataset into Python
* Reviewed dataset structure and data types
* Performed initial data validation

### 2. Data Cleaning

* Handled missing values
* Standardized column names
* Removed redundant information
* Validated data consistency

### 3. Exploratory Data Analysis (EDA)

* Analyzed customer demographics
* Examined product performance
* Investigated purchasing behavior
* Evaluated customer satisfaction
* Studied discount usage patterns

### 4. Feature Engineering

Created additional analytical features:

* Age Group Classification
* Purchase Frequency Days

These features enabled deeper customer segmentation and behavioral analysis.

### 5. SQL Analysis

The cleaned dataset was loaded into a relational database and analyzed using SQL.

Key analyses included:

* Revenue Analysis
* Customer Segmentation
* Product Performance Analysis
* Discount Impact Analysis
* Customer Satisfaction Analysis
* Subscription Behavior Analysis

Example Business Questions:

* Which products generate the highest revenue?
* Do subscribed customers spend more?
* Which locations contribute most to revenue?
* How do discounts affect purchasing behavior?
* Which categories receive the highest customer ratings?

### 6. Dashboard Development

An interactive Power BI dashboard was developed to visualize business insights and support decision-making.

### 7. Reporting & Presentation

* Business report created to summarize findings
* Presentation developed using Gamma
* Dashboard screenshots and insights included

---

## Power BI Dashboard

### KPI Metrics

* Total Revenue
* Total Customers
* Average Purchase Value
* Average Review Rating

### Dashboard Sections

#### Sales & Revenue Analysis

* Revenue by Category
* Revenue by Location
* Top Purchased Products

#### Customer Behavior Analysis

* Purchase Frequency Analysis
* Customer Segmentation
* Discount Usage Analysis

#### Customer Satisfaction Analysis

* Review Rating by Category
* Review Rating by Shipping Type

### Interactive Features

* Dynamic Filters
* Top-N Analysis
* Cross-Filtering
* Drill-Down Capabilities

---

## Key Results

### Insights Discovered

* Clothing products generated the highest revenue.
* Frequent buyers demonstrated consistent spending behavior.
* Discounts significantly influenced customer purchasing decisions.
* Customer ratings remained consistently positive across categories.
* Revenue contributions were distributed across multiple customer age groups.

### Business Recommendations

* Focus marketing efforts on high-performing product categories.
* Strengthen customer retention through loyalty programs.
* Optimize discount strategies to improve profitability.
* Monitor customer feedback to enhance customer satisfaction.
* Invest in high-performing regions while improving underperforming markets.

---

## How to Run

### Prerequisites

Install the required Python libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

### Steps

1. Clone the repository

```bash
git clone <repository-url>
```

2. Open the Jupyter Notebook

```bash
jupyter notebook
```

3. Run the data cleaning and EDA scripts

4. Load the cleaned dataset into PostgreSQL, MySQL, or SQL Server

5. Execute SQL queries for business analysis

6. Open the Power BI report file (.pbix)

7. Refresh the data source

8. Explore the interactive dashboard

---

## Project Deliverables

* Cleaned Dataset
* Python EDA Notebook
* SQL Query Scripts
* Power BI Dashboard (.pbix)
* Business Report
* Gamma Presentation
* Project Documentation

---

## Conclusion

This project demonstrates a complete Data Analytics workflow, showcasing skills in data cleaning, exploratory data analysis, SQL querying, dashboard development, and business storytelling. The resulting insights help organizations better understand customer behavior, improve decision-making, and drive business growth.
