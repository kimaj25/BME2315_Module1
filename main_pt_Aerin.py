#Name: Aerin Kim
#Date: 9/16/26
#Generative AI Statement: This assignment was assisted by ChatGPT-5.6 Luna on September 16, 2026. ChatGPT-5.6 Luna was used to explain the following concepts: class methods, instance methods, and how to create a class that can read data from a CSV file and create objects based on that data. I used the explanations provided by ChatGPT-5.6 Luna to help me understand these concepts and apply them to my code. The work from the class example was also applied here.


from patient_Aerin import *
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import statistics
import pandas as pd
from sklearn.linear_model import LinearRegression


# CREATE PATIENT OBJECTS FROM CSV FILE
#-----------------------------------------------

Patient.instantiate_from_csv(
    "C:/Users/aerin/OneDrive/Desktop/COMP BME 2315 Fall 2026/"
    "Module 1/BME2315_Module 1/BME2315_Module1/"
    "Metadata and Protein Data for Module 1.csv"
)


# PRINT NUMBER OF PATIENTS
#-----------------------------------------------

print(f"Number of patients = {len(Patient.all_patients)}")


# PRINT ONE PATIENT AS AN EXAMPLE
#-----------------------------------------------

print("\nExample patient:")
print(Patient.all_patients[0])



# SORT PATIENTS BY YEARS OF EDUCATION
#-----------------------------------------------

# Sort the list of all patients in ascending order
# based on their years of education.

Patient.all_patients.sort(
    key=lambda patient: patient.years_education,
    reverse=False
)

print("\nPatients sorted by Years of Education:")

for patient in Patient.all_patients:
    print(patient)


# FILTER PATIENTS
# Severe Atherosclerosis + Female + Dementia
#-----------------------------------------------

severe_female_dementia = Patient.filter(
    Patient.all_patients,
    sex="Female",
    cognitive_status="Dementia",
    atherosclerosis="Severe"
)

print("\nSevere Atherosclerosis Female Patients with Dementia:")

for patient in severe_female_dementia:
    print(patient)

print(
    f"\nNumber of severe atherosclerosis female patients "
    f"with dementia = {len(severe_female_dementia)}"
)

# BAR GRAPH
# Age of Onset of Symptoms:
# Female vs. Male Patients with Dementia
#-----------------------------------------------

# Filter for female patients with dementia

female_dementia = Patient.filter(
    Patient.all_patients,
    sex="Female",
    cognitive_status="Dementia"
)

# Filter for male patients with dementia

male_dementia = Patient.filter(
    Patient.all_patients,
    sex="Male",
    cognitive_status="Dementia"
)


# Create empty lists

female_age_onset = []
male_age_onset = []


# Add age of onset values to the lists

for patient in female_dementia:
    if patient.age_onset is not None:
        female_age_onset.append(patient.age_onset)

for patient in male_dementia:
    if patient.age_onset is not None:
        male_age_onset.append(patient.age_onset)


# Calculate means

female_mean = statistics.mean(female_age_onset)
male_mean = statistics.mean(male_age_onset)


# Calculate standard deviations

female_stdev = statistics.stdev(female_age_onset)
male_stdev = statistics.stdev(male_age_onset)


# Print means and standard deviations

print("\nAge of Onset in Dementia Patients:")

print(
    f"Female mean = {female_mean}, "
    f"Female standard deviation = {female_stdev}"
)

print(
    f"Male mean = {male_mean}, "
    f"Male standard deviation = {male_stdev}"
)


# Define graph information

sex_labels = ["Female", "Male"]

mean_age_onset = [
    female_mean,
    male_mean
]

stdev_age_onset = [
    female_stdev,
    male_stdev
]


# T-TEST FOR BAR GRAPH
#-----------------------------------------------
# This works by using the `transform=plt.gca().transAxes` to position the text relative to the axes rather than the data coordinates.
t_statistic, p_value = stats.ttest_ind(
    female_age_onset,
    male_age_onset
)

print("\nStudent's t-test:")
print("t-statistic =", t_statistic)
print("p-value =", p_value)


# MAKE BAR GRAPH
#-----------------------------------------------

plt.bar(
    sex_labels,
    mean_age_onset,
    yerr=stdev_age_onset,
    capsize=10
)

plt.title(
    "Age of Onset of Cognitive Symptoms "
    "in Dementia Patients by Sex"
)

plt.xlabel("Sex")
plt.ylabel("Mean Age of Onset of Symptoms")


# Add p-value to graph

plt.text(
    0.5,
    max(mean_age_onset) + max(stdev_age_onset) * 0.5,
    f"p = {p_value:.3e}",
    ha="center",
    va="bottom"
)

plt.show()


# SCATTER PLOT 1
# Last CASI Score vs. ABeta42
#-----------------------------------------------

casi_scores = []
abeta42_casi = []


for patient in Patient.all_patients:

    if (
        patient.last_casi is not None
        and patient.abeta42 is not None
    ):
        casi_scores.append(patient.last_casi)
        abeta42_casi.append(patient.abeta42)


