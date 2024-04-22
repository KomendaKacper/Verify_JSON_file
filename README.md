
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

### Running Tests with pytest

The project also includes unit tests written using pytest. To run the tests, follow these steps:

1. Ensure you have pytest installed:

```bash
pip install pytest
```

2. Run the tests using pytest:

```bash
pytest tests.py
```

After completing these steps, pytest will test the `verify_iam_role_policy` function for various use cases and return the test results.
