# -*- coding: utf-8 -*-
"""loan-eligibility-prediction-machine-learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LNq3DY3Jhtu49gp8qimd45VO_M9W89zI

<div class='text-center'>
    <h1>🏧 Loan Eligibility Prediction 💰 using Machine Learning Models 🤖   </h1>
</div>

# Introduction

### In this notebook kernal, I'm going to predictions customers are eligible for the loan and check whether what are the missing criteria to know why customer not getting loan to make there own house.


<div class="text-success "><h4> We will learning about, Data Analysis Preprocess such as, </h4></div>

--- 

> ### Steps are:


1. [Gathering Data](#1)
- [Exploratory Data Analysis](#2)
- [Data Visualizations](#3)
- [Machine Learning Model Decision.](#4)
- [Traing the ML Model](#5)
- [Predict Model](#6)
- [Deploy Model](#7)



 
**Hope** you guys ****Love It**** and get a better **learning experience**.  🙏

<img align="center" src="https://www.rdccbank.com/uploads/loan-sub-types-template/housing-b.jpg" alt="House Loan" />

---

<div class="text-danger" >
    <h4>Let's Say, You are the owner of the <b>Housing Finance Company</b> and you want to build your own model to predict the customers are applying for the home loan and company want to check and validate the customer are eligible for the home loan.
    </h4>
</div>

# <div class="text-primary"> The Problem is,  </div>

### In a Simple Term, Company wants to make automate the Loan Eligibility Process in a real time scenario related to customer's detail provided while applying application for home loan forms.


You will use the training set to build your model, and the test set to validate it. Both the files are stored on the web as CSV files; their URLs are already available as character strings in the sample code.

First of all, we need to importing the necessary packages to work with the data to solve our problem

# Import Packages
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Show the Dataset Path to get detaset

import os

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

"""You can load this data with the `read_csv()` method from `pandas` package. It converts the data set to a python dataframe.

## Dataset Key Information.
  
---  
  
> - `Loan_ID`--------------> Unique Loan ID.
- `Gender`   --------------> Male/ Female 
- `Married`  --------------> Applicant married (Y/N) 
- `Dependents` ------------> Number of dependents 
- `Education` -------------> Applicant Education (Graduate/ Under Graduate) 
- `Self_Employed` ---------> Self-employed (Y/N) 
- `ApplicantIncome` -------> Applicant income 
- `CoapplicantIncome` -----> Coapplicant income 
- `LoanAmount`  -----------> Loan amount in thousands 
- `Loan_Amount_Term` ------> Term of a loan in months 
- `Credit_History` --------> Credit history meets guidelines 
- `Property_Area` ---------> Urban/ Semi-Urban/ Rural 
- `Loan_Status` -----------> Loan approved (Y/N)

<a id="1"></a><br>
# 1. Gathering Data
"""

#  Create New Variable and stores the dataset values as Data Frame

loan_train = pd.read_csv('/kaggle/input/loan-eligible-dataset/loan-train.csv')
loan_test = pd.read_csv('/kaggle/input/loan-eligible-dataset/loan-test.csv')

"""- Lets display the some few information from our large datasets

Here, We shows the first five rows from datasets
"""

loan_train.head()

"""- As we can see in the above output, there are too many columns, ( columns known as features as well. )

We can also use `loan_train` to show few rows from the first five and last five record from the dataset
"""

loan_train

"""> ### Here, we can see there are many rows and many columns, To know how many records and columns are available in our dataset, we can use the `shape` attribute or we can use `len()` to know how many records and how many features available in the dataset."""

print("Rows: ", len(loan_train))

"""Pandas has inbuild attribute to get all column from the dataset, With the help of this feature we can get the how many column available we have."""

print("Columns: ", len(loan_train.columns))

"""Also we can get the shape of the dataset using `shape` attribute"""

print("Shape : ", loan_train.shape)

"""> ### *After we collecting the data, Next step we need to understand what kind of data we have.*

### Also we can get the column as an list(array) from dataset

> **Note: DataFrame.columns returns the total columns of the dataset,
> Store the number of columns in variable `loan_train_columns`**
"""

loan_train_columns = loan_train.columns # assign to a variable
loan_train_columns # print the list of columns

"""### Now, Understanding the Data

- First of all we use the `loan_train.describe()` method to shows the important information from the dataset
- It provides the `count`, `mean`, `standard deviation (std)`, `min`, `quartiles` and `max` in its output.
"""

loan_train.describe()

"""#### As I said the above cell, this the information of all the methamatical details from dataset. Like `count`, `mean`, `standard deviation (std)`, `min`, `quartiles(25%, 50%, 75%)` and `max`.

> ### Another method is `info()`, This method show us the information about the dataset, Like

1. What's the type of culumn have?
- How many rows available in the dataset?
- What are the features are there?
- How many null values available in the dataset?
- Ans so on...
"""

