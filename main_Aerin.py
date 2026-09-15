import pandas as pd

df = pd.read_csv("Metadata and Protein Data for Module 1.csv")

for header in df.columns:
    print(header)

# Define a class for patient objects
class Patient:
    all_patients = []

    def __init__(self, donor_id, age_at_death, sex, cognitive_status,
                 age_onset_cognitive_symptoms, age_dementia_diagnosis,
                 known_head_injury, pmi):
        self.donor_id = donor_id
        self.age_at_death = age_at_death
        self.sex = sex
        self.cognitive_status = cognitive_status
        self.age_onset_cognitive_symptoms = age_onset_cognitive_symptoms
        self.age_dementia_diagnosis = age_dementia_diagnosis
        self.known_head_injury = known_head_injury
        self.pmi = pmi
        Patient.all_patients.append(self)

    def __repr__(self):
        return (f"Donor ID: {self.donor_id}, "
                f"Age at Death: {self.age_at_death}, "
                f"Sex: {self.sex}, "
                f"Cognitive Status: {self.cognitive_status}, "
                f"Age of Onset: {self.age_onset_cognitive_symptoms}, "
                f"Age of Dementia Diagnosis: {self.age_dementia_diagnosis}, "
                f"Known Head Injury: {self.known_head_injury}, "
                f"PMI: {self.pmi}")

    def get_age_at_death(self):
        return self.age_at_death
    
    @classmethod
    def instantiate_from_csv(cls, df):
        for index, row in df.iterrows():
           Patient(
    row["Donor ID"],
    row["Age at Death"],
    row["Sex"],
    row["Cognitive Status"],
    row["Age of onset cognitive symptoms"],
    row["Age of Dementia diagnosis"],
    row["Known head injury"],
    row["PMI"]
)

Patient.instantiate_from_csv(df)

Patient.all_patients.sort(key=Patient.get_age_at_death, reverse=False)

for patient in Patient.all_patients:
    print(patient)