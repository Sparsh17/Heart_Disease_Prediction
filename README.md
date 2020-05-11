# Heart_Disease_Prediction

Heart disease describes a range of conditions that affect your heart. Diseases under the heart disease umbrella include blood vessel diseases, such as coronary artery disease, heart rhythm problems (arrhythmias) and heart defects you’re born with (congenital heart defects), among others.
The term “heart disease” is often used interchangeably with the term “cardiovascular disease”. Cardiovascular disease generally refers to conditions that involve narrowed or blocked blood vessels that can lead to a heart attack, chest pain (angina) or stroke. Other heart conditions, such as those that affect your heart’s muscle, valves or rhythm, also are considered forms of heart disease.
Among various life-threatening diseases, heart disease has garnered a great deal of attention in medical research. The diagnosis of heart disease is a challenging task, which can offer automated prediction about the heart condition of patient so that further treatment can be made effective. The diagnosis of heart disease is usually based on signs, symptoms and physical examination of the patient. There are several factors that increase the risk of heart disease, such as body cholesterol level, family history of heart disease, high blood pressure, maximum heart rate achieved and lack of physical exercise.


The main objective of this study is to build a model that can predict the heart disease occurrence.

# Dataset Description:

This data set currently contains 303 instances.

Features information:

1.age - age in years

2.sex - sex(1 = male; 0 = female)

3.chest_pain - chest pain type (1 = typical angina; 2 = atypical angina; 3 = non-anginal pain; 4 = asymptomatic)

4.blood_pressure - resting blood pressure (in mm Hg on admission to the hospital)

5.serum_cholestoral - serum cholestoral in mg/dl

6.fasting_blood_sugar - fasting blood sugar > 120 mg/dl (1 = true; 0 = false)

7.electrocardiographic - resting electrocardiographic results (0 = normal; 1 = having ST-T; 2 = hypertrophy)

8.max_heart_rate - maximum heart rate achieved

9.induced_angina - exercise induced angina (1 = yes; 0 = no)

10.ST_depression - ST depression induced by exercise relative to rest

11.slope - the slope of the peak exercise ST segment (1 = upsloping; 2 = flat; 3 = downsloping)

12.no_of_vessels - number of major vessels (0-3) colored by flourosopy

13.thal - 3 = normal; 6 = fixed defect; 7 = reversable defect

14.num:diagnosis - the predicted attribute - diagnosis of heart disease 

# Requirements

Libraries Used:

1. Numpy

2. Pandas

3. PyQt5

4. sklearn

5. sqlite3

# How to Run the Project:

1. First, install all the libraries mentioned above.
2. Now, run the Heart_Disease_Prediction.py file.


# Introduction to Machine Learning
Machine learning is an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. Machine learning focuses on the development of computer programs that can access data and use it learn for themselves

# Logistic Regression

In this project, Logistic regression is used.

Logistic regression is a supervised learning classification algorithm used to predict the probability of a target variable. The nature of target or dependent variable is dichotomous, which means there would be only two possible classes.

In simple words, the dependent variable is binary in nature having data coded as either 1 (stands for success/yes) or 0 (stands for failure/no).

# Implementing Logistic Regression :
We are going to cover this model building exercise in the following steps:
1. Reading Data
2. Analyzing Data(Basic EDA/Descriptive analysis)
3. Train and Test(Break the sample data into two sets)
4. Accuracy Report(Measuring the model performance using confusion matrix we discussed above )

  Main Objective : To predict heart disease using Logistic Regression Classifier.



