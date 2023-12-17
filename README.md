# DM-Final_Assignment

## Variables

- Over 40 variables, so we're dealing with some curse of dimensionality
  - Apply feature engineering to reduce the amount of variables
- There are multiple boolean based variables. 24 to be exact
- Most of the variables contain `NaN` values -> what to do?

### Feature engineering

- Remove `HeightInMeters` and `WeightInKilograms` in favour to use BMI. use the formula to generate the missing values
  - We can further categorize its values using the BMI scale standard
- Merge `HadHeartAttack`, `HadAngina` and `HadStroke` into a single variable indicating cardiovascular health.
- Create `lifestyleScore` that ranks numericaly how well a person is living?
