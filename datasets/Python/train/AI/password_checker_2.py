import re

def advanced_password_checker(password):
    """強化されたパスワードチェッカー"""
    if len(password) < 12:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    if re.search(r"(.)\1\1", password):  # 連続する同じ文字のチェック
        return False
    common_patterns = ["password", "1234", "qwerty"]  # 一般的なパターン
    if any(pattern in password.lower() for pattern in common_patterns):
        return False
    return True

test_passwords = ["Password1", "password", "Pa$$w0rd!", "12345678", "Qwerty123", "Pass123!@#"]
advanced_results = [advanced_password_checker(pw) for pw in test_passwords]