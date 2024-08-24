# Flask Healthcare Application
*Final Project*

## Overview
This project is a web-based survey tool designed to collect user data for analyzing income spending in preparation for a new product launch in the healthcare industry. The application is built using Flask, MongoDB for data storage, and is deployed on Amazon Web Services (AWS).

## Features
- A web page hosted on AWS for access over the internet that collects user data including Age, Gender, Total Income, and Expenses across categories like utilities, entertainment, school fees, shopping, and healthcare.
- Data storage using MongoDB.
- Data processing using Python to create a CSV file from the collected data.
- Data visualization using Jupyter Notebook to show:
  1. Ages with the highest income.
  2. Gender distribution across spending categories.
- Ability to export the charts as PNG images for use in a PowerPoint presentation.

## Usage
#### Accessing the Web Page
The Hosted webpage can be accessed via this link [Data Collection Form](http://ec2-3-234-146-79.compute-1.amazonaws.com/)

#### Data Processing
- Collected data will be stored in MongoDB.
- Run the Python script ***data_processing.py*** to extract data from MongoDB and create a CSV file.

#### Visualization
- Executing the ***visualization.ipynb*** Jupyter notebook will load the CSV file and perform the following visualizations:
  1. Show the ages with the highest income.
  2. Show the gender distribution across spending categories.
  3. Export the charts as PNG images for use in PowerPoint.

## Interpretation of the Visualization
#### Ages with Highest Income
This visualization is a bar chart that displays the distribution of income across different age groups. Each bar represents a specific age, and the height of the bar corresponds to the average income of individuals in that age group. This analysis can inform decisions on which age demographics are most likely to afford and benefit from the new healthcare product. </br>
Key Insights generated are:
  1. **Peak Income Ages:** The chart may reveal that certain age groups have significantly higher incomes compared to others.
  2. **Target Age Groups:** These insights can help target marketing efforts towards age groups with higher incomes, as they might be more willing or able to spend on healthcare products. </br>
 
#### Gender Distribution Across Spending Categories
This visualization is a bar chart that compares the spending habits of different genders across various expense categories like shopping, healthcare, or entertainment. Understanding these patterns will allow the company to develop more focused strategies for promoting the new healthcare product to the most relevant demographic segments. </br>
Key Insights generated are:
  1. **Spending Patterns by Gender:** The chart may show that one gender spends more in certain categories, such as healthcare or shopping, than the other.
  2. **Category Preferences:** For instance, females have higher spending in entertainment and shopping, while males might allocate more towards entertainment or school fees.
  3. **Product Positioning:** These insights can help tailor the healthcare product to appeal to the gender with higher spending in the healthcare category, or adjust marketing strategies to better target each gender’s spending habits.

## Conclusion
This project successfully develops a web-based survey tool to collect and analyze user data for informed decision-making in the healthcare industry. By leveraging Flask for web development, MongoDB for data storage, and AWS for deployment, the application efficiently gathers and processes data on income and spending habits. The included visualizations provide valuable insights into age-related income trends and gender-based spending patterns, which can guide targeted marketing strategies for the upcoming healthcare product launch. With this tool, the company is well-equipped to understand its customer base and position the product effectively in the market.
