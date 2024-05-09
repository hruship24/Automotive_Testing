import re


class Patient_Registration_Appoinment:
    def __init__(self):
        self.patients = ['p1']
        self.doctors = ['Dr1', 'Dr2', 'Dr3']
        self.appointments = {doctor :{} for doctor in self.doctors}
        self.medical_records = {}  # Adding an attribute to store medical records

    def add_patient(self, name):
        if not isinstance(name, str):
            return False
        name_pattern = r'^[A-Za-z\s_-]{2,15}$'
        if re.match(name_pattern, name):
            self.patients.append(name)
            return True
        else:
            return False

    def make_appointment(self, patient_name, doctor, time):
        if patient_name not in self.patients:
            print("Patient not registered")
            return False  # Patient not registered
        if doctor not in self.doctors:
            print("Doctor not available")
            return False  # Doctor not available
        if not re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}', time):
            print("Invalid time format")
            return False  # Invalid time format

        print("Attempting to add appointment...")
        if time in self.appointments[doctor]:
            print("Appointment conflict")
            return False  # Appointment conflict
        else:
            self.appointments[doctor][time] = patient_name
            print("Appointment added:", self.appointments[doctor])
            return True

    def patient_details_available(self, name):
        if name in self.patients:
            return True
        else:
            return False

    def add_medical_record(self, patient_name, record):
        if patient_name in self.patients:
            self.medical_records[patient_name] = record
            return True
        else:
            return False  # Patient not registered

    def search_medical_record(self, patient_name):
        if patient_name in self.medical_records:
            return self.medical_records[patient_name]
        else:
            return None

    def generate_report(self, criteria=None):
        # Implementation of report generation based on criteria
        # Placeholder implementation returning a dummy report for demonstration
        if criteria:
            # Generate report based on the provided criteria
            report = f"Report generated based on criteria: {criteria}"
        else:
            # Generate a generic report
            report = "Generic report generated"

        return report