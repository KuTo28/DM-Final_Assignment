# Data Mining Final Project

**GROUP 2: CLAUDE SHANNON**

---

## Authors

- Garri Romzova, Antonio
- Mayol Matos, Sergi
- Medina Perelló, Alejandro
- Palmer Perez, Ruben
- Rodríguez Arguimbau, Alejandro

---

## Index

1. Dataset
2. Objective
3. Considerations left behind
4. Conclusions

---

# Dataset

_An exploratory introduction_

---

## Context

Medical data around the US regarding health metrics

---

## Observations

**Over 400k**

_counting duplicated data_

---

## Variables

Most of them are categorical or _Boolean_, e.g.

- `HadSkinCancer`
- `HadDepressiveDisorder`
- `SmokerStatus`
- Etc

---

Only six variables are numeric:

- `PhysicalHealthDays`
- `MentalHealthDays`
- `SleepHours`
- `HeightInMeters`
- `WeightInKilograms`
- `BMI`

---

## Missing data

![](img/nan_values.png)

---

# Objective

_A common goal_

---

## Predictive model

with `HadHeartAttack` as our target

---

## Problem

Large amount of variables

---

## Solution

---

# Data modifications

_To use the least amount of variables_

---

## Observation removal limit

**15%** of the original dataset

_~ 66k_

---

## BMI

Remove `Height` and `Weight` variables and fill non-numeric values on `BMI` applying

$$BMI=\frac{Weight}{Height^2}$$

---

| **Classification** | **BMI Score** |
| ------------------ | ------------- |
| Underweight        | < 18.5        |
| Normal             | 18.5 - 24.9   |
| Overweight         | 25.0 - 29.0   |
| Obese              | 30.0 - 40.0   |
| Extreme Obese      | > 40.0        |

---

## How to fill missing data

- Predictive models
- Median
- Mean
- Remove

---

## Outliers

IQR

$$X<(Q1​−1.5 \times IQR)$$

Or

$$X>(Q3​+1.5 \times IQR)$$

_best for unknown or non-normal distributed data_

---

Z-score

$$\left| \frac{{X - \text{mean}(X)}}{{\text{sd}(X)}} \right| > 3 $$

_best for normal distributed data_

---

## Variable reduction

- Random Forest
- XGBoost

_at least explain 95% of the data_

---

# Simple questions

---

## Age distribution

![](img/age_dist.png)

---

## BMI

![](img/bmi_dist.png)

---

## Heart attack per state

![](img/states_ha_bmi.png)
---

# Conclusions

---
