import re

common_passwords = [
    "password", "123456", "password123", "admin", "letmein",
    "qwerty", "abc123", "monkey", "1234567890", "iloveyou",
    "welcome", "login", "passw0rd", "master", "hello"
]

def check_password(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1

    if len(password) >= 16:
        score += 1

    # Check for uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Check for lowercase
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Check for digits
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add numbers.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add special characters.")

    # Check against common passwords
    if password.lower() in common_passwords:
        score = 0
        feedback.append("This is a commonly used password - choose something more unique.")
        
    # Final assessment
    if score <= 2:
        rating = "Weak 🔴"
    elif score <= 4:
        rating = "Fair 🟡"
    elif score <= 6:
        rating = "Strong 🟢"
    else:
        rating = "Excellent 🟣"

    return score, rating, feedback

password = input("Enter a password to check: ")
score, rating, feedback = check_password(password)

print(f"\nPassword Strength: {rating}")
print(f"Score: {score}/7")

if feedback:
    print("\nSuggestions to improve:")
    for tip in feedback:
        print(f" -> {tip}")