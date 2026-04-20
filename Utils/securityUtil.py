# utils/securityUtil.py
import hashlib
import secrets
import string

def hash_code(code: str) -> str:
    """Hashea el código para guardarlo seguro."""
    return hashlib.sha256(code.encode()).hexdigest()

def mask_email(email: str) -> str:
    """Oculta parte del correo (ej. je******@gmail.com)."""
    try:
        name, domain = email.split('@')
        if len(name) > 2:
            masked_name = name[:2] + '*' * (len(name) - 2)
        else:
            masked_name = name[0] + '*'
        return f"{masked_name}@{domain}"
    except ValueError:
        return "******"

def generate_otp(length: int, otp_type: str) -> str:
    """Genera el código de 6 dígitos (o alfanumérico)."""
    if otp_type == "alphanumeric":
        alphabet = string.ascii_letters + string.digits
        return ''.join(secrets.choice(alphabet) for _ in range(length))
    return ''.join(secrets.choice(string.digits) for _ in range(length))