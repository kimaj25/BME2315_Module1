import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
        female_abeta.append(patient.abeta42)

    if patient.sex == "Male" and patient.cognitive_status == "Dementia":
        male_abeta.append(patient.abeta42)


# find mean and standard deviation
female_mean = np.mean(female_abeta)
male_mean = np.mean(male_abeta)

female_std = np.std(female_abeta, ddof=1)
male_std = np.std(male_abeta, ddof=1)


# bar graph
groups = ["Female", "Male"]
means = [female_mean, male_mean]
stds = [female_std, male_std]

plt.bar(groups, means, yerr=stds, capsize=5)

plt.xlabel("Sex")
plt.ylabel("ABeta42 (pg/ug)")
plt.title("Mean ABeta42 in Patients with Dementia")

plt.savefig("Hira_bar_graph.png")
plt.show()


# scatter plot for ABeta42 vs age at death
ages = []
abeta42 = []

for patient in patients:
    ages.append(patient.age_at_death)
    abeta42.append(patient.abeta42)


plt.scatter(ages, abeta42)

plt.xlabel("Age at Death")
plt.ylabel("ABeta42 (pg/ug)")
plt.title("ABeta42 vs Age at Death")

plt.savefig("Hira_scatter_plot.png")
plt.show()
