def calculate_bmi(height, weight):
    height = float(height)
    weight = float(weight)
    
    print("Height =", height)
    print("Weight =", weight)
    
    bmi = weight / (height ** 2)
    
    print("BMI =", bmi)

calculate_bmi(weight='57', height='1.73')