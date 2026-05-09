# Python Password Strength Checker

A command-line password analysis tool built in Python. Evaluates password strength based on length, complexity, and common password detection — providing a scored rating and actionable feedback to help users build stronger, more secure passwords.

---

## Features

- Evaluates password length across multiple thresholds
- Checks for uppercase letters, lowercase letters, digits, and special characters (LUDS)
- Detects commonly used passwords and flags them immediately
- Generates a scored rating out of 7
- Provides specific, actionable feedback for improvement
- Strength ratings: Weak 🔴 / Fair 🟡 / Strong 🟢 / Very Strong 💪

---

## Technologies

- Python 3.x
- `re` — regular expressions for pattern matching and complexity analysis

---

## Usage

**1. Clone the repository**
```bash
git clone https://github.com/oyezenu/password-strength-checker.git
cd password-strength-checker
```

**2. Run the checker**
```bash
python checker.py
```

**3. Enter a password when prompted**
```
Enter a password to check: 
```

---

## Example Output

**Weak password:**
```
Enter a password to check: password

Password Strength: Weak 🔴
Score: 0/7

Suggestions to improve:
  → Add uppercase letters
  → Add numbers
  → Add special characters (!@#$% etc.)
  → This is a commonly used password — choose something more unique
```

**Strong password:**
```
Enter a password to check: X#9kL$mP2@vQ

Password Strength: Strong 🟢
Score: 6/7
```

---

## Scoring System

| Criteria | Points |
|---|---|
| Length >= 8 characters | +1 |
| Length >= 12 characters | +1 |
| Length >= 16 characters | +1 |
| Contains uppercase letters | +1 |
| Contains lowercase letters | +1 |
| Contains digits | +1 |
| Contains special characters | +1 |
| Common password detected | Score reset to 0 |

---

## Concepts Demonstrated

- Regular expression pattern matching
- Password complexity analysis (LUDS framework)
- Common password detection
- Defensive security awareness
- User feedback and input validation

---

## Disclaimer

This tool is intended for educational purposes only. Never enter real passwords into third party tools. Use this locally to understand password strength principles.

---

## Author

**Anthony Gonzalez**  
Cybersecurity Student  
[GitHub](https://github.com/oyezenu) • [LinkedIn](https://www.linkedin.com/in/anthony-gonzalez-1701a2285)
