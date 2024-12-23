# Use of insecure hash function MD5 (CodeQL vulnerability example)
import hashlib

def store_password(password):
    # Vulnerable code: Using insecure hashing algorithm (MD5)
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    print(f"Storing insecure hashed password: {hashed_password}")

store_password("super_secure_password123")
