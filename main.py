#to determine whether a person is a child, teenager, adult, or senior citizen based on age using user define module concept.

def check_age(age):
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 60:
        return "Adult"
    else:
        return "Senior Citizen"


