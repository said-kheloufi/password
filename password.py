import hashlib

def check_password_requirements(password):
    if (
        len(password) >= 8 
        and any(c.isupper() for c in password)
        and any(c.islower() for c in password)
        and any(c.isdigit() for c in password)
        and any(c in "!@#$%^&*" for c in password)
    ):
        return True
    else:
        return False

def get_valid_password():
    while True:
        password = input("Entrer un mot de passe : ")
        if check_password_requirements(password):
            return password
        else:
            print("Le mot de passe ne respecte pas les exigences de sécurité. Veuillez réessayer.")

password = get_valid_password()

hashed_password = hashlib.sha256(password.encode()).hexdigest()

print(f"Mot de passe choisi : {password}")
print(f"Mot de passe crypté (SHA-256) : {hashed_password}")
