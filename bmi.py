def calculate_bmi(height, weight):
    height = float(height)
    weight = float(weight)
    
    print("Height =", height)
    print("Weight =", weight)
    
    bmi = weight / (height ** 2)
    
    print("BMI =", bmi)
    if bmi<18.5:
        print ("Under Weight")
    elif bmi>25.0:
        print ("Over Weight")
    else:
        print ("Normal Weight")

calculate_bmi(weight='57', height='1.73')
