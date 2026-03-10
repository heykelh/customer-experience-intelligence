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

## NLP Analysis on Customer Complaints

The notebook `02_nlp_analysis.ipynb` focuses on extracting structured insights from unstructured customer complaint narratives.

In many financial institutions, customer feedback is collected through multiple channels such as complaints, surveys and service interactions. These verbatim messages contain valuable information about customer dissatisfaction, operational issues and service failures.

The objective of this notebook is to transform these raw textual complaints into structured signals that can support customer experience monitoring and future predictive modeling.

### Objectives

The NLP analysis aims to:

- explore the structure and richness of customer complaint narratives
- clean and preprocess textual data for analysis
- quantify customer dissatisfaction through sentiment analysis
- identify recurring complaint themes through topic modeling
- transform textual information into structured features usable for analytics and machine learning

This step simulates how organizations can leverage **Voice of Customer (VoC)** data to better understand customer pain points.

---

### Dataset

The analysis uses a sample extracted from the **Consumer Financial Protection Bureau complaint dataset**, which contains real customer complaints submitted to financial institutions.

Each complaint includes:

- the product involved
- the issue category
- the company concerned
- the location
- the date of the complaint
- the complaint narrative written by the customer

The key column analyzed in this notebook is:
complaint_text

which represents the verbatim description of the customer's problem.

---

### Text Preprocessing

Before applying NLP techniques, the complaint narratives are cleaned and standardized.

The preprocessing pipeline includes:

- conversion to lowercase
- removal of punctuation and numeric characters
- removal of stopwords
- tokenization of the text
- removal of very short tokens

This step ensures that the textual data becomes consistent and suitable for further analysis.

A cleaned version of each complaint narrative is stored in a new variable:
clean_text

This processed text is used for all downstream NLP tasks.

---

### Complaint Text Exploration

The notebook first analyzes the structure of the complaint narratives.

This includes:

- displaying sample verbatim complaints
- measuring the length of complaint texts
- visualizing the distribution of text length

These analyses confirm that the complaint narratives contain sufficient detail to perform meaningful NLP analysis.

Understanding text length distribution is important because longer complaints often contain more contextual information about customer issues.

---

### Sentiment Analysis

To quantify the emotional tone of customer complaints, the notebook applies **VADER sentiment analysis**, a lexicon-based method designed for analyzing short texts.

Each complaint is assigned a **sentiment score** representing the polarity of the message.

From this score, a categorical sentiment label is derived:

- **positive**
- **neutral**
- **negative**

This allows us to quantify dissatisfaction levels across the dataset.

Sentiment analysis provides a measurable signal of customer frustration, which can later be integrated into predictive models such as churn prediction.

---

### Frequent Term Analysis

The notebook then identifies the most frequently occurring words in complaint narratives.

This is done using a **CountVectorizer**, which converts textual data into a numerical representation based on word frequencies.

A bar chart of the most frequent terms helps highlight recurring concepts present in customer complaints.

These frequent terms often reveal the operational areas where customers encounter difficulties, such as:

- payment issues
- account servicing problems
- delays or errors in processing
- customer support interactions

This type of analysis helps organizations quickly identify common friction points in customer journeys.

---

### Topic Modeling

To better structure the complaint narratives, the notebook applies **Latent Dirichlet Allocation (LDA)** topic modeling.

Topic modeling allows the system to automatically group complaints into a small number of recurring themes.

Each topic represents a cluster of related terms frequently appearing together in complaints.

Examples of potential topics may include:

- payment or billing issues
- credit reporting disputes
- customer service communication problems
- loan servicing concerns
- unexpected fees or account actions

Each complaint is then assigned a **dominant topic**, which represents the primary issue category for that complaint.

This step transforms unstructured text into structured, interpretable categories that can be used by business teams.

---

### Topic Distribution Analysis

The notebook visualizes the distribution of dominant complaint topics across the dataset.

This allows analysts to understand:

- which types of issues appear most frequently
- which operational domains generate the highest volume of complaints

Such insights are valuable for prioritizing operational improvements and monitoring customer experience performance.

---

### Topic Interpretation

To make the results interpretable, the notebook prints sample complaints associated with each topic.

This step allows analysts to manually interpret the meaning of each topic and translate it into business categories.

For example:

- payment delays
- loan servicing issues
- customer support problems
- unexpected account fees

This interpretation step is critical because topic modeling alone produces statistical clusters that must be translated into meaningful business insights.

---

### Feature Engineering for Downstream Analytics

The notebook converts textual information into structured variables that can be reused in later modeling steps.

The following features are created:

- **clean_text**: processed version of complaint narrative
- **text_length**: length of complaint text
- **sentiment_score**: quantitative sentiment score
- **sentiment_label**: positive / neutral / negative sentiment category
- **dominant_topic**: topic cluster assigned by the LDA model

