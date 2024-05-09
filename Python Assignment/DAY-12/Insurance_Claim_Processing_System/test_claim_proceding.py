import pytest
from insurance_manage_system import InsuranceClaimProcessingSystem

@pytest.fixture
def claim_processing_system():
    return InsuranceClaimProcessingSystem()

@pytest.mark.claim_submission
@pytest.mark.parametrize("policyholder_name, claim_type, claim_amount", [
    ("Hrushi", "Auto", 4000),
    ("Prasad", "Health", 10000),
    ("Atharva", "Home", 25000)
])
def test_submit_claim(claim_processing_system, policyholder_name, claim_type, claim_amount):
    assert claim_processing_system.submit_claim(policyholder_name, claim_type, claim_amount) == "Claim submitted successfully"

@pytest.mark.claim_processing
@pytest.mark.parametrize("claim_type, claim_amount, expected_result", [
    ("Auto", 3000, "Claim processed quickly"),
    ("Health", 15000, "Claim processed within standard time"),
    ("Home", 30000, "Claim processing may take longer")
])
def test_process_claim(claim_processing_system, claim_type, claim_amount, expected_result):
    assert claim_processing_system.process_claim(claim_type, claim_amount) == expected_result

@pytest.mark.claim_disputes
@pytest.mark.parametrize("policyholder_name, claim_type", [
    ("Hrushi", "Auto"),
    ("Prasad", "Health"),
    ("Atharva", "Home")
])
def test_handle_claim_dispute(claim_processing_system, policyholder_name, claim_type):
    assert claim_processing_system.handle_claim_dispute(policyholder_name, claim_type) == "Claim dispute resolved for policyholder: {}, claim type: {}".format(policyholder_name, claim_type)

@pytest.mark.reporting
def test_generate_claim_status_report(claim_processing_system):
    assert claim_processing_system.generate_claim_status_report() == "Claim status report generated"

@pytest.mark.analytics
def test_analyze_claim_processing_times(claim_processing_system):
    assert claim_processing_system.analyze_claim_processing_times() == "Claim processing times analyzed"

@pytest.mark.analytics
def test_identify_claim_submission_trends(claim_processing_system):
    assert claim_processing_system.identify_claim_submission_trends() == "Claim submission trends identified"


"""
# Run tests for claim submission
pytest -m claim_submission

# Run tests for claim processing
pytest -m claim_processing

# Run tests for claim disputes
pytest -m claim_disputes

# Run tests for reporting
pytest -m reporting

# Run tests for analytics
pytest -m analytics
"""