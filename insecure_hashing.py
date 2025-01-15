# Use of insecure hash function MD5 (CodeQL vulnerability example)
from argon2 import PasswordHasher

def store_password(password):
    # Vulnerable code: Using insecure hashing algorithm (MD5)
    ph = PasswordHasher()
    hashed_password = ph.hash(password)
    print(f"Storing secure hashed password: {hashed_password}")

store_password("super_secure_password123")
