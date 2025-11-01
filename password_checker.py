import re

def check_password_strength(password):
    """
    Checks the strength of a password based on several criteria.
    """
    # Initialize a score
    score = 0

    # --- Criteria for a strong password ---

    # 1. Length (at least 8 characters)
    if len(password) >= 8:
        score += 1
    else:
        print("Password should be at least 8 characters long.")
        return "Weak"

    # 2. Contains at least one uppercase letter
    if re.search("[A-Z]", password):
        score += 1
    else:
        print("Password should contain at least one uppercase letter.")

    # 3. Contains at least one lowercase letter
    if re.search("[a-z]", password):
        score += 1
    else:
        print("Password should contain at least one lowercase letter.")

    # 4. Contains at least one number
    if re.search("[0-9]", password):
        score += 1
    else:
        print("Password should contain at least one number.")

    # 5. Contains at least one special character
    if re.search("[_@$!%*?&]", password):
        score += 1
    else:
        print("Password should contain at least one of these special characters: _@$!%*?&")

    # --- Determine the strength based on the score ---
    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"

# --- Get user input ---
user_password = input("Enter a password to check its strength: ")

# --- Check the password and print feedback ---
strength = check_password_strength(user_password)
print(f"Password Strength: {strength}")