# Linear regression
# Below is the linear regression analysis for the relationship between the last CASI score and ABeta42 levels.
X = np.array(casi_scores).reshape(-1, 1)
y = np.array(abeta42_casi)

model_casi = LinearRegression()
model_casi.fit(X, y)

# Calculate predicted values
# Predicted ABeta42 levels based on the linear regression model

y_pred_casi = model_casi.predict(X)

# Calculate slope and R²
# The code below calculates the slope, intercept, and R² value for the linear regression model by using the fitted model.
slope_casi = model_casi.coef_[0]
intercept_casi = model_casi.intercept_
r2_casi = model_casi.score(X, y)

# Scatter plot of last CASI score vs ABeta42 levels

plt.scatter(
    casi_scores,
    abeta42_casi,
    color="blue"
)

# Add line of best fit by plotting the predicted values from the linear regression model

plt.plot(
    casi_scores,
    y_pred_casi,
    color="red",
    label="Line of Best Fit"
)

plt.xlabel("Last CASI Score")
plt.ylabel("ABeta42 (pg/ug)")
plt.title("Last CASI Score vs ABeta42 Levels")

# Add slope and R² to graph
# Below works by using the `transform=plt.gca().transAxes` to position the text relative to the axes rather than the data coordinates.
plt.text(
    0.05,
    0.95,
    f"y = {slope_casi:.3f}x + {intercept_casi:.3f}\nR² = {r2_casi:.3f}",
    transform=plt.gca().transAxes,
    ha="left",
    va="top"
)

plt.legend()
plt.show()


# SCATTER PLOT 2
# Last MMSE Score vs. ABeta42
#-----------------------------------------------
mmse_scores = []
abeta42_mmse = []


for patient in Patient.all_patients:

    if (
        patient.last_mmse is not None
        and patient.abeta42 is not None
    ):
        mmse_scores.append(patient.last_mmse)
        abeta42_mmse.append(patient.abeta42)


# Linear regression

X = np.array(mmse_scores).reshape(-1, 1)
y = np.array(abeta42_mmse)

model_mmse = LinearRegression()
model_mmse.fit(X, y)

# Calculate predicted values

y_pred_mmse = model_mmse.predict(X)

# Calculate slope and R²

slope_mmse = model_mmse.coef_[0]
intercept_mmse = model_mmse.intercept_
r2_mmse = model_mmse.score(X, y)


# Scatter plot

plt.scatter(
    mmse_scores,
    abeta42_mmse,
    color="blue"
)

# Add line of best fit by plotting the predicted values from the linear regression model
# model for the relationship between the last MMSE score and ABeta42 levels.
plt.plot(
    mmse_scores,
    y_pred_mmse,
    color="red",
    label="Line of Best Fit"
)

plt.xlabel("Last MMSE Score")
plt.ylabel("ABeta42 (pg/ug)")
plt.title("Last MMSE Score vs ABeta42 Levels")

# Add slope and R² to graph

plt.text(
    0.05,
    0.95,
    f"y = {slope_mmse:.3f}x + {intercept_mmse:.3f}\nR² = {r2_mmse:.3f}",
    transform=plt.gca().transAxes,
    ha="left",
    va="top"
)

plt.legend()
plt.show()



# SCATTER PLOT 3
# Last MOCA Score vs. ABeta42
#-----------------------------------------------

moca_scores = []
abeta42_moca = []


for patient in Patient.all_patients:

    if (
        patient.last_moca is not None
        and patient.abeta42 is not None
    ):
        moca_scores.append(patient.last_moca)
        abeta42_moca.append(patient.abeta42)


# Linear regression analysis for the relationship between the last MOCA score and ABeta42 levels.

X = np.array(moca_scores).reshape(-1, 1)
y = np.array(abeta42_moca)

model_moca = LinearRegression()
model_moca.fit(X, y)

# Calculate predicted values

y_pred_moca = model_moca.predict(X)

# Calculate slope and R²
slope_moca = model_moca.coef_[0]
intercept_moca = model_moca.intercept_
r2_moca = model_moca.score(X, y)


# Scatter plot of last MOCA score vs ABeta42 levels

plt.scatter(
    moca_scores,
    abeta42_moca,
    color="blue"
)

# Add line of best fit by plotting the predicted values from the linear regression model

plt.plot(
    moca_scores,
    y_pred_moca,
    color="red",
    label="Line of Best Fit"
)

plt.xlabel("Last MOCA Score")
plt.ylabel("ABeta42 (pg/ug)")
plt.title("Last MOCA Score vs ABeta42 Levels")

# Add slope and R² to graph

plt.text(
    0.05,
    0.95,
    f"y = {slope_moca:.3f}x + {intercept_moca:.3f}\nR² = {r2_moca:.3f}",
    transform=plt.gca().transAxes,
    ha="left",
    va="top"
)

plt.legend()
plt.show()


# ONE-WAY ANOVA for the relationship between the last MMSE, MOCA scores and ABeta42 levels
#-----------------------------------------------

f_statistic, p_value = stats.f_oneway(
    abeta42_casi,
    abeta42_mmse,
    abeta42_moca
)

