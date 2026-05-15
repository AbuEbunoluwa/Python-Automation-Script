import os
import csv
import pytest
from lab_sync import process_lab_data, LOCAL_LAB_RESULTS

# This runs BEFORE the test to clean up the folders
@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Make sure we start with a clean lab_results directory
    if not os.path.exists(LOCAL_LAB_RESULTS):
        os.makedirs(LOCAL_LAB_RESULTS)
    # Clear out any leftover files from previous runs
    for f in os.listdir(LOCAL_LAB_RESULTS):
        os.remove(os.path.join(LOCAL_LAB_RESULTS, f))

# 🧪 TEST 1: What happens if an empty CSV drops in?
def test_empty_csv_handling():
    # 1. Create a fake, completely empty CSV file
    bad_file_path = os.path.join(LOCAL_LAB_RESULTS, "corrupted_panel.csv")
    open(bad_file_path, 'w').close() 

    # 2. Run our script's processing engine
    result = process_lab_data()

    # 3. ASSERTION: Prove that the script recognized it was empty
    assert result == "EMPTY_FILE"

# 🧪 TEST 2: What happens if a good CSV drops in?
def test_good_csv_handling():
    # 1. Create a fake good CSV file with headers and data
    good_file_path = os.path.join(LOCAL_LAB_RESULTS, "good_panel.csv")
    with open(good_file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["sample_id", "value"])
        writer.writerow(["SAM-001", "12.5"])

    # 2. Run our script's processing engine
    result = process_lab_data()

    # 3. ASSERTION: Prove that the script successfully processed it
    assert result == "SUCCESS"
