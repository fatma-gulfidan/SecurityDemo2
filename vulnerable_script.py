 # vulnerable_script.py

# Hardcoded secret (example vulnerability)
API_KEY = "1234567890abcdef"

def connect_to_service(api_key):
    print(f"Connecting to service with API key: {api_key}")

connect_to_service(API_KEY)
