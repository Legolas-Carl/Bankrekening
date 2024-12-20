def calc_bmi(massa, hoogte):
    """Bereken de BMI-waarde en rond deze af op 1 decimaal."""
    return round(massa / (hoogte ** 2), 1)

def determine_bmi_category(bmi):
    """Bepaal de BMI-categorie op basis van de berekende BMI-waarde."""
    if bmi < 20:
        return "underweight"
    elif 20 <= bmi < 25:
        return "normal"
    elif 25 <= bmi < 30:
        return "overweight"
    elif 30 <= bmi < 40:
        return "obese"
    else:
        return "morbid obese"
