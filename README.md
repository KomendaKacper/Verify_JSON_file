
# JSON File Format Verification

The `verify_iam_role_policy` function allows you to check the validity of a JSON file containing an IAM (Identity and Access Management) policy in Amazon Web Services (AWS). This tool is useful for developers and AWS administrators to ensure that JSON files defining IAM policies are correctly formatted and meet AWS requirements.

## How to Use

### Checking a JSON File

To use the `verify_iam_role_policy` function, provide the path to the JSON file containing the IAM policy. This function will return `True` if the file is valid, and `False` otherwise. Here's an example usage:

```python
from verify_json import verify_iam_role_policy

# Path to the JSON file
json_file = 'policy.json'

# Call the verify_iam_role_policy function
result = verify_iam_role_policy(json_file)

# Print the result
print("Verification result:", result)
```

**Running Tests with pytest:**

The project includes a comprehensive set of unit tests designed to validate the `verify_iam_role_policy` function under various scenarios. These tests cover both expected and edge cases to ensure robustness and reliability.

**Types of Tests:**

1. **Basic JSON Structure:**
   - Test scenarios where the JSON file is missing required fields like "PolicyName" or "PolicyDocument".
   - Examples include checking for missing fields, invalid formats, or incorrect lengths.

2. **Policy Document Validation:**
   - Tests ensuring the correct format and structure of the "PolicyDocument" field.
   - Verifies that the "PolicyDocument" contains the necessary fields like "Version" and "Statement".

3. **Statement Validation:**
   - Tests focusing on the individual statements within the "PolicyDocument".
   - Verifies that each statement follows the correct format and contains essential components like "Effect", "Action", and "Resource".

4. **Specific Conditions:**
   - Tests for specific conditions, such as statements containing a single asterisk (*) in the "Resource" field.
   - These tests address unique requirements or constraints specified by AWS IAM policies.

**Testing Data:**

In addition to predefined test scenarios, the tests utilize JSON files located in the `json_test_files` folder. These files contain various IAM policy configurations, allowing for more extensive testing beyond what's defined directly in the test code. By incorporating external files, the tests cover a broader range of real-world scenarios and edge cases.

**Executing Tests:**

1. Ensure pytest is installed:
   ```
   pip install pytest
   ```

2. Run the tests using pytest:
   ```
   pytest tests.py
   ```

After running the tests, pytest will provide detailed feedback on each test case, including pass/fail status and any relevant error messages or exceptions encountered during execution. This comprehensive testing approach ensures the reliability and accuracy of the `verify_iam_role_policy` function across a variety of input scenarios.