These features transform qualitative customer feedback into measurable signals.

---

### Output Dataset

The enriched dataset is exported for later use in the project:
data/processed/complaints_nlp_features.csv

This dataset contains the original complaint information along with the newly engineered NLP features.

---

### Key Insights

This analysis demonstrates that customer complaint narratives contain valuable signals about customer dissatisfaction and operational issues.

The key outcomes of this step are:

- customer complaints contain rich textual information that can be analyzed using NLP
- sentiment analysis allows quantification of dissatisfaction levels
- topic modeling helps group complaints into interpretable issue categories
- textual feedback can be transformed into structured variables usable for analytics and predictive models

These insights illustrate how **Voice of Customer data can be leveraged to support customer experience monitoring and decision-making**.

---

### Role in the Overall Project

This NLP step plays a key role in the overall project architecture.

It enables the transformation of qualitative customer feedback into structured features that can complement:

- customer profile data
- transactional data
- survey-based satisfaction metrics

These combined signals can then be used to better understand customer behavior and support churn prediction or experience improvement initiatives.

## Churn Prediction Modeling

The notebook `03_churn_modeling.ipynb` focuses on building a predictive model to estimate customer churn risk based on customer profile data and customer experience indicators.

Customer churn represents a major challenge for financial institutions, as acquiring new customers is often significantly more expensive than retaining existing ones. Being able to identify customers at risk of leaving allows organizations to proactively improve retention strategies and customer experience.

The goal of this notebook is to simulate how customer data and experience metrics can be combined to build a churn prediction model that supports business decision-making.

---

### Objectives

The modeling step aims to:

- combine multiple data sources to build a unified analytical dataset
- engineer customer experience features relevant to churn behavior
- train and evaluate predictive machine learning models
- identify the key drivers behind customer churn
- generate churn risk scores usable for customer segmentation

This step illustrates how machine learning can support **customer retention strategies and customer journey improvements**.

---

### Data Sources

The modeling dataset combines two sources of information:

**1. Customer profile dataset**

This dataset contains customer attributes such as:

- credit score
- geography
- gender
- age
- tenure
- account balance
- number of products owned
- credit card ownership
- activity status
- estimated salary

It also contains the target variable:
Exited

which indicates whether a customer has churned.

---

**2. Customer experience survey dataset**

This dataset simulates customer experience metrics typically collected through surveys or feedback systems.

It includes:

- **NPS score** (Net Promoter Score)
- **Customer Effort Score**
- **Satisfaction score**
- **Interaction channel**
- **Complaint flag**

These variables represent signals related to customer perception and service experience.

---

### Dataset Integration

To simulate a realistic analytical workflow, both datasets are merged into a unified modeling dataset.

A synthetic `customer_id` is created to align both sources.

The resulting dataset combines:

- customer profile information
- customer engagement indicators
- customer experience metrics

This multi-source dataset reflects how organizations combine operational data and Voice of Customer signals for analytics.

---

### Feature Engineering

Additional business-oriented features are created to improve model interpretability.

Examples include:

**NPS segmentation**

Customers are categorized based on their NPS score:

- Promoters
- Passives
- Detractors

This segmentation reflects how companies monitor customer advocacy and loyalty.

---

**Customer satisfaction indicators**

Two additional indicators are derived:

- **Low satisfaction flag**  
  Identifies customers reporting very low satisfaction levels.

- **High effort flag**  
  Identifies customers experiencing high friction in their interactions.

These variables capture customer journey friction signals.

---

### Modeling Approach

The churn prediction task is formulated as a **binary classification problem**, where the objective is to predict whether a customer will churn.

Two machine learning models are implemented:

**Logistic Regression**

A baseline model that provides interpretable results and helps understand linear relationships between variables and churn risk.

**Random Forest**

A tree-based ensemble model capable of capturing non-linear relationships and complex feature interactions.

Both models are implemented using **Scikit-learn pipelines**, which integrate:

- preprocessing
- feature transformation
- model training

This approach ensures reproducibility and proper handling of data transformations.

---

### Data Preprocessing

Before training the models, several preprocessing steps are applied.

**Numerical variables**

- missing value imputation using median strategy
- feature scaling using standardization

**Categorical variables**

- missing value imputation using most frequent values
- encoding using one-hot encoding

These transformations are implemented using a **ColumnTransformer pipeline**, ensuring that preprocessing steps are consistently applied during training and prediction.

---

### Model Training and Evaluation

The dataset is split into training and testing sets using a stratified split to preserve the churn distribution.

Models are evaluated using several performance metrics:

- **Accuracy**
- **Precision**
- **Recall**
- **F1-score**
- **ROC AUC**

A **confusion matrix** is also generated to analyze prediction errors.