loan_train.info()

"""As we can see in the output.

1. There are `614` entries
- There are total 13 features (0 to 12)
- There are three types of datatype `dtypes: float64(4), int64(1), object(8)`
- It's Memory usage that is, `memory usage: 62.5+ KB`
- Also, We can check how many missing values available in the `Non-Null Count` column

<a id="2"></a><br>
# 2. Exploratory Data Analysis

In this section, We learn about extra information about data and it's characteristics.

- First of all, We explore object type of data
So let's make a function to know how many types of values available in the column
"""

def explore_object_type(df ,feature_name):
    """
    To know, How many values available in object('categorical') type of features
    And Return Categorical values with Count.
    """    
    if df[feature_name].dtype ==  'object':
        print(df[feature_name].value_counts())

"""- After defined a function, Let's call it. and check what's the output of our created function."""

# Now, Test and Call a function for gender only
explore_object_type(loan_train, 'Gender')

"""- Here's one little issue occurred, Suppose in your datasets there are lots of feature to defined like this above code. """

# Solution is, Do you remember we have variable with name of `loan_train_columns`, Right,  let's use it
# 'Loan_ID', 'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area', 'Loan_Status'

for featureName in loan_train_columns:
    if loan_train[featureName].dtype == 'object':
        print('\n"' + str(featureName) + '\'s" Values with count are :')
        explore_object_type(loan_train, str(featureName))

"""> ## *Note: Your output maybe shorter or longer, It's totally depend upon your dataset's columns*

- We need to fill null values with `mean` and `median` using `missingno` package
"""

import missingno as msno

# list of how many percentage values are missing
loan_train

loan_train.isna().sum()
# round((loan_train.isna().sum() / len(loan_train)) * 100, 2)

msno.bar(loan_train)

msno.matrix(loan_train )

"""- As we can see here, there are too many columns missing with small amount of null values so we use `mean` amd `mode` to replace with `NaN` values."""

loan_train['Credit_History'].fillna(loan_train['Credit_History'].mode(), inplace=True) # Mode
loan_test['Credit_History'].fillna(loan_test['Credit_History'].mode(), inplace=True) # Mode


loan_train['LoanAmount'].fillna(loan_train['LoanAmount'].mean(), inplace=True) # Mean
loan_test['LoanAmount'].fillna(loan_test['LoanAmount'].mean(), inplace=True) # Mean

"""### # convert Categorical variable with Numerical values.

`Loan_Status` feature boolean values, So we replace `Y` values with `1` and `N` values with `0`
and same for other `Boolean` types of columns
"""

loan_train.Loan_Status = loan_train.Loan_Status.replace({"Y": 1, "N" : 0})
# loan_test.Loan_Status = loan_test.Loan_Status.replace({"Y": 1, "N" : 0}) 

loan_train.Gender = loan_train.Gender.replace({"Male": 1, "Female" : 0})
loan_test.Gender = loan_test.Gender.replace({"Male": 1, "Female" : 0})

loan_train.Married = loan_train.Married.replace({"Yes": 1, "No" : 0})
loan_test.Married = loan_test.Married.replace({"Yes": 1, "No" : 0})

loan_train.Self_Employed = loan_train.Self_Employed.replace({"Yes": 1, "No" : 0})
loan_test.Self_Employed = loan_test.Self_Employed.replace({"Yes": 1, "No" : 0})

loan_train['Gender'].fillna(loan_train['Gender'].mode()[0], inplace=True)
loan_test['Gender'].fillna(loan_test['Gender'].mode()[0], inplace=True)

loan_train['Dependents'].fillna(loan_train['Dependents'].mode()[0], inplace=True)
loan_test['Dependents'].fillna(loan_test['Dependents'].mode()[0], inplace=True)

loan_train['Married'].fillna(loan_train['Married'].mode()[0], inplace=True)
loan_test['Married'].fillna(loan_test['Married'].mode()[0], inplace=True)

loan_train['Credit_History'].fillna(loan_train['Credit_History'].mean(), inplace=True)
loan_test['Credit_History'].fillna(loan_test['Credit_History'].mean(), inplace=True)

"""* Here, `Property_Area`, `Dependents` and `Education` has multiple values so now we can use `LabelEncoder` from `sklearn` package"""

from sklearn.preprocessing import LabelEncoder
feature_col = ['Property_Area','Education', 'Dependents']
le = LabelEncoder()
for col in feature_col:
    loan_train[col] = le.fit_transform(loan_train[col])
    loan_test[col] = le.fit_transform(loan_test[col])

