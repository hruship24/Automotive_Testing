import pytest
from Patient_Registraction_Appoinment import Patient_Registration_Appoinment

# Test cases for patient registration and appointment scheduling functionality


class TestPatientRegistrationAppointment:
    @pytest.mark.registration
    @pytest.mark.parametrize("pname, expected_result",
                             [
                                 ('hrushi123', False),
                                 (123, False),
                                 ('@hrushi', False),
                                 ('name&name', False),
                                 ('name$name', False),
                                 ('1234', False),
                                 ('', False)
                             ])
    def test_add_patient_invalid_name(self, pname, expected_result):
        """
        Test case to check the validity of patient names during registration.
        """
        actual_result = Patient_Registration_Appoinment().add_patient(pname)
        assert actual_result == expected_result, 'Name validity check Error'

    @pytest.mark.registration
    @pytest.mark.parametrize("pname, expected_result",
                             [
                                 ('hrushi', True),
                                 ('Hrushi', True),
                                 ('Hrushi_Pawar', True),
                                 ('HRUSHI', True),
                                 ('HRUSHI-PAWAR', True),
                                 ('_hRUSHI', True)
                             ])
    def test_add_patient_valid_name(self, pname, expected_result):
        """
        Test case to check the validity of patient names during registration.
        """
        actual_result = Patient_Registration_Appoinment().add_patient(pname)
        assert actual_result == expected_result, 'Name validity check Error'

    @pytest.mark.appoinment
    @pytest.mark.parametrize("pname, doctor, expected_result",
                             [
                                 ('p1','Dr1',  True),
                             ])
    def test_make_appointment_valid_patient(self, pname, doctor, expected_result):
        """
        Test case to check if an appointment can be made with a valid patient and doctor.
        """
        Patient_Registration_Appoinment().add_patient(pname)
        actual_result = Patient_Registration_Appoinment().make_appointment(pname, doctor, '2024-05-06 10:00')
        assert actual_result == expected_result, 'Appointment not made'

    @pytest.mark.appoinment
    @pytest.mark.parametrize("pname, doctor, expected_result",
                             [
                                 ('Non_existent_patient', 'Non_existent_doctor', False)
                             ])
    def test_make_appointment_invalid_patient(self, pname, doctor, expected_result):
        """
        Test case to check if an appointment can't be made with invalid patient details.
        """
        actual_result = Patient_Registration_Appoinment().make_appointment(pname, doctor, '2024-05-06 10:00')
        assert actual_result == expected_result, 'Appointment with wrong patient details'

    @pytest.mark.details
    @pytest.mark.parametrize("patient_details, expected_result",
                             [
                                 ('p1', True),
                                 ('p2', False)
                             ])
    def test_patient_details_available(self, patient_details, expected_result):
        """
        Test case to check the availability of patient details.
        """
        actual_result = Patient_Registration_Appoinment().patient_details_available(patient_details)
        assert actual_result == expected_result, 'Patient Details Availability Error'

# Test cases for medical record keeping and reporting functionality


class TestMedicalRecordsReporting:
    @pytest.mark.record
    @pytest.mark.parametrize("patient_name, record",
                             [
                                 ('hrushi', 'Flu'),
                                 ('pawar', 'Fever')
                             ])
    def test_add_medical_record(self, patient_name, record):
        hospital = Patient_Registration_Appoinment()
        hospital.add_patient(patient_name)
        hospital.add_medical_record(patient_name, record)
        assert hospital.search_medical_record(patient_name) == record

    @pytest.mark.report
    def test_generate_report(self):
        """
        Test case to verify the generation of reports.
        """
        # Setup: Create instance of Patient_Registration_Appoinment
        hospital = Patient_Registration_Appoinment()

        # Add some medical records for testing
        hospital.add_medical_record('hrushi', 'Flu')
        hospital.add_medical_record('pawar', 'Fever')

        # Exercise: Generate report
        report = hospital.generate_report()

        # Verify: Check if report is generated
        assert report is not None


        '''
        Execute test case selectively :
        pytest -m registration   -> It will execute only registration related test
        pytest -m appoinment     -> It will execute only appoinment related tests 
        pytest -m details        -> It will execute only details related tests
        pytest -m record         -> It will execute only record related tests 
        pytest -m report         -> It will execute only report related tests    
        '''