Additionally, a **ROC curve** is plotted to visualize the model's ability to distinguish between churn and non-churn customers.

These evaluation methods provide a balanced view of model performance.

---

### Model Comparison

The performance of Logistic Regression and Random Forest models is compared using a summary table and visual comparison charts.

This comparison helps determine which modeling approach provides the best predictive performance while balancing interpretability.

In many real-world customer analytics use cases, both model accuracy and interpretability are important factors when selecting a production model.

---

### Feature Importance Analysis

To better understand the drivers behind churn predictions, feature importance analysis is performed using the Random Forest model.

This analysis highlights which variables contribute the most to predicting customer churn.

Typical drivers identified in such analyses include:

- customer engagement (activity status)
- relationship depth (number of products owned)
- satisfaction indicators
- customer effort
- complaint exposure

This step is essential because predictive models should not only provide predictions but also generate insights that support business decisions.

---

### Churn Risk Scoring

Using the trained model, a **churn probability score** is computed for each customer.

This score represents the estimated probability that a customer will churn.

Customers are then segmented into risk groups:

- **Low risk**
- **Medium risk**
- **High risk**

This segmentation simulates how organizations prioritize retention actions and customer outreach.

For example:

- high-risk customers may receive proactive support
- medium-risk customers may receive engagement campaigns
- low-risk customers require standard monitoring

---

### Output Datasets

The modeling results are exported for further use in the project.

The following files are generated:
data/processed/churn_scored_customers.csv

This dataset contains:

- the original customer attributes
- the predicted churn probability
- the predicted churn class
- the churn risk segment

Additional outputs include:
outputs/tables/model_comparison.csv
outputs/tables/feature_importance.csv

These tables summarize model performance and feature importance.

---

### Model Persistence

The final trained model is saved for reuse in later stages of the project.
models/churn_model.pkl

This saved model can be used for:

- API deployment
- real-time scoring
- integration into analytics pipelines

---

### Key Insights

The churn modeling analysis highlights the importance of combining **customer behavior data and customer experience signals** to better understand churn risk.

Key takeaways include:

- customer engagement plays a strong role in retention
- customers with fewer products tend to churn more frequently
- satisfaction and effort metrics provide valuable predictive signals
- complaint exposure may indicate elevated churn risk

These findings illustrate how customer analytics can help organizations move from reactive churn analysis to proactive customer retention strategies.

---

### Role in the Overall Project

This modeling step integrates the different analytical components developed throughout the project:

- exploratory data analysis
- customer experience metrics
- NLP analysis of customer complaints

Together, these elements demonstrate how organizations can transform raw customer data into actionable insights that support both operational improvements and strategic decision-making.

## FastAPI Deployment

To simulate model industrialization, the project includes a FastAPI application that exposes the churn model as a scoring service.

The API is implemented in:

`api/app.py`

### Objective

The goal of this API is to demonstrate how a trained churn prediction model can be operationalized and reused outside a notebook environment.

Instead of limiting the model to offline analysis, this component makes it possible to score individual customer profiles through a simple HTTP endpoint.

This reflects a real-world use case where predictive models are integrated into business tools, internal applications or decision-support workflows.

### Features

The API provides:

- a root endpoint to verify that the service is running
- a `/predict` endpoint for customer churn scoring
- automatic API documentation through Swagger UI

### Input variables

The `/predict` endpoint accepts a customer profile containing:

- customer financial and demographic variables
- engagement indicators
- customer experience metrics such as NPS, effort and satisfaction
- complaint exposure
- interaction channel

Additional business features are automatically derived inside the API, including:

- NPS category
- low satisfaction flag
- high effort flag

### Output

The API returns:

- `churn_probability`: estimated probability of churn
- `predicted_churn`: predicted churn class
- `risk_segment`: low / medium / high risk segment

This output makes the prediction easier to interpret from a business perspective.

### Example usage

Once the API is running locally with Uvicorn, the interactive documentation is available at:

`/docs`

This interface can be used to test the prediction endpoint with custom customer inputs.

### Business value

This API demonstrates the transition from model development to model operationalization.

It shows how churn prediction can be turned into a reusable service that supports:

- customer risk scoring
- retention prioritization
- integration into downstream tools or dashboards

This component strengthens the project by adding a product-oriented and industrialization dimension beyond notebook-based analysis.

## Power BI Dashboard

A Power BI dashboard was built to translate churn model outputs into actionable business insights.

It highlights how customer experience indicators such as satisfaction, NPS and interaction channels influence churn risk and retention.

The dashboard includes:

- overall churn KPIs
- customer risk segmentation
- churn analysis by experience indicators
- interaction channel analysis

📊 Full dashboard explanation:

➡️ [Dashboard documentation](dashboard/dashboard_insights.md)