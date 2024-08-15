import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[@$!%*?&]', password))

    strength = {
        'Length (>= 8 characters)': length_criteria,
        'Uppercase Letters': uppercase_criteria,
        'Lowercase Letters': lowercase_criteria,
        'Numbers': number_criteria,
        'Special Characters (@$!%*?&)': special_char_criteria
    }

    score = sum(strength.values())

    if score == 5:
        strength_level = "Very Strong"
    elif score == 4:
        strength_level = "Strong"
    elif score == 3:
        strength_level = "Moderate"
    else:
        strength_level = "Weak"

    return strength, strength_level

def provide_feedback(strength, strength_level):
    print("\nPassword Strength Assessment:")
    for criteria, met in strength.items():
        status = "Met" if met else "Not Met"
        print(f"{criteria}: {status}")

    print(f"\nOverall Password Strength: {strength_level}")

def main():
    password = input("Enter a password to assess its strength: ")
    strength, strength_level = assess_password_strength(password)
    provide_feedback(strength, strength_level)

if __name__ == "__main__":
    main()
