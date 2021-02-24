

def get_admin_password():
    return "1234"


def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


user = {"username": "jose", "access_level": "admin"}
get_admin_password = make_secure(get_admin_password)  # 1234


print(get_admin_password())
