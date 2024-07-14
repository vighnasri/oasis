#BMI calculator

def calculate_bmi(weight, height):
    b=weight/(height**2)
    return b

def bmi_category(bmi):
    
    if bmi < 18.5:
        return "UnderWeight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "OverWeight"
    else:
        return "Obesity"

def main():
    print("BMI Calculator")
    
    
    weight = float(input("enter your weight in kg:"))
    height = float(input("enter your height in meters:"))
    
    bmi = calculate_bmi(weight, height)
    
    category = bmi_category(bmi)
    
    print("Your BMI Is:",bmi)
    print("you are categorized into:",category)

    if (category=="UnderWeight"):
        print("Improve your weight,Stay healthy!")
    elif (category=="Normal Weight"):
        print("Stay strong and healthy!")
    elif (category=="OverWeight"):
        print("Balance your Weight")
    elif (category=="Obesity"):
        print("Improve your health Status")

if __name__ == "__main__":
    main()
