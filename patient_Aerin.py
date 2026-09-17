#Name: Aerin Kim
#Date: 9/16/26
#Generative AI Statement: This assignment was assisted by ChatGPT-5.6 Luna on September 16, 2026. ChatGPT-5.6 Luna was used to explain the following concepts: class methods, instance methods, and how to create a class that can read data from a CSV file and create objects based on that data. I used the explanations provided by ChatGPT-5.6 Luna to help me understand these concepts and apply them to my code. The work from the class example was also applied here.

import csv


class Patient:

    # Class variable: keeps track of all patient objects
    all_patients = []

    # Constructor: Defines the attributes of a Patient object and adds it to the class list
    def __init__(self, sex: str, years_education: int, apoe_genotype: str, cognitive_status: str, age_onset: float, last_casi: float, last_mmse: float, last_moca: float, braak: str, thal: str, atherosclerosis: str, abeta42: float, ptau: float, donor_id: str = "n/a"):
        #The attributes from the metadata set that I was interest in; this code will create a new patient object with the specified attributes. The donor_id attribute is optional and has a default value of "n/a". The self parameter is a reference to the current instance of the class, and it is used to access the attributes and methods of the class.
        self.sex = sex
        self.years_education = years_education
        self.apoe_genotype = apoe_genotype
        self.cognitive_status = cognitive_status
        self.age_onset = age_onset
        self.last_casi = last_casi
        self.last_mmse = last_mmse
        self.last_moca = last_moca
        self.braak = braak
        self.thal = thal
        self.atherosclerosis = atherosclerosis
        self.abeta42 = abeta42
        self.ptau = ptau
        self.donor_id = donor_id

        # Add this patient to the class list
        Patient.all_patients.append(self)

    # Representer: Defines the string representation of a Patient object
    def __repr__(self):
        return (
            f"{self.donor_id}: "
            f"(Sex: {self.sex} | "
            f"Education: {self.years_education} | "
            f"APOE: {self.apoe_genotype} | "
            f"Status: {self.cognitive_status} | "
            f"Age Onset: {self.age_onset} | "
            f"CASI: {self.last_casi} | "
            f"MMSE: {self.last_mmse} | "
            f"MOCA: {self.last_moca} | "
            f"Braak: {self.braak} | "
            f"Thal: {self.thal} | "
            f"Atherosclerosis: {self.atherosclerosis} | "
            f"ABeta42: {self.abeta42} | "
            f"pTau: {self.ptau})"
        )
    
    # Getter for age of onset
    def get_age_onset(self):
        return self.age_onset

    # Class method to create Patient objects from CSV
    @classmethod
    def instantiate_from_csv(cls, filename: str):

        # Open the CSV file
        with open(filename, encoding="utf8") as f:
            reader = csv.DictReader(f)
            rows_of_patients = list(reader)

        # Create a Patient object for each row
        for row in rows_of_patients:

            # Convert blank cells into None
            def get_float(column): #This function will convert the value in the specified column to a float, or return None if the cell is blank;
                if row[column] == "":
                    return None
                return float(row[column])

            def get_int(column): #This function will convert the value in the specified column to an integer, or return None if the cell is blank;
                if row[column] == "":
                    return None
                return int(row[column])
            #The code below will create a new Patient object for each row in the CSV file, using the values from the specified columns. If a cell is blank, it will be converted to None.
            Patient(
                sex=row["Sex"],
                years_education=get_int("Years of education"),
                apoe_genotype=row["APOE Genotype"],
                cognitive_status=row["Cognitive Status"],
                age_onset=get_float("Age of onset cognitive symptoms"),
                last_casi=get_float("Last CASI Score"),
                last_mmse=get_float("Last MMSE Score"),
                last_moca=get_float("Last MOCA Score"),
                braak=row["Braak"],
                thal=row["Thal"],
                atherosclerosis=row["Atherosclerosis"],
                abeta42=get_float("ABeta42 pg/ug"),
                ptau=get_float("pTAU pg/ug"),
                donor_id=row["Donor ID"]
            )

    # Class method to filter patients; returns a list of patients that match the specified attributes. If an attribute is not specified, it will return all patients.
    @classmethod
    def filter(
        cls,
        patients,
        sex="any",
        years_education="any",
        apoe_genotype="any",
        cognitive_status="any",
        age_onset="any",
        braak="any",
        thal="any",
        atherosclerosis="any"
    ):

        filtered_patients = patients

        # Dictionary connects the filter names to patient attributes
        filters = {
            "sex": sex,
            "years_education": years_education,
            "apoe_genotype": apoe_genotype,
            "cognitive_status": cognitive_status,
            "age_onset": age_onset,
            "braak": braak,
            "thal": thal,
            "atherosclerosis": atherosclerosis
        }

        # Apply each filter
        for attribute, value in filters.items():

            if value != "any":
                filtered_patients = [
                    patient
                    for patient in filtered_patients
                    if getattr(patient, attribute) == value
                ]

        return filtered_patients