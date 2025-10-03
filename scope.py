"""
Create a BMI calculator that takes a user's weight and height,
 calculates their BMI, and categorizes it as underweight,
   normal weight, overweight, or obese.
"""

LB = 0.453592
IN = 0.0254

def main():
  
    weight_lbs = float(input("Enter your weight in pounds: "))
    height_in = float(input("Enter your height in inches: "))

    weight_kg = weight_lbs * LB
    height_m = height_in * IN

    bmi = weight_kg / (height_m ** 2)

    print(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("Category: Underweight")
    elif 18.5 <= bmi < 25:
        print("Category: Healthy")
    elif 25 <= bmi < 30:
        print("Category: Overweight")
    elif 30 <= bmi < 35:
        print("Category: Obesity Class 1")
    elif 35 <= bmi < 40:
        print("Category: Obesity Class 2")
    else:
        print("Category: Obesity Class 3")
main()

    