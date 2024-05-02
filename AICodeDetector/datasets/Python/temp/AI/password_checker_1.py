import re

def basic_password_checker(password):
    """基本的なパスワードチェッカー"""
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    return True

test_passwords = ["Password1", "password", "Pa$$w0rd!", "12345678", "Qwerty123", "Pass123!@#"]
basic_results = [basic_password_checker(pw) for pw in test_passwords]