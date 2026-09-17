# Define a class for patient objects
class Patient:

    # Constructor: defines the attributes that each patient object will have
    def __init__(self, donor_id, age_at_death, sex, cognitive_status,
                 apoe_genotype, thal, abeta40, abeta42, ttau, ptau):

        self.donor_id = donor_id
        self.age_at_death = age_at_death
        self.sex = sex
        self.cognitive_status = cognitive_status
        self.apoe_genotype = apoe_genotype
        self.thal = thal
        self.abeta40 = abeta40
        self.abeta42 = abeta42
        self.ttau = ttau
        self.ptau = ptau

    # Representer: determines what is displayed when a patient object is printed
    def __repr__(self):
        return (f"Patient {self.donor_id}: "
                f"Age at Death = {self.age_at_death}, "
                f"Sex = {self.sex}, "
                f"Cognitive Status = {self.cognitive_status}, "
                f"APOE Genotype = {self.apoe_genotype}, "
                f"Thal = {self.thal}")

    # Class method that filters patients using TWO attributes:
    # sex and cognitive status
    @classmethod
    def filter_patients(cls, patients, sex, cognitive_status):

        filtered_patients = []

        # Look at each patient and check whether both conditions are true
        for patient in patients:
            if (patient.sex == sex and
                    patient.cognitive_status == cognitive_status):
                filtered_patients.append(patient)

        return filtered_patients