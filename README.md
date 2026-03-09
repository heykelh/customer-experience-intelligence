# Customer Experience Intelligence

## Overview
This project simulates a customer analytics use case in the insurance/banking sector.  
It combines survey data, customer complaints and transactional variables to generate actionable insights on customer experience and churn risk.

## Business objective
The goal is to:
- analyze customer feedback and complaint narratives
- detect key dissatisfaction drivers
- predict churn risk
- support better customer experience decisions

## Project workflow

1. Exploratory Data Analysis  
2. NLP on customer complaints  
3. Churn prediction modeling  
4. API deployment with FastAPI  
5. Dashboarding and business insights

## Tech stack
Python, SQL, Power BI, FastAPI, Scikit-learn, Pandas, Matplotlib

## Project structure

data/
notebooks/
src/
models/
api/
dashboard/
outputs/


## Exploratory Data Analysis

The notebook `01_data_exploration.ipynb` performs the initial exploration of the three main datasets used in the project:

- **Customer complaints**: complaint narratives and complaint metadata
- **Bank customers**: customer profile and churn-related variables
- **Customer survey**: NPS, satisfaction and customer effort indicators

### Objectives of the exploration

This step aims to:

- understand the structure and quality of the datasets
- identify key variables related to customer experience and churn
- detect potential patterns before building NLP and predictive models
- generate first business-oriented insights

### Main analyses performed

#### 1. Data loading and structure review
The notebook loads all datasets and checks:

- first rows of each dataset
- data types
- missing values
- overall consistency

This ensures the datasets are usable for downstream analysis and modeling.

#### 2. Churn distribution analysis
A count plot is used to visualize the distribution between retained and churned customers.

**Purpose:**  
Understand target imbalance and assess whether churn is a minority class.

**Business value:**  
Helps frame retention as a priority and prepares the modeling strategy.

#### 3. Age distribution
A histogram is created to explore customer age distribution.

**Purpose:**  
Identify the demographic structure of the customer base.

**Business value:**  
Can help detect whether some age groups may require more targeted retention strategies.

#### 4. Churn by activity status
A count plot compares churn levels between active and inactive customers.

**Purpose:**  
Measure the relationship between engagement and churn.

**Business value:**  
Shows whether inactive customers are more likely to leave, which can support engagement initiatives.

#### 5. Churn vs number of products
A boxplot is used to compare the number of products held by churned vs retained customers.

**Purpose:**  
Explore whether product ownership is associated with loyalty.

**Business value:**  
Supports cross-sell and customer retention thinking.

#### 6. NPS segmentation
Survey respondents are segmented into:

- **Promoters**
- **Passives**
- **Detractors**

A count plot visualizes the distribution of these categories.

**Purpose:**  
Introduce customer experience segmentation based on NPS.

**Business value:**  
Provides a first view of satisfaction structure and prepares analysis linking customer sentiment to churn risk.

#### 7. Complaint text exploration
The notebook examines the complaint narratives by:

- displaying sample verbatims
- measuring complaint text length
- plotting the distribution of text lengths

**Purpose:**  
Assess whether the textual content is rich enough for NLP analysis.

**Business value:**  
Confirms that complaint narratives contain usable customer voice data for sentiment and topic analysis.

#### 8. Top products with complaints
A bar chart shows the products generating the highest number of complaints.

**Purpose:**  
Identify the most complaint-prone product categories.

**Business value:**  
Highlights areas where customer journeys or operational processes may need improvement.

### Outputs produced

At the end of the notebook, cleaned datasets are exported for the next stages of the project:

- `data/processed/customers_clean.csv`
- `data/processed/survey_clean.csv`

These files will be reused in the NLP and churn modeling steps.

### Key takeaway

This exploratory analysis lays the foundation for the rest of the project by connecting:

- customer profile data
- experience metrics (NPS, satisfaction, effort)
- customer complaints and verbatims

It provides the first evidence that customer engagement, satisfaction and complaint behavior are likely linked to churn risk and customer experience performance.