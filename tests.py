import pytest
from verify_json import verify_iam_role_policy

# Test for missing fields in the JSON
def test_verify_iam_role_policy_missing_fields():
    with pytest.raises(Exception):
        verify_iam_role_policy('{"InvalidKey": "value"}')

# Test for invalid PolicyName format
def test_verify_iam_role_policy_invalid_policy_name():
    with pytest.raises(Exception):
        verify_iam_role_policy('{"PolicyName": "!!invalid!!", "PolicyDocument": {"Version": "2012-10-17", "Statement": []}}')

# Test for invalid PolicyName length
def test_verify_iam_role_policy_invalid_policy_name_length():
    with pytest.raises(Exception):
        verify_iam_role_policy('{"PolicyName": "a" * 129, "PolicyDocument": {"Version": "2012-10-17", "Statement": []}}')

# Test for missing PolicyDocument field
def test_verify_iam_role_policy_missing_policy_document():
    with pytest.raises(Exception):
        verify_iam_role_policy('{"PolicyName": "TestPolicy"}')

# Test for invalid PolicyDocument format
def test_verify_iam_role_policy_invalid_policy_document():
    with pytest.raises(Exception):
        verify_iam_role_policy('{"PolicyName": "TestPolicy", "PolicyDocument": "invalid"}')

# Test for missing Version field in PolicyDocument
def test_verify_iam_role_policy_missing_version():
    with pytest.raises(Exception):
        verify_iam_role_policy('{"PolicyName": "TestPolicy", "PolicyDocument": {"Statement": []}}')

# Test for missing Statement field in PolicyDocument
def test_verify_iam_role_policy_missing_statement():
    with pytest.raises(Exception):
        verify_iam_role_policy('{"PolicyName": "TestPolicy", "PolicyDocument": {"Version": "2012-10-17"}}')

# Test for a JSON file with an asteriks
def test_verify_iam_role_policy_statement_contains_asteriks():
    json_file_asterisk = 'json_test_files/json_file_asterisk.json'
    assert verify_iam_role_policy(json_file_asterisk) == False

# Test for a JSON file without an asteriks
def test_verify_iam_role_policy_statement_doesnt_contain_asteriks():
    json_file_non_asterisk = 'json_test_files/json_file_non_asterisk.json'
    assert verify_iam_role_policy(json_file_non_asterisk) == True

