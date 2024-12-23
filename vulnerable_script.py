# Hardcoded API keys and secrets (Secret Scanning vulnerability)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def connect_to_aws(access_key, secret_key):
    print(f"Connecting to AWS with Access Key: {access_key} and Secret Key: {secret_key}")

connect_to_aws(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
