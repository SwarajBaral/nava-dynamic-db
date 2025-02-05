import bcrypt

def generate_secure_password(_pass: str) -> str:
    """Generate a secure password using bcrypt."""
    password = _pass.encode()
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    return hashed_password.decode()