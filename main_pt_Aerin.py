#Name: Aerin Kim
#Date: 9/16/26
#Generative AI Statement: This assignment was assisted by ChatGPT-5.6 Luna on September 16, 2026. ChatGPT-5.6 Luna was used to explain the following concepts: class methods, instance methods, and how to create a class that can read data from a CSV file and create objects based on that data. I used the explanations provided by ChatGPT-5.6 Luna to help me understand these concepts and apply them to my code. The work from the class example was also applied here.

from patient_Aerin import *
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import statistics 


# CREATE PATIENT OBJECTS FROM CSV FILE
Patient.instantiate_from_csv("C:/Users/aerin/OneDrive/Desktop/COMP BME 2315 Fall 2026/Module 1/BME2315_Module 1/BME2315_Module1/Metadata and Protein Data for Module 1.csv")


# PRINT NUMBER OF PATIENTS
print(f"Number of patients = {len(Patient.all_patients)}")


# PRINT ONE PATIENT AS AN EXAMPLE
print("\nExample patient:")
print(Patient.all_patients[0])


# SORT PATIENTS BY YEARS OF EDUCATION; this will sort the list of all patients in ascending order based on their years of education, and then print the sorted list.
Patient.all_patients.sort(
    key=lambda patient: patient.years_education,
    reverse=False
)

print("\nPatients sorted by Years of Education:")
for patient in Patient.all_patients:
    print(patient)


# FILTER:
# SEVERE ATHEROSCLEROSIS FEMALE PATIENTS WITH DEMENTIA
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



# BAR GRAPH:
# AGE OF ONSET OF SYMPTOMS
# FEMALE VS MALE PATIENTS WITH DEMENTIA

# First filter for female patients with dementia
female_dementia = Patient.filter(
    Patient.all_patients,
    sex="Female",
    cognitive_status="Dementia"
)
# Then filter for male patients with dementia
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

# Define graph information; this code will create a bar graph that compares the mean age of onset of cognitive symptoms in female and male patients with dementia. The error bars represent the standard deviation of the age of onset for each sex.
sex_labels = ["Female", "Male"]

mean_age_onset = [
    female_mean,
    male_mean
]

stdev_age_onset = [
    female_stdev,
    male_stdev
]

# Make bar graph
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

plt.show()




# SCATTER PLOT 1:
# LAST CASI SCORE VS ABETA42
casi_scores = []
abeta42_casi = []

for patient in Patient.all_patients:

    if (
        patient.last_casi is not None
        and patient.abeta42 is not None
    ):
        casi_scores.append(patient.last_casi)
        abeta42_casi.append(patient.abeta42)


X = [casi_scores]  # Independent variable
y = [abeta42_casi]   # Dependent variable

plt.scatter(X, y, color='blue')
plt.xlabel("Last CASI Score")
plt.ylabel("ABeta42 (pg/ug)")
plt.title("Last CASI Score vs ABeta42 Levels")
plt.show()




# SCATTER PLOT 2:
# LAST MMSE SCORE VS ABETA42
mmse_scores = []
abeta42_mmse = []


for patient in Patient.all_patients:

    if (
        patient.last_mmse is not None
        and patient.abeta42 is not None
    ):
        mmse_scores.append(patient.last_mmse)
        abeta42_mmse.append(patient.abeta42)

X = [mmse_scores]  # Independent variable
y = [abeta42_mmse]   # Dependent variable

plt.scatter(X, y, color='blue')
plt.xlabel("Last MMSE Score")
plt.ylabel("ABeta42 (pg/ug)")
plt.title("Last MMSE Score vs ABeta42 Levels")
plt.show()




# SCATTER PLOT 3:
# LAST MOCA SCORE VS ABETA42
moca_scores = []
abeta42_moca = []


for patient in Patient.all_patients:

    if (
        patient.last_moca is not None
        and patient.abeta42 is not None
    ):
        moca_scores.append(patient.last_moca)
        abeta42_moca.append(patient.abeta42)

X = [moca_scores]  # Independent variable
y = [abeta42_moca]   # Dependent variable

plt.scatter(X, y, color='blue')
plt.xlabel("Last MOCA Score")
plt.ylabel("ABeta42 (pg/ug)")
plt.title("Last MOCA Score vs ABeta42 Levels")
plt.show()