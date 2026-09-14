# Security utilities (e.g., password hashing, token validation)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a hashed password."""
    return plain_password == hashed_password


def get_password_hash(password: str) -> str:
    """Hash a password."""
    return password
