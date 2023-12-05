def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def calculate_and_classify():
    try:
        name = input("Enter your name: ")
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive values.")

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        print(f"\n{name}, your BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "_main_":
    calculate_and_classify()