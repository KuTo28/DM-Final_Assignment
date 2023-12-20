# FeedBack

## 1º Presentation

- Take care of NA's of Smoker status depending of the value from ECigaretteUsage.

### Questions 1

- Predict the possibility to have a mental dissorder.
- Identify which patient are mosre likely to have a heart attack.
- Classify U.S. citizens depending on their general health.

### Questions made by teachers 1

- How you have selected those variables to answer the questions? In order to choose we have to make data mining (correlation).
- Why have you converted some variables to factors? Why not make them binary?

## 2º Presentation

- HadHearthAttack is not a good variable because of the imbalances of it, so it's the target.
- They have created some variables using a combination of others.

### Questions 2

- How do mental and physical illness affect the probability of having a heart attack? Comparte how each type acts as a predictor

### Questions made by teachers 2

- For the numerical values why did you use the mean to get rid of the NA's. (Median better if there are a lot of outliers)
- What are you going to do with the ouliers? A solution could be to swap them for the heighest or lowest values.

## 3º Presentation

- Don't select the variables for the questions because you want.

### Questions 3

- Can having one disease make it more likely to have others?
- Is there any relation between depressive disorders and substance use and unhealthy habits?
- Is there any kind of influence by the state on the data?
- Is there a close relationship between COPD and other disease, smoking and some health problems?
- Is it better drinking or smoking? Are diseases related to drink or smoke?
- The importance of sports and weapons

## Questions made by teachers 3

## 4º Presentation

### Questions 4

- Can we predict the general health with the available data? (Which are the illness that affect more to healthier individuals)
- Which are the consequences of being vaccinated against tetanus?
- Which are the characteristics of people that had covid? (And the consequences).
- Is there any relation between the genetic race and the diseases of the individuals?

## Recommendations

- Obtain the accurracy of our prediction of Weight and Height
- Use percentages
- Look very carefully to the outliers of Weight and Height
- Make a graphic to count the number of observation in each BMI range
- Negative correlation between smoke/smoking/ecigaretts

## What needs to be in our presentation

### Dataset

- [x] Say the number of observations and columns
- [x] Show the total amount of NA's and not NA's (pie chart)
- [x] Distribution of NA's across columns
- [x] Distribution of number of NA's in a row in all the dataset (pie chart)
  - [x] Show max an lower bounds
  - Say we will remove observations that have more than "X" NA values (check the barplot to stimate what the threshold should be; Tough bellow 4 seems to be a nice aproach)

### How to handle NA's

We have thought of 3 options

- Use the mean and median for numeric variables
- Oversampling or undersampling
- Try to predict the numeric variables with NA's

We came to the conclusion to go for undersampling and try the prediction of the variables

- Show the accurracy of our prediction of Weight and Height

### Check outliers

After predicting and cleaning the NA's from our dataset we have to check for the outliers

- Make a boxplot for: (Weight, Height; we wont be using these so why plot it?), BMI, SleepHours, PhysicalHealthDays, MentalHealthDays
- Show the distribution using a boxplot

#### Handling the outliers

We hagled multiple options:

- Remove them
- Change them for the highest/lowest value of the whiskers
- Make clustering to group SleepHours, PhysicalHealthDays, MentalHealthDays
- Use zscore for normal distributions
- Checking medical standards

### Question

How likely a person is to have a disease?

### Why

Automatic triage. Able to filter by patient severity

### Preparing the data for our question

Because of our objective we need to reduce the amount of columns of the dataset, so we thought about merging some columns and categorizing some data (feature engineering)

#### Merging

- Grouping Height and Weight into BMI using it's formula (the NA's values were changed by the prediction made)
- HasSmoked -> SmokerStatus, ECigaretteUsage (show the correlation matrix)
- The variables that represent a difficulty for the people (by seeking the corr plot)

#### Target

whyy are we using these variables as our target

- Create a new numeric variable that sums all of them, making it a "diseaseRate" metric

#### Categorize

- AgeCategory (show it) (no consensus, just eyeball it)
- BMI (show it) (medical standard)
- TetanusLast10Tdap by having or not the vaccine (show it)
- HasSmoked by having or not smoked something in their lifes (show it)
- LastCheckupTime (show it)

### How do we plan to solve it?

yap about predictive models
