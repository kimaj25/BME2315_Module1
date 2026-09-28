import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

from patient_Hira import Patient


# read the csv file
df = pd.read_csv("Metadata and Protein Data for Module 1.csv")


# make patient objects
patients = []

for index, row in df.iterrows():

    patient = Patient(
        row["Donor ID"],
        row["Age at Death"],
        row["Sex"],
        row["Cognitive Status"],
        row["APOE Genotype"],
        row["Thal"],
        row["ABeta40 pg/ug"],
        row["ABeta42 pg/ug"],
        row["tTAU pg/ug"],
        row["pTAU pg/ug"]
    )

    patients.append(patient)


print("Number of patients:", len(patients))


# sort patients by age at death
sorted_patients = sorted(patients, key=lambda x: x.age_at_death)

print("\nPatients sorted by age at death:")

for patient in sorted_patients:
    print(patient)


# filter female patients with dementia
female_dementia = Patient.filter_patients(
    patients,
    "Female",
    "Dementia"
)

print("\nFemale patients with dementia:")

for patient in female_dementia:
    print(patient)


# get ABeta42 values for females and males with dementia
female_abeta = []
male_abeta = []

for patient in patients:

    if patient.sex == "Female" and patient.cognitive_status == "Dementia":
        if pd.notna(patient.abeta42):
            female_abeta.append(patient.abeta42)

    if patient.sex == "Male" and patient.cognitive_status == "Dementia":
        if pd.notna(patient.abeta42):
            male_abeta.append(patient.abeta42)


# find mean and standard deviation
female_mean = np.mean(female_abeta)
male_mean = np.mean(male_abeta)

female_std = np.std(female_abeta, ddof=1)
male_std = np.std(male_abeta, ddof=1)


# do t test
t_stat, p_val = stats.ttest_ind(
    female_abeta,
    male_abeta,
    equal_var=False
)

print("\nfemale mean =", female_mean)
print("male mean =", male_mean)
print("female standard deviation =", female_std)
print("male standard deviation =", male_std)
print("t-stat =", t_stat)
print("p-value =", p_val)


# make bar graph
groups = ["Female", "Male"]
means = [female_mean, male_mean]
stds = [female_std, male_std]

plt.bar(groups, means, yerr=stds, capsize=5)

plt.xlabel("Sex")
plt.ylabel("ABeta42 (pg/ug)")
plt.title("Mean ABeta42 in Patients with Dementia")

plt.text(
    0.5,
    0.95,
    f"t = {t_stat:.2f}\np = {p_val:.3e}",
    ha="center",
    va="top",
    transform=plt.gca().transAxes
)

plt.savefig("Hira_bar_graph.png")
plt.show()


# get age and ABeta42 values
ages = []
abeta42 = []

for patient in patients:

    if pd.notna(patient.age_at_death) and pd.notna(patient.abeta42):
        ages.append(patient.age_at_death)
        abeta42.append(patient.abeta42)


# do linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(
    ages,
    abeta42
)

r_squared = r_value ** 2

print("\nslope =", slope)
print("R squared =", r_squared)
print("p-value =", p_value)


# make line of best fit
x_line = np.linspace(min(ages), max(ages), 100)
y_line = slope * x_line + intercept


# make scatter plot
plt.scatter(ages, abeta42)
plt.plot(x_line, y_line)

plt.xlabel("Age at Death")
plt.ylabel("ABeta42 (pg/ug)")
plt.title("ABeta42 vs Age at Death")

plt.text(
    0.05,
    0.95,
    f"R² = {r_squared:.3f}",
    transform=plt.gca().transAxes,
    va="top"
)

plt.savefig("Hira_scatter_plot.png")
plt.show()