"""> ### Finally, We have all the features with numerical values,

<a id="3"></a><br>
# 3. Data Visualizations


In this section, We are showing the visual information from the dataset, For that we need some pakages that are `matplotlib` and `seaborn`
"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline


import seaborn as sns
sns.set_style('dark')

loan_train

loan_train.plot(figsize=(18, 8))

plt.show()

plt.figure(figsize=(18, 6))
plt.subplot(1, 2, 1)


loan_train['ApplicantIncome'].hist(bins=10)
plt.title("Loan Application Amount ")

plt.subplot(1, 2, 2)
plt.grid()
plt.hist(np.log(loan_train['LoanAmount']))
plt.title("Log Loan Application Amount ")

plt.show()

plt.figure(figsize=(18, 6))
plt.title("Relation Between Applicatoin Income vs Loan Amount ")

plt.grid()
plt.scatter(loan_train['ApplicantIncome'] , loan_train['LoanAmount'], c='k', marker='x')
plt.xlabel("Applicant Income")
plt.ylabel("Loan Amount")
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(loan_train['Loan_Status'], loan_train['LoanAmount'])
plt.title("Loan Application Amount ")
plt.show()

plt.figure(figsize=(12,8))
sns.heatmap(loan_train.corr(), cmap='coolwarm', annot=True, fmt='.1f', linewidths=.1)
plt.show()

"""In this heatmap, we can clearly seen the relation between two variables

<a id="4"></a><br>
# 4. Choose ML Model.

* In this step, We have a lots of Machine Learning Model from sklearn package, and we need to decide which model is give us the better performance. then we use that model in final stage and send to the production level.
"""

# import ml model from sklearn pacakge

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score

"""First of all, we are use `LogisticRegression` from `sklearn.linear_model` package. Here is the little information about `LogisticRegression`.

`Logistic Regression` is a **classification algorithm**. It is used to predict a binary outcome (`1 / 0`, `Yes / No`, and `True / False`) given a set of independent variables. To represent binary / categorical outcome, we use dummy variables. You can also think of logistic regression as a special case of linear regression when the outcome variable is categorical, where we are using log of odds as the dependent variable.

![](https://www.analyticsvidhya.com/wp-content/uploads/2015/10/logit.png)

* Let's build the model
"""

logistic_model = LogisticRegression()

"""<a id="5"></a><br>
# 5. Traing the ML Model

> ### **Before fitting the model, We need to decide how many feature are available for testing and training, then after complete this step. fitt the model** 

Currently, we are using `Credit_History', 'Education', 'Gender` features for training so let's create train and test variables
"""

train_features = ['Credit_History', 'Education', 'Gender']

x_train = loan_train[train_features].values
y_train = loan_train['Loan_Status'].values

x_test = loan_test[train_features].values

logistic_model.fit(x_train, y_train)



"""<a id="6"></a><br>
# 6. Predict Model
"""

# Predict the model for testin data

predicted = logistic_model.predict(x_test)

# check the coefficeints of the trained model
print('Coefficient of model :', logistic_model.coef_)

# check the intercept of the model
print('Intercept of model',logistic_model.intercept_)

# Accuray Score on train dataset
# accuracy_train = accuracy_score(x_test, predicted)
score = logistic_model.score(x_train, y_train)
print('accuracy_score overall :', score)
print('accuracy_score percent :', round(score*100,2))

# predict the target on the test dataset
predict_test = logistic_model.predict(x_test)
print('Target on test data',predict_test)

"""<a id="7"></a><br>
# 7. Deploy Model

- Finally, we are done so far. The last step is to deploy our model in production map. So we need to export our model and bind with web application API. 

Using pickle we can export our model and store in to `logistic_model.pkl` file, so we can ealy access this file and calculate customize prediction using Web App API.


#### A little bit information about pickle:

`Pickle` is the standard way of serializing objects in Python. You can use the pickle operation to serialize your machine learning algorithms and save the serialized format to a file. Later you can load this file to deserialize your model and use it to make new predictions


>>  Here is example of the Pickle export model



```
model.fit(X_train, Y_train)
# save the model to disk
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))

# some time later...

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, Y_test)
print(result)
```
"""

import pickle as pkl

# save the model to disk
filename = 'logistic_model.pkl'
pkl.dump(logistic_model, open(filename, 'wb')) # wb means write as binary

"""### Now, You can check your current directory. You can see the file with named "logistic_model.pkl"

- To read model from file

```
# load the model from disk
loaded_model = pkl.load(open(filename, 'rb')) # rb means read as binary
result = loaded_model.score(X_test, Y_test)

```

--- 
---

<div class="text-center">
    <h1>That's it Guys,</h1>
    <h1>🙏</h1>
    
        
        I Hope you guys you like and enjoy it, and learn something interesting things from this notebook, 
        
        Even I learn a lots of things while I'm creating this notebook
    
        Keep Learning,
        Regards,
        Vikas Ukani.
    
</div>

---
---

<img src="https://static.wixstatic.com/media/3592ed_5453a1ea302b4c4588413007ac4fcb93~mv2.gif" align="center" alt="Thank You" style="min-height:20%; max-height:20%" width="90%" />
"""