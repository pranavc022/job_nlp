from collections import Counter

def extract_keywords(sentence, num_keywords):
    # Tokenize the sentence into words
    words = sentence.split()

    # Count the occurrences of each word
    word_counts = Counter(words)

    # Get the most common keywords
    most_common_keywords = word_counts.most_common(num_keywords)

    # Extract the keywords from the most common word-count pairs
    keywords = [keyword for keyword, count in most_common_keywords]

    return keywords

# Example usage:
#sentence = "The quick brown fox jumps over the lazy dog. The dog barks loudly."

sentence = """  Reporting  Data Analysis  Business Analytics  Data Analytics  kpo
 SQL  NoSQL  R  Python  Scala  Data Visualization  Machine Learning  Data Science  Data Modeling  Algorithm
 Data Analysis  Data Analyst  reporting  Quality Control
 QlikView  Data Visualization  Tableau  MS SQL Server  Business Analysis  Business Intelligence  Data Warehousing  Power Bi  Data Modeling  Alteryx
 research analysis  cloud computing  machine learning  business intelligence
Java Hadoop Python C++ Spark Machine Learning NoSQL Oozie Big Data Languages
 analytics  python  data science
 Analyst  Product enhancement  Customer experience  e - Commerce  conversion
 SAS  Data Analytics  Statistics  Analytics
project management people management operations digital analytics data management supply chain management systems Machine learning SAS SQL VBA Tableau Qlik Spotfire
 MIS  Forecasting  Excel  Presentation Skills  coordinating skills
 Analyst  Research  Senior Research Analyst  KPO  Research Analyst
 Data analyst  Billing
 SAS  Hadoop  R  Hive  SQL  Machine Learning  Time Series  Big Data Analytics  Predictive Modeling  Statistics
 data warehouse  Tableau  ETL  SQL
 data extraction  process automation
 data mining  mapping  business intelligence  Data modeling  Statistical analysis  machine learning  Python  R  MATLAB
 SAS  Python  Analytics  Data Analytics  Statistics  Machine Learning  Data Modeling
market risk management sql Regulatory Repoting
 Data Analysis  Data Mining  Analytics  Advanced Excel
 Jenkins  Java  Hadoop  Javascript  JSON  Bash  Spark  Groovy  Play Framework  Python
 Business Intelligence  Excel Powerpoint  Business Analytics  Business Analyst  ms  office  Presentation  Business Analysis  Communication Skills  Business Planning  senior business analyst  Dashboards
 risk management  macros  data analytics  data  mis reporting  data mining  banking operations  cognos  dashboards  excel  vba  written communication  ibm  operational risk management  reporting tools  ms office  communication skills
 R  SAS  GCP  Cloud  Big Data  Machine Learning  AWS  Python
 mis  management information system
 Business Intelligence  SSAS  Big Data  SQL Server  Informatica  SSIS  Data Analytics  ETL  AWS  SQL
 SQL  Campaign Management  Email Marketing  SAS
 Machine Learning  Data Mining  Big Data  Data Science  Python  Data Management  Artificial Intelligence
 Deep Learning  Machine Learning  R  Python  Data Mining  Gradle  Subversion  Statistical Analysis  Design Analysis  Computer Science
 Data Science  Scala  Hadoop  Big Data  Spark  ETL  Machine Learning
 Deep Learning  R  SAS  SQL Queries  Data Science  Machine Learning  Data Mining  Logistic Regression  Statistical Programming  Data Visualization  SQL
 data science  machine learning  python  algorithms  java  data visualization  advanced analytics  data analysis  data mining  Eta  R  Network Optimization
 Analytics  Statistics  Data Management  Business Intelligence  Consumer Insights
 Data Science  NLP  Statistical Modeling  Data Analysis  Perl  Data Modeling  Machine Learning  Deep Learning  Analytics  Python
 Tableau  SQL  R  SAS  Python  Reporting Analyst  Technology
market analysis research analysis formulas trend analysis chemical engineering ms access international business analytical skills refinery operations database architecture LP modelling
 excel  data cleansing  vba  advanced excel  data visualization  data architecture  reporting tools
 MIS  Data Analysis  Advanced Excel
 machine learning  sql  python  r  hadoop  tableau  algorithms  analytics  customer segmentation  business intelligence  data analyst
 Secondary Research  Gartner  Industry Analysis  Quantitative  Market Analysis  Competitor Analysis  MS Office Tools  VB SCRIPT  Report Preparation  Global Hr
 algorithms  python  Problem Solving  machine learning  artificial intelligence  deep learning  software architecture  java  NLP  data modeling  data structures
 Microstrategy  System Administration  Business Intelligence  Production Support  Linux  Shell Scripting
 Data Entry  Data Analysis  analytics  data analytics  report  dashboard
 SQL  ETL  Pentaho  Talend  Informatica  Data Warehousing  Java  Data Science  Python  Data Quality
 SAS  Analytics  Statistics  Cross sell  segmentation  predictive modeling  logistic  regression  pd  EAD  LGD  arima  anova
 Data Science  Java  C  Algorithms  Data Structures  Machine Learning  AWS  Supply Chain  Python  SQL
 Data Science  Business Intelligence  Business Analytics
 data analysis  sql  advanced excel  pivot table  vlookup
Data Validation Customer Relationship Data Quality Negotiation Skills Relationship Management Data Management Business Objects Data Reporting SAP BI FICO
 MIS Preparation  Data Analysis  Advanced Excel
 Data Management  Hadoop  business analysis  Machine Learning  business intelligence  Deep Learning  Data Science  Data Visualization  Computer Vision  Python
advance sas sql python hive campaign management data analysis data analytics data mining ETL Testing ETL developer
SQL SAS Business intelligence Data modeling Data analysis MS Access Account management Schema Publishing data security
 Predictive Modeling  Pattern Recognition  R  Database Design  Data Visualization  Data Modeling  Machine Learning  Python  SQL
 analytics  data analytics  XML  data mining  Javascript  Data Analysis  Business Objects  SQL
 Data Analytics
 Analytics  Data Management  Data Analytics  Statistics  SAS
 Data Mining
 Data Management  Machine Learning  Data Mining  Scripting  Data Visualization  MongoDB  NoSQL  R  MATLAB
 Azure  SQL Database  Spark  HBase
 Data Analysis
 primary research  secondary research  handling client calls  Technology  Customization  Analysis  research analysis  Benchmarking  Research
 Social Media  Statistics
 data warehouse  Senior Consultant  Software  data Modelling  Data Integration  SQL  Testing
 MS Excel  Vlookup  MIS  Analysis  Cash handling  Payments  Reporting  Bank Reconciliation
 Procurement  Spend Analyst  Excel  SAP MM  Data Mining  Operations  Analytics  Ariba  SQL
 HR
 sql server  msbi
 Behavioural Skills  Excel  Computer Science  Problem Solving  Data Analysis  Data Cleansing  Business Operations  Data Collection  Data Analytics  Verbal Communication
 mcom  invoice processing  monthly reports  excel  mba finance  icwa inter  maintenance activities  client interaction  mba fresher  communication skills
 Logistic Regression  SVM  Machine Learning  Deep Learning  PCA
 Business Intelligence  Tableau  SQL  Analytics  Data Analytics  SAS  Statistics  Data Modeling  Consultant
 Biostatistics  Statistical Software  Excel Powerpoint  SAS  SQL  R  Project Management  MS Office Suite  Healthcare  Statistical Analysis  Python
 Artificial Intelligence  Machine Learning
SAS R Advanced Excel Digital Analytics Logistic Regression Statistical Modeling VBA Sales Segmentation Business Process
 Data Science  Data Management  Machine Learning  System Design  GPS
 R  Data Analyst  Data Analytics  Python  SQL
 Excel  Data Analysis  SAS  XML  Data Mining  SQL  Data Analytics  Statistics  Segmentation  Data Collection
 Data Analytics  Data Analyst  SQL  SAS  R  Google Analytics  Data Mining  Algorithm
 Presentation Skills  Business Solutions  Process Automation  Customer Experience  Excel Powerpoint  Business Operations  Advanced Excel  Strong Analytical Skills
 Excel  Social Media  Data Analysis
 Data Analysis
 Data Management
 SAS  Natural Language Processing  Big Data  Machine Learning  Deep Learning  SQL  R  Algorithms  Opencv  Spark  Computer Vision  Python
R Hive Segmentation Linear Regression Spark Tableau Machine Learning Statistics Deep Learning Python
 Excel  Data Enrichment  Data Management  Data Analytics
Sales Financial Services Auto Loans Home Loans Finance Banking Personal Loans HR Customer Service Orientation Credit Cards
 Monthly Reports  Balance sheet  Finance  general accounting  Data Quality  Reconciliation  Data Analysis  General Ledger  trial balance  Test Cases  Data extraction

"""

num_keywords = 150

# Extract the most occurring keywords
keywords = extract_keywords(sentence, num_keywords)

# Print the extracted keywords
print(keywords)
